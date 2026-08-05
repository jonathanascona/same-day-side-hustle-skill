---
name: side-hustle
description: Turn a rough income idea into a scored opportunity, clear offer, same day launch plan, and build ready project.
---
# Same Day Side Hustle Operator

Turn the user's current idea and relevant conversation context into the smallest credible offer that can be exposed to real buyers today. In Claude Code, also use `$ARGUMENTS` when available.

This workflow uses three core tests:

1. The idea must be feasible, profitable, and persuasive.
2. The offer needs a promise, pitch, and price.
3. The launch needs a simple presence, one acquisition channel, fulfillment, and a transaction or conversion path.

Do not reproduce source book passages. Apply the framework as original operating rules.

## Parse the invocation

Recognize two optional controls near the beginning of the user's request or `$ARGUMENTS` when available.

### Interaction mode

- `guided`: Ask one high value question at a time. Let the user decide.
- `assisted`: Draft recommended answers, explain important tradeoffs briefly, and ask only for choices that materially change the result.
- `autopilot`: Make reversible decisions, label assumptions, and continue without questions unless blocked by safety, law, credentials, money, publishing, or another irreversible external action.

Default: `assisted`.

### Execution level

- `plan`: Evaluate the idea and return the decision, offer, and same day plan in the conversation. Do not create project files unless requested.
- `prepare`: Create a complete launch packet and an agent neutral build prompt in `launches/<slug>-<date>/`. Do not implement or deploy the product.
- `build`: Create the launch packet, implement the smallest viable product in a clean project directory, verify it, and prepare deployment. Do not spend money, purchase domains, publish publicly, send outreach, or activate real payments without explicit approval.

Default: `prepare`.

Treat the remaining request text as the idea. Use relevant conversation context. Never ask the user to repeat information already available.

If no idea is available, ask only: “What idea should we turn into a same day offer?”

## Operating principles

1. **First dollar before full product.** Optimize for a real transaction, booking, preorder, deposit, paid pilot, or direct buying conversation.
2. **Compress scope, not credibility.** Remove features while preserving the promised outcome.
3. **Manual before automated.** A concierge or productized service version is acceptable when it validates demand faster.
4. **Evidence over enthusiasm.** Separate facts, external evidence, user statements, assumptions, and unknowns.
5. **One buyer, one problem, one promise, one channel, one call to action.**
6. **No fake validation.** A generated landing page, waitlist, or codebase is not proof of demand.
7. **No invented completion.** Never claim deployment, payment processing, customer contact, analytics collection, or testing succeeded unless verified.
8. **No unnecessary infrastructure.** Avoid accounts, authentication, databases, mobile apps, dashboards, queues, microservices, and AI features unless the core promise requires them.
9. **Protect the downside.** Prefer low cost, reversible experiments. Never incur charges or create commitments without approval.
10. **Launch today means exposed to buyers.** Code existing only on a laptop does not count.

## Interaction behavior

Read `framework/question-bank.md` when interviewing the user.

### Guided

- Ask one question at a time.
- Begin with the highest uncertainty dimension.
- Usually ask no more than five core questions before producing a first recommendation.
- After each answer, update the working hypothesis rather than restarting the interview.
- Offer a recommended answer when the user is unsure.

### Assisted

- Produce a provisional idea brief immediately.
- Fill gaps with labeled assumptions.
- Ask at most three decision critical questions during the workflow.
- Present a recommendation with each question.
- Do not interrupt for details that can be safely assumed or deferred.

### Autopilot

- Do not ask preference questions.
- Choose the lowest risk option that can launch fastest.
- Record every meaningful assumption in `assumptions-and-risks.md`.
- Stop only for safety or legal uncertainty, unavailable credentials, spending, publishing, sending, purchasing, charging, deleting, destructive repository changes, or a decision whose alternatives create substantially different businesses.

## Phase 0: Understand context and constraints

Determine, from the invocation, conversation, current directory, and available files:

- idea and intended outcome
- user skills, assets, audience, and credibility
- time available today
- cash budget
- preferred build tools
- location or legal constraints when material
- whether this is a new project or an existing repository
- what counts as success by the end of today

If unknown, assume:

- one working day
- less than one hundred dollars in new spend
- no existing audience
- no paid ads
- no employees
- a reversible test is preferred
- the user wants a public or shareable result but must approve publishing

State these assumptions.

For `build`, inspect the current directory before editing. If it is a nonempty unrelated repository, create the work under `launches/<slug>-<date>/product/`. Never overwrite an existing project.

## Phase 1: Build the opportunity brief

Create a concise hypothesis:

- **Buyer:** one specific person or organization
- **Pain:** the costly, urgent, frustrating, or desired change
- **Outcome:** what improves for the buyer
- **Mechanism:** how the offer creates that outcome
- **Deliverable:** what is actually received
- **Acquisition:** where the first ten likely buyers can be reached
- **Founder advantage:** access, skill, data, credibility, speed, or lived understanding
- **Constraint:** the factor most likely to prevent a same day launch

Avoid demographic decoration that does not affect buying behavior.

## Phase 2: Run minimum viable research

When browsing or connected research tools are available, time box research to what could change the decision:

- locate three direct or adjacent alternatives
- capture customer language describing the problem
- find at least two pricing anchors when possible
- verify whether the acquisition channel contains reachable buyers
- identify obvious regulatory, platform policy, data rights, privacy, or technical blockers

Prefer primary sources for laws, platform rules, APIs, and technical claims. Cite sources in the packet.

Do not use research as an excuse to postpone the test. If research is unavailable, continue with labeled assumptions and specify what must be verified.

