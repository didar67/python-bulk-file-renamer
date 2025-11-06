"""
Unit tests for centralized logger
Author: Didarul Islam
Purpose: Ensures logger initialization, rotation, and output correctness.
"""

import logging
import pytest
from core.logger import initialize_logger

def test_logger_initialization():
    """
    Test if logger is initialized properly and has handlers.
    """
    logger = initialize_logger(log_file="test.log", level=logging.DEBUG)
    assert logger is not None
    assert len(logger.handlers) > 0

def test_logger_output(capsys):
    """
    Test if logger outputs messages to console correctly.
    """
    logger = initialize_logger(log_file="test.log", level=logging.INFO)
    test_message = "Test log message"
    logger.info(test_message)

    captured = capsys.readouterr()
    # Console output contains message
    assert test_message in captured.out or test_message in captured.err
