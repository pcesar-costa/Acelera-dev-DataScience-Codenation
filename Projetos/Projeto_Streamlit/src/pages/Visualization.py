import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.DataFrame()


def write(**kwargs):
    global data
    data = kwargs['data']
    st.dataframe(data.head(10))

    grps = ["ScatterPlot", "Correlation Matrix", "BoxPlot"]
    selection = st.selectbox("Select a plot type:", grps)

    cols = (data.dtypes != 'object')
    cols = list(cols[cols==True].index)

    if(selection=='Correlation Matrix'):
        columns = st.multiselect("Select features:", cols, default=cols[:7], key="corrmatrix")
        corr = data[columns].corr()
        mask = np.zeros_like(corr)
        mask[np.triu_indices_from(mask)] = True
        plt.figure(figsize=(8,8))
        sns.heatmap(corr, annot=True, mask=mask).set_title("Correlation Matrix")
        st.pyplot()

    if(selection=='ScatterPlot'):
        scatter_columns = st.multiselect("Select features:", cols, default=cols[:1])
        for c in scatter_columns:
            g = sns.distplot(data[c])
            g.set_title(str(c))
            g.set_xlabel("")
            st.pyplot()

    if(selection=='BoxPlot'):

        X = st.selectbox("Axe X:", cols)
        Y = st.selectbox("Axe Y:", data.columns)
        
        sample = int(len(data)*0.35)
        plt.figure(figsize=(8, 12))
        g = sns.boxplot(
            data=data.sample(sample),
            x=X,
            y=Y,
            orient="h"
        )
        #g.set_title(str())
        g.set_xlabel("")
        st.pyplot()
    