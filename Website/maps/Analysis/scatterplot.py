
## Graph takes a list of x values, y values, and x and y variables
## and list of values "text" for each value to demonstrate when clicked. 

# from correlations.py import *
import plotly.plotly as py
py.sign_in('trashpanda2000','oxwvk6ndxa')
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[],
    y=[],
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
    title= "title goes here",
    hovermode='closest',
    xaxis=dict(
        title='title goes here',
        ticklen=5,
        zeroline=False,
        gridwidth=2,
    ),
    yaxis=dict(
        title='',
        ticklen=5,
        gridwidth=2,
    ),
)
fig = go.Figure(data=data, layout=layout)
# py.image.save_as(fig, filename='scatter_plot.png')
# py.iplot(fig, filename='life-expectancy-per-GDP-2007')


