import psycopg2
from sqlalchemy import create_engine
from transform import transform_logs
from extract import read_logs
import pandas as pd

def load_to_postgres(df):
    try:
        # PostgreSQL connection details
        user = "postgres"
        password = "Gsneha%40123"   # 👈 Encoded @ as %40
        host = "localhost"
        port = "5432"
        database = "it_logs"

        # Using SQLAlchemy engine for pandas .to_sql()
        engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")

        # Load DataFrame into PostgreSQL table
        df.to_sql("logs", engine, if_exists="append", index=False)
        print("✅ Data successfully loaded into PostgreSQL!")

    except Exception as e:
        print("❌ Error while loading data:", e)


if __name__ == "__main__":
    # Extract and transform
    logs = read_logs()
    df = transform_logs(logs)

    print("Loading data to PostgreSQL...")
    load_to_postgres(df)


