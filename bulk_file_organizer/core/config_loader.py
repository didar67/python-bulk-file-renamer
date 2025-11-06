"""
Module: config_loader
---------------------
Handles loading and validation of YAML-based configuration files.

Recruiter Comment:
- Modularized configuration management.
- Includes file validation and graceful error handling.
- Ready for extension (e.g., environment overrides or schema validation).
"""

import os
import yaml

class ConfigLoader:
    """
    Loads and validates YAML configuration for the project.
    """

    def __init__(self, config_path: str = "config/config.yaml"):
        self.config_path = config_path
        self.config_data = None

    def load_config(self) -> dict:
        """
        Load configuration file safely.

        Returns:
            dict: Parsed configuration dictionary.

        Raises:
            FileNotFoundError: If config file is missing.
            yaml.YAMLError: If YAML syntax is invalid.
        """
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")

        try:
            with open(self.config_path, "r", encoding="utf-8") as file:
                self.config_data = yaml.safe_load(file)
                if not isinstance(self.config_data, dict):
                    raise ValueError("Invalid YAML structure. Expected a dictionary at root.")
            return self.config_data
        except yaml.YAMLError as e:
            raise yaml.YAMLError(f"YAML parsing error in {self.config_path}: {e}")

    def get(self, key: str, default=None):
        """
        Retrieve a configuration value safely.

        Args:
            key (str): Top-level key (e.g., 'app', 'paths').
            default (any): Default value if key not found.

        Returns:
            any: Configuration value or default.
        """
        if not self.config_data:
            raise RuntimeError("Configuration not loaded. Call load_config() first.")
        return self.config_data.get(key, default)
