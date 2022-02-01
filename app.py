from Pseudocode import Pseudocode
import streamlit as st
from Chapters import Chapter00, Chapter01, Chapter02#, Chapter03
from utils import CHAPTEROPTIONS 
from Chapters.Chapter03 import Chapter03
from Chapters.Chapter03.Exercises import *

st.title('Reinforcement Learning Exercises')

st.sidebar.title('Select a Chapter')
option = st.sidebar.selectbox(label ='',
    options=CHAPTEROPTIONS)

clean_option = option.split('-',1)[0].replace(' ','')

eval(clean_option).run()