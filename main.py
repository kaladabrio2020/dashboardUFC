from dash import Dash, dcc, _dash_renderer

import dash_mantine_components as dmc


app = Dash(__name__, external_stylesheets=[dmc.styles.ALL])

app.layout = dmc.MantineProvider([
    
])

if __name__ == '__main__':
    app.run_server(debug=True)