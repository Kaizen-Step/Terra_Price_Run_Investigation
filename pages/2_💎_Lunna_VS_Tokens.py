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
st.set_page_config(page_title='Lunna VS Tokens - Terra Price Run',
                   page_icon=':bar_chart:', layout='wide')
st.title('💎Lunna VS Tokens')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Luna_VS_Tokens':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/e627da4e-fc25-4066-b74a-971dd5c7e5de/data/latest')
    elif query == 'Hourly_Luna_VS_Tokens':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/d5758b1a-796e-4bd9-8fa1-1c501ec2d07c/data/latest')
    return None


Luna_VS_Tokens = get_data('Luna_VS_Tokens')
Hourly_Luna_VS_Tokens = get_data('Hourly_Luna_VS_Tokens')


st.subheader('Luna Price Charts')

df = Luna_VS_Tokens
df2 = Hourly_Luna_VS_Tokens

# Daily Price- Luna vs MATIC
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df["DATE"], y=df["LUNA_PRICE"],
                      name="LUNA_PRICE"), secondary_y=False)
fig.add_trace(go.Line(x=df["DATE"], y=df["MATIC_PRICE"],
                      name="MATIC_PRICE"), secondary_y=True)
fig.update_layout(
    title_text='Daily Price- Luna vs MATIC'.title())
fig.update_yaxes(title_text='Luna Price', secondary_y=False)
fig.update_yaxes(title_text="Matic Price", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Hourly Price- Luna vs MATIC
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df2["DATE"], y=df2["LUNA_PRICE"],
                      name="LUNA_PRICE"), secondary_y=False)
fig.add_trace(go.Line(x=df2["DATE"], y=df2["MATIC_PRICE"],
                      name="MATIC_PRICE"), secondary_y=True)
fig.update_layout(
    title_text='Hourly Price- Luna vs MATIC'.title())
fig.update_yaxes(title_text='Luna Price', secondary_y=False)
fig.update_yaxes(title_text="Matic Price", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Daily Price- Luna vs OP
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df["DATE"], y=df["LUNA_PRICE"],
                      name="LUNA_PRICE"), secondary_y=False)
fig.add_trace(go.Line(x=df["DATE"], y=df["OP_PRICE"],
                      name="OP_PRICE"), secondary_y=True)
fig.update_layout(
    title_text='Daily Price- Luna vs OP'.title())
fig.update_yaxes(title_text='Luna Price', secondary_y=False)
fig.update_yaxes(title_text="OP_PRICE", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Hourly Price- Luna vs OP
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df2["DATE"], y=df2["LUNA_PRICE"],
                      name="LUNA_PRICE"), secondary_y=False)
fig.add_trace(go.Line(x=df2["DATE"], y=df2["OP_PRICE"],
                      name="OP_PRICE"), secondary_y=True)
fig.update_layout(
    title_text='Hourly Price- Luna vs OP'.title())
fig.update_yaxes(title_text='Luna Price', secondary_y=False)
fig.update_yaxes(title_text="OP_PRICE", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Daily Price- Luna vs ETH
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df["DATE"], y=df["LUNA_PRICE"],
                      name="LUNA_PRICE"), secondary_y=False)
fig.add_trace(go.Line(x=df["DATE"], y=df["ETH_PRICE"],
                      name="ETH_PRICE"), secondary_y=True)
fig.update_layout(
    title_text='Daily Price- Luna vs ETH')
fig.update_yaxes(title_text='Luna Price', secondary_y=False)
fig.update_yaxes(title_text="ETH_PRICE", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Hourly Price- Luna vs ETH
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df2["DATE"], y=df2["LUNA_PRICE"],
                      name="LUNA_PRICE"), secondary_y=False)
fig.add_trace(go.Line(x=df2["DATE"], y=df2["ETH_PRICE"],
                      name="ETH_PRICE"), secondary_y=True)
fig.update_layout(
    title_text='Hourly Price- Luna vs ETH')
fig.update_yaxes(title_text='Luna Price', secondary_y=False)
fig.update_yaxes(title_text="ETH_PRICE", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Daily Price- Luna vs SOL
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df["DATE"], y=df["LUNA_PRICE"],
                      name="LUNA_PRICE"), secondary_y=False)
fig.add_trace(go.Line(x=df["DATE"], y=df["SOL_PRICE"],
                      name="SOL_PRICE"), secondary_y=True)
fig.update_layout(
    title_text='Daily Price- Luna vs SOL')
fig.update_yaxes(title_text='Luna Price', secondary_y=False)
fig.update_yaxes(title_text="SOL_PRICE", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Hourly Price- Luna vs SOL
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df2["DATE"], y=df2["LUNA_PRICE"],
                      name="LUNA_PRICE"), secondary_y=False)
fig.add_trace(go.Line(x=df2["DATE"], y=df2["SOL_PRICE"],
                      name="SOL_PRICE"), secondary_y=True)
fig.update_layout(
    title_text='Hourly Price- Luna vs SOL')
fig.update_yaxes(title_text='Luna Price', secondary_y=False)
fig.update_yaxes(title_text="SOL_PRICE", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Daily Price- Luna vs BTC
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df["DATE"], y=df["LUNA_PRICE"],
                      name="LUNA_PRICE"), secondary_y=False)
fig.add_trace(go.Line(x=df["DATE"], y=df["BTC_PRICE"],
                      name="BTC_PRICE"), secondary_y=True)
fig.update_layout(
    title_text='Daily Price- Luna vs BTC')
fig.update_yaxes(title_text='Luna Price', secondary_y=False)
fig.update_yaxes(title_text="BTC_PRICE", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Hourly Price- Luna vs BTC
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df2["DATE"], y=df2["LUNA_PRICE"],
                      name="LUNA_PRICE"), secondary_y=False)
fig.add_trace(go.Line(x=df2["DATE"], y=df2["BTC_PRICE"],
                      name="BTC_PRICE"), secondary_y=True)
fig.update_layout(
    title_text='Hourly Price- Luna vs BTC')
fig.update_yaxes(title_text='Luna Price', secondary_y=False)
fig.update_yaxes(title_text="BTC_PRICE", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
