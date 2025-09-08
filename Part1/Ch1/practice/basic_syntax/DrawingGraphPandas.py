import altair as alt
import pandas as pd
import numpy as np

x = np.linspace(-5, 5, 100)
y = x ** 2

df = pd.DataFrame({'x': x, 'y': y})

# Create a zooming selection
zoom = alt.selection_interval(bind='scales')

chart = alt.Chart(df).mark_line().encode(
    x = 'x',
    y = 'y'
).properties(
    title = 'y = x^2'
).add_params(
    zoom
)

chart