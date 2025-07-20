# Branching Strategy

We use a simple and effective Git branching strategy to manage collaborative development.

## Branches

- **main**
  - Production-ready code only.
  - Protected — no direct commits.
  - Only merge from `develop` via PR.

- **develop**
  - Stable integration branch.
  - Merges from feature branches via PR.
  - Always testable and deployable to staging.

- **feature/***
  - Created from `develop`.
  - For individual features or bug fixes.
  - Merged back into `develop` via PR.

## PR Workflow

- PRs required for all merges.
- Minimum 1 reviewer required.
- Use **Squash & Merge**.
- PR should include description of changes.

## Example Flow

```bash
# Create a feature branch
git checkout develop
git checkout -b feature/login-api

# Make changes and commit
git add .
git commit -m "Add: login API endpoint"

# Push to origin
git push origin feature/login-api
