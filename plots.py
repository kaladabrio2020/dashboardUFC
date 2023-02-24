import plotly.graph_objects as go
import random


def random_colors():
    files = open('colors.txt','r')
    lista = files.readlines()
    files.close()
    

    new_list = []
    for strings in lista:
        new_list.extend( (strings.replace('\n','')).split(',') )

    number = 0
    cores  = []
    while True:
        cor = random.choice(new_list)
        if cor not in cores: 
            cores.append(cor);number+=1
        if number == 8:
            break

    return cores


def grafico_1(dataframe):
    fig = go.Figure()
    fig.add_trace(
        go.Bar(  
            orientation = 'h',
            x = dataframe.cancelados.tolist(),
            y = dataframe['nome do curso'].tolist(),            
            text = dataframe.cancelados.tolist(),
            marker=dict(
                color="#7030a0"
            ),
        )
    )
        
        
    fig.update_layout(
        plot_bgcolor = '#ffffe6' ,
        template  ='simple_white',
        hovermode ='x' , 
        height    = 620,
              
        title = dict(
            font=dict(
                family='Fire Code',
                size=20
            ),
        text = 'Desistência de Alunos por sexo' 
        ),
             
        font=dict(
            family="Fira Code",
            size=13,
            color="black"
        ),
    );return fig


def grafico_2(dataframes):
    cor = ["#1a53ff"," #ff1a62"]
    fig = go.Figure()
    e = 0
    for dataframe in dataframes:
        fig.add_trace(
            go.Bar(  
                orientation = 'h',
                x = dataframe.cancelados.tolist(),
                y = dataframe['nome do curso'].tolist(),            
                text = dataframe.cancelados.tolist(),
                name = dataframe.sexo.tolist()[1],
                marker=dict(
                color =cor[e]
                ),
            )
        );e+=1
        

    fig.update_layout( 
        height    = 620,
        template  = 'simple_white', 
        barmode   = 'stack',
        hovermode = 'closest' ,

        title = dict(
            font=dict(
                family='Fire Code',
                size=20
            ),
            text = 'Desistência de Alunos por sexo' 
            ),
            font=dict(
                family="Fira Code",
                size=13,
                color="black"
            ),
            plot_bgcolor='#f2f2f2'                     
    );return fig



def grafico_3(df):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x = df.ano_saida.tolist(),
            y = df.cancelados.tolist(),
            mode  = 'lines+markers',
            marker= dict(
                    color='#ff1a62'
            )
            
        )
    )

    fig.update_layout( 
        height    = 620,
        template  = 'simple_white', 
        hovermode = 'x' ,

        title = dict(
            font=dict(
                family='Fire Code',
                size=20
            ),
            text = 'Desistência de Alunos por Ano' 
            ),
            font=dict(
                family="Fira Code",
                size=13,
                color="black"
            ),
            grid=dict(
                rows    =  1, 
                columns =  1,
            ),
            plot_bgcolor='#f2f2f2'                     
    );return fig



def grafico_4(dfs):
    cores = random_colors()

    fig = go.Figure()

    e = 0
    for df in dfs:

        fig.add_trace(
            go.Scatter(
                x = df.ano_saida.tolist(),
                y = df.cancelados.tolist(),
                name  = df.nome_unidade.tolist()[1],
                mode  = 'lines+markers',
                marker= dict(
                    color=cores[e]
                )
            )
        );e+=1


    fig.update_layout( 
        height    = 620,
        template  = 'simple_white', 
        hovermode = 'x unified' ,

        title = dict(
            font=dict(
                family='Fire Code',
                size=20
            ),
            text = 'Desistência de Alunos por Ano' 
            ),
            font=dict(
                family="Fira Code",
                size=13,
                color="black"
            ),
            grid=dict(
                rows    =  1, 
                columns =  1,
            ),
            plot_bgcolor='#FFFFFF'                     
    )

    fig.update_yaxes( 
        tickprefix="$", showgrid=True , dividercolor='black'
    )
    return fig
