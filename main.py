from dash import Dash, dcc, _dash_renderer,html, callback, Input, Output

from  src.backend.static import (
    SerieHistoricaDesistencias,
    FormaDeEntrada,
    PorSexo,
    MediaAprovados,
    CancelamentoMatricular,
    RelacaoAnoEntradaSaida,
    TaxaCancelamento
)

from src.plots.static import (
    SerieHistoricaDesistenciasPlot,
    FormaDeEntradaPlot,
    PorSexoPlot,
    MediaAprovadosPlot,
    CancelamentoMatricularPlot,
    RelacaoAnoEntradaSaidaPlot,
    TaxaCancelamentoPlot
)

import dash_mantine_components as dmc

_dash_renderer._set_react_version('18.2.0')


app = Dash(__name__, external_stylesheets=[dmc.styles.ALL])
#---------------------
from nbconvert import HTMLExporter

file = 'ClassificacaoSK\\Classficacao.ipynb'

exporter = HTMLExporter()
markup, _ = exporter.from_filename(file)

#--------------------------------------------
figS = SerieHistoricaDesistenciasPlot(SerieHistoricaDesistencias())


figCota = CancelamentoMatricularPlot(CancelamentoMatricular())
figBarCota = RelacaoAnoEntradaSaidaPlot(RelacaoAnoEntradaSaida())
configs = {'displaylogo': False, 'displayModeBar':False}



#---Dashboard---

dashboard = dmc.Grid([
    dmc.GridCol([
        #---- Barra iterativa
        dmc.Paper([
            dmc.Grid([ 
                dmc.GridCol([
                    dmc.RangeSlider(minRange=0, 
                                    max=2023, 
                                    min=1948, 
                                    step=1, 
                                    value=[1978,2023], id="ano-slider", labelAlwaysOn=True),
                ], span=4, style={'margin-top': '35px'}),

                dmc.GridCol([
                    dmc.MultiSelect(
                        label="Selecione o Status",
                        value=['Cancelado', 'Ativo', 'Concluído', 'Trancado'],  
                        data =[
                            {'label': 'Cancelado', 'value':'Cancelado'},
                            {'label': 'Ativo'     , 'value':'Ativo'},
                            {'label': 'Concluido' , 'value':'Concluido'},
                            {'label': 'Trancado'  , 'value':'Trancado'},
                        ],
                        id="status-select" 
                    )
                ], span=4),

                dmc.GridCol([
                    dmc.MultiSelect(
                        label="Selecione o Status",
                        value=['SISU', 'VESTIBULAR'],  
                        data =[
                            {'label': 'Seleção SISU', 'value':'SISU'},
                            {'label': 'Vestibular'  , 'value':'VESTIBULAR'},
                        ],
                        id="modo-entrada-select" 
                    )
                ], span=4)
            ], gutter={ "base": 5, "xs": "md", "md": "xl", "xl": 400 })

        ], p="xs", shadow="sm", style={'margin-top': '10px'}),        
    ]),
    dmc.GridCol([
        dmc.Grid([
            dmc.GridCol([
                dmc.Paper([
                    dcc.Graph(id='graph11-selection',  config= configs)
                ], p="xs", shadow="xl", mt="md", withBorder=True)
            ], span=4),
            dmc.GridCol([
                dmc.Paper([
                    dcc.Graph(id='graph12-selection',  config=configs)
                ], p="xs", shadow="xl", mt="md", withBorder=True)
            ], span=4),
                      dmc.GridCol([
                dmc.Paper([
                    dcc.Graph(id='graph13-selection',  config=configs)
                ], p="xs", shadow="xl", mt="md", withBorder=True)
            ], span=4)
        ], style={'margin-top': '0px'})
    ]),
    dmc.GridCol([
        dmc.Grid([
            dmc.GridCol([
                dmc.Paper([
                    dcc.Graph(id='table',  config= configs)
                ], p="xs", shadow="xl", mt="md", withBorder=True)
            ], span=4),
            dmc.GridCol([
                dmc.Paper([
                    dcc.Graph(figure=figCota)
                ], p="xs", shadow="xl", mt="md", withBorder=True)
            ], span=8),
            dmc.GridCol([
                dmc.Paper([
                    dcc.Graph(figure=figBarCota,  config= configs)
                ], p="xs", shadow="xl", mt="md", withBorder=True)
            ], span=12)
        ], style={'margin-top': '0px'})
    ])
])

#------------------------------------------
app.layout = dmc.MantineProvider([
    html.Div([
        dmc.Paper([
            dmc.Title("Dashboard Universidade Federal do Ceará", order=3),
        ], p="md", mb="md", shadow="xs"),


        dmc.Tabs([
            dmc.TabsList([
                dmc.TabsTab('Home', value='home'),
                dmc.TabsTab('Série Historica', value='serie-historica'),
                dmc.TabsTab('Projeto ML', value='projetoML'),
            ]),

            # Dashboard iterativa
            dmc.TabsPanel([dashboard], value='home'),


            # Série Historica
            dmc.TabsPanel([
                dmc.Grid([
                    dmc.GridCol([
                        dmc.Paper(dcc.Graph(figure=figS,  config= {'displaylogo': False}),p="xs", shadow="xl", mt="md", withBorder=True)
                    ], span=12)
                ])
            ], value='serie-historica'),
            dmc.TabsPanel([
               html.Iframe(srcDoc=markup, style={'width': '100%', 'height': '1000px'})
            ], value='projetoML')
        ], color="red", value="dashboard"),



    ], style={'padding': '10px'})
])

#-------------------------------
@callback(
    Output(component_id='graph11-selection', component_property='figure'),
    Input(component_id='ano-slider', component_property='value'),
    Input(component_id='status-select', component_property='value'),
    Input(component_id='modo-entrada-select', component_property='value'),
)
def update_graph11(ano_slider_name, status_select_name, modo_entrada_select_name):
    
    data = FormaDeEntrada(ano_slider_name, status_select_name, modo_entrada_select_name)
    return FormaDeEntradaPlot(data)

#------------------------
@callback(
    Output(component_id='graph12-selection', component_property='figure'),
    Input(component_id='ano-slider', component_property='value'),
    Input(component_id='status-select', component_property='value'),
    Input(component_id='modo-entrada-select', component_property='value'),
)
def update_graph12(ano_slider_name, status_select_name, modo_entrada_select_name):
    fig = PorSexoPlot(PorSexo(ano_slider_name, status_select_name, modo_entrada_select_name))
    return fig


#--------------------
@callback(
    Output(component_id='graph13-selection', component_property='figure'),
    Input(component_id='ano-slider', component_property='value'),
    Input(component_id='status-select', component_property='value'),
    Input(component_id='modo-entrada-select', component_property='value'),
)
def update_graph13(ano_slider_name, status_select_name, modo_entrada_select_name):
    fig = MediaAprovadosPlot(MediaAprovados(ano_slider_name, status_select_name, modo_entrada_select_name))
    return fig


@callback(
    Output(component_id='table', component_property='figure'),
    Input(component_id='ano-slider', component_property='value'),
    Input(component_id='modo-entrada-select', component_property='value'),
)
def update_table(ano_slider_name, modo_entrada_select_name):
    return TaxaCancelamentoPlot(TaxaCancelamento(ano_slider_name, modo_entrada_select_name))



if __name__ == '__main__':app.run_server(debug=True)