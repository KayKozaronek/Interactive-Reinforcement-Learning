import streamlit as st
from Chapters import Chapter00, Chapter01, Chapter02
from utils import CHAPTEROPTIONS 

st.title('Explore Reinforcement Learning')

st.sidebar.title('Select a Chapter')
option = st.sidebar.selectbox(label ='',
    options=CHAPTEROPTIONS)

clean_option = option.split('-',1)[0].replace(' ','')

eval(clean_option).run()