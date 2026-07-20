import yaml
import logging

from src.loader import load_data
from src.cleaner import clean_data

def load_config():
    """Reads settings.yaml from config/ folder."""
    with open("config/settings.yaml", "r", encoding="utf-8") as file:
        return yaml.safe_load(file)

def main():
    # Load YAML settings
    config = load_config()

    # Load raw data
    df_raw = load_data(config)

    # Clean data
    df_clean = clean_data(df_raw, config)

    # Temporary print for testing
    print(df_clean.head())

if __name__ == "__main__":
    main()
