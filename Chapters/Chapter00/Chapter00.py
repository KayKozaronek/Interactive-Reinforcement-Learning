import streamlit as st

def run():
    st.write("""
            Welcome to this interactive Learning Experience.
            
            This is a resource that follows the first 2 Parts in Sutton and Bartos  
            ['An Introduction to Reinforcement Learning'](http://www.incompleteideas.net/book/RLbook2020.pdf)
            
            This resource presents answers to the exercises in the aforementioned book. 
            
            Where possible, interactive visualizations will aim at helping the reader understand key concepts.
            
            Lastly, there is a collection of simple implementations of the pseudocode you'll encounter in the book.
            All implementations are written in Python with the help of NumPy. 
            
            ### Structure:
            
                - Who is this for?
                - What does it contain?
                - Who made it? 
            
            """)
    
    st.write("Click the button if you're ready to learn about Reinforcement Learning!")
    
    if st.button("You're awesome"):
        st.balloons()