import streamlit as st 
import pandas as pd 
import datetime 
# Title 

# Welcome Text 

# Side Bar with Chapters 
st.sidebar.write('This is some text')
st.sidebar.button('Click me!')

# LaTeX example 
st.latex("\int a x^2 \, dx")

# Code Example
st.code("a = 1234")

# Metric example 
st.metric("My metric", 42, 2)

# Line chart 
# st.line_chart(my_data_frame)

# Buttons
clicked = st.button("It's a button!")

selected = st.checkbox("Tick this box")

genre = st.radio(
     "What's your favorite movie genre",
     ('Comedy', 'Drama', 'Documentary'))

option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

age = st.slider('How old are you?', 0, 130, 25)

t = st.time_input('Set an alarm for', datetime.time(8, 45))


# Video 
# video_file = open('myvideo.mp4', 'rb')
# video_bytes = video_file.read()

# st.video(video_bytes)


# Time bar
import time

my_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)
    if percent_complete == 99:
        st.balloons()

