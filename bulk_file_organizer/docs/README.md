# README.md

# Bulk File Organizer

**Version:** 1.0.0
**Author:** Didarul Islam

## Overview

Bulk File Organizer is a professional Python tool for automating file renaming in bulk.
It supports flexible patterns, dry-run simulation, and centralized logging.

## Features

* CLI-driven interface for ease of use
* Dry-run mode for safe testing
* Configurable YAML-based settings
* Rotating logger with console output
* Modular, testable, and scalable architecture

## Setup

```bash
# Clone repository
git clone https://github.com/username/bulk_file_organizer.git
cd bulk_file_organizer

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
python main.py --source ./downloads --rename-pattern file_{index} --dry-run
```

## Logging

* Logs are stored in `bulk_file_organizer.log`
* Console output shows info-level logs for real-time monitoring
* Rotating log files prevent oversized logs

## Contribution

* Follow feature branches under `dev`
* Write unit tests for new functionality
* Ensure modular design and professional docstrings