import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_table
from dash.dependencies import Input, Output
import plotly.express as px

########### Define your variables
tabtitle='SERF: Parameter Space Testing'
########### Define your variables

#### Import Fit Data
##v1
ALL_data_fit_values = pd.read_csv('https://raw.githubusercontent.com/rach6230/Dash_app_Systematic_Testing/main/Full_fit_Data.csv')
#V2
ALL_data_fit_values_v2 = pd.read_csv('https://raw.githubusercontent.com/rach6230/Dash_app_Systematic_Testing/main/Full_fit_Data_V2.csv')
#V3
ALL_data_fit_values_v3 = pd.read_csv('https://raw.githubusercontent.com/rach6230/Dash_app_Systematic_Testing/main/M-LOOP/Full_fit_Data_V3.csv')
#V4
ALL_data_fit_values_v4 = pd.read_csv('https://raw.githubusercontent.com/rach6230/Dash_app_Systematic_Testing/main/M-LOOP/Full_fit_Data_V4.csv')
# 04-03-21 MLOOP-166-loop
ALL_data_fit_values_v5 = pd.read_csv('https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/04-03-21-Full_fit_Data.csv')
# 08-03-21 GA-50-sample
ALL_data_fit_values_v6 = pd.read_csv('https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/08-03-21-Full_fit_Data.csv')
# 12-03-21 MLOOP-500-loop
ALL_data_fit_values_v7 = pd.read_csv('https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/12-03-21-Full_fit_Data.csv')
# 14-03-21GA 200-loop
ALL_data_fit_values_v8 = pd.read_csv('https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/14-03-21-Full_fit_Data.csv')
# 15-03-21 Gradient 189 sample
ALL_data_fit_values_v9 = pd.read_csv('https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/15-03-21-Full_fit_Data.csv')
# 04-02-21 Systematic 512 sample
ALL_data_fit_values_v10 = pd.read_csv('https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/02-04-21-Full_fit_Data.csv')
## 2D 1D 
ALL_data_fit_values_v11 = pd.read_csv('https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/11-04-21-Full_fit_Data.csv')
ALL_data_fit_values_v12 = pd.read_csv('https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/10-04-21-Full_fit_Data.csv')
ALL_data_fit_values_v13 = pd.read_csv('https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/19-04-21-Full_fit_Data.csv')
ALL_data_fit_values_v14 = pd.read_csv('https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/21-04-21-Full_fit_Data.csv')
ALL_data_fit_values_v15 = pd.read_csv('https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/26-04-21-Full_fit_Data.csv')
ALL_data_fit_values_v16 = pd.read_csv('https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/09-05-21-Full_fit_Data.csv')
ALL_data_fit_values_v17 = pd.read_csv('https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/07-05-21-Full_fit_Data.csv')
ALL_data_fit_values_v18 = pd.read_csv('https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/10-05-21-Full_fit_Data.csv')
ALL_data_fit_values_v19 = pd.read_csv('https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/01-06-21-Full_fit_Data.csv')
ALL_data_fit_values_v20 = pd.read_csv('https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/01-06-21-LABVIEW-Full_fit_Data.csv')
ALL_data_fit_values_v21 = pd.read_csv('https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/23-06-21-Full_fit_Data.csv')
ALL_data_fit_values_v22 = pd.read_csv('https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/26-06-21-Full_fit_Data.csv')
ALL_data_fit_values_v23 = pd.read_csv('https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/06-08-21-Full_fit_Data.csv')
ALL_data_fit_values_v24 = pd.read_csv('https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/25-08-21-Full_fit_Data.csv')
ALL_data_fit_values_v25 = pd.read_csv('https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/30-08-21-Full_fit_Data.csv')
ALL_data_fit_values_v26 = pd.read_csv('https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/18-05-21-Full_fit_Data.csv')

#Cs
ALL_data_fit_values_v27 = pd.read_csv('https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/30-11-21-Full_fit_Data.csv')
ALL_data_fit_values_v28 = pd.read_csv('https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/02-12-21-Full_fit_Data.csv')
ALL_data_fit_values_v29 = pd.read_csv('https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/05-12-21-Full_fit_Data.csv')
ALL_data_fit_values_v30 = pd.read_csv('https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/07-12-21-Full_fit_Data.csv')
ALL_data_fit_values_v31 = pd.read_csv('https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/14-12-21-Full_fit_Data.csv')
#ALL_data_fit_values_v = pd.read_csv('')


# Create col of A/C:
ALL_data_fit_values["V/nT"] =  abs(ALL_data_fit_values['A'])/abs(ALL_data_fit_values['G2'])
ALL_data_fit_values["SE"] =  abs(ALL_data_fit_values['G2'])-abs(ALL_data_fit_values['G1'])
#V2
ALL_data_fit_values_v2["V/nT"] =  abs(ALL_data_fit_values_v2['A'])/abs(ALL_data_fit_values_v2['G2'])
ALL_data_fit_values_v2["SE"] =  abs(ALL_data_fit_values_v2['G2'])-abs(ALL_data_fit_values_v2['G1'])
#V3
ALL_data_fit_values_v3["V/nT"] =  abs(ALL_data_fit_values_v3['A'])/abs(ALL_data_fit_values_v3['G2'])
ALL_data_fit_values_v3["SE"] =  abs(ALL_data_fit_values_v3['G2'])-abs(ALL_data_fit_values_v3['G1'])
#V4
ALL_data_fit_values_v4["V/nT"] =  abs(ALL_data_fit_values_v4['A'])/abs(ALL_data_fit_values_v4['G2'])
ALL_data_fit_values_v4["SE"] =  abs(ALL_data_fit_values_v4['G2'])-abs(ALL_data_fit_values_v4['G1'])
# 04-03-21 MLOOP-166-loop
ALL_data_fit_values_v5["V/nT"] =  abs(ALL_data_fit_values_v5['A'])/abs(ALL_data_fit_values_v5['G2'])
ALL_data_fit_values_v5["SE"] =  abs(ALL_data_fit_values_v5['G2'])-abs(ALL_data_fit_values_v5['G1'])
# 08-03-21 GA-50-sample
ALL_data_fit_values_v6["V/nT"] =  abs(ALL_data_fit_values_v6['A'])/abs(ALL_data_fit_values_v6['G2'])
ALL_data_fit_values_v6["SE"] =  abs(ALL_data_fit_values_v6['G2'])-abs(ALL_data_fit_values_v6['G1'])
# 12-03-21 MLOOP-500-loop
ALL_data_fit_values_v7["V/nT"] =  abs(ALL_data_fit_values_v7['A'])/abs(ALL_data_fit_values_v7['G2'])
ALL_data_fit_values_v7["SE"] =  abs(ALL_data_fit_values_v7['G2'])-abs(ALL_data_fit_values_v7['G1'])
# 14-03-21GA 200-loop
ALL_data_fit_values_v8["V/nT"] =  abs(ALL_data_fit_values_v8['A'])/abs(ALL_data_fit_values_v8['G2'])
ALL_data_fit_values_v8["SE"] =  abs(ALL_data_fit_values_v8['G2'])-abs(ALL_data_fit_values_v8['G1'])
# 15-03-21 Gradient 189 sample
ALL_data_fit_values_v9["V/nT"] =  abs(ALL_data_fit_values_v9['A'])/abs(ALL_data_fit_values_v9['G2'])
ALL_data_fit_values_v9["SE"] =  abs(ALL_data_fit_values_v9['G2'])-abs(ALL_data_fit_values_v9['G1'])
# 04-02-21 Systematic 512 sample
ALL_data_fit_values_v10["V/nT"] =  abs(ALL_data_fit_values_v10['A'])/abs(ALL_data_fit_values_v10['G2'])
ALL_data_fit_values_v10["SE"] =  abs(ALL_data_fit_values_v10['G2'])-abs(ALL_data_fit_values_v10['G1'])
# 04-02-21 Systematic 512 sample
ALL_data_fit_values_v11["V/nT"] =  abs(ALL_data_fit_values_v11['A(1D)'])/abs(ALL_data_fit_values_v11['G(1D)'])
ALL_data_fit_values_v12["V/nT"] =  abs(ALL_data_fit_values_v12['A(1D)'])/abs(ALL_data_fit_values_v12['G(1D)'])
ALL_data_fit_values_v13["V/nT"] =  abs(ALL_data_fit_values_v13['A(1D)'])/abs(ALL_data_fit_values_v13['G(1D)'])
ALL_data_fit_values_v14["V/nT"] =  abs(ALL_data_fit_values_v14['A(1D)'])/abs(ALL_data_fit_values_v14['G(1D)'])
ALL_data_fit_values_v15["V/nT"] =  abs(ALL_data_fit_values_v15['A(1D)'])/abs(ALL_data_fit_values_v15['G(1D)'])
ALL_data_fit_values_v16["V/nT"] =  abs(ALL_data_fit_values_v16['A(1D)'])/abs(ALL_data_fit_values_v16['G(1D)'])
ALL_data_fit_values_v17["V/nT"] =  abs(ALL_data_fit_values_v17['A(1D)'])/abs(ALL_data_fit_values_v17['G(1D)'])
ALL_data_fit_values_v18["V/nT"] =  abs(ALL_data_fit_values_v18['A(1D)'])/abs(ALL_data_fit_values_v18['G(1D)'])
ALL_data_fit_values_v19["V/nT"] =  abs(ALL_data_fit_values_v19['A(1D)'])/abs(ALL_data_fit_values_v19['G(1D)'])
ALL_data_fit_values_v20["V/nT"] =  abs(ALL_data_fit_values_v20['A(1D)'])/abs(ALL_data_fit_values_v20['G(1D)'])
ALL_data_fit_values_v21["V/nT"] =  abs(ALL_data_fit_values_v21['A(1D)'])/abs(ALL_data_fit_values_v21['G(1D)'])
ALL_data_fit_values_v22["V/nT"] =  abs(ALL_data_fit_values_v22['A(1D)'])/abs(ALL_data_fit_values_v22['G(1D)'])
ALL_data_fit_values_v23["V/nT"] =  abs(ALL_data_fit_values_v23['A(1D)'])/abs(ALL_data_fit_values_v23['G(1D)'])
ALL_data_fit_values_v24["V/nT"] =  abs(ALL_data_fit_values_v24['A(1D)'])/abs(ALL_data_fit_values_v24['G(1D)'])
ALL_data_fit_values_v25["V/nT"] =  abs(ALL_data_fit_values_v25['A(1D)'])/abs(ALL_data_fit_values_v25['G(1D)'])
ALL_data_fit_values_v26["V/nT"] =  abs(ALL_data_fit_values_v26['A(1D)'])/abs(ALL_data_fit_values_v26['G(1D)'])

##Cs
ALL_data_fit_values_v27["V/nT"] =  abs(ALL_data_fit_values_v27['A(1D)'])/abs(ALL_data_fit_values_v27['G(1D)'])
ALL_data_fit_values_v28["V/nT"] =  (abs(ALL_data_fit_values_v28['A(1D)'])*2)/abs(ALL_data_fit_values_v28['G(1D)'])
ALL_data_fit_values_v29["V/nT"] =  (abs(ALL_data_fit_values_v29['A(1D)'])*2)/abs(ALL_data_fit_values_v29['G(1D)'])
ALL_data_fit_values_v30["V/nT"] =  (abs(ALL_data_fit_values_v30['A(1D)'])*2)/abs(ALL_data_fit_values_v30['G(1D)'])
ALL_data_fit_values_v31["V/nT"] =  (abs(ALL_data_fit_values_v31['A(1D)']))/abs(ALL_data_fit_values_v31['G(1D)'])

