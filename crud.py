import pickle 
import pandas as pd

import mysql.connector as mysql

def conexao():
    try:
        file  = open('conect.dat','rb')
        dados = pickle.load(file)
        file.close()

        conn = mysql.connect(
            database=dados[2],
            user=dados[0],
            host='localhost',
            password =dados[1],
        ); return conn

    except Exception as e:
        print(e)

   

def selecao(ano_saida,nome_unidade):
    a = f'''
    SELECT da.nome_curso as 'nome do curso', count(da.status) as cancelados FROM dados_alunos as da
    WHERE da.nome_unidade='{nome_unidade}' and da.status='CANCELADO' and da.ano_saida={ano_saida}
    GROUP BY da.nome_curso;
         '''
    return pd.read_sql(a,conexao())


def nome_unidade():
    sql  =  '''
    SELECT da.nome_unidade FROM dados_alunos AS da 
    GROUP BY da.nome_unidade
    ORDER BY da.nome_unidade DESC;
            '''
    return pd.read_sql(sql,conexao()).nome_unidade.tolist()


def por_sexo(ano_saida,nome_unidade):
    sql1 = f'''
    SELECT da.nome_curso as 'nome do curso', count(da.status)  as cancelados, da.sexo FROM dados_alunos as da
    WHERE da.nome_unidade='{nome_unidade}' and da.status='CANCELADO' and da.ano_saida={ano_saida} and da.sexo = 'M'
    GROUP BY da.nome_curso;
         '''
    
    sql2 = f'''
    SELECT da.nome_curso as 'nome do curso', count(da.status) as cancelados ,da.sexo FROM dados_alunos as da
    WHERE da.nome_unidade='{nome_unidade}' and da.status='CANCELADO' and da.ano_saida={ano_saida} and da.sexo = 'F'
    GROUP BY da.nome_curso;
         '''

    return pd.read_sql(sql1,conexao()) , pd.read_sql(sql2,conexao())


def por_ano_geral():
    sql  =  '''
    SELECT da.ano_saida , count(da.status) as cancelados FROM dados_alunos as da
    WHERE da.status = 'CANCELADO' 
    GROUP BY da.ano_saida
    ORDER BY da.ano_saida desc;
        '''
    return pd.read_sql(sql,conexao())


def por_ano_unidade(unidade):
    sql =f'''
    SELECT da.ano_saida , da.nome_unidade ,count(da.status) as cancelados FROM dados_alunos as da
    WHERE da.status = 'CANCELADO' and da.nome_unidade = '{unidade}'
    GROUP BY da.ano_saida 
    ORDER BY da.ano_saida DESC;
    '''
    return pd.read_sql(sql,conexao())

