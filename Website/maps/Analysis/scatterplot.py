
## Graph takes a list of x values, y values, and x and y variables
## and list of values "text" for each value to demonstrate when clicked. 
from correlations import get_scatter_array
import plotly.plotly as py
py.sign_in('healthy_neighborhoods','d806djbyh8')
import plotly.graph_objs as go

VALUES = ["var0", "var1", "var2","var3", "var4", "var5", "var6", "var7", "var8"]
# COLORS = ["FF0000", "FF00FF"]
# l = [[[1, 2, 3], [2, 2, 2], ["Hyde_park", "Town 1", "town 2"]], [[3, 4], [7, 7], ["town3", "town4"]]]

def create_trace(i, val, colors):
    print (i, val)

    trace = VALUES[i]
    color = colors[i]
    x_vals = val[0]
    if len(x_vals) == 0:
        return None
    y_vals = val[1]
    neighborhoods = val[2]
    trace = go.Scatter(
    x= x_vals,
    y= y_vals,
    mode='markers',
     marker=dict(color=color, size=12,
                line=dict(width=1)
               ),      
      name='neighborhood',
      text=neighborhoods)
    return trace

def plot_graph(var1, var2):
    scatter, colors = get_scatter_array(var1, var2)
    data = []
    for i, val in enumerate(scatter):
        trace = create_trace(i, val, colors)
        if trace:
          data.append(trace)
    layout = go.Layout(
    title= 'Var1 vs Var2',
    hovermode='closest',
    xaxis=dict(
        title='Variable 1',
        ticklen=5,
        zeroline=False,
        gridwidth=2,
    ),
    yaxis=dict(
        title='Variable 2',
        ticklen=5,
        gridwidth=2,
    ),
  )
    fig = go.Figure(data=data, layout=layout)
    py.image.save_as(fig, filename='testing_plot.png')
# py.iplot(fig, filename='healthy-neighborhoods')
  
plot_graph("Gonorrhea in Females", "Below Poverty Level")



# py.image.save_as(fig, filename='scatter_plot.png')
# py.iplot(fig, filename='life-expectancy-per-GDP-2007')


