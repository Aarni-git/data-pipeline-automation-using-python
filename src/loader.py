import pandas as pd
import logging
import yaml

logger = logging.getLogger(__name__)

def load_data(config):
    """
    Loads raw CSV data according to settings.yaml paths.
    """

    logger.info("Loading data and configuration.")

    # Read raw data path from YAML
    paths = config.get("paths", {})
    raw_data_path = paths.get("raw_data")

    # Read CSV settings
    csv_settings = config.get("csv_settings", {})
    separator = csv_settings.get("separator", ",")
    encoding = csv_settings.get("encoding", "utf-8")

    # Load CSV
    try:
        df = pd.read_csv(
            raw_data_path,
            sep=separator,
            encoding=encoding,
            dtype=str,  # <-- prevents int conversion
            engine="pyarrow", # <-- pyarrow -> faster reading
        )
        logger.info(f"Data loaded successfully from {raw_data_path}")
        return df

    except Exception as e:
        logger.error(f"Failed to load CSV: {e}")
        raise
