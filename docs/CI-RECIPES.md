# CI Recipes — Opt-in per Project

The active [Starter Quality workflow](../.github/workflows/quality.yml) checks only starter documentation. A real project must add its language/platform tests **before release**.

## Swift Package (macOS)

After adding a valid Package.swift and Swift targets, create a separate workflow under .github/workflows:

```yaml
name: Swift
on:
  push:
    branches: [main]
  pull_request:
permissions:
  contents: read
jobs:
  test:
    runs-on: macos-latest
    timeout-minutes: 20
    steps:
      - uses: actions/checkout@v4
      - run: swift --version
      - run: swift test
```

For Xcode application projects, replace `swift test` with a verified `xcodebuild test -project ... -scheme ... -destination ...` command. The exact macOS/Xcode runner version and signing strategy must match the project; keep signing credentials outside the repository and use minimal scoped secrets.

## Node.js (after adding package.json and a lockfile)

```yaml
name: Node
on:
  push:
    branches: [main]
  pull_request:
permissions:
  contents: read
jobs:
  test:
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: npm
      - run: npm ci
      - run: npm test --if-present
      - run: npm run build --if-present
```

These examples are **not active workflows** and are not evidence that any program has passed a build. Replace versions and commands according to the actual project, and pin Actions to reviewed commit SHAs for stronger supply-chain controls when possible.

## Project-specific security baseline

- Review dependency alerts and update policy in repository Settings.
- Enable private vulnerability reporting if available.
- Consider CodeQL/code scanning when the language and project risk justify it.
- Set branch rules or repository rulesets requiring meaningful checks.
- Keep Actions `permissions` read-only unless a job genuinely needs writes.
- Publish explicit support/release status and fix security issues using private coordination.
