import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns

PAGE_NAME = "Home"
CSS_FILE = './src/css/style.css'
CODENATION_LOGO = "./src/images/codenation.png"
codenation_logo = Image.open(CODENATION_LOGO)

def title_purple(text, kind):
    return st.markdown(f"<{kind} style='text-align: center; color: blueviolet;'>{text}</{kind}>", unsafe_allow_html=True)

def bold(text):
    return st.markdown(f"<h2><b>{text}</h2>", unsafe_allow_html=True)

def violet(text):
    return f"<a style='color: blueviolet;'>{text}<a>"

def write(**kwargs):
    with st.spinner(f"Loading {PAGE_NAME}..."):
        with open(CSS_FILE) as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

        if('data' in kwargs):
            data = kwargs['data']
            bold("About your data")
            st.markdown(f"Samples: {data.shape[0]} | Features: {data.shape[1]}")
            
            data_dtypes = data.dtypes.value_counts()
            data_dtypes = data_dtypes.apply(lambda l: round(l / data.shape[0] * 100, 2))
            plt.title("How datatype are distributed")
            g = sns.barplot(
                x=[str(i) for i in data_dtypes.index],
                y=data_dtypes.values,
                dodge=False,
                palette=sns.cubehelix_palette(reverse=True)
            )
            g.set_xlabel("type")
            g.set_ylabel("% Features")
            st.pyplot()

            data_na = data.isna().sum().sort_values(ascending=False)
            data_na = data_na.apply(lambda l: round(l / data.shape[0] * 100, 2))
            data_na = data_na[data_na > 0]
            plt.figure(figsize=(8, int(data.shape[1]/3) ))
            plt.title("Missing values in dataset")
            g_missing = sns.barplot(
                x=data_na.values,
                y=[str(i) for i in data_na.index],
                dodge=False,
                palette=sns.cubehelix_palette(reverse=True, n_colors=len(data_na)+6)
            )
            g_missing.set_xlabel("% Missing values")
            st.pyplot()

            st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            st.title("Take a look:")
            options = {
                "Header": data.head(10),
                "Tail": data.tail(10),
                "Sample": data.sample(10),
                "Describe": data.describe()
            }
            option = st.radio("", list(options.keys()))
            st.dataframe(options[option])
            




        #bold("About")
        #st.info("Hi guys, this page has the proposal to enable you to make data analysis and data exploration in a simple way. I hope you like and enjoy it!")
        
        