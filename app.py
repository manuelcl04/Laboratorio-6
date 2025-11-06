import plotly as pl
import plotly.express as px
import numpy as np
import pandas as pd
import pathlib
import dash
import dash_bootstrap_components as dbc
#para hacer dashboards
from dash import Dash,dcc,html,Input,Output
from dash import dash_table


df=pd.read_excel("edadmedia.xlsx")

#dashboards financiera

#paso 1 inciar dash
app=dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

#git
server=app.server

app.title="Dashboard Financiero"


sales_list=["Guatemala","Escuintla","Quetzaltenango","Sololá","Quiche"]

#app layout
app.layout=html.Div([
    #linea al incio del dashboard con todos los dropdowns y filtros:
    html.Div([
        #html del segundo dropdown para elegir variable numerica a ver en el dashboard
        html.Div(dcc.Dropdown(
            id="numericdropdown",value="Guatemala",clearable=False,
            options=[{"label":x,"value":x} for x in sales_list], multi=True),className="six columns",
                 style={"width":"50%"})],className="row"),

    #html de las graficas
    html.Div([dcc.Graph(id="line",figure={})])

    ])

#paso 3 callback para actualizar las graficas y la tabla

@app.callback(
    #output: las 2 graficas actializadas y la tabla
    [Output("line","figure")],
    [Input("numericdropdown","value")]
)

#paso 4: definicion de las funciones para armar las graficas y la tabla

def display_value(selected_numeric):
  #seleccionar empresas

  #primera grafica de lineas con empresas selecionadas

  fig=px.line(df,x="Year",markers=True,y=selected_numeric,
              width=1000,height=500)

  #hacer titulo de la grafica variable

  fig.update_layout(title=f"{selected_numeric}",
                    xaxis_title="Year")

  fig.update_traces(line=dict(width=2))#ancho de lineas, si no, usa default

  return [fig]


#Paso 5
if __name__=="__main__":
    app.run(debug=False, host="0.0.0.0",port=10000)
