
## Graph takes a list of x values, y values, and x and y variables
## and list of values "text" for each value to demonstrate when clicked. 

# from correlations.py import *
import plotly.plotly as py
py.sign_in('healthy_neighborhoods','d806djbyh8')
import plotly.graph_objs as go
# trace0 = 0
# trace1 = 0 
# trace2 = 0
# trace3 = 0
# trace4 = 0 
# trace5 = 0
# trace6 = 0
# trace7 = 0
# trace8 = 0


COLORS = ["FF0000", "FF00FF"]

l = [[[1, 2, 3], [2, 2, 2], ["Hyde_park", "Town 1", "town 2"]], [[3, 4], [7, 7], ["town3", "town4"]]]

def scatter_plot(l, COLORS):
  for i, val in enumerate(l):
    color = COLORS[i]
    x = val[0]
    y = val[1]
    text = val[2]
    


trace0 = go.Scatter(
    x=[1, 2, 3, 4, 5, 6, 7],
    y=[3, 5, 9, 10, 11, 12, 13],
    mode='markers',
     marker=dict(color="FF0000", size=12,
                line=dict(width=1)
               ),      
      # color='red',
      name='Americas',
      text=["testing", "t2", "t3", "t4", "t5", "t6"]
    )


data= [trace0]
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
<<<<<<< HEAD
py.image.save_as(fig, filename='testing_plot.png')
# py.iplot(fig, filename='healthy-neighborhoods')

scatter_plot(l)
=======


py.image.save_as(fig, filename='scatter_plot.png')
py.iplot(fig, filename='life-expectancy-per-GDP-2007')

>>>>>>> 0b1a9e423f97c40f07c56dc480251e92fca2a82e
