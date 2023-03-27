from bokeh.layouts import row, gridplot
from bokeh.models import ColumnDataSource, CustomJS
from bokeh.plotting import figure, show
from bokeh.io import output_file, show
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("factbook_fixed.xlsx")
# data = pd.read_csv("factbook_fixed.xlsx", delimiter= ',')

# print(data.columns)

x = data['  Population ']

x = np.asarray(x)

# for i in range(len(x)):
#   x[i] = x[i].replace(",","")
#   x[i] = x[i].replace(" ","")
# x = x.astype(int)

y = data['  Oil consumption ']

y = np.asarray(y)
# for i in range(len(y)):
#   y[i] = y[i].replace(",", "")
#   y[i] = y[i].replace(" ", "")
# y = y.astype(int)

z = data['  GDP per capita ']
z = np.asarray(z)
for i in range(len(z)):
  z[i] = z[i].replace(",","")
  z[i] = z[i].replace(" ","")
  z[i] = z[i].replace("$","")
zi = [int(float(j)) for j in z]

p = data[' Death rate']
p = np.asarray(p)

q = data[' Birth rate']
q = np.asarray(q)

xy = list(zip(x, y, zi))

# Mengurutkan array berdasarkan array x
xy.sort(key=lambda a: a[0])
x_sorted, y_sorted, z_sorted = zip(*xy)

pq = list(zip(zi, p, q))

# Mengurutkan array berdasarkan array x
pq.sort(key=lambda a: a[0])
x1_sorted, p_sorted, q_sorted = zip(*pq)

output_file("brushing.html")

x = x_sorted
x1 = x1_sorted
y0 = z_sorted
y1 = y_sorted
p0 = p_sorted
p1 = q_sorted

# create a column data source for the plots to share
source = ColumnDataSource(data=dict(x=x, y0=y0, y1=y1))
source1 = ColumnDataSource(data=dict(x1=x1, p0=p0, p1=p1))

TOOLS = "box_select,lasso_select,help,wheel_zoom"

# create a new plot and add a renderer
left = figure(tools=TOOLS, width=300, height=300, title=None)
left.circle('x', 'y0', source=source)
left.xaxis.axis_label = 'Population'
left.yaxis.axis_label = 'GDP per Capita'
# create another new plot and add a renderer
right = figure(tools=TOOLS, width=300, height=300, title=None)
right.circle('x', 'y1', source=source)
right.xaxis.axis_label = 'Population'
right.yaxis.axis_label = 'Oil Consumtion'
# create another new plot and add a renderer
pi = figure(tools=TOOLS, width=300, height=300, title=None)
pi.circle('x1', 'p0', source=source1)
pi.xaxis.axis_label = 'GDP per Capita'
pi.yaxis.axis_label = 'Death Rate'
# create another new plot and add a renderer
qi = figure(tools=TOOLS, width=300, height=300, title=None)
qi.circle('x1', 'p1', source=source1)
qi.xaxis.axis_label = 'GDP per Capita'
qi.yaxis.axis_label = 'Birth Rate'

p = gridplot([[left, right], [pi, qi]])
show(p)