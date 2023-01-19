# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Global Variables
theme_plotly = None  # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'Sunday']

# Layout
st.set_page_config(page_title='Price Moving Averages - Terra Price Run',
                   page_icon=':bar_chart:', layout='wide')
st.title('📈Price Moving Averages')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Hourly_Price_MA':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/cf8753e0-4b4c-43cf-a4be-ce6ef89cca93/data/latest')
    elif query == 'Daily_Price_MA':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/67e84570-f811-494c-840f-3ea046558e63/data/latest')
    return None


Hourly_Price_MA = get_data('Hourly_Price_MA')
Daily_Price_MA = get_data('Daily_Price_MA')


st.subheader('Luna Price Charts')

df = Hourly_Price_MA
df2 = Daily_Price_MA


# Luna Price Moving averages[Hourly]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df['DATE'], y=df["LUNA_PRICE"],
                      name="LUNA_PRICE"), secondary_y=False)
fig.add_trace(go.Line(x=df['DATE'], y=df['MA7'],
                      name='Hourly Moving average (MA7))'), secondary_y=True)
fig.add_trace(go.Line(x=df['DATE'], y=df['MA26'],
                      name='Hourly Moving average (MA26)'), secondary_y=True)
fig.add_trace(go.Line(x=df['DATE'], y=df['MA52'],
                      name='Hourly Moving average (MA52))'), secondary_y=True)
fig.add_trace(go.Line(x=df['DATE'], y=df['MA100'],
                      name='Hourly Moving average (MA100)'), secondary_y=True)
fig.add_trace(go.Line(x=df['DATE'], y=df['MA200'],
                      name='Hourly Moving average (MA200)'), secondary_y=True)
fig.update_layout(
    title_text='Luna Price Moving averages[Hourly]')
fig.update_yaxes(
    title_text='Price', secondary_y=False)
fig.update_yaxes(title_text='Moving averages', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Luna Price Moving averages[Daily]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df2['DATE'], y=df2["LUNA_PRICE"],
                      name="LUNA_PRICE"), secondary_y=False)
fig.add_trace(go.Line(x=df2['DATE'], y=df2['MA7'],
                      name='Daily Moving average (MA7))'), secondary_y=True)
fig.add_trace(go.Line(x=df2['DATE'], y=df2['MA26'],
                      name='Daily Moving average (MA26)'), secondary_y=True)
fig.add_trace(go.Line(x=df2['DATE'], y=df2['MA52'],
                      name='Daily Moving average (MA52))'), secondary_y=True)
fig.add_trace(go.Line(x=df2['DATE'], y=df2['MA100'],
                      name='Daily Moving average (MA100)'), secondary_y=True)
fig.add_trace(go.Line(x=df2['DATE'], y=df2['MA200'],
                      name='Daily Moving average (MA200)'), secondary_y=True)
fig.update_layout(
    title_text='Luna Price Moving averages[Daily]')
fig.update_yaxes(
    title_text='Price', secondary_y=False)
fig.update_yaxes(title_text='Moving averages', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
