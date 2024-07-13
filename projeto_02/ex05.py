#Faça um programa que crie um dashboard

import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import webbrowser
from threading import Timer

# Leia os dados do arquivo Excel
excel_file = 'tabela_despesas_gastos.xlsx'
df_2022 = pd.read_excel(excel_file, sheet_name='2022')
df_2023 = pd.read_excel(excel_file, sheet_name='2023')
df_2024 = pd.read_excel(excel_file, sheet_name='2024')
df_pendentes = pd.read_excel(excel_file, sheet_name='PENDENTES 2023 e 2024')

# Inicialize o app Dash
app = dash.Dash(__name__)

# Layout do dashboard
app.layout = html.Div([
    html.H1("Dashboard de Dados Excel"),
    dcc.Dropdown(
        id='year-dropdown',
        options=[
            {'label': '2022', 'value': '2022'},
            {'label': '2023', 'value': '2023'},
            {'label': '2024', 'value': '2024'},
            {'label': 'PENDENTES 2023 e 2024', 'value': 'PENDENTES'}
        ],
        value='2022'
    ),
    dcc.Graph(id='line-chart')
])

# Callback para atualizar o gráfico
@app.callback(
    Output('line-chart', 'figure'),
    Input('year-dropdown', 'value')
)
def update_chart(selected_year):
    if selected_year == '2022':
        df = df_2022
    elif selected_year == '2023':
        df = df_2023
    elif selected_year == '2024':
        df = df_2024
    else:
        df = df_pendentes

    # Gráfico de barras colorido
    fig = px.bar(df, x='Data', y='Valor', title=f'Dados de {selected_year}', color='Data')
    return fig

# Função para abrir o navegador automaticamente
def open_browser():
    webbrowser.open_new("http://127.0.0.1:8050/")

# Execute o app
if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run_server(debug=True)
