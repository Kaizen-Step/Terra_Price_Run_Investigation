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
st.title('🌌Swap and Price')

st.text(" \n")
st.subheader('Swaps to Luna Effect')
st.text(" \n")

st.write("""  
The last part of this dashboard is related to the swaps of Luna.
In my opinion, CEX swap volume is the main reason for token price changes, but we cannot access them, so we just consider DEX swaps based on the idea that CEX and DEX trades are correlated
The metrics that consider are the number of transactions, volume, and the number of users in hourly charts.
Metrics are divided into swaps from Luna and swaps to Luna.





""")


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

st.text(" \n")
st.subheader('Swaps From Luna Effect')
st.text(" \n")

st.write("""  
As we know, Luna's price increased to 1.7 on Jan 9,17 UTC. In that period, there were more swaps and swappers to the Luna token than swaps and swappers from the Luna token.
The volume of swaps to Luna tokens during that time was 337K, while the volume of swaps from Luna tokens was 480K.
We see that all the above swap metrics have increased significantly since Luna's price was increased on 9 January.





""")


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