# list of all data frames
all_df=[ALL_data_fit_values_v5,ALL_data_fit_values_v6,ALL_data_fit_values_v7, ALL_data_fit_values_v8,
        ALL_data_fit_values_v9, ALL_data_fit_values_v10, ALL_data_fit_values_v11, ALL_data_fit_values_v12, 
        ALL_data_fit_values_v13,ALL_data_fit_values_v14, ALL_data_fit_values, ALL_data_fit_values_v2, ALL_data_fit_values_v3,
        ALL_data_fit_values_v4, ALL_data_fit_values_v15, ALL_data_fit_values_v16, ALL_data_fit_values_v17, 
        ALL_data_fit_values_v18,ALL_data_fit_values_v19, ALL_data_fit_values_v20, ALL_data_fit_values_v21, ALL_data_fit_values_v22,
        ALL_data_fit_values_v23,ALL_data_fit_values_v24,ALL_data_fit_values_v25, ALL_data_fit_values_v26,
        ALL_data_fit_values_v27,ALL_data_fit_values_v28,ALL_data_fit_values_v29,ALL_data_fit_values_v30,
        ALL_data_fit_values_v31]
  

## Load data for sliders/ tables
df = ALL_data_fit_values_v5
D1Ddf = ALL_data_fit_values_v11

# File names
Github_urls_v1= pd.read_csv("https://raw.githubusercontent.com/rach6230/Dash_app_Systematic_Testing/main/Data_pt2/Github_urls_sorted.csv")
#v2
Github_urls_v2 = pd.read_csv("https://raw.githubusercontent.com/rach6230/Dash_app_Systematic_Testing/main/Version_2_Data_1/Github_urls_sortedV2.csv")
#v3
Github_urls_v3 = pd.read_csv("https://raw.githubusercontent.com/rach6230/Dash_app_Systematic_Testing/main/M-LOOP/Github_urls_sortedV3.csv")
#v4
Github_urls_v4 = pd.read_csv("https://raw.githubusercontent.com/rach6230/Dash_app_Systematic_Testing/main/M-LOOP/Github_urls_sortedV4.csv")
# 04-03-21 MLOOP-166-loop
Github_urls_v5 = pd.read_csv("https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/04-03-21-Github_urls_sorted.csv")
# 08-03-21 GA-50-sample
Github_urls_v6 = pd.read_csv("https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/08-03-21Github_urls_sorted.csv")
# 12-03-21 MLOOP-500-loop
Github_urls_v7 = pd.read_csv("https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/12-03-21_Github_urls_sorted.csv")
# 14-03-21GA 200-loop
Github_urls_v8 = pd.read_csv("https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/14-03-21_Github_urls_sorted.csv")
# 15-03-21 Gradient 189 sample
Github_urls_v9 = pd.read_csv("https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/15-03-21_Github_urls_sorted.csv")
# 04-02-21 Systematic 512 sample
Github_urls_v10 = pd.read_csv("https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/02-04-21_Github_urls_sorted.csv")
## 2D
Github_urls_v11 = pd.read_csv("https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/11-04-21_Github_urls_sorted.csv")
Github_urls_v12 = pd.read_csv("https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/10-04-21_Github_urls_sorted.csv")
Github_urls_v13 = pd.read_csv("https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/19-04-21_Github_urls_sorted.csv")
Github_urls_v14 = pd.read_csv("https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/21-04-21_Github_urls_sorted.csv")
Github_urls_v15 = pd.read_csv("https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/26-04-21_Github_urls_sorted.csv")
Github_urls_v16 = pd.read_csv("https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/09-05-21_Github_urls_sorted.csv")
Github_urls_v17 = pd.read_csv("https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/07-05-21_Github_urls_sorted.csv")
Github_urls_v18 = pd.read_csv("https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/10-05-21_Github_urls_sorted.csv")
Github_urls_v19 = pd.read_csv("https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/01-06-21_Github_urls_sorted.csv")
Github_urls_v20 = pd.read_csv("https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/01-06-21_Github_urls_sorted.csv")
Github_urls_v21 = pd.read_csv("https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/23-06-21_Github_urls_sorted.csv")
Github_urls_v22 = pd.read_csv("https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/26-06-21_Github_urls_sorted.csv")
Github_urls_v23 = pd.read_csv("https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/06-08-21_Github_urls_sorted.csv")
Github_urls_v24 = pd.read_csv("https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/25-08-21_Github_urls_sorted.csv")
Github_urls_v25 = pd.read_csv("https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/30-08-21_Github_urls_sorted.csv")
Github_urls_v26 = pd.read_csv("https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/30-08-21_Github_urls_sorted.csv")

#Cs
Github_urls_v27 = pd.read_csv("https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/30-11-21_Github_urls_sorted.csv")
Github_urls_v28 = pd.read_csv("https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/02-12-21_Github_urls_sorted.csv")
Github_urls_v29 = pd.read_csv("https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/05-12-21_Github_urls_sorted.csv")
Github_urls_v30 = pd.read_csv("https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/07-12-21_Github_urls_sorted.csv")
Github_urls_v31 = pd.read_csv("https://raw.githubusercontent.com/rach6230/Dash_app_V2/main/Data/Fit_and_Link_References/14-12-21_Github_urls_sorted.csv")
#Github_urls_v = pd.read_csv("")

# list of all data frames
all_git_df=[Github_urls_v5, Github_urls_v6, Github_urls_v7, Github_urls_v8,Github_urls_v9,
            Github_urls_v10, Github_urls_v11, Github_urls_v12, Github_urls_v13, Github_urls_v14,
            Github_urls_v1, Github_urls_v2, Github_urls_v3, Github_urls_v4, Github_urls_v15, Github_urls_v16,
            Github_urls_v17,Github_urls_v18, Github_urls_v19, Github_urls_v20, Github_urls_v21, Github_urls_v22,
            Github_urls_v23,Github_urls_v24,Github_urls_v25,Github_urls_v26,Github_urls_v27,
            Github_urls_v28, Github_urls_v29,Github_urls_v30,Github_urls_v31 ]


# Inital data to show (selected point)
x = 14

## Colour values
colors = {
    'background': '#f2f2f2',
    'text': '#7FDBFF'
}

## Version details
#Version = '''
#* **Cell**: Cs
#* **Coil Drivers**: DAQ
#* **Heater Driver**: MOSFET, 150kHz, square
#* **Heaters**: 1 x 8 Ohm (non-magnetic)'''


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle


########### Set up the layout
app.layout = html.Div(children=[
  html.Div(className='row',  # Define the row elemen
           children=[
             html.Div(className='three columns div-for-charts',
                      style={'backgroundColor': colors['background']},
                      children = [
                        html.H6('Filters'),
                        html.P('Parameter Range:'),
                        html.Div(id='TEMP_slider-drag-output', style={'margin-top': 20,'fontSize': 12}),
                        html.Div(id = 'Temp_slider_container'),
                        html.Div(id='LP_slider-drag-output', style={'margin-top': 20,'fontSize': 12}),
                        html.Div(id = 'LP_slider_container'),
                        html.Div(id='LD_slider-drag-output', style={'margin-top': 20,'fontSize': 12}),
                        html.Div(id = 'LD_slider_container'), 
                        html.Div([html.Div(id="V/nT_range_output"),
                                  html.Div(id = 'V/nT_range_container')]),                           
                        html.Br(), #new line
                        html.P('Fit filters:'), 
                        html.Div([html.Div(id="A_range_output"),
                                  html.Div(id = 'A_range_container')]),                           
                        html.Div([html.Div(id="G1_range_output"),
                                  html.Div(id = 'G1_range_container')]),  
                        html.Div([html.Div(id="G2_range_output"),
                                  html.Div(id = 'G2_range_container')]),   
                        html.Div([html.Div(id="G1_error_range_output"),
                                  html.Div(id = 'G1_error_range_container')]),  
                        html.Div([html.Div(id="G2_error_range_output"),
                                  html.Div(id = 'G2_error_range_container')]),                                  
                        html.Br(), #new line
                      ]
                     ),  # Define the 1st column
             html.Div(className='five columns div-for-charts',
                      children = [
                        html.H6('All Parameter Space Data'),
                        html.Div("Atomic Species:", style={'fontSize': 12}),
                        dcc.RadioItems(id='atomic_species_radioitem',
                                       options=[{"label": i, "value": i} for i in ["Cs", "Rb"]],
                                       value='Cs',
                                       inputStyle={"margin-left": "20px"}, # add space between radio items
                                       labelStyle={'display': 'inline-block'},
                                       style={'fontSize': 12}), 
                        html.Div("Data Set", style={'fontSize': 12}), 
                        html.Div(id="dataset_dropdown_container"),   
                        html.Div("Fit Values:", style={'fontSize': 12}),    
                        html.Div(id="value_dropdown_container"),                                  
                        dcc.Graph(id='graph-with-slider',config={'displayModeBar': True}),
                        html.Br(), #new line
                        html.Div(id='HanleScanType', style={'fontSize': 12}),                          
                        html.Div(id='totalpoints', style={'fontSize': 12}),  
                        html.H6('Single Parameter Space Point Data'),
                        html.Div(id='click-data', style={'fontSize': 12}),
                        html.Div(id='hide_3D_table_box',
                                     children = [
                                         html.P('3D Fit values'),
                                         dash_table.DataTable(id='my-table',
                                                              style_cell={'textAlign': 'left', 'font_size': '10px'},
                                                              columns=[{"name": i, "id": i} for i in df.columns[19:20]]+[{"name": i, "id": i} for i in df.columns[0:7]]),
                                         html.Br(), #new line
                                         html.P('3D Fit Error Values'),  
                                         dash_table.DataTable(id='my-table2',
                                                              style_cell={'textAlign': 'left', 'font_size': '10px'},
                                                              columns=[{"name": i, "id": i} for i in df.columns[7:14]]),  
                                         html.Br(), #new line  
                                     ]
                                ), 
                          html.Div(id='hide_2D_1D_table_box',
                                     children = [
                                         html.P('1D Fit values'),
                                         dash_table.DataTable(id='2D1D-my-table',
                                                              style_cell={'textAlign': 'left', 'font_size': '10px'},
                                                              columns=[{"name": i, "id": i} for i in D1Ddf.columns[28:29]]+[{"name": i, "id": i} for i in D1Ddf.columns[7:14]]),
                                         html.Br(), #new line
                                         html.P('2D Fit values'), 
                                         dash_table.DataTable(id='2D1D-my-table2',
                                                              style_cell={'textAlign': 'left', 'font_size': '10px'},
                                                              columns=[{"name": i, "id": i} for i in D1Ddf.columns[15:26]]),  
                                         html.Br(), #new line  
                                     ]
                                ), 
                          #html.P('Experiment Version Details:'),
                          #dcc.Markdown(Version, style={'fontSize': 12}),  
                          #html.P('Data Set Details:'),
                          #dcc.Markdown(id='Markdown_notes', style={'fontSize': 12}),  
                      ]
                     ),  # Define the 2nd column
               html.Div(className='four columns div-for-charts',
                        children = [
                            dcc.RadioItems(
                                id='value_dropdown_2',
                                options=[{"label": i, "value": i} for i in ["Hanle", "Plotter"]],
                                value='Hanle',
                                inputStyle={"margin-left": "20px"}, # add space between radio items
                                labelStyle={'display': 'inline-block'},
                                style={'fontSize': 12}
                                ), 
                            html.Div(id='hide_hanle_box',
                                     children = [
                                         html.H6('3-Axis Hanle'),
                                         html.P('For Single Parameter Space Point', style={'fontSize': 12}),
                                         html.Div(id='1D-title'),
                                         html.Div(id='hide_1D_scan'),
                                         html.Div(id='2D-title'),
                                         html.Div(id='2D-graph-container'),
                                         html.Div(id='facet-container'),
                                         html.Br(), #new line
                                         html.Div(id='radioitems-sensitivity-container'),
                                         html.Div(id='hide_hanle_box2',
                                                  children = [
                                                      html.H6('Single Axis Hanle'),
                                                      html.Div(id='click-data-2', style={'fontSize': 12}),
                                                      html.P('Transverse'),
                                                      dcc.Graph(id='click-data-4',config={'displayModeBar': False}),
                                                      html.P('Longitudinal'),
                                                      dcc.Graph(id='click-data-3',config={'displayModeBar': False}),  
                                                  ]
                                                 ),
                                         html.Div(id='hide_sensitivity-box',
                                                  children = [
                                                      html.H6('Sensitivity', id = 'sensitivity-title'),
                                                      html.Div(id='hide_sensitivity_scan'),                                                   
                                                  ]
                                                 ),   
                                         html.Div(id='hide_noise-box',
                                                  children = [
                                                      html.H6('Noise', id='noise-title'),
                                                      html.Div(id='hide_noise_scan')                                                      
                                                  ]
                                                 ),                                            
                                     ]
                                    ),       
                            html.Div(id='hide_plotter_box',
                                     children = [
                                         html.P('X'),
                                         html.Div(id='drop_down_custom1'),
                                         html.P('Y'),
                                         html.Div(id='drop_down_custom2'),
                                         html.P('Colour (optional)'),
                                         html.Div(id='drop_down_custom3'),
                                         dcc.Graph(id='custom_plot',config={'displayModeBar': True}),
                                         html.P('X-axis scale'),                                         
                                         dcc.RadioItems(
                                             id='x-axis-scale-radio',
                                             options=[{"label": i, "value": i} for i in ["Linear", "Log"]],
                                             value='Linear',
                                             inputStyle={"margin-left": "20px"}, # add space between radio items
                                             labelStyle={'display': 'inline-block'},
                                             style={'fontSize': 12}),
                                         html.P('Y-axis scale'),
                                         dcc.RadioItems(
                                             id='y-axis-scale-radio',
                                             options=[{"label": i, "value": i} for i in ["Linear", "Log"]],
                                             value='Linear',
                                             inputStyle={"margin-left": "20px"}, # add space between radio items
                                             labelStyle={'display': 'inline-block'},
                                             style={'fontSize': 12}),  
                                         html.P('colour-axis scale'),
                                         dcc.RadioItems(
                                             id='colour-axis-scale-radio',
                                             options=[{"label": i, "value": i} for i in ["Linear", "Log"]],
                                             value='Linear',
                                             inputStyle={"margin-left": "20px"}, # add space between radio items
                                             labelStyle={'display': 'inline-block'},
                                             style={'fontSize': 12}),                                           
                                     ]
                                    )
                      ]
                     ),  # Define the 3rd column
           ]
          )
]
)

