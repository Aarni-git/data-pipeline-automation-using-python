import yaml
import logging

from src.loader import load_data
from src.cleaner import clean_data
from src.transformer import transform_data
from src.exporter import export_data

def load_config():
    """Reads settings.yaml from config/ folder."""
    with open("config/settings.yaml", "r", encoding="utf-8") as file:
        return yaml.safe_load(file)

def main():
    # Load YAML settings
    config = load_config()

    # Load raw data
    df_raw = load_data(config)
    print("Data loaded.")

    # Clean data
    df_clean = clean_data(df_raw, config)
    print("Data cleaned.")

    # Transform data
    results = transform_data(df_clean)
    print("Data transformed.")

    # Export results
    export_data(results, config["paths"]["processed_data_dir"])
    print("Results exported.")

    print("Pipeline completed successfully.")

if __name__ == "__main__":
    main()
