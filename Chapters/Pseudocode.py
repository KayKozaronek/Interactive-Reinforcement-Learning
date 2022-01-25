import streamlit as st
import numpy as np


def run():
    st.write("A simple bandit algorithm")
   
    # st.text("""
    #         Initialize, for a = 1 to k:
    #             Q(a) <- 0
    #             N(a) <- 0
                
    #         Loop forever:
    #             A <- argmax_a Q(a)with probability 1 '(breaking ties randomly)a random action  with probability'
    #             R <- bandit(A)
    #             N(A) <- N(A) + 1 
    #             Q(A) <- Q(A) + 1/N(A)[R - Q(A)]
    #         """)
    
    st.image('Chapters\simple_bandit_alg.png')
    
    code = '''action_space = [0,1,2,3]
epsilon = 0.05

def bandit_algorithm(action, epsilon):
    bandit = np.random.randn(len(action_space))
    Q = np.zeros(len(action_space))
    N = np.zeros(len(action_space))
    
    finished = False 
    
    while finished:
        if np.random.rand() < 1- epsilon:
            action = np.argmax(Q)
        else:
            np.random.choice(action_space)
        reward = bandit(action)
        N[action] = N[action] + 1
        Q[action] = Q[action] + 1/N[action] * (reward - Q[action])
    ''' 
    
    with st.expander("See NumPy implementation:"):
        st.code(code, language="python")

action_space = [0,1,2,3]
epsilon = 0.05

def bandit_algorithm(action, epsilon):
    bandit = np.random.randn(len(action_space))
    Q = np.zeros(len(action_space))
    N = np.zeros(len(action_space))
    
    finished = False 
    
    while finished:
        if np.random.rand() < 1- epsilon:
            action = np.argmax(Q)
        else:
            np.random.choice(action_space)
        reward = bandit(action)
        N[action] = N[action] + 1
        Q[action] = Q[action] + 1/N[action] * (reward - Q[action])