# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1regcFEndwcDIk90glJgrCrTGG2KaTcOO
"""

import dash_bootstrap_components as dbc
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from dash.dependencies import Input, Output
from google.colab import files
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate("/content/drive/My Drive/Colab Notebooks/data-analytics-1-a1fc9-firebase-adminsdk-7pw8e-d090a8ace0.json") #key connect database
firebase_admin.initialize_app(cred)
db = firestore.client()
app = dash.Dash(__name__, suppress_callback_exceptions=True,
                external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
])
 # home page
main = html.Div([
    html.Div([
      html.Div('Home page', style={'font-size': '60px','text-align': 'center','font-weight': 'bold',}),
      # another page
      html.Div([
        dcc.Link('Simple Chart', href='/matplotlib', style={'font-size': '30px'}),
        dcc.Link('Data Analysis', href='/data-analysis', style={'font-size': '30px'})
       ],style={'display': 'flex','justify-content': 'space-evenly',}),
      html.Div([
        html.Div([
            html.Div('Giới thiệu về project: ', style={'font-size': '25px','font-weight': 'bold',}),
            html.Div([
                html.Div( [
                    html.Div('- swazsxedrcftvgybhnujmik,lzsxedcrfvtgbhnjmksedfgbhnjmklxdfvgbhjmkldrgybhnujmikdcfgbhjkfghjk'),
                    html.Div('- dfghjfosidjfsdplf]sdlfodsjfwpo[flw[ef;d[fmosdjfkspodlfsd[lf')
                ]),
            ], className='row', style={ 'font-size': '18px' ,'border':'2px black solid','background-color': '#fefbd8'})
        ])
      ]),
      html.Br(),
      html.Div([
        html.Div([
            html.Div('About my team:', style={'font-size': '25px','font-weight': 'bold',}),
            html.Div([
                html.Div([
                  html.Div('Nguyễn Thế Đạt - 18036401'),
                  html.Div('Ngô Quang Long 18039011'),
                  html.Div('Lê Dĩ Khang - 18037851'),  
                  ],className='col-6'),
                html.Div( [
                  html.Div('Nguyễn Trần Nhật Hưng - 18036971'),
                  html.Div('Bùi Thành Nam - 18055471'),
                  html.Div('Nguyễn Thanh Hoài - 18052451'),   
                  html.Div('Lý Huỳnh Gia Thịnh - 18036741')       
                  ],className='col-6'),
                ], className='row',  style={ 'font-size': '18px' ,'border':'2px black solid','background-color': '#fefbd8'})
            ])
      ]),
    ],className='col-12 bg-light') 
],className='container')

##-----------------------------------------------------
#matplotlib Link
matplotlib = html.Div([
     # home page text
    html.Div([
        html.Div([
            html.Ul([
                dcc.Link('MATPLOTLIB', href="/matplotlib"),
                dcc.Link('Line Chart', href="/line-chart"),
                dcc.Link('Bar Chart', href="/bar-chart"),
                dcc.Link('Pie Chart', href="/pie-chart"),
                dcc.Link('Scatter Chart', href="/scatter-chart"),
            ],style={'display': 'flex','flex-direction': 'column','padding': '10px 20px','transition': '0.3s','border-bottom-right-radius': '5px','border-top-right-radius': '5px'})
        ],
        className='col-3 listContainer bg-light',style={'border':'2px black solid'}),
        html.Div([
            html.Div([
                html.Div('MATPLOTLIB',style={'text-align':'center','font-size':'40px','font-weight': 'bold'}),
                dcc.Link('Home Page', href="/",style={'font-size':'25px','display': 'flex','justify-content': 'space-evenly'}),
            ]),
            html.Div([
                 html.Span('Giới thiệu về Dash - Plotly:'),
                html.Span('Dash là một framework mã nguồn mở dành cho xây dựng ứng dụng phân tích dữ liệu mà không cần đến Ngôn ngữ JavaScript, và nó được tích hợp với thi viện Plotly - một thư viện đồ họa. '
                ,style={'margin-left': '30px'})
            ])
           
        ],className='col-9 bg-light',style={'border-radius': '3px','padding': '20px 40px'}),
    ], className = 'row')
], className='container')
state_list=['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Country_Of_Mexico','Delaware','District_Of_Columbia','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Missouri','Nevada','New_Hampshire','New_Jersey','New_Mexico','New_York','North_Carolina','North_Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode_Island','South_Carolina','South_Dakota','Tennessee','Texas','Utah','Virginia','Washington','Wisconsin','Wyoming']
docs =db.collection(u'linechart_AQI_year_CO').stream()
c=[]
year=[]
docsNO2 =db.collection(u'linechart_AQI_year_NO2').stream()
cNO2=[]
docsO3 =db.collection(u'linechart_AQI_year_O3').stream()
cO3=[]
docsSO2 =db.collection(u'linechart_AQI_year_SO2').stream()
cSO2=[]
for docO3 in docsO3:
  cO3.append(docO3.to_dict())
for docSO2 in docsSO2:
  cSO2.append(docSO2.to_dict())
for docNO2 in docsNO2:
  cNO2.append(docNO2.to_dict())
for doc in docs:
  c.append(doc.to_dict())
  year.append(doc.id)
y = [list() for x in range(47)]
yNO2 = [list() for x in range(47)]
yO3 = [list() for x in range(47)]
ySO2 = [list() for x in range(47)]
for i in range(16):
  for j in range(47):
    y[j].append(c[i][state_list[j]])
    yNO2[j].append(cNO2[i][state_list[j]])  
    yO3[j].append(cO3[i][state_list[j]])
    ySO2[j].append(cSO2[i][state_list[j]])
  figO3 = go.Figure()
  figCO = go.Figure()
  figO3 = go.Figure()
  figSO2 = go.Figure()
  figNO2 = go.Figure()
for k in range(46):
  figCO.add_trace(go.Scatter(x=year, y=y[k],mode='lines',name=state_list[k]))
  figNO2.add_trace(go.Scatter(x=year, y=yNO2[k],mode='lines',name=state_list[k]))
  figO3.add_trace(go.Scatter(x=year, y=yO3[k],mode='lines',name=state_list[k]))
  figSO2.add_trace(go.Scatter(x=year, y=ySO2[k],mode='lines',name=state_list[k]))
figCO.update_layout(title='Biểu đồ đường CO AQI của các State',
                      xaxis_title='year',
                      yaxis_title='Mean AQI')




  
  
figNO2.update_layout(title='Biểu đồ đường NO2 AQI của các State',
                      xaxis_title='year',
                      yaxis_title='Mean AQI')
figO3.update_layout(title='Biểu đồ đường O3 AQI của các State',
                      xaxis_title='year',
                      yaxis_title='Mean AQI')
figSO2.update_layout(title='Biểu đồ đường SO2 AQI của các State',
                      xaxis_title='year',
                      yaxis_title='Mean AQI')
docs =db.collection(u'pie_and_line_mean_AQI_2000_2016').stream()
c=[]
year=[]
meana=[]
meanb=[]
meanc=[]
meand=[]
for doc in docs:
    c.append(doc.to_dict())
    year.append(doc.id)
y = [list() for x in range(17)]
for i in range(17):
    meana.append(c[i]['mean_AQI_CO'])
    meanb.append(c[i]['mean_AQI_NO2'])
    meanc.append(c[i]['mean_AQI_O3'])
    meand.append(c[i]['mean_AQI_SO2'])
figmean=go.Figure()
figmean.add_trace(go.Scatter(x=year, y=meana,mode='lines',name ='mean_AQI_CO' ))
figmean.add_trace(go.Scatter(x=year, y=meanb,mode='lines',name ='mean_AQI_NO2' ))
figmean.add_trace(go.Scatter(x=year, y=meanc,mode='lines',name ='mean_AQI_O3' ))
figmean.add_trace(go.Scatter(x=year, y=meand,mode='lines',name ='mean_AQI_SO2' ))
figmean.update_layout(title='Biểu đồ đường mean của các khí ',
                      xaxis_title='year',
                      yaxis_title='Mean AQI')
# Line Chart 
lineChart = html.Div([
     # home page text
    html.Div([
        html.Div([
            html.Ul([
                dcc.Link('MATPLOTLIB', href="/matplotlib"),
                dcc.Link('Line Chart', href="/line-chart"),
                dcc.Link('Bar Chart', href="/bar-chart"),
                dcc.Link('Pie Chart', href="/pie-chart"),
                dcc.Link('Scatter Chart', href="/scatter-chart"),
            ],style={'display': 'flex','flex-direction': 'column','padding': '10px 20px','transition': '0.3s','border-bottom-right-radius': '5px','border-top-right-radius': '5px'})
        ],
        className='col-3 listContainer bg-light',style={'border':'2px black solid'}),
        html.Div([
            html.Div([
                html.Div('Line Chart',style={'text-align':'center','font-size':'40px','font-weight': 'bold'}),
                dcc.Link('Home Page', href="/",style={'font-size':'25px','display': 'flex','justify-content': 'space-evenly'}),
            ]),
            html.Div([
                html.Span('Mô tả:'),html.Br(),
                html.Span('Đây là dạng biểu đồ để thể hiện tiến trình phát triển, động thái phát triển của một đối tượng hay một nhóm đối tượng nào đó qua thời gian. Vì vậy với các bài vẽ biểu đồ đường thường có các cụm từ thể hiện sự phát triển, tốc độ tăng trưởng… với các mốc thời gian nhất định.'
                ,style={'margin-left': '30px'})
            ]),
            html.Div([
                 html.Span('Sử dụng khi nào?:'),html.Br(),
                html.Span('Line chart (biểu đồ đường): được sử dụng khi dữ liệu được mô tả phụ thuộc vào thời gian với trục hoành biểu diễn thời gian và trục tung biểu diễn đại lượng.'
                ,style={'margin-left': '30px'})
            ]),
            html.Div([
                html.Div('CO:', className='col-3  line-chart'),
                html.Div(
                dcc.Graph(figure=figCO), 
                )
            ], className='row'),

             html.Div([
                html.Div('NO2:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure=figNO2),
                )
            ], className='row'),
            html.Div([
                html.Div('O3:', className='col-3  line-chart'),
                html.Div(
                     dcc.Graph(figure=figO3),
                )
            ], className='row'),
            html.Div([
                html.Div('SO2:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure=figSO2),
                )
            ], className='row'),
            html.Div([
                html.Div('Mean theo nam:', className='col-3  line-chart'),
                html.Div(
                    dcc.Graph(figure=figmean),
                )
            ], className='row')
    
        ],className='col-9 bg-light',style={'border-radius': '3px','padding': '20px 40px'}),
    ], className = 'row')
], className='container')




# # Bar Chart 
barChart = html.Div([
     # home page text
    html.Div([
        html.Div([
            html.Ul([
                dcc.Link('MATPLOTLIB', href="/matplotlib"),
                dcc.Link('Line Chart', href="/line-chart"),
                dcc.Link('Bar Chart', href="/bar-chart"),
                dcc.Link('Pie Chart', href="/pie-chart"),
                dcc.Link('Scatter Chart', href="/scatter-chart"),
            ],style={'display': 'flex','flex-direction': 'column','padding': '10px 20px','transition': '0.3s','border-bottom-right-radius': '5px','border-top-right-radius': '5px'})
        ],
        className='col-3 listContainer bg-light',style={'border':'2px black solid'}),
        html.Div([
            html.Div([
                html.Div('Bar Chart',style={'text-align':'center','font-size':'40px','font-weight': 'bold'}),
                dcc.Link('Home Page', href="/",style={'font-size':'25px','display': 'flex','justify-content': 'space-evenly'}),
            ]),
            html.Div([
                html.Span('Mô tả:'),html.Br(),
                html.Span('Dạng biểu đồ này được thể hiện động thái phát triển, so sánh tương quan về độ lớn giữa các đại lượng hoặc thể hiện một thành phần cơ cấu trong một tổng thể.'
                ,style={'margin-left': '30px'})
            ]),
            html.Div([
                html.Span('Sử dụng khi nào?:'),html.Br(),
                html.Span('Bar chart (biểu đồ cột): thường được dùng khi cần phân loại dữ liệu và so sánh độ tương quản giữa chúng '
                ,style={'margin-left': '30px'})
            ]),
            html.Div([
                 html.Span('Type of Charts:')
            ]),
            html.Div([
                html.Div('Type 1:'),
              html.Div([

    dcc.Dropdown(id='dropdown', options=[
            {'label': 'Bar2000', 'value': 'Bar2000'},
            {'label': 'Bar2001', 'value': 'Bar2001'},
            {'label': 'Bar2002', 'value': 'Bar2002'},
            {'label': 'Bar2003', 'value': 'Bar2003'},
            {'label': 'Bar2004', 'value': 'Bar2004'},
            {'label': 'Bar2005', 'value': 'Bar2005'},
            {'label': 'Bar2006', 'value': 'Bar2006'},
            {'label': 'Bar2007', 'value': 'Bar2007'},
            {'label': 'Bar2008', 'value': 'Bar2008'},
            {'label': 'Bar2009', 'value': 'Bar2009'},
            {'label': 'Bar2010', 'value': 'Bar2010'},
            {'label': 'Bar2011', 'value': 'Bar2011'},
            {'label': 'Bar2012', 'value': 'Bar2012'},
            {'label': 'Bar2013', 'value': 'Bar2013'},
            {'label': 'Bar2014', 'value': 'Bar2014'},
            {'label': 'Bar2015', 'value': 'Bar2015'},
            {'label': 'Bar2016', 'value': 'Bar2016'},
          ], placeholder="chon nam",
            value='Bar2000'),
    dcc.Graph(id='graph-court')

    ], style={'padding-right': '5px','padding-left': '5px'})
            ]),
        ],className='col-9 bg-light',style={'border-radius': '3px'}),
    ], className = 'row')
], className='container')


@app.callback(Output('graph-court', 'figure'), 
              [Input('dropdown', 'value')])

def update_graph(selected_value):
  if selected_value ==  'Bar2000':
    docs = db.collection(u'barchart_AQI_State_2000').stream()
  elif selected_value== 'Bar2001':
    docs = db.collection(u'barchart_AQI_State_2001').stream()
  elif selected_value== 'Bar2002':
    docs = db.collection(u'barchart_AQI_State_2002').stream()
  elif selected_value== 'Bar2003':
    docs = db.collection(u'barchart_AQI_State_2003').stream()
  elif selected_value== 'Bar2004':
    docs = db.collection(u'barchart_AQI_State_2004').stream()
  elif selected_value== 'Bar2005':
    docs = db.collection(u'barchart_AQI_State_2005').stream()
  elif selected_value== 'Bar2006':
    docs = db.collection(u'barchart_AQI_State_2006').stream()
  elif selected_value== 'Bar2007':
    docs = db.collection(u'barchart_AQI_State_2007').stream()
  elif selected_value== 'Bar2008':
    docs = db.collection(u'barchart_AQI_State_2008').stream()
  elif selected_value== 'Bar2009':
    docs = db.collection(u'barchart_AQI_State_2009').stream()
  elif selected_value== 'Bar2010':
    docs = db.collection(u'barchart_AQI_State_2010').stream()
  elif selected_value== 'Bar2011':
    docs = db.collection(u'barchart_AQI_State_2011').stream()
  elif selected_value== 'Bar2012':
    docs = db.collection(u'barchart_AQI_State_2012').stream()
  elif selected_value== 'Bar2013':
    docs = db.collection(u'barchart_AQI_State_2013').stream()
  elif selected_value== 'Bar2014':
    docs = db.collection(u'barchart_AQI_State_2014').stream()
  elif selected_value== 'Bar2015':
    docs = db.collection(u'barchart_AQI_State_2015').stream()
  elif selected_value== 'Bar2016':
    docs = db.collection(u'barchart_AQI_State_2016').stream()
  c=[]
  for doc in docs:
    c.append(doc.to_dict())
  state_list=[]
  AQI_NO2=[]
  AQI_O3=[]
  AQI_SO2=[]
  AQI_CO=[]
  for i in range(len(c)):
    state_list.append(c[i]['state'])
    AQI_NO2.append(c[i]['mean_AQI_NO2'])
    AQI_O3.append(c[i]['mean_AQI_O3'])
    AQI_SO2.append(c[i]['mean_AQI_SO2'])
    AQI_CO.append(c[i]['mean_AQI_CO'])
  data=[
                {'x': state_list, 'y': AQI_NO2 , 'type': 'bar', 'name': 'AQI NO2'},
                {'x': state_list, 'y': AQI_O3, 'type': 'bar', 'name': 'AQI_O3'},
                {'x': state_list, 'y': AQI_SO2, 'type': 'bar', 'name': 'AQI_SO2'},
                {'x': state_list, 'y': AQI_CO, 'type': 'bar', 'name': 'AQI_CO'},
            ]
  b=data   
  fig = go.Figure()
  fig.add_bar(x=b[0]["x"],y=b[0]["y"],name=b[0]["name"])
  fig.add_bar(x=b[1]["x"],y=b[1]["y"],name=b[1]["name"])
  fig.add_bar(x=b[2]["x"],y=b[2]["y"],name=b[2]["name"])
  fig.add_bar(x=b[3]["x"],y=b[3]["y"],name=b[3]["name"])
  return fig

docs =db.collection(u'pie_and_line_mean_AQI_2000_2016').stream()
c=[]
for doc in docs:
  c.append(doc.to_dict())
  year.append(doc.id)
y = [list() for x in range(17)]
for i in range(17):
  y[i].append(c[i]['mean_AQI_CO'])
  y[i].append(c[i]['mean_AQI_NO2'])
  y[i].append(c[i]['mean_AQI_O3'])
  y[i].append(c[i]['mean_AQI_SO2'])
## pie chart
pieChart = html.Div([
     # home page text
    
    html.Div([
        html.Div([
            html.Ul([
                dcc.Link('MATPLOTLIB', href="/matplotlib"),
                dcc.Link('Line Chart', href="/line-chart"),
                dcc.Link('Bar Chart', href="/bar-chart"),
                dcc.Link('Pie Chart', href="/pie-chart"),
                dcc.Link('Scatter Chart', href="/scatter-chart"),
            ],style={'display': 'flex','flex-direction': 'column','padding': '10px 20px','transition': '0.3s','border-bottom-right-radius': '5px','border-top-right-radius': '5px'})
        ],
        className='col-3 listContainer bg-light',style={'border':'2px black solid'}),
        html.Div([
            html.Div([
                html.Div('Pie Chart',style={'text-align':'center','font-size':'40px','font-weight': 'bold'}),
                dcc.Link('Home Page', href="/",style={'font-size':'25px','display': 'flex','justify-content': 'space-evenly'}),
            ]),
            html.Div([
                html.Span('Mô tả:'),html.Br(),
                html.Span('Đây là dạng biểu đồ thường được dùng để vẽ các biểu đồ liên quan đến cơ cấu, tỷ lệ các thành phần trong một tổng thể chung hoặc cũng có thể vẽ biểu đồ tròn khi tỷ lệ % trong bảng số liệu cộng lại tròn 100.'
                ,style={'margin-left': '30px'})
            ]),
            html.Div([
                html.Span('Sử dụng khi nào?:'),html.Br(),
                html.Span('Pie chart (biểu đồ tròn) được sử dụng khi cần biểu diễn dữ liệu dưới dạng % '
                ,style={'margin-left': '30px'})
            ]),
            html.Div([
                 html.Span('Type of Charts:')
            ]),
            html.Div([
                html.Div('Type 1:', className='col-3  line-chart'),
                html.Div([ dcc.Dropdown(id='dropdown2', options=[
            {'label': 'pie2000', 'value': 'pie2000'},
            {'label': 'pie2001', 'value': 'pie2001'},
            {'label': 'pie2002', 'value': 'pie2002'},
            {'label': 'pie2003', 'value': 'pie2003'},
            {'label': 'pie2004', 'value': 'pie2004'},
            {'label': 'pie2005', 'value': 'pie2005'},
            {'label': 'pie2006', 'value': 'pie2006'},
            {'label': 'pie2007', 'value': 'pie2007'},
            {'label': 'pie2008', 'value': 'pie2008'},
            {'label': 'pie2009', 'value': 'pie2009'},
            {'label': 'pie2010', 'value': 'pie2010'},
            {'label': 'pie2011', 'value': 'pie2011'},
            {'label': 'pie2012', 'value': 'pie2012'},
            {'label': 'pie2013', 'value': 'pie2013'},
            {'label': 'pie2014', 'value': 'pie2014'},
            {'label': 'pie2015', 'value': 'pie2015'},
            {'label': 'pie2016', 'value': 'pie2016'},
          ], placeholder="chon nam",
            value='pie2000'),
    dcc.Graph(id='graph-court2')
                ],style={'padding-right': '5px','padding-left': '5px'})
            ]),
        ],className='col-9 bg-light',style={'border-radius': '3px','padding': '20px 40px'}),
    ], className = 'row')
], className='container')
@app.callback(Output('graph-court2', 'figure'), 
              [Input('dropdown2', 'value')])

def update_graph2(selected_value):
  docs =db.collection(u'pie_and_line_mean_AQI_2000_2016').stream()
  c=[]
  for doc in docs:
    c.append(doc.to_dict())
    year.append(doc.id)
  y = [list() for x in range(17)]
  for i in range(17):
    sum=c[i]['mean_AQI_CO']+c[i]['mean_AQI_NO2']+c[i]['mean_AQI_O3']+c[i]['mean_AQI_SO2']
    y[i].append(c[i]['mean_AQI_CO']/sum)
    y[i].append(c[i]['mean_AQI_NO2']/sum)
    y[i].append(c[i]['mean_AQI_O3']/sum)
    y[i].append(c[i]['mean_AQI_SO2']/sum)
  Air = ['CO', 'NO2', 'O3','SO2']
  fig = go.Figure()
  if selected_value ==  'pie2000':
    fig.add_trace(go.Pie(labels=Air, values=y[0], name="Trung bình khínam2000"))
  elif selected_value ==  'pie2001':
    fig.add_trace(go.Pie(labels=Air, values=y[1], name="Trung bình khínam2001"))
  elif selected_value ==  'pie2002':
    fig.add_trace(go.Pie(labels=Air, values=y[2], name="Trung bình khínam2002"))
  elif selected_value ==  'pie2003':
    fig.add_trace(go.Pie(labels=Air, values=y[3], name="Trung bình khínam2003"))
  elif selected_value ==  'pie2004':
    fig.add_trace(go.Pie(labels=Air, values=y[4], name="Trung bình khínam2004"))
  elif selected_value ==  'pie2005':
    fig.add_trace(go.Pie(labels=Air, values=y[5], name="Trung bình khínam2005"))
  elif selected_value ==  'pie2006':
    fig.add_trace(go.Pie(labels=Air, values=y[6], name="Trung bình khínam2006"))
  elif selected_value ==  'pie2007':
    fig.add_trace(go.Pie(labels=Air, values=y[7], name="Trung bình khínam2007"))
  elif selected_value ==  'pie2008':
    fig.add_trace(go.Pie(labels=Air, values=y[8], name="Trung bình khínam2008"))
  elif selected_value ==  'pie2009':
    fig.add_trace(go.Pie(labels=Air, values=y[9], name="Trung bình khínam2009"))
  elif selected_value ==  'pie2010':
    fig.add_trace(go.Pie(labels=Air, values=y[10], name="Trung bình khínam2010"))
  elif selected_value ==  'pie2011':
    fig.add_trace(go.Pie(labels=Air, values=y[11], name="Trung bình khínam2011"))
  elif selected_value ==  'pie2012':
    fig.add_trace(go.Pie(labels=Air, values=y[12], name="Trung bình khínam2012"))
  elif selected_value ==  'pie2013':
    fig.add_trace(go.Pie(labels=Air, values=y[13], name="Trung bình khínam2013"))
  elif selected_value ==  'pie2014':
    fig.add_trace(go.Pie(labels=Air, values=y[14], name="Trung bình khínam2014"))
  elif selected_value ==  'pie2015':
    fig.add_trace(go.Pie(labels=Air, values=y[15], name="Trung bình khínam2015"))
  elif selected_value ==  'pie2016':
    fig.add_trace(go.Pie(labels=Air, values=y[16], name="Trung bình khínam2016"))
  return fig


#scatter charts
scatterChart = html.Div([
     # home page text
    
    html.Div([
        html.Div([
            html.Ul([
                dcc.Link('MATPLOTLIB', href="/matplotlib"),
                dcc.Link('Line Chart', href="/line-chart"),
                dcc.Link('Bar Chart', href="/bar-chart"),
                dcc.Link('Pie Chart', href="/pie-chart"),
                dcc.Link('Scatter Chart', href="/scatter-chart"),
            ],style={'display': 'flex','flex-direction': 'column','padding': '10px 20px','transition': '0.3s','border-bottom-right-radius': '5px','border-top-right-radius': '5px'})
        ],
        className='col-3 listContainer bg-light',style={'border':'2px black solid'}),
        html.Div([
            html.Div([
                html.Div('Scatter chart',style={'text-align':'center','font-size':'40px','font-weight': 'bold'}),
                dcc.Link('Home Page', href="/",style={'font-size':'25px','display': 'flex','justify-content': 'space-evenly'}),
            ]),
            html.Div([
                html.Span('Mô tả:'),html.Br(),
                html.Span('Biểu đồ phân tán trong tiếng Anh là Scatter diagram. Biểu đồ phân tán thực chất là một đồ thị biểu hiện mối tương quan giữa nguyên nhân và kết quả hoặc giữa các yếu tố ảnh hưởng đến chất lượng.'
                ,style={'margin-left': '30px'})
            ]),
            html.Div([
                html.Span('Sử dụng khi nào?:'),html.Br(),
                html.Span('Scatter chart (biểu đồ phân tán) thường được sử dụng để thể hiện mối tương quan giữa các yếu tố trên đồ thị. '
                ,style={'margin-left': '30px'})
            ]),
            html.Div([
                 html.Span('Type of Charts:')
            ]),
            html.Div([
                html.Div('Type 1:', className='col-3  line-chart'),
                html.Div(
                    
                )
            ], className='row'),

             html.Div([
                html.Div('Type 2:', className='col-3  line-chart'),
                html.Div(
                    
                )
            ], className='row'),
            
    
        ],className='col-9 bg-light',style={'border-radius': '3px','padding': '20px 40px'}),
    ], className = 'row')
], className='container')





##---------------------------------------------------------
DataAnalysis = html.Div([
     # home page text
    html.Div([
        html.Div([
            html.Div([
                html.Div('Data Analysis', style={'font-size':'60px','text-align':'center','font-weight': 'bold'}),
                dcc.Link('Home Page', href="/",style={'font-size':'30px','text-align':'center'}),
            ], style={'text-align':'center'}),
            html.Br(),
            html.Br(),
            html.Div([
                 html.Span('- Dữ liệu thu thập được:'),
                 html.Div('dữ liệu thứ cấp'
                 , style={'margin-left': '30px'})
            ]),
             html.Div([
                 html.Span('- Định nghĩa các biến số:'),
                 html.Div([
                          html.Div('gss_code: (Government Statistical Service code): mã dịch vụ thống kê của chính phủ'),
                          html.Div('component: dân số'),
                          html.Div('year: năm'),
                          html.Div('Births:  sinh'),
                          html.Div('Deaths: tử'),
                          html.Div('international_in: nhập cư'),
                          html.Div('international_out: xuất cư'),
                          html.Div('domestic_in: trong nước'),
                          html.Div('domestic_out: ngoài nước'),
                          html.Div('district: thành phố'),
                          html.Div('sex: giới tính'),
                          html.Div('age: tuổi'),
                          html.Div('2010, 2011,... 2050: các năm dự đoán')]
                          , style={'margin-left': '30px'})  
            ]),
             html.Div([
                 html.Span('- Dạng dữ liệu:'),
                 html.Div([
                           html.Div('Định tính: sex, district, component '),
                           html.Div('Định lượng: age, 2010, 2011, … 2050, year, births, deaths, international_in, international_out, domestic_in, domestic_out')]
                          ,style={'margin-left': '30px'})
            ]),
             html.Div([
                 html.Span('- Thang do cho dữ liệu: '),
                 html.Div([
                          html.Div('Thang do định danh (norminal): district, sex, component ',className='content'),
                          html.Div('Thang đo khoảng( (interval): 2010, 2011,… 2050 ,year, births, deaths, international_in, international_out, domestic_in, domestic_out ',className='content')]
                          ,style={'margin-left': '30px'})
            ]),
             html.Div([
                 html.Span('- Kiểu dữ liệu: '),
                 html.Div([
                          html.Div('String: District, component,sex. '),
                          html.Div('Integer: Age. '),
                          html.Div('Decimal: 2010, 2011, 2012,.. 2050 year, births, deaths, international_in, international_out, domestic_in, domestic_out ',className='content')]
                          ,style={'margin-left': '30px'})
            ]),
             html.Div([
                 html.Span('- Mục tiêu nghiên cứu: ', className='introMatplotlib'),
                 html.Div('nghiên cứu về dân số cùa thành phố london cùng với các thành phố khác trong khu vực và dự đoán dân số. '
                 ,style={'margin-left': '30px'})
            ]),
             html.Div([
                 html.Span('- Phạm vi nghiên cứu:'),
                 html.Div('10 năm sau ( 2020 -> 2031 ).'
                 ,style={'margin-left': '30px'})
            ]),
             html.Div([
                 html.Span('- Nhóm biến tham gia quá trình nghiên cứu:'),
                 html.Div('district, sex, age, 2020,… 2031, births, deaths '
                 ,style={'margin-left': '30px'})
            ])
        ],className='col-12 bg-light',style={'border-radius': '3px','padding': '20px 40px'}),
    ], className = 'row')
], className='container')



##---------------------------------------------------------
# and this code to transfer to another link
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/matplotlib':
        return matplotlib
    elif pathname == '/line-chart':
        return lineChart
    elif pathname =='/bar-chart':
        return barChart
    elif pathname =='/pie-chart':
        return pieChart
    elif pathname =='/scatter-chart':
        return scatterChart
    elif pathname =='/data-analysis':
        return DataAnalysis
    else:
        return main

server = app.server

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
