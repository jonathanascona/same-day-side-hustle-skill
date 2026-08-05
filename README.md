# Same Day Side Hustle Skill

Turn a rough income idea into a focused offer, a practical validation plan, and a build ready launch packet for Claude, Claude Code, Cursor, or another coding agent.

The skill evaluates whether an idea is feasible, profitable, and persuasive. It then narrows the concept into something that can be sold or tested today, creates the offer and basic economics, designs the launch path, and optionally prepares an MVP build plan.

## What it does

The skill helps you:

- identify a specific buyer and paid problem
- score the idea for feasibility, profitability, and persuasion
- separate a long term vision from a version that can launch today
- choose a suitable business model instead of defaulting to software
- create a promise, pitch, price, and call to action
- map a simple presence, acquisition channel, fulfillment flow, and conversion path
- model conservative, base, and optimistic economics
- generate launch copy, outreach, metrics, and fulfillment instructions
- create an agent neutral build prompt for Claude Code, Cursor, or another coding agent
- optionally implement and verify the smallest credible MVP

## Why I built it

I often start projects by talking through an idea in an AI chat. Building was rarely the main problem. The harder problem was deciding what deserved to be built, whether anyone would pay for it, how small the first version should be, and what needed to happen before I could honestly call it launched.

After reading Chris Guillebeau's book *Side Hustle: From Idea to Income in 27 Days*. Three ideas stood out:

1. A side hustle should be feasible, profitable, and persuasive.
2. An idea becomes an offer through a promise, a pitch, and a price.
3. A launch needs a simple online presence, a way to reach people, a fulfillment path, and a way for someone to take action.

I turned those ideas into an independent workflow for Claude. This repository contains an original implementation. It does not reproduce the book or the summary, and it is not affiliated with Chris Guillebeau, Four Minute Books, Anthropic, or Cursor.

Read more in [docs/inspiration.md](docs/inspiration.md).

## Install in Claude

The easiest option is the prepared ZIP:

1. Download `dist/side-hustle.zip` from this repository.
2. In Claude, open **Customize**, then **Skills**.
3. Select the plus button, choose **Create skill**, then **Upload a skill**.
4. Upload `side-hustle.zip`.
5. Turn the skill on.

The ZIP uses Claude's required structure:

```text
side-hustle.zip
  side-hustle/
    skill.md
    framework/
    references/
    templates/
```

The folder name and the metadata name are both `side-hustle`.

## Install in Claude Code

### Clone and install

```bash
git clone https://github.com/jonathanascona/same-day-side-hustle-skill.git
cd same-day-side-hustle-skill
python scripts/install.py
```

On systems where Python is invoked with `python3`:

```bash
python3 scripts/install.py
```

The installer copies the skill to:

```text
~/.claude/skills/side-hustle
```

### Manual Claude Code installation

Copy the repository's `side-hustle` folder to:

```text
~/.claude/skills/side-hustle
```

The final entry file should be:

```text
~/.claude/skills/side-hustle/SKILL.md
```

Restart Claude Code only if the top level skills directory did not exist when the session started.

## How to use it

In Claude, describe the idea and explicitly ask it to use the `side-hustle` skill.

```text
Use the side-hustle skill in assisted mode to prepare a weekly competitor report for small supplement brands.
```

In Claude Code, you can invoke it directly:

```text
/side-hustle assisted prepare A weekly competitor report for small supplement brands
```

The workflow accepts an interaction mode and an execution level.

### Interaction modes

**guided**

Claude asks one important question at a time and lets you make the major decisions.

```text
/side-hustle guided plan I want to create an AI powered research service
```

**assisted**

Claude proposes answers, explains important tradeoffs, and asks only when a decision would materially change the result.

```text
/side-hustle assisted prepare A weekly competitor report for small supplement brands
```

**autopilot**

Claude makes reversible decisions, labels assumptions, and continues until it reaches an action that needs approval.

```text
/side-hustle autopilot prepare A local fabric car interior cleaning service
```

The default mode is `assisted`.

### Execution levels

**plan**

Returns the evaluation, offer, economics, and launch plan in the conversation.

**prepare**

Creates a complete launch packet, including an agent neutral build prompt.

**build**

Creates the packet and implements the smallest credible product. It still stops before spending money, purchasing a domain, publishing publicly, activating real payments, or sending outreach.

The default execution level is `prepare`.

## Example outputs

Prepare and build modes can create:

```text
launches/<idea-slug>-<date>/
  00-decision-summary.md
  01-idea-brief.md
  02-research-evidence.md
  03-opportunity-scorecard.md
  04-offer.md
  05-economics.md
  06-validation-plan.md
  07-same-day-launch-plan.md
  08-launch-copy.md
  09-outreach.md
  10-fulfillment-sop.md
  11-metrics-and-experiments.md
  assumptions-and-risks.md
  MASTER_BUILD_PROMPT.md
```

For a software idea, the output can also include a build ready product folder with architecture, security, tasks, acceptance criteria, and environment documentation.

## The core framework

### Feasible

Can the smallest version be delivered with the available time, skills, tools, budget, and permissions? Can it produce useful buyer evidence within a week?

### Profitable

Is there a plausible price, positive contribution margin, and believable path to a first transaction?

### Persuasive

Can a buyer understand the result and why this offer is preferable in two sentences?

### Promise, pitch, and price

The skill turns the idea into a clear buyer result, a concise explanation of delivery, and a price with one call to action.

### Presence, acquisition, fulfillment, and conversion

The skill designs the smallest complete path from discovering the offer to taking action and receiving the result.

## Build and validate the packages

```bash
python scripts/package_skill.py
python scripts/check_repository.py
python -m unittest discover -s tests
```

The packaging script creates:

- `dist/side-hustle.zip` for Claude skill uploads
- `dist/side-hustle-claude-code.zip` for Claude Code installation

## Project status

This is version 0.2.0. It is an early public release intended for real world testing. Feedback, examples, bug reports, and focused contributions are welcome.

## License

MIT. See [LICENSE](LICENSE).
