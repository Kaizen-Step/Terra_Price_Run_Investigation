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
st.set_page_config(page_title='Luna Daily & Hourly Change - Terra Price Run',
                   page_icon=':bar_chart:', layout='wide')
st.title('🚀Luna Daily & Hourly Change')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Hourly_Price_Change':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/0fd22bc0-fa87-4f33-b1fc-3133ddef76d1/data/latest')
    elif query == 'Daily_Price_Change':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/f4c71920-1bd8-41e3-a1eb-be6aadb537fe/data/latest')
    return None


Hourly_Price_Change = get_data('Hourly_Price_Change')
Daily_Price_Change = get_data('Daily_Price_Change')


st.subheader('Luna Price Charts')

df = Hourly_Price_Change
df2 = Daily_Price_Change


# Hourly Price Change Comprison
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df["DATE"], y=df["SOL_CHANGE"],
                      name="SOL_CHANGE"), secondary_y=False)
fig.add_trace(go.Line(x=df["DATE"], y=df["BTC_CHANGE"],
                      name="BTC_CHANGE"), secondary_y=False)
fig.add_trace(go.Line(x=df["DATE"], y=df["ETH_CHANGE"],
                      name="ETH_CHANGE"), secondary_y=False)
fig.add_trace(go.Line(x=df["DATE"], y=df["MATIC_CHANGE"],
                      name="MATIC_CHANGE"), secondary_y=False)
fig.add_trace(go.Line(x=df["DATE"], y=df["OP_CHANGE"],
                      name="OP_CHANGE"), secondary_y=False)
fig.update_layout(
    title_text='Hourly Price Change Comprison'.title())
fig.update_yaxes(title_text='Price Change', secondary_y=False)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Daily Price Change Comprison
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df2["DATE"], y=df2["SOL_CHANGE"],
                      name="SOL_CHANGE"), secondary_y=False)
fig.add_trace(go.Line(x=df2["DATE"], y=df2["BTC_CHANGE"],
                      name="BTC_CHANGE"), secondary_y=False)
fig.add_trace(go.Line(x=df2["DATE"], y=df2["ETH_CHANGE"],
                      name="ETH_CHANGE"), secondary_y=False)
fig.add_trace(go.Line(x=df2["DATE"], y=df2["MATIC_CHANGE"],
                      name="MATIC_CHANGE"), secondary_y=False)
fig.add_trace(go.Line(x=df2["DATE"], y=df2["OP_CHANGE"],
                      name="OP_CHANGE"), secondary_y=False)
fig.update_layout(
    title_text='Daily Price Change Comprison'.title())
fig.update_yaxes(title_text='Price Change', secondary_y=False)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
