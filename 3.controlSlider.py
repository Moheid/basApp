## Project Created Date: 2023-08-23
## Project authoer: 'Mohamed Ibrahim'
## Project version: 01

# Preview project on window
## panel serve 'basApp.py' --autoreload --show

import panel as pn 


# YOu can change the template type 
pn.extension(sizing_mode = "stretch_widh", template="fast")

# Create site and and Dashboard Title 
pn.state.template.param.update(site="Dashboard", title="Slider Control", sidebar_width=200)

def model(count=5): # Create a widget slider counter
    return "# Hi World developers\n"*count
pn.panel("# Setting").servable(area="sidebar") # area="sidebar" put in sidebar
count_widget = pn.widgets.IntSlider(value=5, start=0, end=5, name="Count").servable(area="sidebar")
imodel = pn.bind(model, count=count_widget)


pn.panel(imodel).servable() # Bold font weight, changed by #
