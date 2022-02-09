import streamlit as st

def show(): 
    st.write('### Exercise 2.1')
    st.write("""
             In ε-greedy action selection, for the case of two actions and **ε = 0.5**, what is the probability that the greedy action is selected?
             """)
    
    with st.expander('See Solution'):
        st.write("An exploratory action (which is uniformly selected over all actions) gets selected with probability") 
        st.latex(r"\text{P(Selecting Exploratory Action)} = \frac{ε}{\text{Number of Actions}}")
        st.write("We can thus infer the follwing to be true:")
        st.latex(r'\text{P(Selecting Greedy Action)} = 1 - ε + \frac{ε}{\text{Number of Actions}}')
        
        st.write('For the case of 2 actions and ε = 0.5:')
        st.latex(r'\text{P(Selecting Greedy Action)} = 1 - 0.5 + \frac{0.5}{2} = 0.75')