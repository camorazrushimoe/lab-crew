#!/usr/bin/env python3
"""Lab Crew Dashboard — lightest possible monitor on top of the factory.

Runs a tiny HTTP server that reads Docker container status + Hermes state.db
for all three agents and serves JSON for the dashboard UI. Does NOT touch the
factory itself — reads Docker API and state.db read-only via docker exec.

Single file, zero dependencies beyond Python stdlib + Docker CLI.
"""

import json
import os
import re
import subprocess
import time
import urllib.parse
from datetime import datetime, timezone
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from typing import Any

# --------------- config ---------------

AGENTS = {
    "research-lead":       {"port": 8651, "label": "Research Lead",       "icon": "🧠"},
    "research-engineer":   {"port": 8652, "label": "Research Engineer",   "icon": "🔧"},
    "evaluation":          {"port": 8653, "label": "Evaluation Specialist","icon": "📊"},
}

CONTAINER_PREFIX = "lab-crew-"
POLL_INTERVAL_S = 3
HTTP_PORT = 8699

# --------------- helpers ---------------

def run(cmd: list[str], timeout: int = 5) -> str:
    """Run a shell command, return stdout or ''."""
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return r.stdout.strip()
    except Exception:
        return ""


def docker_ps() -> list[dict]:
    """Parse `docker ps` for lab-crew containers."""
    out = run(["docker", "ps", "--format", "{{.Names}}|{{.Status}}|{{.State}}"])
    if not out:
        return []
    result = []
    for line in out.split("\n"):
        if CONTAINER_PREFIX not in line:
            continue
        name, status, state = line.split("|", 2)
        agent_key = name.replace(CONTAINER_PREFIX, "")
        result.append({"container": name, "agent": agent_key, "status": status, "state": state})
    return result


def docker_inspect(container: str) -> dict:
    """Get container start time."""
    out = run(["docker", "inspect", container, "--format", "{{.State.StartedAt}}|{{.State.ExitCode}}"])
    if not out:
        return {}
    started, exit_code = out.split("|", 1)
    return {"started_at": started, "exit_code": exit_code}


def read_state_db(container: str) -> dict:
    """Read the last message + session info via docker exec python3."""
    code = """
import sqlite3, json
conn = sqlite3.connect('/opt/data/state.db')
# last assistant or user message
row = conn.execute("SELECT role, content, finish_reason, session_id, timestamp FROM messages WHERE role IN ('assistant','user') ORDER BY rowid DESC LIMIT 1").fetchone()
result = {'last_message': None}
if row:
    content = row[1]
    if content and len(content) > 300:
        content = content[:297] + '...'
    result['last_message'] = {'role': row[0], 'content': content, 'finish_reason': row[2], 'session_id': row[3], 'ts': row[4]}
# count active sessions (sessions not ended)
active = conn.execute("SELECT COUNT(*) FROM sessions WHERE ended_at IS NULL").fetchone()[0]
result['active_sessions'] = active
# recent history (last 5 user+assistant messages)
rows = conn.execute("SELECT role, substr(content,1,120), timestamp FROM messages WHERE role IN ('assistant','user') ORDER BY rowid DESC LIMIT 10").fetchall()
result['history'] = [{'role': r[0], 'content': r[1], 'ts': r[2]} for r in rows]
conn.close()
print(json.dumps(result))
"""
    out = run(["docker", "exec", container, "python3", "-c", code], timeout=10)
    if not out:
        return {}
    try:
        return json.loads(out)
    except json.JSONDecodeError:
        return {}


def collect_status() -> dict:
    """Collect full dashboard state."""
    containers = docker_ps()
    agents_status = {}

    for c in containers:
        agent_key = c["agent"]
        info = AGENTS.get(agent_key, {})
        details = docker_inspect(c["container"])
        state_data = read_state_db(c["container"])

        agents_status[agent_key] = {
            "label": info.get("label", agent_key),
            "icon": info.get("icon", "?"),
            "port": info.get("port", 0),
            "running": c["state"] == "running",
            "status": c["status"],
            "started_at": details.get("started_at", ""),
            "last_message": state_data.get("last_message"),
            "active_sessions": state_data.get("active_sessions", 0),
            "history": state_data.get("history", []),
        }

    # Fill missing agents as down
    for key, info in AGENTS.items():
        if key not in agents_status:
            agents_status[key] = {
                "label": info["label"],
                "icon": info["icon"],
                "port": info["port"],
                "running": False,
                "status": "down",
                "started_at": "",
                "last_message": None,
                "active_sessions": 0,
                "history": [],
            }

    all_running = all(a.get("running") for a in agents_status.values())
    any_running = any(a.get("running") for a in agents_status.values())

    factory_status = "stopped"
    if all_running:
        factory_status = "running"
    elif any_running:
        factory_status = "degraded"

    return {
        "ts": datetime.now(timezone.utc).isoformat(),
        "factory_status": factory_status,
        "agents": agents_status,
    }


# --------------- HTTP handler ---------------

DASHBOARD_HTML = Path(__file__).parent / "index.html"


class Handler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # silence logs

    def do_GET(self):
        path = urllib.parse.urlparse(self.path).path

        if path == "/api/status":
            data = collect_status()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(data, ensure_ascii=False).encode())
            return

        if path == "/" or path == "/index.html":
            html = DASHBOARD_HTML.read_text()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html.encode())
            return

        self.send_response(404)
        self.end_headers()


def main():
    print(f"Lab Crew Dashboard → http://localhost:{HTTP_PORT}")
    server = HTTPServer(("", HTTP_PORT), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down.")
        server.shutdown()


if __name__ == "__main__":
    main()