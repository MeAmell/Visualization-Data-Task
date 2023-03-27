#Imports
from bokeh.plotting import figure, show
from bokeh.layouts import layout
from bokeh.models import Div, RangeSlider, Spinner
import pandas as pd

df = pd.read_excel('factbook_fixed.xlsx')

cols = df.columns
cols = cols.map(lambda x: x.strip().replace(' ', '_'))
df.columns = cols

#Create Data
# x = df['Life_expectancy_at_birth']
# y = df["Population"]
x = df['Industrial_production_growth_rate']
y = df["GDP_real_growth_rate"]


#create plot/figure
p = figure(x_range=(1,9), width=800, height=400)
p.xaxis.axis_label = 'Industrial Production Growth Rate'
p.yaxis.axis_label = 'GDP Real Growth Rate'
points = p.circle(x=x, y=y, size=40, fill_color="#FFE1FF")


#Div
div = Div(
    text="""<p>Select the circle's size using this controller:</p>""",
    width=200,
    height=300
)

#Spinner
spinner = Spinner(
    title="Circle Size",
    low=0,
    high=60,
    step=5,
    value = points.glyph.size,
    width=200,
)

spinner.js_link("value", points.glyph, "size")

#Range Slider
range_slider = RangeSlider(
    title="Adjust X-Axis Range",
    start=0,
    end= 10,
    step=1,
    value=(p.x_range.start, p.x_range.end),
)

range_slider.js_link("value", p.x_range, "start", attr_selector=0)

range_slider.js_link("value", p.x_range, "end", attr_selector=1)

# Create layout
layout = layout(
    [
        [div, spinner],
        [range_slider],
        [p],
    ],

)

show(layout)
