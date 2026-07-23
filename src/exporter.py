import os
import pandas as pd
import logging

logger = logging.getLogger(__name__)

def export_data(results: dict, output_path: str) -> None:
    """
    Saves each DataFrame from the results dict into CSV files.
    """

    logger.info("Starting export step.")

    # Create output folder if it doesn't exist
    os.makedirs(output_path, exist_ok=True)

    for name, df in results.items():
        file_path = os.path.join(output_path, f"{name}.csv")
        df.to_csv(file_path, index=False)
        print(f"Saved: {file_path}")

    logger.info(f"Saved aggregated data to {output_path}.")
