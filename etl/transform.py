import logging
import pandas as pd
from pathlib import Path


def clean_data(df: pd.DataFrame, output_path: str) -> pd.DataFrame:
    """
    Clean raw data and save cleaned data to processed layer
    """
    try:
        logging.info("Starting data cleaning")

        if df is None or df.empty:
            raise ValueError("Input DataFrame is empty or None")

        before = len(df)
        df = df.drop_duplicates()
        logging.info(f"Removed {before - len(df)} duplicate rows")

        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

        df = df.dropna()

        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        df.to_csv(output_path, index=False)
        logging.info(f"Cleaned data saved to {output_path}")

        logging.info(f"Data cleaning finished. Final row count: {len(df)}")
        return df

    except Exception as e:
        logging.exception("Failed during data transformation")
        raise



