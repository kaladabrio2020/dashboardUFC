from dash import Dash, dcc, _dash_renderer,html

from  src.backend.static import (
    SerieHistoricaDesistencias
)

from src.plots.static import (
    SerieHistoricaDesistenciasPlot
)
import dash_mantine_components as dmc

_dash_renderer._set_react_version('18.2.0')


app = Dash(__name__, external_stylesheets=[dmc.styles.ALL])
#--------------------------------------------
figS = SerieHistoricaDesistenciasPlot(SerieHistoricaDesistencias())





#---Dashboard---

dashboard = dmc.Grid([
    dmc.GridCol([
        #---- Barra iterativa
        dmc.Paper([
            dmc.Grid([ 
                dmc.GridCol([
                    dmc.RangeSlider(minRange=0, 
                                    max=2023, 
                                    min=1978, 
                                    step=1, 
                                    value=[1978,2023], id="ano-slider", labelAlwaysOn=True),
                ], span=4, style={'margin-top': '35px'}),

                dmc.GridCol([
                    dmc.MultiSelect(
                        label="Selecione o Status",
                        value=['Cancelado', 'Ativo', 'Mobilidade', 'Trancado'],   
                    )
                ], span=4),

                dmc.GridCol([
                    dmc.MultiSelect(
                        label="Selecione o Status",
                        value=['Seleção SISU', 'Vestibular'],   
                    )
                ], span=4)
            ], gutter={ "base": 5, "xs": "md", "md": "xl", "xl": 400 })

        ], p="xs", shadow="xl", style={'margin-top': '10px'}),        
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
            ]),

            # Dashboard iterativa
            dmc.TabsPanel([dashboard], value='home'),

            # Série Historica
            dmc.TabsPanel([
                dmc.Grid([
                    dmc.GridCol([
                        dmc.Paper(dcc.Graph(figure=figS),p="xs", shadow="xl", mt="md", withBorder=True)
                    ], span=6)
                ])
            ], value='serie-historica'),
        ], color="red", value="dashboard"),



    ], style={'padding': '10px'})
])

if __name__ == '__main__':
    app.run_server(debug=True)