##################### Call back for characterising data 3D or 2D/1D ########################
@app.callback(Output('HanleScanType', 'children'),
              Input('segselect', 'value'))
def update_figure(data_version):
  if data_version == 0 or data_version == 1 or data_version ==2 or data_version ==3 or data_version == 4 or data_version ==5 or data_version == 10 or data_version == 11 or data_version == 12 or data_version == 13 :        
    A = 'Scan Type = 3D'
  if data_version ==6 or data_version == 7 or data_version == 8 or data_version == 9 or data_version == 14 or data_version == 15 or data_version == 16 or data_version == 17 or data_version == 25 or data_version == 18 or data_version == 19 or data_version == 20 or data_version == 21 or data_version == 22 or data_version == 23 or data_version == 24 or data_version == 26  or data_version == 27  or data_version == 28 or data_version == 29 or data_version == 30:  
    A = 'Scan Type = 2D/1D'
  return A


## Callback for hiding sensitivity and noise titles
@app.callback(
    Output('noise-title', 'style'),
    Input('HanleScanType', 'children'))
def show_hide_element(scan_type):
    if scan_type == 'Scan Type = 2D/1D': 
        return {'display': 'block'}
    if scan_type == 'Scan Type = 3D': 
        return {'display': 'none'}     

@app.callback(
    Output('sensitivity-title', 'style'),
    Input('HanleScanType', 'children'))
def show_hide_element(scan_type):
    if scan_type == 'Scan Type = 2D/1D': 
        return {'display': 'block'}
    if scan_type == 'Scan Type = 3D': 
        return {'display': 'none'}        
    

## Callback for hiding tables
@app.callback(Output('hide_3D_table_box', 'style'),         
              Input('HanleScanType', 'children'))
def show_hide_element(scan_type):
  if scan_type == 'Scan Type = 3D':
    return {'display': 'block'}
  if scan_type == 'Scan Type = 2D/1D': 
    return {'display': 'none'}

## Callback for hiding plotter
@app.callback(Output('hide_2D_1D_table_box', 'style'),         
              Input('HanleScanType', 'children'))
def show_hide_element(scan_type):
  if scan_type == 'Scan Type = 3D':
    return {'display': 'none'}
  if scan_type == 'Scan Type = 2D/1D': 
    return {'display': 'block'}
    
############ Callbacks for dropdowns for custom graph #############################
@app.callback(Output('drop_down_custom1', 'children'),
              Input('segselect', 'value'),
              Input('HanleScanType', 'children'))
def display_click_data(data_version, scan_type):
  df2 = all_df[data_version] 
  if scan_type == 'Scan Type = 3D':
    O = [{"label": i, "value": i} for i in df2.columns[0:21]]
  if scan_type == 'Scan Type = 2D/1D': 
    O = [{"label": i, "value": i} for i in df2.columns[0:27]]+[{"label": i, "value": i} for i in df2.columns[27:31]] 
  A =  dcc.Dropdown(id='x_value_dropdown',
                      options=O,
                      value='V/nT',
                      style={'fontSize': 12}),           
  return A

@app.callback(Output('drop_down_custom2', 'children'),
              Input('segselect', 'value'),
              Input('HanleScanType', 'children'))
def display_click_data(data_version, scan_type):
  df2 = all_df[data_version] 
  if scan_type == 'Scan Type = 3D':
    O = [{"label": i, "value": i} for i in df2.columns[0:21]]
  if scan_type == 'Scan Type = 2D/1D': 
    O = [{"label": i, "value": i} for i in df2.columns[0:27]]+[{"label": i, "value": i} for i in df2.columns[27:31]] 
  A =  dcc.Dropdown(id='y_value_dropdown',
                      options=O,
                      value='V/nT',
                      style={'fontSize': 12}),           
  return A

@app.callback(Output('drop_down_custom3', 'children'),
              Input('segselect', 'value'),
              Input('HanleScanType', 'children'))
def display_click_data(data_version, scan_type):
  df2 = all_df[data_version] 
  if scan_type == 'Scan Type = 3D':
    O = [{"label": i, "value": i} for i in df2.columns[0:21]]
  if scan_type == 'Scan Type = 2D/1D': 
    O = [{"label": i, "value": i} for i in df2.columns[0:27]]+[{"label": i, "value": i} for i in df2.columns[28:29]] 
  A =  dcc.Dropdown(id='z_value_dropdown',
                      options=O,
                      value='',
                      style={'fontSize': 12}),           
  return A
############ Callbacks for radio element of Dataset selection #############################
@app.callback(Output('dataset_dropdown_container', 'children'),
              Input('atomic_species_radioitem', 'value'))
def display_click_data(species):
  if species == 'Cs':
    A = dcc.Dropdown(
        id='segselect',
        options=[
            {'label': 'V1: Systematic Testing V1', 'value': 10},
            {'label': 'V1: Systematic Testing V2', 'value': 11},
            {'label': 'V1: M-LOOP V1', 'value': 12},
            {'label': 'V1: M-LOOP V2', 'value': 13},                            
            {'label': 'V2: M-LOOP (166 Loop, 04-03-21)', 'value': 0},
            {'label': 'V2: GA (50 sample, 08-03-21)', 'value': 1},
            {'label': 'V2: M-LOOP (500 sample, 12-03-21)', 'value': 2},
            {'label': 'V2: GA (200 sample, 14-03-21)', 'value': 3},  
            {'label': 'V2: Gradient (189 sample, 15-03-21)', 'value':4},    
            {'label': 'V2: Systematic (512 sample, 02-04-21)', 'value': 5}, 
            {'label': 'V2: GA (500 sample, 10-04-21)', 'value':7}, 
            {'label': 'V2: Gradient (492 sample, 11-04-21)', 'value':6}, 
            {'label': 'V2: GA (500 sample, 19-04-21)', 'value':8}, 
            {'label': 'V2: GA (500 sample, 21-04-21)', 'value':9},
            {'label': 'V2: GA (250 sample, 26-04-21)', 'value':14},
            {'label': 'V2: Gradient, V/nT (492 sample, 07-05-21)', 'value':16},
            {'label': 'V2: Gradient, sensitivity (492 sample, 09-05-21)', 'value':15},
            {'label': 'V2: GA, V/nT (500 sample, 10-05-21)', 'value':17},
            {'label': 'V2: MLOOP, V/nT (500 sample, 18-05-21)', 'value':25},
            {'label': 'V2: Systematic Testing (sample 3375, 01-06-21)', 'value': 18},
            #{'label': 'V2: Systematic Testing (sample 3375, 01-06-21) (LABIVEW fit)', 'value': 19},
            {'label': 'V2: Systematic Testing (sample 1350, 23-06-21) ', 'value': 20},
            {'label': 'V2: Systematic Testing (sample 363, 26-06-21, new PCB) ', 'value': 21},
            {'label': 'V2: PD benchmark v1 Gradient (36 sample, 06-08-21)', 'value': 22},
            {'label': 'V2: PD benchmark v2 Gradient (36 sample, 25-08-21)', 'value': 23},
            {'label': 'V2: Systematic (144 sample, 30-08-21)', 'value': 24}

        ],
        value=2)
  if species == 'Rb':
        A = dcc.Dropdown(
        id='segselect',
        options=[
            {'label': 'V1: Systematic, Temp vs Detuning (198 sample, 29-11-21)', 'value': 26},
            {'label': 'V1: Systematic, PID Temp vs Detuning (112 sample, 02-12-21)', 'value': 27},
            {'label': 'V1: Systematic, 3D (1451 sample, 05-12-21)', 'value': 28},
            {'label': 'V1: Systematic, Power vs Detuning (128 sample, 07-12-21)', 'value': 29},
            {'label': 'V1: M-LOOP (85 sample, 14-12-21)', 'value': 30}     
        ],
        value=26)     
  return A
############ Callbacks for radio element of 3D graph #############################
@app.callback(Output('value_dropdown_container', 'children'),
              Input('segselect', 'value'),
              Input('HanleScanType', 'children'))
def display_click_data(data_version, scan_type):
  df2 = all_df[data_version] 
  if scan_type == 'Scan Type = 3D':
    O = [{"label": i, "value": i} for i in df2.columns[19:21]]+[{"label": i, "value": i} for i in df2.columns[0:7]]
  if scan_type == 'Scan Type = 2D/1D': 
    O = [{"label": i, "value": i} for i in df2.columns[3:29]]
  A =  dcc.RadioItems(id='value_dropdown',
                      options=O,
                      value='V/nT',
                      inputStyle={"margin-left": "20px"}, # add space between radio items
                      labelStyle={'display': 'inline-block'},
                      style={'fontSize': 12}),           
  return A

    
    
