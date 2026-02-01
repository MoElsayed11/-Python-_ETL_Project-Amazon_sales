import logging
from pathlib import Path

from etl.extract import extract_csv
from etl.transform import clean_data
from etl.config_loader import load_config
from etl.load import load_to_postgres   # ✅ PostgreSQL loader


def setup_logging(log_file: str, level: str):
    Path(log_file).parent.mkdir(exist_ok=True)
    logging.basicConfig(
        filename=log_file,
        level=getattr(logging, level),
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


if __name__ == "__main__":
    try:
        # 1️⃣ Load config
        config = load_config()

        # 2️⃣ Setup logging
        setup_logging(
            log_file=config["logging"]["file"],
            level=config["logging"]["level"],
        )

        # 3️⃣ Extract
        raw_df = extract_csv(config["paths"]["raw_data"])

        # 4️⃣ Transform
        clean_df = clean_data(
            raw_df,
            output_path=config["paths"]["processed_data"],
        )

        print(clean_df.head())

        # 5️⃣ Load (PostgreSQL)
        load_to_postgres(
            clean_df,
            db_config=config["database"],
            table_name="products"
        )

        logging.info("ETL pipeline completed successfully")

    except Exception as e:
        logging.critical("ETL pipeline failed", exc_info=True)
        raise
