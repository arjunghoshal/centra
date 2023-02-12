import yaml
from yaml.loader import SafeLoader

def load_config(config_file: str):
    # Load configuration from configutation file
    with open(config_file) as config_file:
        config = yaml.load(config_file, Loader=SafeLoader)
    return config