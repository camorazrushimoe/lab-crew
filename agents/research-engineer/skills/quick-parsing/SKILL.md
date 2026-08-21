# Skill: quick-parsing

## Purpose

Build lightweight parsers and collectors for research data sources (web pages, APIs, public datasets, files).

## When to use

- An experiment needs data that is not already available locally
- The goal is signal-finding, not production-grade ingestion

## Principles

1. **Minimum viable collection** — collect only fields required by the hypothesis
2. **Temporary by default** — store under `workspace/<topic>/data/`
3. **Readable scripts** — prefer clear Python scripts over clever frameworks
4. **Document limitations** — rate limits, missing fields, sampling bias, ToS risks
5. **Stop early** — if the first small sample already answers the question, do not scale yet

## Typical sources (examples)

- Public product pages / store pages (e.g. Steam-like)
- Review / comment pages
- Simple public APIs
- CSV / JSON dumps
- Search result pages (with care)

## Anti-patterns

- Building a general-purpose crawler “for later”
- Persisting to production databases during research
- Ignoring robots.txt / ToS / rate limits when it creates risk
- Collecting everything “just in case”
