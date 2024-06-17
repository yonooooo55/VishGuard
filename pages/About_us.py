import streamlit as st
import components as components


components.about_page()

container_1 = st.container(height=100,border=True)
container_1.write("This is inside the container")
st.write("This is outside the container")


container_2 = st.container(border=True)
container_2.write("This is inside the container")
st.write("This is outside the container")