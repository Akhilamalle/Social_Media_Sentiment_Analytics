# load_to_postgres.py

import pandas as pd
from sqlalchemy import create_engine

def load_to_postgres(csv_path, db_url, table_name):
    df = pd.read_csv(csv_path)
    engine = create_engine(db_url)
    df.to_sql(table_name, engine, if_exists='replace', index=False)
