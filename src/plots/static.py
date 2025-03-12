import pandas as pd
import plotly.graph_objects as go


def SerieHistoricaDesistenciasPlot(data):
    fig = go.Figure(
        go.Scatter(
            x = data['ano_saida'],
            y = data['count'],
            fill='tozeroy',
            fillcolor='rgba(255, 99, 71, 0.422)'
        )
    )
    fig.update_traces(
        hovertemplate = '<b>Ano:%{x}<b><br>Desistencias:%{y}<br><extra></extra>',
        marker = dict(
            color = 'tomato'
        )
    )

    fig.update_layout(
        hovermode = 'x unified',
        template = 'simple_white',
        title    = dict(
            text = 'Série historica Desistência de Alunos'
        ),
        xaxis = dict(
            nticks = 7,
            title = dict(
                text=None
            )
        ),
        yaxis = dict(
            showgrid  = True, 
            gridwidth = 1,
            griddash  = 'dot',
            gridcolor = 'black',
            linecolor = 'white',
            title = dict(
                text = 'Quantidade' 
            )
        ),
        margin = dict(
            r = 20,
            b = 20
        ),
        height = 350,
        
    )
    return fig