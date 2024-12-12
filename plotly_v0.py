import json
from datetime import datetime
import plotly.graph_objects as go

def my_plot(filename: str):
    #print("filename::::: ", filename)
    # Load JSON data from a file
    with open(f"{filename}.json", "r") as file:
        data = json.load(file)

    # Prepare data for plotting
    x_values = []
    y_values = []

    for timestamp, values in data.items():
        x_values.append(datetime.fromtimestamp(int(timestamp)))  # Convert timestamp to datetime
        y_values.append(values['score'] * 100)  # Convert score to percentage

    # Create a Plotly figure
    fig = go.Figure()

    # Add the line plot
    fig.add_trace(go.Scatter(
        x=x_values,
        y=y_values,
        mode='lines+markers',
        line=dict(color='blue'),
        marker=dict(size=6),
        name=f"{filename} Score"
    ))

    # Customize layout
    fig.update_layout(
        title=f"{filename} Activity Score over Time",
        xaxis_title="Date",
        yaxis_title=f"{filename} Score (%)",
        xaxis=dict(tickformat="%Y-%m-%d", tickangle=45),
        margin=dict(l=40, r=40, t=50, b=50),
        height=400
    )

    return fig
