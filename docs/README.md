# Compliance Module Overview

Compliance captures how AMI turns governance theory into operational guardrails. Even before the runtime backend lands, this documentation shows teams what standards we cover, how evidence should flow, and where the gaps remain.

## What Exists
- **Static Guidance** – `CODE_QUALITY_ISSUES.md` (module root) tracks lint/type gaps picked
  up by the shared pre-commit hooks (ruff, mypy, pytest). No bespoke linters remain here.
- **CI/DI Alignment** – The orchestrator GitHub workflows run `python scripts/run_tests.py`,
  which delegates into module-level runners. Compliance inherits the same checks by design;
  no additional pipelines are defined in this module.
- **Environment Contract** – `module_setup.py` delegates to Base `EnvironmentSetup` so any
  future backend code automatically reuses uv virtualenv provisioning and hook installation.

## What Exists
- **Static Guidance** – `CODE_QUALITY_ISSUES.md` (module root) tracks lint/type gaps picked
  up by the shared pre-commit hooks (ruff, mypy, pytest). No bespoke linters remain here.
- **CI/DI Alignment** – The orchestrator GitHub workflows run `python scripts/run_tests.py`,
  which delegates into module-level runners. Compliance inherits the same checks by design;
  no additional pipelines are defined in this module.
- **Environment Contract** – `module_setup.py` delegates to Base `EnvironmentSetup` so any
  future backend code automatically reuses uv virtualenv provisioning and hook installation.

## How To Work With Compliance Today
1. **Rely on Base Pipelines** – All enforcement for linting, typing, tests, and audit logging
   is located in `/base`. When adding compliance backend code, wire into those services instead
   of creating module-specific substitutes.
2. **Document Only What Ships** – Create lightweight status notes under this directory when new
   compliance functionality lands. If documentation predates the Base design or references
   unimplemented systems, move it into `research/` (see below).
3. **Keep Hooks Passing** – Before committing, run `uv run --python 3.12 --project compliance \
   python ../scripts/run_tests.py` to execute the shared check harness. Add targeted tests only
   after real backend code exists.

## Research Archive
Legacy requirement breakdowns, standards digests, and the compliance backend spec have been
moved into `./research/`. These documents document historical analysis and should be treated as
reference material until the backend is implemented. Update them only when converting the
research into shippable code that conforms to Base patterns.
