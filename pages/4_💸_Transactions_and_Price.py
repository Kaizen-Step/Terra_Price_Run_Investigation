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
st.set_page_config(page_title='Transaction and Price - Terra Price Run',
                   page_icon=':bar_chart:', layout='wide')
st.title('💸Transactions and Price')

st.text(" \n")
st.subheader('On Chain Transactions')
st.text(" \n")

st.write("""  
In this part, we take look at the on-chain transactions of the Luna token.
The metrics that consider are the number of transactions, volume, and the number of users in hourly and daily charts.




""")

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'DailyLuna_TX_Volume_Price':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/44b30281-85a8-43c2-902f-055a415a3f82/data/latest')
    elif query == 'HourlyLuna_TX_Volume_Price':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/a23782b4-4a8b-4de3-8f28-b119a122e773/data/latest')
    return None


DailyLuna_TX_Volume_Price = get_data('DailyLuna_TX_Volume_Price')
HourlyLuna_TX_Volume_Price = get_data('HourlyLuna_TX_Volume_Price')


df = DailyLuna_TX_Volume_Price
df2 = HourlyLuna_TX_Volume_Price


# Luna Transactions & Price[Daily]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df["DATE"], y=df["Number of Transactions"],
                     name="Number of Transactions"), secondary_y=False)
fig.add_trace(go.Line(x=df["DATE"], y=df["LUNA_PRICE"],
                      name="LUNA_PRICE"), secondary_y=True)
fig.update_layout(
    title_text='Luna Transactions & Price[Daily]')
fig.update_yaxes(
    title_text="Number of Transactions", secondary_y=False)
fig.update_yaxes(title_text="LUNA_PRICE", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Luna Transactions & Price[Hourly]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df2["DATE"], y=df2["Number of Transactions"],
                     name="Number of Transactions"), secondary_y=False)
fig.add_trace(go.Line(x=df2["DATE"], y=df2["LUNA_PRICE"],
                      name="LUNA_PRICE"), secondary_y=True)
fig.update_layout(
    title_text='Luna Transactions & Price[Hourly]')
fig.update_yaxes(
    title_text="Number of Transactions", secondary_y=False)
fig.update_yaxes(title_text="LUNA_PRICE", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
st.text(" \n")
st.subheader('Volume')
st.text(" \n")
st.write("""  
Prior to the skyrocketing Luna price, this chart shows no particular pattern, but we can see a huge increase after 9 January. In other words, on-chain Luna activity doesn't have a significant effect on Luna's price, and vice versa it can lead to more on-chain activity when Luna's price rises.




""")
# Luna Transactions & Volume [Daily]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df["DATE"], y=df["VOLUME"],
                     name="VOLUME"), secondary_y=False)
fig.add_trace(go.Line(x=df["DATE"], y=df["LUNA_PRICE"],
                      name="LUNA_PRICE"), secondary_y=True)
fig.update_layout(
    title_text='Luna Volume & Price[Daily]')
fig.update_yaxes(
    title_text="VOLUME", secondary_y=False)
fig.update_yaxes(title_text="LUNA_PRICE", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Luna Transactions & Volume [Hourly]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df2["DATE"], y=df2["VOLUME"],
                     name="VOLUME"), secondary_y=False)
fig.add_trace(go.Line(x=df2["DATE"], y=df2["LUNA_PRICE"],
                      name="LUNA_PRICE"), secondary_y=True)
fig.update_layout(
    title_text='Luna Volume & Price [Hourly]')
fig.update_yaxes(
    title_text="VOLUME", secondary_y=False)
fig.update_yaxes(title_text="LUNA_PRICE", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

st.text(" \n")
st.subheader('Number of Users')
st.text(" \n")


# Luna Transactions & Users [Daily]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df["DATE"], y=df["Number of Users"],
                     name="Number of Users"), secondary_y=False)
fig.add_trace(go.Line(x=df["DATE"], y=df["LUNA_PRICE"],
                      name="LUNA_PRICE"), secondary_y=True)
fig.update_layout(
    title_text='Luna Users & Price[Daily]')
fig.update_yaxes(
    title_text="Number of Users", secondary_y=False)
fig.update_yaxes(title_text="Number of Users", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Luna Transactions & Users [Hourly]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df2["DATE"], y=df2["Number of Users"],
                     name="Number of Users"), secondary_y=False)
fig.add_trace(go.Line(x=df2["DATE"], y=df2["LUNA_PRICE"],
                      name="LUNA_PRICE"), secondary_y=True)
fig.update_layout(
    title_text='Luna Users & Price [Hourly]')
fig.update_yaxes(
    title_text="Number of Users", secondary_y=False)
fig.update_yaxes(title_text="Number of Users", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
