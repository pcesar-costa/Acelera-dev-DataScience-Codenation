import base64
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split

from time import sleep

PAGE_NAME = "Splitdata"
TOTAL = 100.0

def get_table_download_link(df, file_name):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(
        csv.encode()
    ).decode()  # some strings <-> bytes conversions necessary here
    return f'<a href="data:file/csv;base64,{b64}" download="{file_name}.csv">Download {file_name}</a>'

def write(**kwargs):
    data = kwargs['data']
    splits = st.number_input('Select a number of splits', value=2, min_value=2, max_value=3)

    train_size = st.slider('Wich value would you like to your train?', 1.0, TOTAL-5.0, value = 75.0)
    test_size_slider = st.empty()
    message = st.empty()
    test_size = round(100 - train_size, 2)
    validation_size = 0
    shape = data.shape
    if(splits == 3):
        test_size = test_size_slider.slider('Wich value would you like to your test?', 2.0, test_size - 2)
        validation_size = round(100 - train_size - test_size, 2)
        message.markdown(f'**Train size:** {train_size}% | **Test size**: {test_size}% | **Validation size**: {validation_size}%',unsafe_allow_html=True)
    else:
        message.markdown(f'**Train size:** {train_size}% | **Test size**: {test_size}%',unsafe_allow_html=True)

    target_colum = st.selectbox("Target column:", data.columns)

    single_file = st.radio("Download as a single file", ('No', 'Yes'))
    button = st.button("Next")
    if(button):
        Y = data[target_colum]
        X = data.drop(target_colum, axis=1)

        if(splits==3):
            aux = (data.shape[0]*validation_size) / (data.shape[0] * 100)*2

            x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=(test_size+validation_size)/100)
            x_test, x_val, y_test, y_val = train_test_split(x_test, y_test, test_size=aux)
            
        else:
            x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=test_size/100)

        if(single_file=='No'):
            st.markdown(f"{get_table_download_link(x_train, 'train.csv')}", unsafe_allow_html=True)
            st.markdown(f"{get_table_download_link(x_test, 'test.csv')}", unsafe_allow_html=True)
        else:
            x_train['train'] = True
            x_test['train'] = False

            x_train['target'] = y_train
            x_test['target'] = y_test

            file_download = pd.concat([x_train, x_test])
            st.markdown(f"{get_table_download_link(file_download, 'data.csv')}", unsafe_allow_html=True)

        if(splits == 3):
            x_val['target'] = y_val
            st.markdown(f"{get_table_download_link(x_val, 'validation.csv')}", unsafe_allow_html=True)




    
    

    
