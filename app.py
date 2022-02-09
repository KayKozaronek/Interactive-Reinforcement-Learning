from Chapters.Chapter00 import Chapter00
from Chapters.Chapter01 import Chapter01
from Chapters.Chapter02 import Chapter02
from Chapters.Chapter03 import Chapter03
from Chapters.Chapter09 import Chapter09
from Pseudocode import Pseudocode
import streamlit as st
from utils import CHAPTEROPTIONS 


st.title('Reinforcement Learning Exercises')

st.sidebar.title('Select a Chapter')
option = st.sidebar.selectbox(label ='',
    options=CHAPTEROPTIONS)

clean_option = option.split('-',1)[0].replace(' ','')

eval(clean_option).run()