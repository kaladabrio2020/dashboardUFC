import json
import pandas as pd
from sqlalchemy import create_engine


engine = create_engine('postgresql+psycopg2://postgres:datascience007@localhost:5432/machineLearning')


def SerieHistoricaDesistencias():
    with open('json\queries.json', 'r', encoding='utf-8') as f:
        queries = json.load(f)

    sql = queries['SerieHistoricaDesistencia']
    return pd.read_sql(sql, engine)