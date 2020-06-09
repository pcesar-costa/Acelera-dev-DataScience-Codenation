import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import base64

def get_table_download_link(df, file_name):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(
        csv.encode()
    ).decode()  # some strings <-> bytes conversions necessary here
    return f'<a href="data:file/csv;base64,{b64}" download="{file_name}.csv">Download {file_name}</a>'

@st.cache(allow_output_mutation=True)
def load_data(df):
    return { 'df': df }


CSS_FILE = './src/css/style.css'

with open(CSS_FILE) as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

def title(text, kind):
    return st.markdown(f"<{kind}><b>{text}</b></{kind}>", unsafe_allow_html=True)

def write(**kwargs):
    title("What you would like to do with missing values?", 'h2')
    data = load_data(kwargs['data'])
    
    
    data_dtypes = data['df'].dtypes
    data_na = data['df'].isna().sum().sort_values(ascending=False).copy()
    data_na = data_na[data_na > 0]
    columns_missing = st.multiselect('Select features:', list(data_na.index), key="na")
    value_to_fill = st.text_input("Fill with value:")

    button = st.button("Fill missing values")
    if(button):
        with st.spinner("Working on it..."):
            d = data['df'].copy()
            for column in columns_missing:
                if(value_to_fill.isdigit()):
                    v = float(value_to_fill)
                d[column] = d[column].fillna(value=v)
                st.success("done")
            data['df'] = d.copy()

    title("Create dummie features", 'h2')
    column_dummie = st.selectbox('Select features:', list(data['df'].columns))
    button_dummie = st.button("Transform into dummie")
    if(button_dummie):
        data_dummie = pd.get_dummies(data['df'][column_dummie])
        data['df'] = data['df'].drop(columns=[column_dummie]).join(data_dummie)
        st.success(f"Column {column_dummie} transform into {list(data_dummie.columns)}")

    st.dataframe(data['df'].head(10))
    button_download = st.button("Download file")
    if(button_download):
        st.markdown(f"{get_table_download_link(data['df'], 'data.csv')}", unsafe_allow_html=True)