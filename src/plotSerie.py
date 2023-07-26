import plotly.express as px
import plotly.graph_objects as go

def LinePlotSerieEvasãoPorUnidade(dataset):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x = dataset['ano_saida'],
            y = dataset['status'],
            mode='lines+markers',
        )
    )

    fig.update_layout(
        plot_bgcolor = '#0E1117' ,
        template     ='simple_white',
        hovermode    ="x unified" ,

        xaxis=dict(
            linewidth = 2,
            linecolor ='white'  
            
        ),
        yaxis=dict(
            linewidth = 2,
            linecolor='white'  
        ),
        title=dict(
            text='Total de evasão na Universidade federal do ceara'
        )
    )
    return fig