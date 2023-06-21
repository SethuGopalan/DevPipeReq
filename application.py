import dash
import dash_bootstrap_components as dbc
from dash import dcc,html,Dash



application=Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

server=application.server

application.layout=dbc.Container(

    [
        dbc.Row(
            [
                dbc.Col([

                    html.Div([

                        html.H1("DevWebApplication"),
                        html.P("Welcome to webapplication page"),
                        html.H2(" best web app")
                    ])
                ])
            ]
        )
    ]
)

if __name__ == "__main__":
    application.run(debug=True,port=8000)
