"""
Unit tests for CLI argument parsing
Author: Didarul Islam
Purpose: Validates CLI argument parsing and proper error handling.
"""

import pytest
import sys
from script.cli import run_cli

def test_cli_args(monkeypatch):
    """
    Test CLI argument parsing with example arguments.
    """
    test_args = ["program", "--source", "/path/to/folder", "--rename-pattern", "prefix123", "--dry-run"]
    monkeypatch.setattr("sys.argv", test_args)
    args = run_cli()
    
    assert args.source == "/path/to/folder"
    assert args.rename_pattern == "prefix123"
    assert args.dry_run is True

def test_cli_missing_args(monkeypatch):
    """
    Test that missing required arguments raise SystemExit.
    """
    test_args = ["program"]
    monkeypatch.setattr("sys.argv", test_args)
    with pytest.raises(SystemExit):
        run_cli()
