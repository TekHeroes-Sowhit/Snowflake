
import streamlit as st
import requests
##pip install pillow
##pip install lottie
from streamlit_lottie import st_lottie
st.set_page_config(page_title='new',page_icon="tada",layout="wide") 
st.title('My first app')
st_name=st.text_input('Enter your name','John')
st.write(f'Hello {st_name}')
st.write('Hello',st_name)
## To add side bar
st_name=st.sidebar.text_input('sidebar')
def load_lottieurl(url):
    r=request.get(url)
    if r.status_code!=200:
        return None
    return r.json()
## localcss
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True )
local_css("style/style.css")
with st.container:
    st.write('---')
    left_col,right_col=st.columns(2)
    with left_col:
        st.header('new')
        st.write('##')
        st.write('new values')
        st.write("[Youtube channel>](https://www.youtube.com/watch?v=VqgUkExPvLY)")
    with right_col:
        st_lottie(lottie_coding,height=300,key="coding")
## project
with st.container:
    st.write('---')
    st.header('new content')
    st.write('##')
    image_col,text_col=st.columns(2,1)
    with image_col:
        st.image(img_lottie_animation)
        with text_col:
            st.subheader('new values')
            st.write("new values")
            st.markdown("[Watch video](https://www.youtube.com/watch?v=VqgUkExPvLY)")
with st.container():
    st.write('###')
    st.header("Get Intouch")
    st.write('###')
    contact_form="""
<form action="https://www.youtube.com/watch?v=VqgUkExPvLY" method="POST">
    """
    left_col,right_col=st.columns(2)
    with left_col:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_col:
        st.empty()