############ Callbacks for slider containers #############################
# A
@app.callback(Output('A_range_container', 'children'),
              Input('segselect', 'value'),
              Input('HanleScanType', 'children'))
def display_click_data(data_version, scan_type):
  df2 = all_df[data_version]    
  if scan_type == 'Scan Type = 3D':
    A1 = 'A'
  if scan_type == 'Scan Type = 2D/1D': 
    A1 = 'A(1D)'   
  A = dcc.Input(id="A_min", type="number",debounce=True, value = df2[A1].min(), style={'width':'50%', 'fontSize': 12})
  B = dcc.Input(id="A_max", type="number",debounce=True, value = df2[A1].max(), style={'width':'50%', 'fontSize': 12})
  C = html.Div([A,
                B])  
  return C

# displaying values of A
@app.callback(
    Output("A_range_output", "children"),
    Input('segselect', 'value'),
    Input("A_min", "value"),
    Input("A_max", "value"),
    Input('HanleScanType', 'children'))
def number_render(data_version, A_min, A_max, scan_type):
  df2 = all_df[data_version]    
  if scan_type == 'Scan Type = 3D':
    A = 'A'
    TEXT = "Full A range: {} to {}"
  if scan_type == 'Scan Type = 2D/1D': 
    A = 'A(1D)'       
    TEXT ="Full A (1D) range: {} to {}"
  A = TEXT.format(round(df2[A].min(),3), round(df2[A].max(), 3))
  B = "Selected range: {} to {}".format(round(A_min, 3), round(A_max, 3))
  C = html.Div([
                html.Div(A, style={'margin-top': 20,'fontSize': 12}),
                html.Div(B, style={'fontSize': 12})])
  return C

# V/nT
@app.callback(Output('V/nT_range_container', 'children'),
              Input('segselect', 'value'))
def display_click_data(data_version):
  df2 = all_df[data_version]   
  A = dcc.Input(id="V/nT_min", type="number",debounce=True, value = df2['V/nT'].min(), style={'width':'50%', 'fontSize': 12})
  B = dcc.Input(id="V/nT_max", type="number",debounce=True, value = df2['V/nT'].max(), style={'width':'50%', 'fontSize': 12})
  C = html.Div([A,
                B])  
  return C

# displaying values of V/nT
@app.callback(
    Output("V/nT_range_output", "children"),
    Input('segselect', 'value'),
    Input("V/nT_min", "value"),
    Input("V/nT_max", "value"))
def number_render(data_version, VnT_min, VnT_max):
  df2 = all_df[data_version]    
  A = "Full V/nT range: {} to {}".format(round(df2['V/nT'].min(),3), round(df2['V/nT'].max(), 3))
  B = "Selected V/nT range: {} to {}".format(round(VnT_min, 3), round(VnT_max, 3))
  C = html.Div([
                html.Div(A, style={'margin-top': 20,'fontSize': 12}),
                html.Div(B, style={'fontSize': 12})])
  return C

## G1

@app.callback(Output('G1_range_container', 'children'),
              Input('segselect', 'value'),
              Input('HanleScanType', 'children'))
def display_click_data(data_version,scan_type):
  df2 = all_df[data_version]    
  if scan_type == 'Scan Type = 3D':
    G1 = 'G1'
  if scan_type == 'Scan Type = 2D/1D': 
    G1 = 'G(1D)'    
  A = dcc.Input(id="G1_min", type="number",debounce=True, value = df2[G1].min(), style={'width':'50%', 'fontSize': 12})
  B = dcc.Input(id="G1_max", type="number",debounce=True, value = df2[G1].max(), style={'width':'50%', 'fontSize': 12})
  C = html.Div([A,
                B])  
  return C



# displaying values of G1
@app.callback(
    Output("G1_range_output", "children"),
    Input('segselect', 'value'),
    Input("G1_min", "value"),
    Input("G1_max", "value"),
    Input('HanleScanType', 'children'))
def number_render(data_version, G1_min, G1_max, scan_type):
  df2 = all_df[data_version]     
  if scan_type == 'Scan Type = 3D':
    G1 = 'G1'
    TEXT = "Full G1 range: {} to {}"    
  if scan_type == 'Scan Type = 2D/1D': 
    G1 = 'G(1D)' 
    TEXT ="Full G (1D) range: {} to {}"
  A = TEXT.format(round(df2[G1].min(),5), round(df2[G1].max(),5))
  B = "Selected range: {} to {}".format(round(G1_min, 5), round(G1_max, 5))
  C = html.Div([
                html.Div(A, style={'margin-top': 20,'fontSize': 12}),
                html.Div(B, style={'fontSize': 12})])
  return C

# G2
@app.callback(Output('G2_range_container', 'children'),
              Input('segselect', 'value'),
              Input('HanleScanType', 'children'))
def display_click_data(data_version, scan_type):
  df2 = all_df[data_version]  
  if scan_type == 'Scan Type = 3D':
    G2 = 'G2'
    TEXT = "Full G2 range: {} to {}"    
  if scan_type == 'Scan Type = 2D/1D': 
    G2 = 'G2(2D)' 
  A = dcc.Input(id="G2_min", type="number",debounce=True, value = df2[G2].min(), style={'width':'50%', 'fontSize': 12})
  B = dcc.Input(id="G2_max", type="number",debounce=True, value = df2[G2].max(), style={'width':'50%', 'fontSize': 12})
  C = html.Div([A,
                B])  
     
  return C

# displaying values of G2
@app.callback(
    Output("G2_range_output", "children"),
    Input('segselect', 'value'),
    Input("G2_min", "value"),
    Input("G2_max", "value"),
    Input('HanleScanType', 'children'))
def number_render(data_version, G2_min, G2_max, scan_type):
  df2 = all_df[data_version]  
  if scan_type == 'Scan Type = 3D':
    G2 = 'G2'
    TEXT = "Full G2 range: {} to {}"    
  if scan_type == 'Scan Type = 2D/1D': 
    G2 = 'G2(2D)' 
    TEXT ="Full G2 (2D) range: {} to {}"    
  A = "Full G2 range: {} to {}".format(round(df2[G2].min(),5), round(df2[G2].max(),5))
  B = "Selected G2 range: {} to {}".format(round(G2_min, 5), round(G2_max, 5))
  C = html.Div([
                html.Div(A, style={'margin-top': 20,'fontSize': 12}),
                html.Div(B, style={'fontSize': 12})])
  return C

## G1 error_

#@app.callback(Output('G1_error_range_container', 'children'),
#              Input('segselect', 'value'))
#def display_click_data(data_version):
#  df2 = all_df[data_version]   
#  A = dcc.Input(id="G1_error_min", type="number",debounce=True, value = df2['Error_G1'].min(), style={'width':'50%', 'fontSize': 12})
#  B = dcc.Input(id="G1_error_max", type="number",debounce=True, value = df2['Error_G1'].max(), style={'width':'50%', 'fontSize': 12})
#  C = html.Div([A,
#                B])  
#  return C#

# displaying values of G1 error
#@app.callback(
#    Output("G1_error_range_output", "children"),
#    Input('segselect', 'value'),
#    Input("G1_error_min", "value"),
#    Input("G1_error_max", "value"))
#def number_render(data_version, G1_error_min, G1_error_max):
#  df2 = all_df[data_version]    
#  A = "Full G1 error range: {} to {}".format(round(df2['Error_G1'].min(),5), round(df2['Error_G1'].max(),5))
#  B = "Selected G1 error range: {} to {}".format(round(G1_error_min, 5), round(G1_error_max, 5))
#  C = html.Div([
#                html.Div(A, style={'margin-top': 20,'fontSize': 12}),
#                html.Div(B, style={'fontSize': 12})])
#  return C

# G2 error
#@app.callback(Output('G2_error_range_container', 'children'),
#              Input('segselect', 'value'))
#def display_click_data(data_version):
#  df2 = all_df[data_version]    
#  A = dcc.Input(id="G2_error_min", type="number",debounce=True, value = df2['Error_G2'].min(), style={'width':'50%', 'fontSize': 12})
#  B = dcc.Input(id="G2_error_max", type="number",debounce=True, value = df2['Error_G2'].max(), style={'width':'50%', 'fontSize': 12})
#  C = html.Div([A,
#                B])  
#  return C

# displaying values of G2 error
#@app.callback(
#    Output("G2_error_range_output", "children"),
#    Input('segselect', 'value'),
#    Input("G2_error_min", "value"),
#    Input("G2_error_max", "value"))
#def number_render(data_version, G2_error_min, G2_error_max):
#  df2 = all_df[data_version]    
#  A = "Full G2 range: {} to {}".format(round(df2['Error_G2'].min(),5), round(df2['Error_G2'].max(),5))
#  B = "Selected G2 range: {} to {}".format(round(G2_error_min, 5), round(G2_error_max, 5))
#  C = html.Div([
#                html.Div(A, style={'margin-top': 20,'fontSize': 12}),
#                html.Div(B, style={'fontSize': 12})])
#  return C

############ Callbacks for slider containers #############################
@app.callback(Output('Temp_slider_container', 'children'),
              Input('segselect', 'value'),
              Input('HanleScanType', 'children'))
def display_click_data(data_version, scan_type):
  df2 = all_df[data_version]   
  if scan_type == 'Scan Type = 3D':        
    temp = 'Temp'
  if scan_type == 'Scan Type = 2D/1D': 
    temp = 'Temperature (C) '
  A = dcc.RangeSlider(id = "temp-range-slider",
                      min=df2[temp].min(),
                      max=df2[temp].max()+(df2[temp].max()*0.01),
                      step=1/100000,
                      value=[df2[temp].min(), df2[temp].max()+(df2[temp].max()*0.01)],
                      marks={60: {'label': '60 °C', 'style': {'color': '#77b0b1'}},
                             80: {'label': '80 °C'},
                             100: {'label': '100 °C'},
                             120: {'label': '120°C', 'style': {'color': '#f50'}}
                            }
                     )
  return A

@app.callback(Output('LP_slider_container', 'children'),
              Input('segselect', 'value'),
              Input('HanleScanType', 'children'))
def display_click_data(data_version, scan_type):
  df2 = all_df[data_version]     
  if scan_type == 'Scan Type = 3D':
    LP = 'Laser_Power'
  if scan_type == 'Scan Type = 2D/1D': 
    LP = 'Laser Power (uW) '
  A = dcc.RangeSlider(
                          id='LP-range-slider',
                          min=df2[LP].min(),
                          max=df2[LP].max()+1,
                          step=1/100000,
                          value=[df2[LP].min(), df2[LP].max()+1],
                          marks={200: {'label': '200', 'style': {'color': '#77b0b1'}},
                                 300: {'label': '300'},
                                 400: {'label': '400'},
                                 500: {'label': '500'},
                                 600: {'label': '600'},
                                 700: {'label': '700', 'style': {'color': '#f50'}}
                                }
                  
                        )
  return A


@app.callback(Output('LD_slider_container', 'children'),
              Input('segselect', 'value'),
              Input('HanleScanType', 'children'))
