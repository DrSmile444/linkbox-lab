# linkbox-lab

A tiny in-memory URL shortener and click-tracking core. There is no web
framework and no database here — just pure domain logic (dataclasses and
plain functions) covering how a shortened link gets created and later
resolved, including click counting and expiry. It is small on purpose:
fast for a live coding agent to explore and extend, and fast for a test
suite to verify in seconds.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

## About this repo

This is the Workshop 1 training baseline for the "AI for Developers"
series. It is deliberately kept at a base level of tooling: no strict
static-analysis harness and no spec-driven change process yet — those
are introduced in later sessions. Participants will, live, with an AI
coding agent:

1. Ask the agent to explore this repository and explain what it does.
2. Find and fix the one test that fails on purpose — figure out why it
   fails and correct the underlying logic, not the test.
3. Add one small feature themselves, directly with the agent, with no
   spec-driven workflow involved yet. A good candidate feature: add a
   configurable per-link click limit (`max_clicks`), after which
   `resolve_link` should treat the link as exhausted and return `None`
   even if it has not expired yet.

One test in `tests/test_service.py` is currently failing on purpose.
Finding out which one, and why, is part of the exercise.
