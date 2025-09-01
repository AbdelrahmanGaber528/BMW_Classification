import streamlit as st 


st.set_page_config(
    page_title="BMW App",
    layout="wide"
)

st.header("BMW Classification : ")


sidebar = st.sidebar.header("Upload File")
uploaded_file = None

with sidebar : 
    uploaded_file = st.sidebar.file_uploader("", type=["csv", "pdf", "JSON"])

