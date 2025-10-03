# Coding Interview

![Tests](https://github.com/tomaszmichalak/coding-interview/actions/workflows/test.yml/badge.svg)

This repository contains coding interview practice problems and solutions from various sources.

I decided to use Python as the main language for solving these problems - I want to improve my Python skills as well.
It is free to use any code from this repository for your own learning and practice.

## How to run

```bash
# Navigate to any module directory (e.g., two_pointers, hash_map_set, tree, etc.)
cd two_pointers

# Set up virtual environment
python -m venv ../.venv
source ../.venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run tests for this module
pytest -s -vv --log-cli-level=DEBUG
```

To run all tests from the root directory:
```bash
# Run tests for all modules (cleans cache between runs to avoid import conflicts)
for dir in hash_map_set graphs sorting linked_lists intervals tree two_pointers; do
  find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
  pytest -v "$dir"
done
```

### Pytest options explained:
- `-s` : Don't capture output (allows print statements and logging to show)
- `-v` : Verbose mode (shows test names)
- `--log-cli-level=DEBUG` : Show logging messages at DEBUG level and above

## Continuous Integration

This repository uses GitHub Actions to automatically run all tests on every push and pull request. The workflow tests the code against Python 3.11, 3.12, and 3.13 to ensure compatibility across versions.

You can view the test results by clicking on the badge above or by checking the "Actions" tab in the GitHub repository.