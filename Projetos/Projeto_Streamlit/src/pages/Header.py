import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns

PAGE_NAME = "Home"
CSS_FILE = './src/css/style.css'
CODENATION_LOGO = "./src/images/codenation.png"
codenation_logo = Image.open(CODENATION_LOGO)

with open(CSS_FILE) as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

def title_purple(text, kind):
    return st.markdown(f"<{kind} style='text-align: center; color: blueviolet;'>{text}</{kind}>", unsafe_allow_html=True)

def center(text, kind):
    return st.markdown(f"<{kind} style='text-align: center;'>{text}</{kind}>", unsafe_allow_html=True)


def bold(text):
    return st.markdown(f"<h2><b>{text}</h2>", unsafe_allow_html=True)

def violet(text):
    return f"<a style='color: blueviolet;'>{text}<a>"

def write(**kwargs):
    with st.spinner(f"Loading {PAGE_NAME}..."):
        with open(CSS_FILE) as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

        st.image(codenation_logo)
        title_purple("DATA SCIENCE STREAMLIT PLATFORM", 'h1')
        #center("vizualization and cleaning data in a simple way", 'h4')
