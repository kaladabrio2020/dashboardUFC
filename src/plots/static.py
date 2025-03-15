import pandas as pd
import plotly.express as px
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
            text = 'Série historica Cancelamento de Matricula',
            automargin=True,
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
            b = 20,
            t = 20,
        ),
        height = 350,
        
    )
    return fig

def FormaDeEntradaPlot(data):
    data['forma_ingresso'] = data['forma_ingresso'].str.title()
    fig = go.Figure()
    color = ['#bad9b5', '#732c2c']

    for subset, c in zip(data['forma_ingresso'].unique(), color):
        fig.add_trace(
            go.Bar(
                x = data[data['forma_ingresso'] == subset]['status'],
                y = data[data['forma_ingresso'] == subset]['count'],
                name = subset,
                text = data[data['forma_ingresso'] == subset]['count'],
                textposition = 'auto',
                customdata  = [data[data['forma_ingresso'] == subset]['forma_ingresso']],
                marker_color = c,
                meta=[subset]

            )
        )
    fig.update_traces(
        hovertemplate = '<b>Status:%{x} - %{meta[0]}<b><br>Quantidade:%{y}<br><extra></extra>',
    )
    fig.update_layout(
        dragmode = False,
        height = 300,
        hovermode = 'x unified',
        template = 'simple_white',
        title    = dict(
            text = 'Distribuição de Status por Forma de Ingresso',
            font = dict(
                size = 14
            ),
            automargin=True,
        ),
        legend = dict(
            title = dict(
                text = None, 
            ),
            font = dict(
                size = 8
            ),
            orientation = 'h',
            yanchor = 'bottom',
            y = 1.02,
            xanchor = 'right',
            x = 1
        ),
        xaxis = dict(
            title = dict(
                text = None
            )
        ),
        yaxis = dict(
            title = dict(
                text = 'Quantidade',
                font = dict(
                    size = 8
                )
            )
        ),
        margin = dict(
            r = 20,
            b = 10,
            l = 0 ,
            t = 50
        )
    )
    return fig


def PorSexoPlot(data):
    data['forma_ingresso'] = data['forma_ingresso'].str.title()
    fig = px.sunburst(
        data, 
        path=['sexo', 'forma_ingresso', 'status'], 
        values='count',
        color_discrete_sequence=['lightskyblue', 'lightpink'],

    )
    fig.update_traces(
        textinfo = 'label+percent parent',
        texttemplate  ='%{label}<br>%{percentEntry}',
        hovertemplate = '<b>%{label}</b><br>Quantidade: %{value} (%{percentRoot:.2f})<extra></extra>',
        marker = dict(
            line = dict(
                width = 1,
                color = 'white'
            )
        )
    )
    fig.update_layout(
        height = 300,
        template = 'simple_white',
        uniformtext=dict(
            minsize=10, 
        ),
        margin = dict(
            r = 50,
            b = 10,
            l = 50,
            t = 50
        ),
        title = dict(
            text = 'Proporção por sexo e Forma de ingresso',
            font = dict(
                size = 14
            ),
            automargin=True
        ),
        hovermode = 'x',
        hoverlabel = dict(
            bgcolor = 'white',
            font  = dict(
                size = 12
            ),
            align = 'right',
        )
    )
    return fig



def MediaAprovadosPlot(data):
    data['forma_ingresso'] = data['forma_ingresso'].str.title()
    
    fig = go.Figure()
    color = ['#bad9b5', '#732c2c']

    for subset, c in zip(data['forma_ingresso'].unique(), color):
        fig.add_trace(
            go.Bar(
                x = data[data['forma_ingresso'] == subset]['status'],
                y = data[data['forma_ingresso'] == subset]['media'],
                name = subset,
                text = data[data['forma_ingresso'] == subset]['media'],
                textposition = 'auto',
                marker_color = c,
                customdata  = [data[data['forma_ingresso'] == subset]['forma_ingresso']],
                meta=[subset]

            )
        )
    fig.update_layout(
        height = 300,
        template = 'simple_white',
        uniformtext=dict(
            minsize=10, 
        ),
        margin = dict(
            r = 50,
            b = 10,
            l = 50,
            t = 50
        ),
        title = dict(
            text = 'Media Tempo de Forma de ingresso',
            font = dict(
                size = 14
            ),
            automargin=True
        ),
        yaxis = dict(
            visible = False
        ),
        barmode='stack',
        hovermode = 'x unified',
        hoverlabel = dict(
            bgcolor = 'white',
            font  = dict(
                size = 12
            ),
            align = 'right',
        )
    )
    return fig