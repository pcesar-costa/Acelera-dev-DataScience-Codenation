import streamlit as st
import src.utils.utils as utils

import src.sidebar.main_sidebar as msb
import src.pages.Header as Header
import src.pages.Home as Home
import src.pages.Splitdata as Splitdata
import src.pages.Visualization as Visualization
import src.pages.Manipulation as Manipulation

import pandas as pd

PAGES = {
    "Home": Home,
    "Split Data": Splitdata,
    "Data Visualization": Visualization,
    "Data Manipulation": Manipulation
}

@st.cache
def load_data(n):
    return 'teste'

def main():
    page = PAGES['Home']
    st.sidebar.title("Navigation")
    st.sidebar.title("To start, upload a csv file")
    file = st.sidebar.file_uploader("Upload or drop your file here:")
    utils.write_page(Header)

    if file is not None:
        data = pd.read_csv(file)
        shape = data.shape
        
        st.sidebar.markdown(f"<h3 style='text-align: center;'>Wow! Your file have <a style='color: blueviolet;'>{shape[0]}</a> rows and <a style='color: blueviolet;'>{shape[1]}</a> columns. What would you like to do?</h3>", unsafe_allow_html=True)
        selection = st.sidebar.selectbox('',('Home','Split Data','Data Manipulation','Data Visualization'))
        
        if(selection == 'Select a option'):
            page = PAGES['Home']
        else:
            page = PAGES[selection]

        with st.spinner(f"Loading page ..."):
            utils.write_page(page, data=data)
    
if __name__ == "__main__":
    main()