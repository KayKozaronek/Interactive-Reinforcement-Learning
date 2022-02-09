import streamlit as st

def show():    
    st.write('### Exercise 2.2: Bandit example')
    st.write(r"""
                Consider a *k*-armed bandit problem with *k = 4* actions,
                denoted 1, 2, 3, and 4.
                """)
    st.write(r"""
                Consider applying to this problem 
                a bandit algorithm using ε-greedy action selection, 
                sample-average action-value estimates, and initial 
                estimates of $Q_1(a) = 0$, for all *a*.
                """)
    st.write(r""" 
                Suppose the initial sequence of actions and rewards is
                
                $A_1=1, R_1=1, A_2=2, R_2=1, A_3=2, R_3=2, A_4=2, 
                R_4=2, A_5=3, R_5=0$. 
                """)
    st.write(r"""
                On some of these time steps the ε case may have occurred, 
                causing an action to be selected at random. 
                - On which time steps did this definitely occur? 
                - On which time steps could thispossibly have occurred?
                """)

    with st.expander('See Solution'):
        st.write('TO BE WRITTEN')