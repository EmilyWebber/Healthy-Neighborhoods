# Healthy-Neighborhoods

A technology and data science project for the University of Chicago's CMSC 122 Course

Primary Contributors
- Charity King
- Devin Munger
- Emily Webber

Project Proposal:
https://docs.google.com/document/d/1bp4peNHxVyWs_Vg9kCtkTzJGqBRb-ejcQmlKnwEuiv8/edit?usp=sharing

Presentation:
https://docs.google.com/presentation/d/1J2pvvc-qbDQdTnJbEbQt7Xx7Zh1wwgyArGSHP-7P1fw/edit?usp=sharing

Imported Modules
  - Plotly
  - Django
  - numpy
  - csv

Instructions for Running
  - ~Healthy-Neighborhoods/Healthy-Neighborhoods$ python3 manage.py runserver
  - URL: 127.0.0.1:8000/healthyneighborhoods

Code Structure:
  - “Healthy-Neighborhoods”
      - manage.py
          This is the file used to run the localhost server
      -mysite
          Django template, modified slightly
  - “maps”
    Analysis:
        - “data_analysis.py”
          - This file handles the data cleaning, gets correlation coefficients, assigns colors based on color matrix calculation, sends out google maps data structures, creates a trace object for plotly scatter plot
Interacts with Django framework through a primary function
main(variable_one, variable_two)
That calls plot_graph(variable_one, variable_two) and returns google maps tuples of neighborhoods
        - “color_support.py”
          - Is a support file linking x/y values into 9 different color categories of specific order, which can be changed in this file
Website:
  - “apps.py”
    - Updated Django template
  - “urls.py”
    - Updated Django template
  - “forms.py”
    - Defines Django form Variable, as well as helper functions to communicate between the Analysis and Mapping files
  - “views.py”
    - Django view functions
  - “templates”
    - Html templates for website: contains “base.html”, which is built on to form “default.html,” “documentation.html,” and health_neighborhoods_base.html”, which is in turn built on to form “health_neighborhoods_start.html” (the landing page) and         “health_neighborhoods.html” (the main graphics page)
  - “static”
    - contains static files used by website, as well as our data saved in csv
Mapping:
  - “Mapping.py” - reads in from csv in “static” directory and creates dictionary of neighborhoods linked to list of coordinates

Functionality:
On the landing page of our site, we included buttons with sample queries as a catchy hook, to give the user an idea of possible interesting or informative searches. Alternatively, a user could select two variables to interact; selecting the same indicators, or choosing a value of “None” for Variable 2, simply displays the range of the single variable. After making a selection, the user can compare indicators indefinitely. Effort was made to ensure the website was clean and easy to navigate. Consideration was also given to make the site’s graphics transition gracefully at various browser sizes. A Documentation page was added to provide context to our graphics.

Development Process:
  - Initially used recursive and object-oriented approach to querying. This proved unnecessary, even though it was fun to build and get working. Streamlined and modular approach proved most effective for teammate and user-application - that is, it was most effective to return lists of neighborhoods every time the user sent in a query, rather than generating every list of neighborhoods when the website is opened, store it, and access it per query.
    - Compared correlation coefficients for many economic indicators against many health indicators, included some of the most interesting correlations in the buttons recommended for user.
    - There are a lot of ways to get correlation coefficients, for example using pandas, but by far the easiest and most straightforward method of getting the coefficient was with numpy
- Parsing lattitude and longitude data from city’s portal was complicated
  - Researched various methods of interactive mapping
  - Initially attempted to use the Google Earth KML Layer to import a KML of polygons, but due to the deprecation of the API, resorted to building GE polygons where we could access each polygon color tag for dynamic change. 
We create a polygon for each neighborhood that is mapped onto Google Maps api in views.py, grabbing the color for each polygon from the correlation assignment in data_analysis.py
- Scatter plot
  - Plotting function in data_analysis.py file. 
  - Again, researched ways to achieve interactive graphing, and decided on Plotly
  - Had to accommodate both types of queries in data_analysis,py
  - Plotly API allows easy integration of interactive graph with html embed tag. 
