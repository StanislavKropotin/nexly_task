import yaml


def load_config(config_path: str) -> dict:
    """
    Loads the configuration from a YAML file.

    :param config_path: Path to the YAML configuration file.
    :return: Configuration dictionary.
    """
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)
