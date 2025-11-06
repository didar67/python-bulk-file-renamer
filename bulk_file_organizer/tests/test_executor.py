"""
Unit tests for Executor Logic (Bulk File Renamer)
Author: Didarul Islam
Purpose: Ensures file rename executor behaves correctly in dry-run
         and actual execution modes with edge case handling.
"""

import os
import pytest
from unittest import mock
from script.executor import BulkFileRenamer
from core.logger import initialize_logger

@pytest.fixture
def setup_dummy_folder(tmp_path):
    """
    Creates a temporary folder with dummy files for testing.
    """
    files = ["fileA.txt", "fileB.doc", "fileC.pdf"]
    for f in files:
        (tmp_path / f).write_text("dummy content")
    return tmp_path

def test_bulk_rename_dry_run(setup_dummy_folder):
    """
    Validate dry-run mode does not rename files.
    """
    folder = setup_dummy_folder
    renamer = BulkFileRenamer(folder_path=str(folder), prefix="test", dry_run=True)
    logger = initialize_logger(log_file="test.log", level=10)
    
    result = renamer.rename_files(logger)
    
    # Assert all files remain unchanged in dry-run
    assert set(os.listdir(folder)) == {"fileA.txt", "fileB.doc", "fileC.pdf"}
    assert result["renamed_count"] == 3  # Count expected

def test_bulk_rename_actual_run(setup_dummy_folder):
    """
    Validate actual renaming occurs correctly.
    """
    folder = setup_dummy_folder
    renamer = BulkFileRenamer(folder_path=str(folder), prefix="real", dry_run=False)
    logger = initialize_logger(log_file="test.log", level=10)

    result = renamer.rename_files(logger)
    
    # Assert files are renamed
    renamed_files = os.listdir(folder)
    for idx, filename in enumerate(sorted(renamed_files), start=1):
        assert filename.startswith("real_")
        assert filename.endswith((".txt", ".doc", ".pdf"))
    assert result["renamed_count"] == 3

def test_invalid_folder(monkeypatch):
    """
    Validate that invalid folder path raises proper logging and exception.
    """
    renamer = BulkFileRenamer(folder_path="/invalid/path", prefix="fail", dry_run=False)
    logger = initialize_logger(log_file="test.log", level=10)

    result = renamer.rename_files(logger)
    assert result["renamed_count"] == 0
    assert "error" in result
