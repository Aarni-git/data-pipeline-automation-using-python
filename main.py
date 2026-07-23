import yaml
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler("logs/automation.log"),
        logging.StreamHandler()
    ]
)

from src.loader import load_data
from src.cleaner import clean_data
from src.transformer import transform_data
from src.exporter import export_data


def load_config():
    """Reads settings.yaml from config/ folder."""
    with open("config/settings.yaml", "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def main():
        logging.info("Pipeline started.")

        # Load YAML settings
        config = load_config()

        # Load raw data
        df_raw = load_data(config)
        logging.info("Data loaded.")

        # Clean data
        df_clean = clean_data(df_raw, config)
        logging.info("Data cleaned.")

        # Transform data
        results = transform_data(df_clean)
        logging.info("Data transformed.")

        # Export results
        export_data(results, config["paths"]["processed_data_dir"])
        logging.info("Results exported.")

        logging.info("Pipeline finished.")


if __name__ == "__main__":
    main()
