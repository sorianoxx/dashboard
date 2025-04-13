import dash
from dash import dcc, html

app = dash.Dash(__name__)


# Criando Aplicativo de Dashboard
app = dash.Dash(__name__)

# Definir o layout do Dashboard
app.layout = html.Div(
    children=[
        html.H1('Meu Dashboard'),
        dcc.Graph(
            id='Meu-Grafico',
            figure={
                'data': [  # Corrigido de 'Data' para 'data'
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Bar chart'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'line', 'name': 'Line chart'}
                ],
                'layout': {
                    'title': 'Titulo do Gráfico',
                    'xaxis': {'title': 'Eixo X'},  # Corrigido de 'x-axis' para 'xaxis'
                    'yaxis': {'title': 'Eixo Y'}
                }
            }
        )
    ]
)

# Executar Aplicativo
if __name__ == '__main__':
    app.run(debug=True)
