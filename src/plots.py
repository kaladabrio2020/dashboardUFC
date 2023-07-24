import plotly.express as px
import plotly.graph_objects as go

def BarplotDesistenciaAlunos(dataset):
    fig = go.Figure()

    fig.add_trace(
        go.Bar(  
            orientation = 'h',
            x = dataset['status'],
            y = dataset['nome_curso'],            
            text = dataset['status'],
            marker=dict(
                color="#f0be09"
            ),
        )
    )
             
    fig.update_layout(
        plot_bgcolor = '#ffffff' ,
        template  ='simple_white',
        hovermode ='x' , 

        width  = 900,
        height = 450,

        title = dict(
            font=dict(
                family='Fire Code',
                size=20
            ),
        text = 'Desistência de Alunos' 
        ),
             
        font=dict(
            family='Droid Sans Mono',
            size=14,
            color="black"
        ),
    )
    return fig


def BarplotDesistenciaGenero(dataset):
    index  = 0
    fig    = go.Figure()
    colors = ['#ff85a1','#73d2de'] 
    for genero in ['Feminino','Masculino']:
        data = dataset.loc[dataset['sexo'] == genero[0]]
        fig.add_trace(
            go.Bar(  
                orientation = 'h',
                name=genero,
                x = data['status'],
                y = data['nome_curso'],            
                text = data['status'],
                marker=dict(
                    color=colors[index]
                ),
            )
        )
        index +=1
          
    fig.update_layout(
        barmode='stack',
        plot_bgcolor = '#ffffff' ,
        template  ='simple_white',
        hovermode ='x' , 
        height = 520,
        title = dict(
            font=dict(
                family='Fire Code',
                size=20
            ),
        text = 'Desistência de Alunos' 
        ),      
        font=dict(
            family='Droid Sans Mono',
            size=14,
            color="black"
        ),
    )
    return fig


def PiePlotGeneroDesistencia(dataset):
    fig = go.Figure()

    fig.add_trace(
        go.Pie(
            labels=dataset['sexo'],  
            values=dataset['status'],
        )
    )
    fig.update_traces(
        marker=dict(
            colors=['#ff85a1','#73d2de']
            )
        )
    fig.update_layout(
        height=400,  
        width =350,
        title = dict(
            text ='Por gênero',
        )
    )
    return fig

def PiePlotIgressoDesistencia(dataset):
    print(dataset)
    if len(dataset.loc[dataset['modalidade_considerada']!='Nenhuma']) == 0:
        fig = px.pie(
            dataset,
            names ='forma_ingresso',
            values= 'status'
        )
    else:        
        fig = px.sunburst(
            dataset,
            path=['forma_ingresso','modalidade_considerada'],
            values  ='status'
        )
    return fig

