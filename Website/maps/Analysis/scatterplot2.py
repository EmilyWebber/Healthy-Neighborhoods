
## Graph takes a list of x values, y values, and x and y variables
## and list of values "text" for each value to demonstrate when clicked. 

# from correlations.py import *
import plotly.plotly as py
py.sign_in('trashpanda2000','oxwvk6ndxa')
import plotly.graph_objs as go
import plotly.tools as tls




trace0 = go.Scatter(
    x=[12779.379640000001, 3822.1370840000004, 9065.800825, 36319.235010000004,
       13171.63885, 7006.580419, 9645.06142, 8948.102923, 6025.374752000001,
       6873.262326000001, 5728.353514, 5186.050003, 1201.637154,
       3548.3308460000003, 7320.880262000001, 11977.57496, 2749.320965,
       9809.185636, 4172.838464, 7408.905561, 19328.70901, 18008.50924,
       42951.65309, 10611.46299, 11415.805690000001],
    y=[75.32, 65.554, 72.39, 80.653, 78.553, 72.889, 78.782, 78.273, 72.235,
       74.994, 71.878, 70.259, 60.916000000000004, 70.19800000000001, 72.567,
       76.195, 72.899, 75.53699999999999, 71.752, 71.421, 78.74600000000001,
       69.819, 78.242, 76.384, 73.747],
    mode='markers',
    marker=dict(size=12,
                line=dict(width=1)
               ),
    name='Americas',
    text=['Country: Argentina<br>Population: 40301927.0', 
          'Country: Bolivia<br>Population: 9119152.0', 
          'Country: Brazil<br>Population: 190010647.0', 
          'Country: Canada<br>Population: 33390141.0', 
          'Country: Chile<br>Population: 16284741.0', 
          'Country: Colombia<br>Population: 44227550.0', 
          'Country: Costa Rica<br>Population: 4133884.0', 
          'Country: Cuba<br>Population: 11416987.0', 
          'Country: Dominican Republic<br>Population: 9319622.0', 
          'Country: Ecuador<br>Population: 13755680.0', 
          'Country: El Salvador<br>Population: 6939688.0', 
          'Country: Guatemala<br>Population: 12572928.0', 
          'Country: Haiti<br>Population: 8502814.0', 
          'Country: Honduras<br>Population: 7483763.0', 
          'Country: Jamaica<br>Population: 2780132.0', 
          'Country: Mexico<br>Population: 108700891.0', 
          'Country: Nicaragua<br>Population: 5675356.0', 
          'Country: Panama<br>Population: 3242173.0', 
          'Country: Paraguay<br>Population: 6667147.0', 
          'Country: Peru<br>Population: 28674757.0', 
          'Country: Puerto Rico<br>Population: 3942491.0', 
          'Country: Trinidad and Tobago<br>Population: 1056608.0', 
          'Country: United States<br>Population: 301139947.0', 
          'Country: Uruguay<br>Population: 3447496.0', 
          'Country: Venezuela<br>Population: 26084662.0'],
    )


data = [trace0]
layout = go.Layout(
    title='xpectancy v. Per Capita GDP, 2007',
    hovermode='closest',
    xaxis=dict(
        title='Losing their soul',
        ticklen=5,
        zeroline=False,
        gridwidth=2,
    ),
    yaxis=dict(
        title='Gingerness',
        ticklen=5,
        gridwidth=2,
    ),
)
fig = go.Figure(data=data, layout=layout)
py.image.save_as(fig, filename='scatter_plot.png')
py.iplot(fig, filename='life-expectancy-per-GDP-2007')
