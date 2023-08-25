## Project Created Date: 2023-08-25
## Project version: 06

# Preview project on window
## panel serve 'basApp.py' --autoreload --show

import panel as pn 
import pandas as pd
import hvplot.pandas # pip install hvplot
import plotly.express as px 

ACCENT = "green"

# You can change the template type 
pn.extension(sizing_mode = "stretch_width", template="fast")

# Create site and and Dashboard Title 
pn.state.template.param.update(
    site="Dasher", title="Data Analysis Insight", sidebar_width=200,
    accent_base_color=ACCENT, header_background=ACCENT, font="Comic Sans MS"
    )

def model(count=5): # Create a widget slider counter
    data = pd.DataFrame ({"respondents": range(0, count), "views": range(0,count)})
    plot = px.line(data, color_discrete_sequence=[ACCENT]) # Add color plot that matach the theme
    return plot

# ADD IMAGE 

pn.pane.PNG("https://miro.medium.com/v2/resize:fit:540/1*J_EXEmUkOcg-rgzJudUhZQ.png", sizing_mode="scale_width", embed=False).servable(area="sidebar")
pn.panel("# Setting").servable(area="sidebar") # area="sidebar" put in sidebar

## Plot one
count_widget = pn.widgets.IntSlider(value=5, start=0, end=5, name="Count").servable(area="sidebar")
imodel = pn.bind(model, count=count_widget)
pn.panel(imodel, inbox= False, loading_indicator=True).servable() # Bold font weight, changed by #

## Plot Two
count_widget = pn.widgets.IntSlider(value=5, start=0, end=5, name="Count").servable(area="sidebar")
imodel = pn.bind(model, count=count_widget)
pn.panel(imodel, inbox= False, loading_indicator=True).servable() # Bold font weight, changed by #
