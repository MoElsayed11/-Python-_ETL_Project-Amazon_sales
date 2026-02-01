import yaml
from pathlib import Path


def load_config(config_path: str = "config/config.yaml") -> dict:
    """
    Load YAML configuration file
    """
    path = Path(config_path)

    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(path, "r") as file:
        config = yaml.safe_load(file)

    return config