def display_click_data(data_version, scan_type):
  df2 = all_df[data_version] 
  if scan_type == 'Scan Type = 3D':        
    LD = 'Laser_Detuning'
  if scan_type == 'Scan Type = 2D/1D': 
    LD = 'Detuning (GHz) ' 
  A = dcc.RangeSlider(id='LD-range-slider',
                      min=-20,
                      #min=df2['Laser_Detuning'].min(),
                      max=df2[LD].max()+1,
                      step=1/100000,
                      value=[df2[LD].min(), df2[LD].max()+1],
                      marks={
                          -20: {'label': '-20', 'style': {'color': '#77b0b1'}},
                          -10: {'label': '-10'},
                          0: {'label': '0'},
                          10: {'label': '10', 'style': {'color': '#f50'}}
                      }
                     )
  return A
######## Call back for updating custom graph ###############################################
@app.callback(Output('custom_plot', 'figure'),
              Input('temp-range-slider', 'value'),
              Input('LP-range-slider', 'value'),
              Input('V/nT_min', 'value'),
              Input('V/nT_max', 'value'),
              Input('LD-range-slider', 'value'),
              Input('segselect', 'value'),
              Input('x_value_dropdown', 'value'),
              Input('y_value_dropdown', 'value'),
              Input('z_value_dropdown', 'value'),
              Input('G1_min', 'value'),
              Input('G1_max', 'value'),
              Input('G2_min', 'value'),
              Input('G2_max', 'value'),
#              Input('G1_error_min', 'value'),
#              Input('G1_error_max', 'value'),
#              Input('G2_error_min', 'value'),
#              Input('G2_error_max', 'value'),
              Input('A_min', 'value'),
              Input('A_max', 'value'),
              Input('HanleScanType', 'children'),
              Input('x-axis-scale-radio', 'value'),
              Input('y-axis-scale-radio', 'value'),
              Input('colour-axis-scale-radio', 'value'),)
def update_figure(TEMP, LP, VnT_min, VnT_max, LD, data_version, x_value, y_value, z_value, G1_min, G1_max,
                  G2_min, G2_max, #G1_error_min, G1_error_max, G2_error_min, G2_error_max,
                  A_min, A_max, scan_type, x_scale, y_scale, col_scale):
  df2 = all_df[data_version]   
  if scan_type == 'Scan Type = 3D':        
    temp='Temp'
    ld='Laser_Detuning'
    lp='Laser_Power'
    A = 'A'
    G1 = 'G1'
    G2 ='G2'
  if scan_type == 'Scan Type = 2D/1D': 
    temp='Temperature (C) '
    ld='Detuning (GHz) '
    lp='Laser Power (uW) '
    A = 'A(1D)'
    G1 = 'G(1D)'
    G2 = 'G2(2D)'
  filtered_df = df2[(df2[temp]<= TEMP[1])&(df2[temp]>= TEMP[0])&
                    (df2[lp]<= LP[1])&(df2[lp]>= LP[0])&
                    (df2['V/nT']<=VnT_max)&(df2['V/nT']>= VnT_min)&
                    (df2[A]<= A_max)&(df2[A]>= A_min)&                    
                    (df2[G1]<= G1_max)&(df2[G1]>= G1_min)&
                    (df2[G2]<= G2_max)&(df2[G2]>= G2_min)&  
#                   (df2['Error_G1']<= G1_error_max)&(df2['Error_G1']>= G1_error_min)&
#                   (df2['Error_G2']<= G2_error_max)&(df2['Error_G2']>= G2_error_min)&                    
                    (df2[ld]<= LD[1])&(df2[ld]>= LD[0])] 
  if x_scale == "Log":
        XLOG = True
  if y_scale == "Log":
        YLOG = True  
  if x_scale == "Linear":
        XLOG = False
  if y_scale == "Linear":
        YLOG = False  

  if col_scale == "Log":
      if z_value =="":
            fig = px.scatter(filtered_df, y=y_value, x=x_value, log_x=XLOG, log_y=YLOG)
      if z_value !="":
        fig = px.scatter(filtered_df, y=y_value, x=x_value, color=np.log10(z_value), log_x=XLOG, log_y=YLOG)
  if col_scale == "Linear":
      if z_value =="":
            fig = px.scatter(filtered_df, y=y_value, x=x_value, log_x=XLOG, log_y=YLOG)
      if z_value !="":
        fig = px.scatter(filtered_df, y=y_value, x=x_value, color=z_value, log_x=XLOG, log_y=YLOG)        
  fig.update_layout(margin={'l': 0, 'b': 0, 't': 30, 'r': 0}, hovermode='closest')
  fig.update_layout(height=300)  
    
  return fig
######## Call backs for sensitivity plot ################
@app.callback(
    Output('radioitems-sensitivity-container', 'children'),
    Input('HanleScanType', 'children'),
    Input('segselect', 'value'))
def update_figure(scan_type, data_version):
    if scan_type == 'Scan Type = 2D/1D': 
        # Includes sensitivity data
        if data_version== 14 or data_version== 15 or data_version== 16 or data_version== 17 or data_version== 18 or data_version== 19 or data_version== 20 or data_version== 21 or data_version== 22 or data_version== 23 or data_version== 24 or data_version == 26 or data_version == 29 or data_version == 30: 
            A = dcc.RadioItems(
                id='value_dropdown_1D_sensitivity',
                options=[{"label": i, "value": i} for i in ["Hanle Single Axis", "Sensitivity"]],
                value='Sensitivity',
                inputStyle={"margin-left": "20px"}, # add space between radio items
                labelStyle={'display': 'inline-block'},
                style={'fontSize': 12}
            ), 
        # No sensitivity data:    
        if data_version == 26 or data_version == 27 or data_version == 28: 
            A = dcc.RadioItems(
                id='value_dropdown_1D_sensitivity',
                options=[{"label": i, "value": i} for i in ["Hanle Single Axis"]],
                value='Hanle Single Axis',
                inputStyle={"margin-left": "20px"}, # add space between radio items
                labelStyle={'display': 'inline-block'},
                style={'fontSize': 12}
            ),     
        else:
            A = dcc.RadioItems(
                id='value_dropdown_1D_sensitivity',
                options=[{"label": i, "value": i} for i in ["Hanle Single Axis", "Sensitivity", "Noise"]],
                value='Sensitivity',
                inputStyle={"margin-left": "20px"}, # add space between radio items
                labelStyle={'display': 'inline-block'},
                style={'fontSize': 12}
            ), 
    if scan_type == 'Scan Type = 3D': 
        A = dcc.RadioItems(
            id='value_dropdown_1D_sensitivity',
            options=[{"label": i, "value": i} for i in ["Hanle Single Axis"]],
            value='Hanle Single Axis',
            inputStyle={"margin-left": "20px"}, # add space between radio items
            labelStyle={'display': 'inline-block'},
            style={'fontSize': 12}
        ),  
    return A
    
## Callback for sensitivity plotter
@app.callback(
    Output('hide_sensitivity-box', 'style'),
    Input('value_dropdown_1D_sensitivity', 'value'),
    Input('HanleScanType', 'children'))
def show_hide_element(visibility_state, scan_type):
    if scan_type == 'Scan Type = 2D/1D': 
        if visibility_state == 'Sensitivity':
            return {'display': 'block'}
        if visibility_state != 'Sensitivity':
            return {'display': 'none'}
    if scan_type == 'Scan Type = 3D': 
        return {'display': 'none'}        
    
    
## Callback for Hanle 1 axis
@app.callback(
    Output('hide_hanle_box2', 'style'),
    Input('value_dropdown_1D_sensitivity', 'value'),
    Input('HanleScanType', 'children'))
def show_hide_element(visibility_state, scan_type):
    if scan_type == 'Scan Type = 2D/1D': 
        if visibility_state == 'Hanle Single Axis':
            return {'display': 'block'}
        if visibility_state != 'Hanle Single Axis':
            return {'display': 'none'}  
    if scan_type == 'Scan Type = 3D':  
        return {'display': 'block'}        
    
## Callback for Noise
@app.callback(
    Output('hide_noise-box', 'style'),
    Input('value_dropdown_1D_sensitivity', 'value'),
    Input('HanleScanType', 'children'))
def show_hide_element(visibility_state, scan_type):
    if scan_type == 'Scan Type = 2D/1D': 
        if visibility_state == 'Noise':
            return {'display': 'block'}
        if visibility_state != 'Noise':
            return {'display': 'none'} 
    if scan_type == 'Scan Type = 3D':  
        return {'display': 'none'}
        

## Call back for sensitivity SCAN
@app.callback(
    Output('hide_sensitivity_scan', 'children'),
    Input('graph-with-slider', 'clickData'), 
    Input('segselect', 'value'),
    Input('HanleScanType', 'children'))
def update_figure(clickData, data_version, scan_type):
    if scan_type == 'Scan Type = 2D/1D': 
        df2 = all_df[data_version] 
        Github_urls = all_git_df[data_version]        
        if clickData == None:
            x = 14
            line = df2.iloc[x,] 
            lp = line[2]
            ld = line[1]
            temp = line[0]
        else:
            temp = clickData['points'][0]['y']
            lp = clickData['points'][0]['x']
            ld = clickData['points'][0]['z']
        filtered_df = Github_urls[(Github_urls['Temp']== temp)]
        filtered_df2 = filtered_df[(filtered_df['Laser_power']== lp)]
        filtered_df3 = filtered_df2[(filtered_df2['Laser_Detuning']== ld)]
        data_url = filtered_df3.iloc[0,0]
        df = pd.read_table(data_url)
        if data_version ==14:
            df = df.reset_index()
            df.columns = df.iloc[0]
            df =df.iloc[1:]
            df = df.iloc[0:25000, 7:9] # 3D data
            df = df.rename(columns={"Heater Current (A)" : "Frequency (Hz)" ,"Temperature (C)" : "Photodiode Voltage (V)"})
        if data_version ==15 or data_version ==16 or data_version ==17 or data_version == 25 :
            df.columns = df.iloc[0]
            df =df.iloc[1:]
            df.reset_index(drop=True, inplace=True)   
            df.columns = ["a","b","a2", "Frequency (Hz)", "Photodiode Voltage (V)", "c","d", "e"]
        if  data_version ==18 or data_version ==19:
            df.columns = df.iloc[0]
            df =df.iloc[1:]
            df.reset_index(drop=True, inplace=True)   
            df.columns = ["a","b","a2","gg","f", "Frequency (Hz)", "Photodiode Voltage (V)", "c","d", "e"]  
        if  data_version ==20 or data_version ==21 or data_version ==22 or data_version ==23 or data_version== 24 or data_version == 26 or data_version == 27 or data_version == 28 or data_version == 29 or data_version == 30:
            df.columns = df.iloc[0]
            df =df.iloc[1:]
            df.reset_index(drop=True, inplace=True)   
            df.columns = ["a","b","a2","gg","f","ff", "Frequency (Hz)", "Photodiode Voltage (V)", "c","d", "e"]                     
        else:
            df.columns = df.iloc[0]
            df =df.iloc[1:]
            df.reset_index(drop=True, inplace=True)
            df.columns = ["a","b", "Frequency (Hz)", "Photodiode Voltage (V)", "c","d"]
            df = df.apply(pd.to_numeric)
            df2 = all_df[data_version] 
            df2_f1 = df2[(df2['Temperature (C) ']== temp)]
            df2_f2 = df2_f1[(df2_f1['Laser Power (uW) ']== lp)]
            df2_f3 = df2_f2[(df2_f2['Detuning (GHz) ']== ld)]
            vnt = df2_f3['V/nT']
            vnt = vnt.apply(pd.to_numeric)
            vnt = vnt.iloc[0,]
            df["Photodiode Voltage (V)"]= (df["Photodiode Voltage (V)"]/vnt)*(1*10**-9) #convert to sensitivity
        df = df.apply(pd.to_numeric)
        fig2 = px.line(df, x="Frequency (Hz)", y="Photodiode Voltage (V)", log_x=True, log_y=True,                  
                       labels={"Photodiode Voltage (V)": "Sensitivity (T/√Hz)"},) 
        fig2.update_layout(height=300)
        fig2.update_layout(font=dict(size=8)) # Change font size        
        fig2.update_layout(margin={'l': 0, 'b': 0, 't': 0, 'r': 10}, hovermode='closest') #Change margins           
        B = dcc.Graph(figure=fig2, id='1D', config={'displayModeBar': False}),
        return B    
    
