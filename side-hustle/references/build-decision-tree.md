# Build Decision Tree

The business hypothesis determines the stack.

## Does the first transaction require custom software?

### No

Create the minimum sales and fulfillment system:

- static sales page or marketplace listing
- form, booking, checkout, or email CTA
- reusable delivery template
- manual tracking

Do not create an application.

### Yes

Identify the single core user action and build one vertical slice.

## Stack selection

### Existing relevant repository

Use its language, package manager, conventions, tests, and deployment pattern unless they block same day completion.

### Static sales page

Prefer the smallest maintainable option already available. Plain HTML, CSS, and JavaScript are acceptable. Use a framework only when it reduces total effort.

### Interactive browser utility

Use a simple typed frontend with no backend when data can remain local. Avoid accounts.

### Data analysis or dashboard

Use a lightweight data app or static generated report when that produces the promised result. Add a database only for persistent multiuser data.

### Server workflow

Use one deployable service and one datastore only when persistence or secret server side logic is essential.

### AI feature

Use AI only when it directly enables the promised outcome, a deterministic or manual alternative is inadequate, costs and failure modes are visible, and user input and generated output are handled safely.

## Same day exclusions by default

Exclude unless essential:

- native mobile apps
- multitenant architecture
- role based permissions
- social graphs
- realtime collaboration
- custom authentication
- admin dashboards
- microservices
- queues and event buses
- complex billing
- recommendation engines
- broad scraping
- custom design systems
- premature analytics infrastructure

## Quality floor

A same day build still needs a working primary path, clear states where relevant, no committed secrets, input validation, basic accessibility, usable mobile layout for public pages, setup instructions, truthful limitations, and verification evidence.

## Deployment

Prefer a target the user already controls. Do not create paid infrastructure without approval.

Before declaring deployment ready, verify the production build, document environment variables, use test mode or a safe mock for transactions, document the deploy command, and define the post deploy smoke test.
