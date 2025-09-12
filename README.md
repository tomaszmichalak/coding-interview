# Coding Interview

This repository contains coding interview practice problems and solutions.

## How to run

```bash
cd project_group
python -m venv ../.venv
source ../.venv/bin/activate
pip install -r requirements.txt
pytest -s -v --log-cli-level=DEBUG
```

### Pytest options explained:
- `-s` : Don't capture output (allows print statements and logging to show)
- `-v` : Verbose mode (shows test names)
- `--log-cli-level=DEBUG` : Show logging messages at DEBUG level and above

## Two Pointers

### Problem 1: Pair with Target Sum
- return indices of the two numbers such that they add up to a specific target
- it can be any (a single) pair, not necessarily unique
