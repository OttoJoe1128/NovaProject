import plotly.express as px
import pandas as pd

def create_plot(data):
    df = pd.DataFrame({'Zaman': list(range(len(data))), 'Değer': data})
    fig = px.line(df, x='Zaman', y='Değer', title='Veri Zaman Serisi')
    return fig.to_html(full_html=False)
