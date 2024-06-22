import streamlit as st
import time

def home_page():
    st.set_page_config(page_title="Vishguard App", page_icon=":shield:")
    st.markdown("# Main page 🎈")
    st.header("", divider='rainbow')


def about_page():
    st.set_page_config(page_title="About us", page_icon=":shield:")
    st.header("About Us", divider='rainbow')


def spam_detection():
    st.set_page_config(page_title="Spam Detective", page_icon=":shield:")
    st.header("Spam Detective", divider='rainbow')


def loading():
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Loading {i + 1}')
        bar.progress(i + 1)
        time.sleep(0.03)

    st.header(''':rainbow[Loading Successful...] .''')
