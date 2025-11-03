# Contribution Guidelines

## Continuous Integration

This repository uses GitHub Actions to automatically run all tests on every push and pull request. The workflow tests the code against Python 3.11, 3.12, and 3.13 to ensure compatibility across versions.

You can view the test results by checking the "Actions" tab in the GitHub repository.

### How to run tests locally
You need to have Docker installed on your machine to run GitHub Actions workflows locally using `act`.

```bash
# Install act (macOS)
brew install act

# Run your workflow locally
cd ./coding-interview
act push

# Or run a specific job
act -j test

# Use a specific Python version
act -j test --matrix python-version:3.13
```