import streamlit as st
import numpy as np
from Chapters.Chapter02.Exercises import exercise_2_1, exercise_2_2, figure_2_1

def run():
    st.write('## Chapter 02 - Multi-armed Bandits')
    
    exercise_2_1.show()
    
    figure_2_1.show()    
    
    exercise_2_2.show()