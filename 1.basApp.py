## Project Created Date: 2023-08-23
## Project authoer: 'Mohamed Ibrahim'
## Project version: 01

# Preview project on window
## panel serve 'basApp.py' --autoreload --show

import panel as pn 


# YOu can change the template type 
pn.extension(template="fast")

# Create site and and Dashboard Title 
pn.state.template.param.update(site="Learn Panel", title="Panel Courses")

pn.panel("# Setting").servable(area="sidebar") # area="sidebar" put in sidebar

# Intro Dashboard body
#pn.panel("Hi World developers").servable() # Normal font weight
pn.panel("# Hi World developers").servable() # Bold font weight, changed by #
