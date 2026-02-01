import logging
import pandas as pd
from pathlib import Path


def extract_csv(file_path: str) -> pd.DataFrame:
    """
    Extract data from a CSV file and return a DataFrame
    """
    try:
        logging.info("Starting CSV extraction")

        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        df = pd.read_csv(path)

        if df.empty:
            raise ValueError("Extracted DataFrame is empty")

        logging.info(f"Extracted {len(df)} rows from {file_path}")
        return df

    except Exception as e:
        logging.exception("Failed during CSV extraction")
        raise




