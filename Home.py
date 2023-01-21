# Libraries
import streamlit as st
from PIL import Image


# Layout
st.set_page_config(page_title='Terra Price Run Investigation',
                   page_icon=':bar_chart:', layout='wide')
st.title('Terra Price Run Investigation')

# Content
c1, c2, c3, c4 = st.columns(4)
c4.image(Image.open('Images/3.png'))
with c1:
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")
    st.text(" \n")

    st.write("""# 🌔Terra (Blockchain) #""")

st.write("""
Terra is a blockchain protocol and payment platform used for algorithmic stablecoins. The project was created in 2018 by Terraform Labs, a startup co-founded by Do Kwon and Daniel Shin. It is most known for its Terra stablecoin and the associated Luna reserve asset cryptocurrency.  
In May 2022, the Terra blockchain was temporarily halted after the collapse of the stablecoin TerraUSD (UST) and Luna, in an event that wiped out almost USD45 billion in capitalization within a week. 
Terra is a blockchain that leverages fiat-pegged stablecoins to power a payment system. For consensus the Terra blockchain uses a proof-of-stake codesign. Several stablecoins are built atop the Terra protocol, including TerraUSD, which was the third-largest stablecoin by capitalization before its collapse in May 2022. The Terra blockchain has a fully functional ecosystem of Dapps such as Anchor, Mirror, and Pylon which has utilized the stable-coin infrastructure of Terra. 
Terra is a group of algorithmic stablecoins, named according to the currencies to which they are pegged—for example, TerraUSD (UST) is pegged to the U.S. dollar.  
Luna serves as the primary backing asset for Terra, and is also used as a governance token for users to vote on Terra community proposals.  
UST stablecoins were not backed by U.S. dollars; instead, it was designed to maintain its peg through a complex model called a "burn and mint equilibrium". This method uses a two-token system, whereby one token is supposed to remain stable (UST) while the other token (LUNA) is meant to absorb volatility. 
### Event ###
Beginning in the wee hours of Monday, January 9 (ET), the price of LUNA skyrocketed, from 1.37 to a high of nearly 2 before settling down at roughly 1.60.
This dashboard is designed to identify some of the major reasons for the recent price increase, and then to back up our assertions with data that underpins our findings.

### Method ###
The topics we investigate in this dashboard are as follows:  

  1- Compare the price of Luna with the price of some other cryptocurrencies. Also, compare the percentage change in price between Luna and those other cryptocurrencies in daily and hourly metrics.
  The most famous coins on the market, BTC and ETH, are being considered for this section, as well as the three most famous blockchain coins, SOL, Matic, and OP.  

  2- Look at simple moving average (SMA) indicators on daily and hourly price charts in order to perform technical analysis.  

  3- The Terra network's on-chain activity will be assessed and the impact it will have on the Luna price will be considered.  

  4- An investigation has been made into the swaps activity to and from Luna, as well as the impact it has on the price for Luna.  

We obtained all the above metrics by using the Flipside database and the Terra core schema tables.


 





 
 """
         )


st.write("""   
##### Sources #####   """)
st.write("""    1.https: // www.scoutinsights.co. in /post/luna-and -lunc-coins-destroyed  
        2.https: // www.bloomberg.com/news/articles/2022-05-14  
        3.https: // social.techcrunch.com/2022/05/12/  
        4.https: // metricsdao.notion.site/Bounty-Programs-d4bac7f1908f412f8bf4ed349198e5fe 
              """)

st.text(" \n")
st.text(" \n")

c1, c2, c3 = st.columns(3)
with c2:
    st.info(
        '**Project Supervisor:  [MetricsDao](https://metricsdao.notion.site/)**', icon="👨🏻‍💼")
with c1:
    st.info(
        '**Data:  [Flipside Crypto](https://flipsidecrypto.xyz/)**', icon="🧠")
co1, co2, co3 = st.columns(3)

with c3:

    st.info(
        '**GuitHub Link:  [GuitHub](https://github.com/Kaizen-Step/Terra_Price_Run_Investigation)**', icon="💻")