## Call back for noise SCAN
@app.callback(
    Output('hide_noise_scan', 'children'),
    Input('graph-with-slider', 'clickData'), 
    Input('segselect', 'value'),
    Input('HanleScanType', 'children'))
def update_figure(clickData, data_version, scan_type):
    if scan_type == 'Scan Type = 2D/1D' : 
        df2 = all_df[data_version] 
        Github_urls = all_git_df[data_version]        
        if clickData == None:
            x = 14
            line = df2.iloc[x,] 
            lp = line[2]
            ld = line[1]
            temp = line[0]
        else:
            temp = clickData['points'][0]['y']
            lp = clickData['points'][0]['x']
            ld = clickData['points'][0]['z']
        filtered_df = Github_urls[(Github_urls['Temp']== temp)]
        filtered_df2 = filtered_df[(filtered_df['Laser_power']== lp)]
        filtered_df3 = filtered_df2[(filtered_df2['Laser_Detuning']== ld)]
        data_url = filtered_df3.iloc[0,0]
        df = pd.read_table(data_url)
        if data_version ==14:
            df = df.reset_index()
            df.columns = df.iloc[0]
            df =df.iloc[1:]
            df = df.iloc[0:25000, 7:9] # 3D data
            df = df.rename(columns={"Heater Current (A)" : "Frequency (Hz)" ,"Temperature (C)" : "Photodiode Voltage (V)"})
        if data_version ==15 or data_version ==16 or data_version ==17 or data_version ==18 or data_version ==19 or data_version == 25:
            df.columns = df.iloc[0]
            df =df.iloc[1:]
            df.reset_index(drop=True, inplace=True)   
            df.columns = ["a","b","a2", "Frequency (Hz)", "Photodiode Voltage (V)", "c","d", "e"]
        else:
            df.columns = df.iloc[0]
            df =df.iloc[1:]
            df.reset_index(drop=True, inplace=True)
            df.columns = ["a","b", "Frequency (Hz)", "Photodiode Voltage (V)", "c","d"]
        fig2 = px.line(df, x="Frequency (Hz)", y="Photodiode Voltage (V)", log_x=True, log_y=True,                  
                       labels={"Photodiode Voltage (V)": "Noise (V/√Hz)"},) 
        fig2.update_layout(height=300)
        fig2.update_layout(font=dict(size=8)) # Change font size        
        fig2.update_layout(margin={'l': 0, 'b': 0, 't': 0, 'r': 10}, hovermode='closest') #Change margins           
        B = dcc.Graph(figure=fig2, id='1D', config={'displayModeBar': False}),
        return B    


    
######## Call backs for the plotter and hanle options ################
## Callback for hiding plotter
@app.callback(
   Output('hide_plotter_box', 'style'),
   [Input('value_dropdown_2', 'value')])
def show_hide_element(visibility_state):
    if visibility_state == 'Plotter':
        return {'display': 'block'}
    if visibility_state == 'Hanle':
        return {'display': 'none'}
    
## Callback for hiding 3D hanle
@app.callback(
    Output('hide_hanle_box', 'style'),
    Input('value_dropdown_2', 'value'))
def show_hide_element(visibility_state):
    if visibility_state == 'Hanle':
        return {'display': 'block'}
    if visibility_state == 'Plotter':
        return {'display': 'none'}  
    
################# Callbacks for selected data details  ############################

#@app.callback(
#  Output('Markdown_notes', 'children'),
#  Input('segselect', 'value'))
#def display_click_data(data_version):
#  if data_version == 0:  
#    A = '''
#* **Testing type**: M-LOOP for parameter space (Temp: 60-125C, Laser power: 150-800 μW, Laser detuning: -20 to 10 GHz)
#* **Notes**: 166 loop'''
#  if data_version == 2:
#    A = '''
#* **Testing type**: M-LOOP for parameter space (Temp: 70-125C, Laser power: 150-700 μW, Laser detuning: -20 to 10 GHz)
#* **Notes**: 500 loop'''
#  if data_version == 3:
#    A = '''
#* **Testing type**: Genetic Algorithm for parameter space (Temp: 70-125C, Laser power: 150-700 μW, Laser detuning: -20 to 10 GHz)
#* **Notes**: 200 Samples (10 population for 20 loops)'''    
#  if data_version == 1:
#    A = '''
#* **Testing type**: Genetic Algorithm for parameter space (Temp: 100-130C, Laser power: 350-800 μW, Laser detuning: 0-10 GHz)
#* **Notes**: 50 Samples (10 population for 5 loops) '''
#  if data_version ==4:
#    A = '''
#* **Testing type**: Gradient search for parameter space (Temp: 100-130C, Laser power: 350-800 μW, Laser detuning: 0-10 GHz)
#* **Notes**: 20 resolution for 3 axis * 3 loops '''  
#  if data_version == 5:
#    A = '''
#* **Testing type**: Systematic search for parameter space (Temp: 75-125C, Laser power: 500-1200 μW, Laser detuning: -20 to 10 GHz)
#* **Notes**: 8*8*8 full systematic search '''      
#  return A

## Callback for selected data text ################
## Call back for text under graph
@app.callback(Output('totalpoints', 'children'),
              Input('temp-range-slider', 'value'),
              Input('LP-range-slider', 'value'),
              Input('V/nT_min', 'value'),
              Input('V/nT_max', 'value'), 
              Input('LD-range-slider', 'value'),
              Input('value_dropdown', 'value'),
              Input('segselect', 'value'),
              Input('G1_min', 'value'),
              Input('G1_max', 'value'),
              Input('G2_min', 'value'),
              Input('G2_max', 'value'),
#              Input('G1_error_min', 'value'),
#              Input('G1_error_max', 'value'),
#              Input('G2_error_min', 'value'),
#              Input('G2_error_max', 'value'),
              Input('A_min', 'value'),
              Input('A_max', 'value'),
              Input('HanleScanType', 'children'))
def update_figure(TEMP, LP, VnT_min, VnT_max, LD, col, data_version, G1_min, G1_max,
                  G2_min, G2_max,# G1_error_min, G1_error_max, G2_error_min, G2_error_max, 
                  A_min, A_max, scan_type):
  df2 = all_df[data_version]      
  if scan_type == 'Scan Type = 3D':        
    temp='Temp'
    ld='Laser_Detuning'
    lp='Laser_Power'
    A = 'A'
    G1 = 'G1'
    G2 ='G2'
  if scan_type == 'Scan Type = 2D/1D': 
    temp='Temperature (C) '
    ld='Detuning (GHz) '
    lp='Laser Power (uW) '
    A = 'A(1D)'
    G1 = 'G(1D)'
    G2 = 'G2(2D)'
  filtered_df = df2[(df2[temp]<= TEMP[1])&(df2[temp]>= TEMP[0])&
                    (df2[lp]<= LP[1])&(df2[lp]>= LP[0])&
                    (df2['V/nT']<=VnT_max)&(df2['V/nT']>= VnT_min)&
                    (df2[A]<= A_max)&(df2[A]>= A_min)&                    
                    (df2[G1]<= G1_max)&(df2[G1]>= G1_min)&
                    (df2[G2]<= G2_max)&(df2[G2]>= G2_min)&  
#                   (df2['Error_G1']<= G1_error_max)&(df2['Error_G1']>= G1_error_min)&
#                   (df2['Error_G2']<= G2_error_max)&(df2['Error_G2']>= G2_error_min)&                    
                    (df2[ld]<= LD[1])&(df2[ld]>= LD[0])]     

  length = len(filtered_df[temp])
  return 'Total points =  {}'.format(length)


@app.callback(
    Output('click-data', 'children'),
    Input('graph-with-slider', 'clickData'),
    Input('segselect', 'value'),
    Input('value_dropdown', 'value'))
def display_click_data(clickData, data_version, parameter_value):
  df2 = all_df[data_version]    
  if clickData == None:
    x = 14
    line = df2.iloc[x,] 
    lp = line[15]
    ld = line[16]
    temp = line[17]
    vnt = line[19]
    A = 'Temperature ={}°C, Laser Power = {}μW, Laser Detuning = {}GHz, {} = {}'.format(temp, lp, ld,parameter_value, vnt)
  else:
    temp = clickData['points'][0]['y']
    lp = clickData['points'][0]['x']
    ld = clickData['points'][0]['z']
    vnt = clickData['points'][0]['marker.color']
    A = 'Temperature ={}°C, Laser Power = {}μW, Laser Detuning = {}GHz, {} = {}'.format(temp, lp, ld,parameter_value, vnt)
  return A

########### Call backs for Slider indicators text ##########################################################
## Call back for TEMP slider indicator
@app.callback(Output('TEMP_slider-drag-output', 'children'),
              [Input('temp-range-slider', 'value')]
             )
def display_value(value):
  low = value[0]
  high = value[1]
  return 'Temperature = {} to {}°C'.format(low, high)

## Call back for lp slider indicator
@app.callback(Output('LP_slider-drag-output', 'children'),
              [Input('LP-range-slider', 'value')])
def display_value(value):
  low = value[0]
  high = value[1]
  return 'Laser Power = {} to {}μW'.format(low, high)

## Call back for LD slider indicator
@app.callback(Output('LD_slider-drag-output', 'children'),
              [Input('LD-range-slider', 'value')])
def display_value(value):
  low = value[0]
  high = value[1]
  return 'Laser Detuning = {} to {}GHz'.format(low, high)



############### Call back for graphs #################################
## Call back for updating the 3D graph
@app.callback(Output('graph-with-slider', 'figure'),
              Input('temp-range-slider', 'value'),
              Input('LP-range-slider', 'value'),
              Input('V/nT_min', 'value'),
              Input('V/nT_max', 'value'),              
              Input('LD-range-slider', 'value'),
              Input('value_dropdown', 'value'),
              Input('segselect', 'value'),
              Input('G1_min', 'value'),
              Input('G1_max', 'value'),
              Input('G2_min', 'value'),
              Input('G2_max', 'value'),
#              Input('G1_error_min', 'value'),
#              Input('G1_error_max', 'value'),
#              Input('G2_error_min', 'value'),
#              Input('G2_error_max', 'value'),
              Input('A_min', 'value'),
              Input('A_max', 'value'),
              Input('HanleScanType', 'children'))
