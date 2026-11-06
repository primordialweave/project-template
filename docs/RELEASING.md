# Release Procedure

No release is implied by the existence of this template.

## Before first release
- Choose and commit a valid LICENSE.
- Confirm ownership, third-party notices, and visual brand rights.
- Replace all placeholders and document verified install/build instructions.
- Implement actual tests, formatting and build CI beyond starter structure checks.
- Choose a documented version policy (SemVer is recommended for compatible APIs).
- Configure main branch protection, restricted Actions permissions, and security reporting.

## Each release
1. Confirm CI success and review breaking changes.
2. Update CHANGELOG.md and bilingual documentation when needed.
3. Create a version tag and release notes describing actual shipped behavior.
4. Attach only verified binaries or checksums; disclose signing/notarization status for macOS apps.
5. State known limitations and support lifecycle.

## Retirement
If a project is archived, record the last supported version, any security implications, and recommended migration options.
