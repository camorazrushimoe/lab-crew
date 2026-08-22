# Lab Crew as an Agent Office template

This repository is the **template** for Lab team instances under [Agent Office](https://github.com/camorazrushimoe/agent-office).

Agent Office is a multi-repo system:

- **agent-office** — shell (Office agents, shared Redis bus, shared pre-prod, composition)
- **lab-crew** (this repo) — template for research teams
- **dev-crew** — template for implementation teams

Operators clone Office, then spawn as many Lab instances as they need from pinned refs of this template.

Full composition model: [agent-office/docs/composition.md](https://github.com/camorazrushimoe/agent-office/blob/main/docs/composition.md)

## What changes when running under Office

| Standalone Lab Crew (direction) | Under Agent Office |
|---------------------------------|--------------------|
| Own Redis when implemented | **Office shared Redis bus** |
| Research-only lifecycle | Same + **idle stop + wake-on-demand** for agent containers |
| Handoff narrative to “DevCrew” | Handoff to **Office**, which routes to a Dev **instance** |
| Self-contained research factory | **Instance** of a template, registered in Office |

What **stays** in this template:

- Roles: research-lead, research-engineer, evaluation
- Hypothesis-driven cycle, Research Package, skills
- Workspace layout for topics / experiments
- Doors + send client (wake-aware under Office)

Lab teams typically **do not** need a full private dev-cluster; temporary workspace is enough unless a future case needs more.

## Template contract (Office-compatible mode)

When composed under Office, this template MUST:

1. Connect all agents to the **external** Office Redis URL (no default private inter-agent bus).
2. Keep HMAC webhook doors; send path MUST **wake** a stopped target before POST.
3. Emit Office-compatible bus events (including research lifecycle and `agent.started` / `agent.stopped`), with team-qualified actor ids when multiple instances exist (e.g. `lab-1/research-lead`).
4. Run a **lifecycle controller** for this instance’s agent containers (idle ~40m, wake on demand). See Office `docs/agent-lifecycle.md`.
5. Use controller-managed restart policy for agents (`restart: "no"`).
6. Hand research outcomes to **Office** (Research Package / stop); Office assigns Dev instances — Lab does not own product implementation routing.
7. Be registrable: name, type=`lab`, door/health/lifecycle endpoints, template ref.

Migration detail (Office side): [migration-teams-to-office-bus.md](https://github.com/camorazrushimoe/agent-office/blob/main/docs/migration-teams-to-office-bus.md)

## Standalone mode

This repo MAY support standalone operation for developing the research factory itself.

**Default for Office operators is Office-attached mode.**

## Implementation roadmap (spec → code)

Lab Crew is still largely specification-stage for Docker runtime. When implementing, Office-compatible mode should be the default design:

- [ ] Compose with external Redis configuration
- [ ] Lifecycle controller + agent `restart: "no"`
- [ ] Wake-aware door client
- [ ] Busy lock / activity signals for long research steps
- [ ] Team-qualified actors when `TEAM_NAME` is set
- [ ] Handoff events aimed at Office (`research.ready`, handoff package pointers)
- [ ] Env vars documented for Office attach

## Versioning

- Pin instances to **tags** of this repo in production compositions.
- Note breaking protocol needs: `Office compatibility: requires agent-office ≥ x.y`.

## Related

- [Agent Office](https://github.com/camorazrushimoe/agent-office)
- [Dev Crew template](https://github.com/camorazrushimoe/dev-crew)
- Factory standard in this repo: `crew/FACTORY-STANDARD.md`
