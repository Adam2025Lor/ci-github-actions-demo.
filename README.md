# CI GitHub Actions Demo

# Workflows Implemented

### 1. Python Unit Test Workflow
- **Trigger**: On push to `main`
- **Runs**: a shell command that prints "Hello, CI with GitHub
Actions!"

### 2. Python Unit Test Workflow
- **Trigger**: On push to `main`
- **Runs**: `main.py` unit tests using `test_main.py`

### 3. Scheduled Workflow
- **Trigger**: Every day at midnight UTC
- **Job**: Prints `Scheduled build completed successfully!`

### 4. Matrix Build Workflow
- **Trigger**: On push to `main`
- **Runs**: Unit tests on multiple Python versions using matrix strategy (3.7, 3.8, 3.9, 3.10)

### 4. Self-Hosted Runner
- Configured a self-hosted runner
- One workflow uses `runs-on: self-hosted`

## Repository
https://github.com/Adam2025Lor/ci-github-actions-demo./tree/main/.github/workflows
