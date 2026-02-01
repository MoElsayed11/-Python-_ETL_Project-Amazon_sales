import logging
from sqlalchemy import create_engine


def load_to_postgres(df, db_config, table_name):
    logging.info("Starting load to PostgreSQL")

    engine = create_engine(
        f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}"
        f"@{db_config['host']}:{db_config['port']}/{db_config['database']}"
    )

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    logging.info(f"Loaded data into PostgreSQL table: {table_name}")

