import pandas as pd
import logging

def clean_data(df, config):
    """
    Cleans the loaded DataFrame according to settings.yaml rules.
    """

    # Read processing settings from YAML
    processing_settings = config.get("processing", {})
    drop_duplicates_flag = processing_settings.get("drop_duplicates", False)

    fill_missing_settings = processing_settings.get("fill_missing", {})
    fill_amount_value = fill_missing_settings.get("amt", None)
    fill_category_value = fill_missing_settings.get("category", None)

    # Drop duplicates if YAML says so
    if drop_duplicates_flag:
        before = len(df)
        df = df.drop_duplicates()
        after = len(df)
        logging.info(f"Removed {before - after} duplicate rows.")

    # Fill missing values according to YAML
    # Fill numeric column "amount"
    if fill_amount_value is not None and "amt" in df.columns:
        df["amt"] = df["amt"].fillna(fill_amount_value)

    # Fill categorical column "category"
    if fill_category_value is not None and "category" in df.columns:
        df["category"] = df["category"].fillna(fill_category_value)

    logging.info("Missing values filled according to YAML settings.")

    # Convert data types (optional but recommended)
    # Convert amount → float
    if "amt" in df.columns:
        df["amt"] = pd.to_numeric(df["amt"], errors="coerce")

    # Convert date → datetime and
    # Create trans_date column from trans_date_trans_time
    if "trans_date_trans_time" in df.columns:
        df["trans_date"] = pd.to_datetime(df["trans_date_trans_time"], errors="coerce").dt.date

    # Convert is_fraud → int (0/1)
    if "is_fraud" in df.columns:
        df["is_fraud"] = pd.to_numeric(df["is_fraud"], errors="coerce").fillna(0).astype(int)

    # Ensure merchant and category are strings
    if "merchant" in df.columns:
        df["merchant"] = df["merchant"].astype(str)

    if "category" in df.columns:
        df["category"] = df["category"].astype(str)

    logging.info("Data types converted where applicable.")

    # Return cleaned DataFrame
    return df