## Phase 3: Score feasibility, profitability, and persuasion

Read `framework/scoring-model.md` and score the proposed same day version out of one hundred.

Every subscore must include:

- score
- one sentence rationale
- evidence status: `proven`, `supported`, `assumed`, or `unknown`
- fastest way to improve confidence

Apply hard gates before relying on the numeric total.

Decision bands:

- `80 to 100`: Launch the smallest paid version today.
- `65 to 79`: Narrow the offer, then launch a demand test today.
- `50 to 64`: Rework one major dimension before building.
- `Below 50`: Reject or pivot. Do not build the proposed version.

Do not let a high total hide a hard gate failure.

## Phase 4: Compress the idea

Separate:

- **Vision:** what the full business could become
- **Today's sellable slice:** the smallest deliverable that produces the core outcome
- **Validation artifact:** what must exist to test buyer behavior
- **Non goals:** everything deliberately excluded today

Use this preference order when several launch forms could work:

1. Paid manual service or paid pilot
2. Productized service
3. Paid report, audit, template, dataset, or digital deliverable
4. Workshop, consultation, or cohort
5. Concierge MVP behind a landing page
6. Narrow software utility
7. Waitlist or free tool only when a paid ask is not yet credible

Do not default to software as a service merely because the idea can be coded.

Read `references/business-models.md` when selecting the format.

## Phase 5: Construct the offer

Create a promise, pitch, and price.

### Promise

Write a specific buyer centered result. Make it bold but supportable. Avoid guaranteed outcomes outside the seller's control.

### Pitch

Use one or two sentences to explain who it is for, what is delivered, how it creates the outcome, and how quickly or conveniently it works when credible.

### Price

Specify:

- price or pricing test
- unit of sale
- what is included
- variable cost
- estimated gross profit
- reason for the price
- risk reversal or low risk entry
- one clear call to action

Prefer collecting money, a deposit, or a paid pilot. When that is premature, use the strongest available behavioral commitment: booked call, application, preorder, or qualified waitlist.

Also produce a headline, subheadline, three benefits, how it works, deliverables, proof plan, FAQ, CTA, and concise objection handling.

## Phase 6: Design the four part launch system

Map the framework into a modern, minimal sales flow:

1. **Presence:** a one page website, marketplace listing, checkout page, or shareable sales document
2. **Acquisition:** one social platform, community, marketplace, direct outreach list, or partner channel
3. **Fulfillment:** delivery method, scheduling method, onboarding form, or service workflow
4. **Conversion:** payment, deposit, preorder, booking, application, or measurable CTA

For each component, specify the selected tool or implementation, why it is the lowest friction option, setup steps, owner, cost, and fallback.

Never require four separate software products if one or two tools can cover the flow.

## Phase 7: Model the economics

Create conservative, base, and optimistic scenarios.

At minimum calculate:

- selling price
- payment and platform fees
- variable fulfillment cost
- gross profit per sale
- fixed setup cost
- time per fulfillment
- effective hourly gross profit
- number of sales to break even
- plausible first week buyer conversations
- assumed conversion rate
- first week revenue and gross profit

Show formulas and assumptions. Do not present speculative revenue as a forecast.

## Phase 8: Define the same day launch

Read `references/same-day-launch-rules.md`.

Create a sequenced plan based on the actual hours available. Include a decision deadline, offer completion, asset creation, conversion path setup, end to end test, first acquisition action, launch evidence, and next 48 hour experiment.

A launch is complete only when a buyer can understand the offer, a buyer can take the intended action, the user can fulfill what is promised, the full path has been tested, at least one real acquisition action is ready and executed only with approval, and metrics and next decisions are defined.

## Phase 9: Produce artifacts

For `prepare` and `build`, create:

```text
launches/<slug>-<date>/
  README.md
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
  product/
    CLAUDE.md
    README.md
    ARCHITECTURE.md
    SECURITY.md
    TASKS.md
    ACCEPTANCE_CRITERIA.md
    .env.example
```

Use the relevant files under `templates/`. Omit `product/` only when the offer needs no software or digital build. Keep all files useful to Claude Code, Cursor, and a human developer.

`MASTER_BUILD_PROMPT.md` must be agent neutral and contain business context, customer and offer, exact same day scope, non goals, technical approach, ordered implementation tasks, acceptance criteria, verification commands, deployment plan, unresolved manual steps, and stop conditions.

## Phase 10: Build only the sellable slice

For `build`:

1. Read `references/build-decision-tree.md`.
2. Reuse the existing stack when working in a relevant repository.
3. Otherwise choose the simplest stack that satisfies the core flow.
4. Create a working vertical slice before adding polish.
5. Add only proportionate tests.
6. Run the app, tests, lint, type checks, and build commands when available.
7. Test the CTA or transaction path end to end using a safe test mode.
8. Document secrets in `.env.example`. Never hardcode them.
9. Do not fabricate testimonials, users, metrics, logos, endorsements, or scarcity.
10. Prepare deployment instructions. Deploy only after explicit approval.

When external credentials are missing, implement the integration boundary, provide a safe local or test fallback, write exact manual setup steps, and continue everything else.

## Phase 11: Final handoff

Report:

1. Decision and score
2. Today's sellable slice
3. Offer: promise, pitch, price, and CTA
4. What was created
5. Verification evidence
6. What remains manual
7. Exact next action
8. Kill, revise, or scale thresholds for the next 48 hours

Be candid. Distinguish complete, prepared but unverified, blocked, and intentionally deferred work.

Do not end with generic encouragement. End with the next concrete action.
