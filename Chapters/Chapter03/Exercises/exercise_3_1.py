import streamlit as st

def show():    
    st.write('### Exercise 3.1')
    st.write("""
             Devise three example tasks of your own that fit into the MDP framework,
             identifying for each its states, actions, and rewards. 
             Make the three examples as different from each other as possible. 
             The framework is abstract and flexible and can be applied in many different ways. 
             Stretch its limits in some way in at least one of your examples.
             """)
    
    with st.expander('See Solution'):
        st.write('#### Example 1:')
        st.write("""**Scenario:** \n 
    Deciding when and how much to fish.""")
        st.write("""**States:** \n 
    Number of fish in a given region. (Discrete)""")
        st.write("""**Actions:** \n
    - Fish
    - Don't fish
    - Artificially increase fish population
                 """)
        st.write("""**Rewards:** \n
    - Minus 10 for artificially increasing fish population 
    - Minus 1 for not fishing
    - Plus 1 for fishing
                 """)