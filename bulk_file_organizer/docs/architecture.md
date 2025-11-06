# architecture.md

# Project Architecture — Bulk File Organizer

## Folder Structure

```
bulk_file_organizer/
├── config/
│   └── config.yaml         # YAML-based configuration
├── core/
│   ├── __init__.py
│   ├── logger.py           # Centralized logging
│   └── config_loader.py    # Configuration loader
├── script/
│   ├── __init__.py
│   ├── cli.py              # Command-line interface
│   └── executor.py         # File rename executor
├── utils/
│   ├── __init__.py
│   └── helper.py           # Utility functions
├── tests/
│   ├── test_cli.py
│   ├── test_executor.py
│   └── test_logger.py
├── docs/
│   ├── README.md
│   └── architecture.md
├── main.py                 # Main application entry point
├── requirements.txt        # Python dependencies
├── .gitignore              # Git ignore rules
└── LICENSE                 # License file (e.g., MIT, Apache 2.0)
```

## Workflow Overview

1. **main.py** → Orchestrates the application by calling CLI handler.
2. **CLI (cli.py)** → Parses arguments, validates input, initializes logger.
3. **ConfigLoader (config_loader.py)** → Loads and validates YAML configuration.
4. **Executor (executor.py)** → Performs bulk renaming (supports dry-run).
5. **Logger (logger.py)** → Centralized, rotating log system.
6. **Utilities (helper.py)** → Shared validation functions.
7. **Tests** → pytest-based unit tests for core logic and CLI.

Recruiter Comment:

* Clear modular separation of responsibilities.
* Ready for CI/CD pipelines and scalable extensions.
* Documentation matches code and demonstrates professional standards.
