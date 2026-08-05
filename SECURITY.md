# Security Policy

## Supported version

Security fixes currently target the latest version on the default branch.

## Reporting a problem

Do not open a public issue for a vulnerability that could expose secrets, enable destructive behavior, or create unsafe payment or publishing actions.

Use GitHub's private vulnerability reporting feature when it is enabled for the repository. If it is not available, contact the repository owner through the public profile and request a private reporting channel.

## Security boundaries

The skill is designed to:

- avoid hardcoded secrets
- prefer test modes for external services
- require approval before payments, purchases, publishing, sending, or destructive changes
- distinguish prepared work from verified completion
- document external credentials and manual setup

The skill cannot guarantee that every generated project is secure. Review generated code, dependencies, data handling, legal requirements, and deployment settings before public use.
