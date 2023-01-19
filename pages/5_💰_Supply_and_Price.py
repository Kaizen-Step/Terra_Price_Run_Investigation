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
st.set_page_config(page_title='Supply and Price - Terra Price Run',
                   page_icon=':bar_chart:', layout='wide')
st.title('💰Supply and Price')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Hourly_Swap_to_Luna_Vol_Num':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/bf5c3d50-a8c2-49fa-bccf-51decd2b4866/data/latest')
    elif query == 'Hourly_Swap_From_Luna_Vol_Num':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/e720740d-6e81-4d3f-bac0-ef7077849e0d/data/latest')
    return None


Hourly_Swap_to_Luna_Vol_Num = get_data('Hourly_Swap_to_Luna_Vol_Num')
Hourly_Swap_From_Luna_Vol_Num = get_data('Hourly_Swap_From_Luna_Vol_Num')

st.subheader('Luna Price Charts')

df = Hourly_Swap_to_Luna_Vol_Num
df2 = Hourly_Swap_From_Luna_Vol_Num


# Number of Swappers to Luna [Hourly]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df["DATE"], y=df["Daily Number of Swappers to Luna"],
                     name="Hourly Number of Swappers to Luna"), secondary_y=False)
fig.add_trace(go.Line(x=df["DATE"], y=df["LUNA_PRICE"],
                      name="LUNA_PRICE"), secondary_y=True)
fig.update_layout(
    title_text='Number of Swappers to Luna [Hourly]')
fig.update_yaxes(
    title_text="Hourly Number of Swappers to Luna", secondary_y=False)
fig.update_yaxes(title_text="LUNA_PRICE", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Number of Swaps to Luna [Hourly]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df["DATE"], y=df["Daily Number of Swaps to Luna"],
                     name="Hourly Number of Swaps to Luna"), secondary_y=False)
fig.add_trace(go.Line(x=df["DATE"], y=df["LUNA_PRICE"],
                      name="LUNA_PRICE"), secondary_y=True)
fig.update_layout(
    title_text='Number of Swaps to Luna [Hourly]')
fig.update_yaxes(
    title_text="Hourly Number of Swaps to Luna", secondary_y=False)
fig.update_yaxes(title_text="LUNA_PRICE", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Swaps Volume to Luna [Hourly]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df["DATE"], y=df["Daily Volume of Swaps to Luna"],
                     name="Hourly Volume of Swaps to Luna"), secondary_y=False)
fig.add_trace(go.Line(x=df["DATE"], y=df["LUNA_PRICE"],
                      name="LUNA_PRICE"), secondary_y=True)
fig.update_layout(
    title_text='Swaps Volume to Luna [Hourly]')
fig.update_yaxes(
    title_text="Hourly Volume of Swaps to Luna", secondary_y=False)
fig.update_yaxes(title_text="LUNA_PRICE", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Swaps Volume from Luna [Hourly]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df2["DATE"], y=df2["Daily Volume of Swaps from Luna"],
                     name="Hourly Volume of Swaps from Luna"), secondary_y=False)
fig.add_trace(go.Line(x=df2["DATE"], y=df2["LUNA_PRICE"],
                      name="LUNA_PRICE"), secondary_y=True)
fig.update_layout(
    title_text='Swaps Volume from Luna [Hourly]')
fig.update_yaxes(
    title_text="Hourly Volume of Swaps from Luna", secondary_y=False)
fig.update_yaxes(title_text="LUNA_PRICE", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Number of Swaps from Luna [Hourly]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df2["DATE"], y=df2["Daily Number of Swaps from Luna"],
                     name="Hourly Number of Swaps from Luna"), secondary_y=False)
fig.add_trace(go.Line(x=df2["DATE"], y=df2["LUNA_PRICE"],
                      name="LUNA_PRICE"), secondary_y=True)
fig.update_layout(
    title_text='Number of Swaps from Luna [Hourly]')
fig.update_yaxes(
    title_text="Hourly Number of Swaps from Luna", secondary_y=False)
fig.update_yaxes(title_text="LUNA_PRICE", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Number of Swappers from Luna [Hourly]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df2["DATE"], y=df2["Daily Number of Swappers from Luna"],
                     name="Hourly Number of Swappers from Luna"), secondary_y=False)
fig.add_trace(go.Line(x=df2["DATE"], y=df2["LUNA_PRICE"],
                      name="LUNA_PRICE"), secondary_y=True)
fig.update_layout(
    title_text='Number of Swappers from Luna [Hourly]')
fig.update_yaxes(
    title_text="Hourly Volume of Swaps to Luna", secondary_y=False)
fig.update_yaxes(title_text="LUNA_PRICE", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
