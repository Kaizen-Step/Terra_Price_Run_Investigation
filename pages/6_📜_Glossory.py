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
st.set_page_config(page_title='Glossory - Terra Price Run Dashboard',
                   page_icon=':bar_chart:', layout='wide')
st.title('📜Glossory')

st.write(""" ## SQL Codes ## """)
# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.write("""  In this dashboard, some comparisons are derived from [Mr. Hesam Inanloo's dashboard-Surge of Optimism](https://app.flipsidecrypto.com/dashboard/a-surge-of-optimism-QOVd_S) that analyzes Optimism token price over time.    

At the following links, you can find the SQL codes that are used in this dashboard: 

""")

# SQL Codes
st.write("""
1. https://app.flipsidecrypto.com/velocity/queries/0fd22bc0-fa87-4f33-b1fc-3133ddef76d1
2. https://app.flipsidecrypto.com/velocity/queries/f4c71920-1bd8-41e3-a1eb-be6aadb537fe
3. https://app.flipsidecrypto.com/velocity/queries/e627da4e-fc25-4066-b74a-971dd5c7e5de
4. https://app.flipsidecrypto.com/velocity/queries/cf8753e0-4b4c-43cf-a4be-ce6ef89cca93
5. https://app.flipsidecrypto.com/velocity/queries/44b30281-85a8-43c2-902f-055a415a3f82
6. https://app.flipsidecrypto.com/velocity/queries/d5758b1a-796e-4bd9-8fa1-1c501ec2d07c
7. https://app.flipsidecrypto.com/velocity/queries/67e84570-f811-494c-840f-3ea046558e63
8. https://app.flipsidecrypto.com/velocity/queries/a23782b4-4a8b-4de3-8f28-b119a122e773
9. https://app.flipsidecrypto.com/velocity/queries/bf5c3d50-a8c2-49fa-bccf-51decd2b4866
10. https://app.flipsidecrypto.com/velocity/queries/e720740d-6e81-4d3f-bac0-ef7077849e0d


""")
