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

    return data.reset_index().sort_values(by='status')


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

    return data.reset_index().sort_values(by='status')

def TotalDeEvasaoPorUnidadeModalidade(Unidade,Ano):
    pd.set_option('mode.chained_assignment', None)

    data  = Dataset()

    datac = data.loc[
            (data['ano_saida']    == str(Ano))   &
            (data['nome_unidade'] == Unidade )   &
            (data['status']       == 'CANCELADO')
    ]
    datac = datac.groupby(
        by = ['nome_curso','forma_ingresso','modalidade_considerada']
    )['status'].count().reset_index()

    datac['modalidade_considerada'].loc[datac['modalidade_considerada'] == ' '] = 'Nenhuma'
    
    return datac


def SerieEvasãoPorUnidade():
    data = Dataset().loc[
        (data['status']=='CANCELADO') &
        (data['ano_saida'] != ' ')
        ]
    
    data = data.groupby(by=['ano_saida','nome_unidade'])['status'].count()

    return data.reset_index()