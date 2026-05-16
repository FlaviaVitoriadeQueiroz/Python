import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Scatter(y=[1, 3, 2], line=dict(color="crimson"))],
    layout=dict(title=dict(text="A Graph Objects Figure Without Magic Underscore Notation"))
)

fig.show()