# Contributing

Thanks for considering a contribution.

## Good contributions

Useful changes include:

- clearer decision rules
- better scoring guidance
- additional worked examples
- safer build boundaries
- improved launch templates
- installation fixes
- tests that catch regressions

## Before opening a pull request

1. Keep the workflow focused on trustworthy buyer evidence.
2. Do not add features that encourage needless software or infrastructure.
3. Do not copy text from books, summaries, courses, or proprietary frameworks.
4. Keep external actions behind explicit approval.
5. Run the repository checks and tests.

```bash
python scripts/check_repository.py
python -m unittest discover -s tests -v
python scripts/package_skill.py
```

## Writing style

Repository prose should be direct, specific, and readable.

Do not use em dash or en dash characters. Do not use consecutive three hyphen sequences in repository text. The validation script enforces this rule.

Use headings, bullets, numbered steps, and short paragraphs instead of decorative separators.

## Pull requests

Describe:

- what changed
- why it changed
- how it affects users
- how it was tested
- any unresolved tradeoffs

Keep each pull request focused on one coherent improvement.
