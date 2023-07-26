import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
cores = [
'#f94144',
'#f8961e',
'#43aa8b',
'#90be6d',
'#577590',
'#d9ae94',
'#d08c60',
'#5c0099',
'#e40b0b',
'#208b3a',
'#c43240',
'#f20089',
'#b5c806',
'#066839',
'#8399a2',
'#00e9d8',
'#000000',
'#9b8074',
'#ce653b',
'#ffc462',
'#852170',
'#f20089',
'#208b3a',


]
def LinePlotSerieEvasãoSerieHistorica(dataset):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x = dataset['ano_saida'],
            y = dataset['status'],
            mode   = 'lines+markers',
            marker = dict(
                color="#8035fa"
            )
        )
    )

    fig.update_layout(
        plot_bgcolor = '#0E1117' ,
        template     ='simple_white',
        hovermode    ="x unified" ,
        width= 1300,
        xaxis=dict(
            linewidth = 2,
            linecolor ='white',  
      
        ),
        yaxis=dict(
            linewidth = 2,
            linecolor='white' , 
            gridcolor ='white',
            showgrid  =True   
        ),
        title=dict(
            text='Total de evasão na Universidade Federal do Ceará'
        )
    )
    return fig


def LinePlotSerieEvasãoPorUnidade(dataset:pd.DataFrame,Unidades):
    index = 0
    dataset['ano_saida'] = dataset['ano_saida'].astype(int)
    fig = go.Figure()

    if (len(Unidades)!=0):
        dataset = dataset.loc[
            dataset['nome_unidade'].isin(Unidades)
        ]

    for unidade in dataset['nome_unidade'].value_counts().index.to_list(): 
        data = dataset.loc[dataset['nome_unidade'] == unidade]

        fig.add_traces(
            go.Scatter(
                x = data['ano_saida'],
                y = data['status'],
                name = unidade,
                mode   = 'lines',
                marker = dict(
                    color=cores[index]
                ),
                hovertemplate='%{y}'
            )
        )
        index += 1

    fig.update_layout(

        template     ='seaborn',
        hovermode    ="x unified" ,
        width = 1300,
        height  = 500,
        xaxis=dict(
            linecolor ='white',
            gridcolor ='black',
            showgrid  =True               
        ),
        yaxis=dict(
            linecolor='white' , 
            gridcolor ='white',
            showgrid  =True   
        ),
        title=dict(
            text='Total de evasão na Universidade Federal do Ceará'
        ),
        hoverlabel=dict(
            bgcolor     ="white",
            font_size   =14,
            font_family ="Rockwell",
            font = dict(
                color='black'
            ),
        )
    )
    return fig

def SerieEvasãoCursoTotais(dataset):
    fig = go.Figure()

    fig.add_trace(
        go.Bar(  
            orientation = 'h',
            x = dataset['status'],
            y = dataset['nome_curso'],            
            marker=dict(
                color="#8035fa"
            ),
        )
    )
             
    fig.update_layout(
        plot_bgcolor = '#0E1117' ,
        template     ='simple_white',
        hovermode    ="y unified" , 
        
        width  = 900,

        ### Mudar o titulo
        title = dict(
            font = dict(
                family ='Fire Code',
                size   = 20
            ),
        text = 'Desistência de Alunos' 
        ),
        ### Font
        font = dict(
            family = 'Droid Sans Mono',
            size   = 14,
            color  = "black"
        ),

        ### eixos do grafico
        xaxis = dict(
            linewidth = 2,
            linecolor ='white'  
            
        ),
        yaxis = dict(
            linewidth = 2,
            linecolor = 'white'  
        )
    )
    return fig
