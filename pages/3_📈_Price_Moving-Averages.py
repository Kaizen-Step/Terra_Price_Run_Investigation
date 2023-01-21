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
st.title('📈Technichal Indicators')

st.text(" \n")
st.subheader('Price Moving Averages')
st.text(" \n")

st.write("""  
Moving averages are one of the core indicators in technical analysis, and there are a variety of different versions. SMA is the easiest moving average to construct. It is simply the average price over the specified period. The average is called "moving" because it is plotted on the chart bar by bar, forming a line that moves along the chart as the average value changes.  
SMAs are often used to determine trend direction. If the SMA is moving up, the trend is up. If the SMA is moving down, the trend is down. A 200-bar SMA is a common proxy for the long-term trend. 50-bar SMAs are typically used to gauge the intermediate trend. Shorter-period SMAs can be used to determine shorter-term trends.



""")


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

st.write("""  
Price crossing SMA is often used to trigger trading signals. When prices cross above the SMA, you might want to go long or cover short; when they cross below the SMA, you might want to go short or exit long.
SMA Crossing SMA is another common trading signal. When a short period SMA crosses above a long period SMA, you may want to go long. You may want to go short when the short-term SMA crosses back below the long-term SMA.
In addition, SMAs indicate a rising trend if different period moving averages are placed on top of each other respectively and the price is higher than theirs.




""")

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

st.write("""  
On 8 and 9 Jan, we saw this pattern of SMA in both hourly and daily charts of Luna price, which indicated that the trend was rising.




""")
