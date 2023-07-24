import pandas as pd


def Dataset():
    return pd.read_csv(r'dataset/UFC.csv',sep=',',encoding='latin')

def Localidades():
    return Dataset()['nome_unidade'].value_counts().index.to_list()


def TotalDeEvasaoPorUnidade(Unidade,Ano):
    data = Dataset()

    data = data.loc[
    (data['ano_saida']    == str(Ano)    ) &
    (data['nome_unidade'] == str(Unidade)) &
    (data['status']       == 'CANCELADO')
    ]

    data = data.groupby(
        by='nome_curso'
    )['status'].count()

    return data.reset_index()


def TotalDeEvasaoPorUnidadeGenero(Unidade,Ano):
    data = Dataset()

    data = data.loc[
    (data['ano_saida']    == str(Ano)    ) &
    (data['nome_unidade'] == str(Unidade)) &
    (data['status']       == 'CANCELADO')
    ]

    data = data.groupby(
        by=['nome_curso','sexo']
    )['status'].count()

    return data.reset_index()


