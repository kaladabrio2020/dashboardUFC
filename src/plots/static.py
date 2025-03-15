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
        hovertemplate = '<br>Cancelamentos:%{y}<br><extra></extra>',
        marker = dict(
            color = 'tomato'
        )
    )

    fig.update_layout(
        hovermode = 'x unified',
        template = 'simple_white',
        title    = dict(
            text = 'Série historica Cancelamento de Matricula',
            font = dict(
                weight="bold",   
                size=16
            ),
            automargin=True,
        ),
        xaxis = dict(
            nticks = 7,
            title = dict(
                text=None, 
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
        font = dict(
            family="Inter, sans-serif",
        )
        
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
                size = 16,
                family="Inter, sans-serif",
                weight="bold"   
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
        ),
        font = dict(
            family="Inter, sans-serif",
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
        dragmode = False,
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
                size=16,
                family="Inter, sans-serif",
                weight="bold"   
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
        ),
        font = dict(
            family="Inter, sans-serif",
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
    fig.update_traces(
        hovertemplate = '%{meta[0]}<br>Quantidade:%{y}<br><extra></extra>',
    )
    fig.update_layout(
        dragmode = False,
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
            text = 'Média Tempo de Forma de ingresso',
            font = dict(
                size=16,
                family="Inter, sans-serif",
                weight="bold"  
            ),
            automargin=True
        ),
        yaxis = dict(
            visible = False
        ),
        legend = dict(
            font = dict(
                size = 10
            )  
        ),
        barmode='stack',
        hovermode = 'x unified',
        hoverlabel = dict(
            bgcolor = 'white',
            font  = dict(
                size = 12
            ),
            align = 'right',
        ),
        font = dict(
            family="Inter, sans-serif",
        )
    )
    return fig



def CancelamentoMatricularPlot(data):
    fig = go.Figure()

    for name_ in data['modalidade_considerada'].unique():
        subset = data[data['modalidade_considerada'] == name_].sort_values(by='ano_saida')
        meta_  = subset['nome_mobilidadade_considerada'].unique()[0] 
        fig.add_trace(
            go.Scatter(
                x = subset['ano_saida'],
                y = subset['count'],
                mode = 'lines',
                name = name_,
                meta = [meta_, name_],
            )
        )
    fig.update_traces(
        hovertemplate = '<b>%{meta[0]} (%{meta[1]})<b> - %{y}<extra></extra>',
        hoverlabel = dict(
            font = dict(
                size = 16
            )
        )
    )
    
    fig.update_layout(
        height = 350,
        hovermode = 'x unified',
        template = 'simple_white',
        margin = dict(
            r = 20,
            b = 10,
            l = 20,
            t = 50
        ),
        title = dict(
            text = 'Cancelamento Matriculas por Modalidade dos anos 2017 à 2023',
            font = dict(
                size=14,
                family="Inter, sans-serif",
                weight="bold"  
            ),
            automargin=True
        ),
        yaxis = dict(
            showgrid = True
        ),
        legend = dict(
            font = dict(
                size = 12
            ),
            borderwidth = 0,
            orientation = 'h',
            yanchor = 'top',
            xanchor = 'left',
            y = 1
        ),
        font = dict(
            family="Inter, sans-serif",
        )
    )
    return fig


def RelacaoAnoEntradaSaidaPlot(data):
    fig = go.Figure()
    order=['No mesmo ano', 'Primeiro ano', 'Segundo ano', 'Terceiro ano', 'Quarto ano', 'Quinto ano', 'Sexto ano']   
    colors = px.colors.qualitative.Dark24[0:10]

    for name_, c in zip(data['modalidade_considerada'].unique(), colors):
        subset = data[data['modalidade_considerada'] == name_]
        meta_  = subset['nome_mobilidadade_considerada'].unique()[0]
        fig.add_trace(
            go.Bar(
                x = subset['ano_de_cancelamento'],
                y = subset['count'],
                name = name_,
                meta = [meta_],
                marker = dict(
                    color = c
                )
            )
        )
    fig.update_traces(
        hovertemplate = '<extra></extra>%{meta[0]}<br> <b>%{y}</b>',
        hoverlabel = dict(
            font = dict(
                size =14
            )

        )
    )
 
    fig.update_layout(
        height = 350,
        dragmode = False,
        hovermode = 'x unified',
        template = 'simple_white',
        xaxis = dict(
            categoryorder='array', 
            categoryarray=list(order)
        ),
        yaxis = dict(
            showgrid = True
        ),
        margin = dict(
            r = 10,
            b = 10,
            l = 10,
            t = 50
        ),
        title = dict(
            text = 'Relação entre Ano de Entrada e Ano de Saida',
            font = dict(
                size=14,
                family="Inter, sans-serif",
                weight="bold"
            ),
            automargin=True
        ),
        legend = dict(
            y = 1,
            x = 0.85,
            title = dict(
                text = 'Modalidade',
            )
        ),
        font = dict(
            family="Inter, sans-serif",
        )
    )
    return fig
       

def TaxaCancelamentoPlot(data):
    fig = go.Figure(
        go.Table(
            header = dict(
                values = ['Curso', 'Taxa de Cancelamento'],
                line_color = '#732c2c',
                fill_color = '#732c2c',
                align = ['left', 'left'],
                font = dict(color = 'white', size = 14),
                height = 30
            ),
            cells = dict(
                values = [data['nome_curso'], data['taxa_cancelamento']],
                line_color = '#732c2c',
                fill_color = 'white',
                font = dict(color = 'black', size = 14),
                align = ['left', 'left'],
            ),
        )
    )
    fig.update_layout(
        height = 350,
        margin = dict(
            l = 5,
            r = 5,
            t = 30,
            b = 0
        ),
        title = dict(
            text = 'Top 8 Cursos com Taxa de Cancelamento',
            font = dict(
                size=16,
                color='black',
                family="Inter, sans-serif",
                weight="bold"
            ),
            automargin=True
        ),
        font = dict(
            family="Inter, sans-serif",
        )
    )
    return fig