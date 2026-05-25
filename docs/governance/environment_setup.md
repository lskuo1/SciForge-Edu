# Environment Setup

## Requirements

- Python 3.12+
- Git
- PyCharm (recommended)

## Clone project

```bash
git clone <repository_url>

cd SciForge-Edu
```

## Create virtual environment

```bash
python -m venv ~/.python-venvs/sciforge-edu
```

## Activate environment

Linux/macOS:

```bash
source ~/.python-venvs/sciforge-edu/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

## Install dependencies

```bash
pip install -e .[dev]
```

## Run tests

```bash
pytest
```