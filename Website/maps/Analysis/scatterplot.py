
## Graph takes a list of x values, y values, and x and y variables
## and list of values "text" for each value to demonstrate when clicked. 
from correlations import get_scatter_array
import plotly.plotly as py
py.sign_in('healthy_neighborhoods','d806djbyh8')
import plotly.graph_objs as go

VALUES = ["var0", "var1", "var2","var3", "var4", "var5", "var6", "var7", "var8"]

def create_trace(i, val, colors):
    '''
    Takes index, list of X, Y, and neighborhood values and creates a trace object
    with color
    '''

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
      text=neighborhoods)
    return trace

def plot_graph(var1, var2):
    '''
    input: Receives two string variables from django
         Receives scatter, list of 9 lists, each interior list with an x, y, and neighborhood get_scatter_array 
         Receives colors, an ordered list corresponding with the interior lists of scatter
    output: Creates a trace for each of 9 lists , append to data file and creating scatterplot 
  
    '''
    scatter, colors = get_scatter_array(var1, var2)
    graph_title = var1 + ' vs ' + var2
    data = []
    for i, val in enumerate(scatter):
        trace = create_trace(i, val, colors)
        if trace:
          data.append(trace)
    layout = go.Layout(
    showlegend=False,
    title= graph_title,
    hovermode='closest',
    xaxis=dict(
        title=var1,
        ticklen=5,
        zeroline=False,
        gridwidth=2,
    ),
    yaxis=dict(
        title=var2,
        ticklen=5,
        gridwidth=2,
    ),
  )
    fig = go.Figure(data=data, layout=layout)
    py.image.save_as(fig, filename='neighborhoods.png')
    py.iplot(fig, filename='healthy-neighborhoods')
  
plot_graph(var1, var2)

# for Devin, new html embed  for website as of 03/09/2016
# <div>
#     <a href="https://plot.ly/~healthy_neighborhoods/0/" target="_blank" title="Gonorrhea in Females vs Below Poverty Level" style="display: block; text-align: center;"><img src="https://plot.ly/~healthy_neighborhoods/0.png" alt="Gonorrhea in Females vs Below Poverty Level" style="max-width: 100%;width: 974px;"  width="974" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
#     <script data-plotly="healthy_neighborhoods:0"  src="https://plot.ly/embed.js" async></script>
# </div>