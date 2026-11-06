# New Project Setup Checklist

This is a starter repository. Do not promote it as finished software before these steps.

## Identity
- [ ] Rename the GitHub repository and replace PROJECT_NAME in both READMEs.
- [ ] Write a verifiable user problem, target audience, project status, and supported platforms.
- [ ] Add real screenshots only after the application exists.
- [ ] Remove template-only explanations and stale placeholder links.

## Licensing and rights
- [ ] Choose a source-code license with the project owner and add the actual LICENSE file.
- [ ] Audit dependencies, example content, fonts, stock art and third-party images.
- [ ] Keep Primordial Weave trademarks, seal glyph and brand artwork under a separate explicit policy.
- [ ] Confirm all contributors have the right to submit their changes.

## Engineering
- [ ] Add language-appropriate lint, test, typecheck/build CI jobs (the current workflow only checks template structure).
- [ ] Document exact installation and tests on a clean machine or CI runner.
- [ ] Configure branch protection / rulesets and required checks in Settings.
- [ ] Review least-privilege Actions permissions, Dependabot, code scanning, and private security advisories.
- [ ] Set the project-specific support channel and maintainers.

## Launch
- [ ] Remove template labels from docs.
- [ ] Set lifecycle status (experimental/active/maintenance/archived).
- [ ] Add a tested release artifact, release notes, semantic version or alternate documented version policy.
- [ ] Publish a known-limitations section and ensure the English/Chinese basics match.
- [ ] Use a fresh disposable test repository to validate onboarding before the first public release.

## Local health checks

Run:

```bash
python3 scripts/check_project.py
python3 -m unittest discover -s tests -v
```

These checks validate the starter itself, **not** any future product code.