def update_figure(TEMP, LP, VnT_min, VnT_max, LD, col, data_version, G1_min, G1_max,
                  G2_min, G2_max, #G1_error_min, G1_error_max, G2_error_min, G2_error_max, 
                  A_min, A_max, scan_type):
  df2 = all_df[data_version]   
  if scan_type == 'Scan Type = 3D':        
    temp='Temp'
    ld='Laser_Detuning'
    lp='Laser_Power'
    A = 'A'
    G1 = 'G1'
    G2 ='G2'
  if scan_type == 'Scan Type = 2D/1D': 
    temp='Temperature (C) '
    ld='Detuning (GHz) '
    lp='Laser Power (uW) '
    A = 'A(1D)'
    G1 = 'G(1D)'
    G2 = 'G2(2D)'
  filtered_df = df2[(df2[temp]<= TEMP[1])&(df2[temp]>= TEMP[0])&
                    (df2[lp]<= LP[1])&(df2[lp]>= LP[0])&
                    (df2['V/nT']<=VnT_max)&(df2['V/nT']>= VnT_min)&
                    (df2[A]<= A_max)&(df2[A]>= A_min)&                    
                    (df2[G1]<= G1_max)&(df2[G1]>= G1_min)&
                    (df2[G2]<= G2_max)&(df2[G2]>= G2_min)&  
#                   (df2['Error_G1']<= G1_error_max)&(df2['Error_G1']>= G1_error_min)&
#                   (df2['Error_G2']<= G2_error_max)&(df2['Error_G2']>= G2_error_min)&                    
                    (df2[ld]<= LD[1])&(df2[ld]>= LD[0])]     
  fig = px.scatter_3d(filtered_df, y=temp, z=ld, x=lp, color=col)  
  fig.update_layout(margin={'l': 0, 'b': 0, 't': 30, 'r': 0}, hovermode='closest')
  fig.update_layout(transition_duration=500)
  fig.update_layout(height=500)
  camera = dict(
      center=dict(x=0.1, y=0, z=-0.1),
  )
  fig.update_layout(scene_camera=camera)
  fig.update_layout(scene = dict(
                    xaxis_title='Laser Power (μW)',
                    yaxis_title='Temperature (°C)',
                    zaxis_title='Laser Detuning (GHz)'))
  return fig

###### Callbacks for all tables ################

## Callback for table
@app.callback(
    Output("my-table", "data"),
    Input('graph-with-slider', 'clickData'), 
    Input('segselect', 'value'),
    Input('HanleScanType', 'children'))
def on_trace_click(clickData, data_version,scan_type):
    df2 = all_df[data_version]  
    if scan_type == 'Scan Type = 3D':
        if clickData== None:
            x = 14
            line = df2.iloc[x,] 
            lp = line[15]
            ld = line[16]
            temp = line[17]
        else:
            temp = clickData['points'][0]['y']
            lp = clickData['points'][0]['x']
            ld = clickData['points'][0]['z']
        filtered_df = df2[(df2['Temp']== temp)&
                          (df2['Laser_Power']== lp)&
                          (df2['Laser_Detuning']== ld)]
        row = filtered_df
        return row.to_dict('records')
    
## Callback for error table
@app.callback(
    Output("my-table2", "data"),
    Input('graph-with-slider', 'clickData'), 
    Input('segselect', 'value'),
    Input('HanleScanType', 'children'))
def on_trace_click(clickData, data_version,scan_type):
    df2 = all_df[data_version]  
    if scan_type == 'Scan Type = 3D':
        if clickData== None:
            x = 14
            line = df2.iloc[x,] 
            lp = line[15]
            ld = line[16]
            temp = line[17]
        else:
            temp = clickData['points'][0]['y']
            lp = clickData['points'][0]['x']
            ld = clickData['points'][0]['z']
        filtered_df = df2[(df2['Temp']== temp)&
                          (df2['Laser_Power']== lp)&
                          (df2['Laser_Detuning']== ld)]
        row = filtered_df
        return row.to_dict('records')

## 2D/1D        
## Callback for table
@app.callback(
    Output("2D1D-my-table", "data"),
    Input('graph-with-slider', 'clickData'), 
    Input('segselect', 'value'),
    Input('HanleScanType', 'children'))
def on_trace_click(clickData, data_version,scan_type):
    df2 = all_df[data_version]  
    if scan_type == 'Scan Type = 2D/1D': 
        if clickData== None:
            x = 14
            line = df2.iloc[x,] 
            lp = line[15]
            ld = line[16]
            temp = line[17]
        else:
            temp = clickData['points'][0]['y']
            lp = clickData['points'][0]['x']
            ld = clickData['points'][0]['z']
        filtered_df = df2[(df2['Temperature (C) ']== temp)&
                          (df2['Laser Power (uW) ']== lp)&
                          (df2['Detuning (GHz) ']== ld)]
        row = filtered_df
        return row.to_dict('records')
    
## Callback for error table
@app.callback(
    Output("2D1D-my-table2", "data"),
    Input('graph-with-slider', 'clickData'), 
    Input('segselect', 'value'),
    Input('HanleScanType', 'children'))
def on_trace_click(clickData, data_version,scan_type):
    df2 = all_df[data_version]  
    if scan_type == 'Scan Type = 2D/1D': 
        if clickData== None:
            x = 14
            line = df2.iloc[x,] 
            lp = line[15]
            ld = line[16]
            temp = line[17]
        else:
            temp = clickData['points'][0]['y']
            lp = clickData['points'][0]['x']
            ld = clickData['points'][0]['z']
        filtered_df = df2[(df2['Temperature (C) ']== temp)&
                          (df2['Laser Power (uW) ']== lp)&
                          (df2['Detuning (GHz) ']== ld)]
        row = filtered_df
        return row.to_dict('records')
    
## Call back for updating facet 3D scan
@app.callback(
    Output('facet-container', 'children'),
    Input('graph-with-slider', 'clickData'), 
    Input('segselect', 'value'),
    Input('HanleScanType', 'children'))
def update_figure(clickData, data_version, scan_type):
    if scan_type == 'Scan Type = 3D':
        df2 = all_df[data_version] 
        Github_urls = all_git_df[data_version]        
        if clickData == None:
            x = 14
            line = df2.iloc[x,] 
            lp = line[15]
            ld = line[16]
            temp = line[17]
        else:
            temp = clickData['points'][0]['y']
            lp = clickData['points'][0]['x']
            ld = clickData['points'][0]['z']
        filtered_df = Github_urls[(Github_urls['Temp']== temp)]
        filtered_df2 = filtered_df[(filtered_df['Laser_power']== lp)]
        filtered_df3 = filtered_df2[(filtered_df2['Laser_Detuning']== ld)]
        data_url = filtered_df3.iloc[0,0]
        df = pd.read_table(data_url)
        df.columns = df.iloc[0]
        df =df.iloc[1:]
        newdf = df.apply(pd.to_numeric)
        newdf["Z  Field (nT)"] = newdf["Z  Field (nT)"].round(2)
        fig = px.scatter(newdf, x="X  Field (nT)", y="Y  Field (nT)",
                         color="Photodiode Voltage (V)", facet_col="Z  Field (nT)",  facet_col_wrap=4, color_continuous_scale='aggrnyl')
        fig.update_layout(xaxis=dict(scaleanchor='y', constrain='domain')) #Make axis equal (squares)
        fig.update_layout(margin={'l': 0, 'b': 0, 't': 10, 'r': 0}, hovermode='closest') #Change margins
        fig.update_layout(font=dict(size=8)) # Change font size
        fig.for_each_annotation(lambda a: a.update(text=a.text.replace("Z  Field (nT)=", "Bz ="))) # change title of each facet
        fig['layout']['yaxis']['title']['text']=''
        fig['layout']['yaxis5']['title']['text']=''
        fig['layout']['yaxis13']['title']['text']=''
        fig['layout']['yaxis17']['title']['text']=''
        fig['layout']['xaxis']['title']['text']=''
        fig['layout']['xaxis']['title']['text']=''
        fig['layout']['xaxis3']['title']['text']=''
        fig['layout']['xaxis4']['title']['text']=''
        ##fig.update_layout(coloraxis_showscale=False)
        fig.layout.coloraxis.colorbar.title = 'PD (V)'
        fig.update_layout(height=400)
        A = dcc.Graph(figure=fig, id='facet', config={'displayModeBar': False}),
        return A

############# 2D/1D Scan ####################    
## Call back for updating 2D scan
@app.callback(
    Output('2D-graph-container', 'children'),
    Input('graph-with-slider', 'clickData'), 
    Input('segselect', 'value'),
    Input('HanleScanType', 'children'))
def update_figure(clickData, data_version, scan_type):
    if scan_type == 'Scan Type = 2D/1D': 
        df2 = all_df[data_version] 
        Github_urls = all_git_df[data_version]        
        if clickData == None:
            x = 14
            line = df2.iloc[x,] 
            lp = line[2]
            ld = line[1]
            temp = line[0]
        else:
            temp = clickData['points'][0]['y']
            lp = clickData['points'][0]['x']
            ld = clickData['points'][0]['z']
        filtered_df = Github_urls[(Github_urls['Temp']== temp)]
        filtered_df2 = filtered_df[(filtered_df['Laser_power']== lp)]
        filtered_df3 = filtered_df2[(filtered_df2['Laser_Detuning']== ld)]
        data_url = filtered_df3.iloc[0,0]
        df = pd.read_table(data_url, index_col=False)
        df.columns = df.iloc[0]
        df =df.iloc[1:]
        if data_version == 14 or data_version == 15 or data_version ==16 or data_version ==17 or data_version == 25 or data_version ==18 or data_version ==19: 
            df_2d = df.iloc[0:960, 0:3] #2D data 
        if data_version == 20 or data_version == 21 or data_version == 22 or data_version ==23 or data_version== 24 or data_version == 26 or data_version == 27 or data_version == 28 or data_version == 29 or data_version == 30: 
            df_2d = df.iloc[0:2500, 0:3] #2D data                   
        else :
            df_2d = df.iloc[0:441, 0:3] #2D data       
        df_2d = df_2d.apply(pd.to_numeric)
        if  data_version == 27 or data_version == 28 or data_version == 29: 
            df_2d["Photodiode Voltage (V)"] =  df_2d["Photodiode Voltage (V)"]*2                 
        fig = px.scatter(df_2d, x="X  Field (nT)", y="Z  Field (nT)",
                         color="Photodiode Voltage (V)", color_continuous_scale='aggrnyl')      
        fig.update_layout(margin={'l': 0, 'b': 0, 't': 0, 'r': 0}, hovermode='closest') #Change margins        
        fig.update_layout(height=250)
        fig.update_layout(font=dict(size=8)) # Change font size
        fig.layout.coloraxis.colorbar.title = 'PD (V)' 
        fig.update_traces(marker=dict(size=12)) # increase marker sizes
        #fig.update_layout(xaxis=dict(scaleanchor='y', constrain='domain')) #Make axis equal (squares)
        A = dcc.Graph(figure=fig, id='facet', config={'displayModeBar': False}),
        return A     


## Call back for 1D SCAN
@app.callback(
    Output('hide_1D_scan', 'children'),
    Input('graph-with-slider', 'clickData'), 
    Input('segselect', 'value'),
    Input('HanleScanType', 'children'))
