# Architecture

## Design goal

The project separates business reasoning from implementation instructions.

This allows the framework to improve without forcing every build template to change, and it allows the build templates to evolve without changing the core business tests.

## Source layout

### `skill/SKILL.body.md`

The main workflow instructions without Claude's required metadata markers.

### `skill/framework/`

Decision rules, question logic, and the scoring model.

### `skill/references/`

Supporting guidance for launch definitions, business model selection, and build scope.

### `skill/templates/`

Reusable output structures for the launch packet.

### `scripts/install.py`

Generates the required `SKILL.md` metadata and installs the skill into a personal or custom Claude skills directory.

### `scripts/package_skill.py`

Builds a portable ZIP archive containing the final installable skill.

### `scripts/check_repository.py`

Checks required files, validates links between the source components, and enforces repository writing rules.

## Why installation generates the entry file

Claude Code requires metadata at the top of `SKILL.md`. This repository also follows a style rule that excludes em dash characters and consecutive three hyphen sequences from source text.

The installer constructs the metadata markers at runtime. The installed skill remains valid while the repository source stays compliant with the style rule.

## Portability

The skill itself runs in Claude Code. Its launch packet is designed to be portable.

The generated master build prompt contains:

- business context
- buyer and offer
- exact scope
- non goals
- technical approach
- ordered tasks
- acceptance criteria
- verification commands
- deployment plan
- manual steps
- stop conditions

That file can be used by Claude Code, Cursor, or another coding agent.
