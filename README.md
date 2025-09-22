# Coding Interview
This repository contains coding interview practice problems and solutions from various sources.

I decided to use Python as the main language for solving these problems - I want to improve my Python skills as well.
It is free to use any code from this repository for your own learning and practice.

## How to run

```bash
cd project_group
python -m venv ../.venv
source ../.venv/bin/activate
pip install -r requirements.txt
pytest -s -vv --log-cli-level=DEBUG
```

### Pytest options explained:
- `-s` : Don't capture output (allows print statements and logging to show)
- `-v` : Verbose mode (shows test names)
- `--log-cli-level=DEBUG` : Show logging messages at DEBUG level and above