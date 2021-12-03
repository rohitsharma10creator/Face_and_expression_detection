import streamlit as st
from multiapp import MultiApp
import dash
from apps import home, app1, convert # import your app modules here

app = MultiApp()

st.markdown("""
# One For All Application

This Application contain all the projects that I have build in python to create this web app I have used multi-app and streamlit. 

""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("app1", app1.app)
app.add_app("Convert", convert.app)
# The main app
app.run()
