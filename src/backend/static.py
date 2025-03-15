import json
import pandas as pd
from sqlalchemy import create_engine


engine = create_engine('postgresql+psycopg2://postgres:datascience007@localhost:5432/machineLearning')


def SerieHistoricaDesistencias():
    with open('json//queries.json', 'r', encoding='utf-8') as f:
        queries = json.load(f)

    sql = queries['SerieHistoricaDesistencia']
    return pd.read_sql(sql, engine)


def FormaDeEntrada(anos = [2010, 2010], status = ['Cancelado', 'Ativo','Concluído', 'Trancado'], modo_entrada = ['VESTIBULAR', 'SISU']):
    with open('json//queries.json', 'r', encoding='utf-8') as f:
        queries = json.load(f)

    sql = queries['Forma de entrada']
    sql = sql.replace('ano1_', str(anos[0])).replace('ano2_', str(anos[1]))

    for j, i in zip(status,['d1', 'd2', 'd3', 'd4']):
        sql = sql.replace(f'{i}', f'{j}')

    for j, i in zip(modo_entrada, ['c1', 'c2']):
        sql = sql.replace(f'{i}', f'{j}')
    return pd.read_sql(sql, engine)

def PorSexo(anos = [2010, 2010], status = ['Cancelado', 'Ativo','Concluído', 'Trancado'], modo_entrada = ['VESTIBULAR', 'SISU']):
    with open('json//queries.json', 'r', encoding='utf-8') as f:
        queries = json.load(f)

    sql = queries['PorSexo']
    sql = sql.replace('ano1_', str(anos[0])).replace('ano2_', str(anos[1]))

    for j, i in zip(status,['d1', 'd2', 'd3', 'd4']):
        sql = sql.replace(f'{i}', f'{j}')

    for j, i in zip(modo_entrada, ['c1', 'c2']):
        sql = sql.replace(f'{i}', f'{j}')

    return pd.read_sql_query(sql, engine)

def MediaAprovados(anos = [2010, 2010], status = ['Cancelado', 'Ativo','Concluído', 'Trancado'], modo_entrada = ['VESTIBULAR', 'SISU']):
    with open('json/queries.json', 'r',encoding='utf-8') as f:
        queries = json.load(f)
    sql = queries['MediaAprovados']
    sql = sql.replace('ano1_', f'{anos[0]}').replace('ano2_',f'{anos[1]}')

    d_ = ['d1', 'd2', 'd3', 'd4']
    for e, i in enumerate(status):
        sql = sql.replace(f'{d_[e]}', f'{i}')

    c_ = ['c1', 'c2']
    for e, i in enumerate(modo_entrada):
        sql = sql.replace(f'{c_[e]}', f'{i}')

    return pd.read_sql_query(sql, engine)