def update_figure(clickData, data_version, scan_type):
    if scan_type == 'Scan Type = 2D/1D': 
        df2 = all_df[data_version] 
        Github_urls = all_git_df[data_version]        
        if clickData == None:
            x = 14
            line = df2.iloc[x,] 
            lp = line[2]
            ld = line[1]
            temp = line[0]
        else:
            temp = clickData['points'][0]['y']
            lp = clickData['points'][0]['x']
            ld = clickData['points'][0]['z']
        filtered_df = Github_urls[(Github_urls['Temp']== temp)]
        filtered_df2 = filtered_df[(filtered_df['Laser_power']== lp)]
        filtered_df3 = filtered_df2[(filtered_df2['Laser_Detuning']== ld)]
        data_url = filtered_df3.iloc[0,0]
        df = pd.read_table(data_url, index_col=False)
        df.columns = df.iloc[0]
        df =df.iloc[1:]
        if data_version ==14:
            df_1d = df.iloc[0:50, 4:6] # 3D data
            df_1d = df_1d.rename(columns={"Photodiode Voltage (V)" : "Y  Field (nT)","Frequency (Hz)" : "Photodiode Voltage (V)"})
        if data_version ==15 or data_version ==16 or data_version ==17 or data_version ==18 or data_version ==19 or data_version == 25:
            df_1d = df.iloc[0:100, 3:5] # 3D data  
        if data_version ==20 or data_version ==21 or data_version ==22 or data_version ==23 or data_version== 24 or data_version == 26 or data_version == 27 or data_version == 28 or data_version == 29 or data_version == 30:
            df_1d = df.iloc[0:200, 3:5] # 3D data             
        else:
            df_1d = df.iloc[0:51, 4:6] # 3D data
        df_1d = df_1d.apply(pd.to_numeric)
        if  data_version == 27 or data_version == 28 or data_version == 29: 
            df_1d["Photodiode Voltage (V)"] =  df_1d["Photodiode Voltage (V)"]*2 
        fig2 = px.line(df_1d, x="Y  Field (nT)", y="Photodiode Voltage (V)")
        fig2.update_traces(mode='markers+lines',line_color='red')  
        fig2.update_layout(height=150)
        fig2.update_layout(font=dict(size=8)) # Change font size        
        fig2.update_layout(margin={'l': 0, 'b': 0, 't': 0, 'r': 10}, hovermode='closest') #Change margins           
        B = dcc.Graph(figure=fig2, id='1D', config={'displayModeBar': False}),
        return B

## Callback for Titles for 2D
@app.callback(
    Output('2D-title', 'children'),
    Input('HanleScanType', 'children'))
def display_click_data(scan_type):
    if scan_type == 'Scan Type = 2D/1D': 
        A = html.P('2D Hanle')
        return A      
    
## Callback for Titles for 1D
@app.callback(
    Output('1D-title', 'children'),
    Input('HanleScanType', 'children'))
def display_click_data(scan_type):
    if scan_type == 'Scan Type = 2D/1D': 
        A = html.P('1D Hanle')
        return A            
    
####################### Single Axis Sweeps ##########################
## Callback for selected data text hanle
@app.callback(
    Output('click-data-2', 'children'),
    Input('facet', 'clickData'),
    Input('graph-with-slider', 'clickData'), 
    Input('segselect', 'value'),
    Input('HanleScanType', 'children'))
def display_click_data(clickData2, clickData, data_version, scan_type):
    if scan_type == 'Scan Type = 3D': # 3D requires the back data to find z
        df2 = all_df[data_version] 
        Github_urls = all_git_df[data_version]  
        if clickData == None:
            x = 14
            line = df2.iloc[x,]
            lp = line[15]
            ld = line[16]
            temp = line[17]
        else:
            temp = clickData['points'][0]['y']
            lp = clickData['points'][0]['x']
            ld = clickData['points'][0]['z']
        filtered_df = Github_urls[(Github_urls['Temp']== temp)]
        filtered_df2 = filtered_df[(filtered_df['Laser_power']== lp)]
        filtered_df3 = filtered_df2[(filtered_df2['Laser_Detuning']== ld)]
        data_url = filtered_df3.iloc[0,0]
        df = pd.read_table(data_url)
        df.columns = df.iloc[0]
        df =df.iloc[1:]
        newdf = df.apply(pd.to_numeric)  
        z_list = sorted(list(set(newdf['Z  Field (nT)'])))
        if clickData2 == None:
            x = 1000
            y = 1000
            z = 1000
        else:
            y = clickData2['points'][0]['y']
            x = clickData2['points'][0]['x']
            z_index = clickData2['points'][0]['curveNumber']
            z = z_list[z_index]
        A = 'Selected point 3D: Bx = {}, By = {}, Bz = {}'.format(x,y,z)
        return A
    if scan_type == 'Scan Type = 2D/1D': 
        if clickData2 == None:
            x = 0
            y = 0
        else:
            y = clickData2['points'][0]['y']
            x = clickData2['points'][0]['x']
        A = 'Selected point 2D: Bx = {}, Bz = {}'.format(x,y)
        return A    

## Callback for graph: Longitudinal hanle
@app.callback(
    Output('click-data-3', 'figure'),
    Input('facet', 'clickData'),
    Input('graph-with-slider', 'clickData'), 
    Input('segselect', 'value'),
    Input('HanleScanType', 'children'))
def display_click_data(clickData2, clickData, data_version, scan_type):
    if scan_type == 'Scan Type = 3D': # 3D requires the back data to find z
        df2 = all_df[data_version] 
        Github_urls = all_git_df[data_version]      
        if clickData == None:
            x = 14
            line = df2.iloc[x,]
            lp = line[15]
            ld = line[16]
            temp = line[17]
        else:
            temp = clickData['points'][0]['y']
            lp = clickData['points'][0]['x']
            ld = clickData['points'][0]['z']
        filtered_df = Github_urls[(Github_urls['Temp']== temp)]
        filtered_df2 = filtered_df[(filtered_df['Laser_power']== lp)]
        filtered_df3 = filtered_df2[(filtered_df2['Laser_Detuning']== ld)]
        data_url = filtered_df3.iloc[0,0]
        df = pd.read_table(data_url)
        df.columns = df.iloc[0]
        df =df.iloc[1:]
        newdf = df.apply(pd.to_numeric)  
        z_list = sorted(list(set(newdf['Z  Field (nT)'])))
        if clickData2 == None:
            x = 1000
            y = 1000
            z = 1000
        else:
            y = clickData2['points'][0]['y']
            x = clickData2['points'][0]['x']
            z_index = clickData2['points'][0]['curveNumber']
            z = z_list[z_index]
        filtered_df = newdf[(newdf['X  Field (nT)']== x)]
        filtered_df2 = filtered_df[(filtered_df['Y  Field (nT)']== y)]
        fig = px.line(filtered_df2, x='Z  Field (nT)', y='Photodiode Voltage (V)')
        fig.update_traces(mode='markers+lines')  
        fig.update_layout(margin={'l': 0, 'b': 0, 't': 0, 'r': 10}, hovermode='closest') #Change margins
        fig.update_layout(height=150)
        fig.update_layout(font=dict(size=8)) # Change font size
        return fig
    if scan_type == 'Scan Type = 2D/1D': 
        df2 = all_df[data_version] 
        Github_urls = all_git_df[data_version]      
        if clickData == None:
            x = 14
            line = df2.iloc[x,]
            lp = line[2]
            ld = line[1]
            temp = line[0]
        else:
            temp = clickData['points'][0]['y']
            lp = clickData['points'][0]['x']
            ld = clickData['points'][0]['z']
        filtered_df = Github_urls[(Github_urls['Temp']== temp)]
        filtered_df2 = filtered_df[(filtered_df['Laser_power']== lp)]
        filtered_df3 = filtered_df2[(filtered_df2['Laser_Detuning']== ld)]
        data_url = filtered_df3.iloc[0,0]        
        df = pd.read_table(data_url, index_col=False)
        df.columns = df.iloc[0]
        df =df.iloc[1:]
        if data_version == 14: 
            df_2d = df.iloc[0:960, 0:3] #2D data 
        else :
            df_2d = df.iloc[0:441, 0:3] #2D data   
        newdf = df_2d.apply(pd.to_numeric)
        if clickData2 == None:
            x = 0
        else:
            x = clickData2['points'][0]['x']
        filtered_df = newdf[(newdf['X  Field (nT)']== x)]
        fig = px.line(filtered_df, x='Z  Field (nT)', y='Photodiode Voltage (V)')
        fig.update_traces(mode='markers+lines')  
        fig.update_layout(margin={'l': 0, 'b': 0, 't': 0, 'r': 10}, hovermode='closest') #Change margins
        fig.update_layout(height=150)
        fig.update_layout(font=dict(size=8)) # Change font size
        return fig    

## Callback for graph: transverse hanle
@app.callback(
  Output('click-data-4', 'figure'),
  Input('facet', 'clickData'),
  Input('graph-with-slider', 'clickData'), 
  Input('segselect', 'value'),
    Input('HanleScanType', 'children'))
def display_click_data(clickData2, clickData, data_version, scan_type):
    if scan_type == 'Scan Type = 3D':
        df2 = all_df[data_version] 
        Github_urls = all_git_df[data_version]          
        if clickData == None:
            x = 14
            line = df2.iloc[x,]
            lp = line[15]
            ld = line[16]
            temp = line[17]
        else:
            temp = clickData['points'][0]['y']
            lp = clickData['points'][0]['x']
            ld = clickData['points'][0]['z']
        filtered_df = Github_urls[(Github_urls['Temp']== temp)]
        filtered_df2 = filtered_df[(filtered_df['Laser_power']== lp)]
        filtered_df3 = filtered_df2[(filtered_df2['Laser_Detuning']== ld)]
        data_url = filtered_df3.iloc[0,0]
        df = pd.read_table(data_url)
        df.columns = df.iloc[0]
        df =df.iloc[1:]
        newdf = df.apply(pd.to_numeric)  
        z_list = sorted(list(set(newdf['Z  Field (nT)'])))
        if clickData2 == None:
            x = 1000
            y = 1000
            z = 1000
        else:
            y = clickData2['points'][0]['y']
            x = clickData2['points'][0]['x']
            z_index = clickData2['points'][0]['curveNumber']
            z = z_list[z_index]
        filtered_df = newdf[(newdf['Z  Field (nT)']== z)]
        filtered_df2 = filtered_df[(filtered_df['Y  Field (nT)']== y)]
        fig = px.line(filtered_df2, x='X  Field (nT)', y='Photodiode Voltage (V)')
        fig.update_traces(mode='markers+lines')  
        fig.update_layout(margin={'l': 0, 'b': 0, 't': 0, 'r': 10}, hovermode='closest') #Change margins
        fig.update_layout(height=150)
        fig.update_layout(font=dict(size=8)) # Change font size
        return fig
    if scan_type == 'Scan Type = 2D/1D': 
        df2 = all_df[data_version] 
        Github_urls = all_git_df[data_version]      
        if clickData == None:
            x = 14
            line = df2.iloc[x,]
            lp = line[2]
            ld = line[1]
            temp = line[0]
        else:
            temp = clickData['points'][0]['y']
            lp = clickData['points'][0]['x']
            ld = clickData['points'][0]['z']
        filtered_df = Github_urls[(Github_urls['Temp']== temp)]
        filtered_df2 = filtered_df[(filtered_df['Laser_power']== lp)]
        filtered_df3 = filtered_df2[(filtered_df2['Laser_Detuning']== ld)]
        data_url = filtered_df3.iloc[0,0]        
        df = pd.read_table(data_url, index_col=False)
        df.columns = df.iloc[0]
        df =df.iloc[1:]
        if data_version == 14: 
            df_2d = df.iloc[0:960, 0:3] #2D data 
        else :
            df_2d = df.iloc[0:441, 0:3] #2D data  
        newdf = df_2d.apply(pd.to_numeric)
        if clickData2 == None:
            x = 0
        else:
            y = clickData2['points'][0]['y']
        filtered_df = newdf[(newdf['Z  Field (nT)']== y)]
        fig = px.line(filtered_df, x='X  Field (nT)', y='Photodiode Voltage (V)')
        fig.update_traces(mode='markers+lines')  
        fig.update_layout(margin={'l': 0, 'b': 0, 't': 0, 'r': 10}, hovermode='closest') #Change margins
        fig.update_layout(height=150)
        fig.update_layout(font=dict(size=8)) # Change font size
        return fig  
    
    
if __name__ == '__main__':
    app.run_server()
