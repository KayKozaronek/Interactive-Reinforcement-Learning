import streamlit as st
import pandas as pd 
import numpy as np
import plotly.express as px
from Chapters.Chapter09.Exercises import exercise_9_2, exercise_9_3 
# from CodeSnippets import 

def run():
    st.write('## Chapter 09 - On-policy Prediction with Approximation')

    exercise_9_2.show()
    exercise_9_3.show()
    

