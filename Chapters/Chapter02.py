import streamlit as st
import pandas as pd 
import numpy as np
import plotly.express as px
from CodeSnippets import VIOLIN_PLOT_10_ARMED_TESTBED

def run_experiment(epsilons, timesteps, k, bandit):
    q = np.zeros(k)
    n = np.zeros(k)
    average_reward = np.zeros((timesteps, len(epsilons)))

    for epsilon_idx, epsilon in enumerate(epsilons):
        for time in range(timesteps):
            action = choose_action(epsilon, q, k)
            reward = np.random.normal(bandit[action], 1)
            n[action] += 1
            q[action] += 1/n[action] *(reward - q[action])

            average_reward[time, epsilon_idx] = (1-epsilon) * np.max(q) + epsilon * np.mean(q)

    return average_reward


def choose_action(epsilon, q, k):
    
    np.random.seed(42)  
    
    if np.random.rand() < 1-epsilon:
        action = np.argmax(q)
    else:
        action = np.random.choice(k)
    return action

def create_bandit(k):
    return np.array([np.random.normal(np.random.randn(), 1) for _ in range(k)])


def run():
    st.write('## Chapter 02 - Multi-armed Bandits')
    
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


############################### FIGURE 2.1 ###############################
    st.write('### Figure 2.1 The 10-armed Testbed')
    st.write('For those of you who want to play around with the 10-armed Testbed or are just wonder how it was created, here it is.')
    np.random.seed(42)  
    num_random = 2
    k = 10 
        
    # True value of q*(a):
    action_values = [np.random.normal(0,1) for i in range(10)] 

    d = []

    # Randomly generate 2000 k-armed bandit problems (k=10)
    for run in range(1):
        for action in range(0,10):
            # Select action a (randomly - can be any other method)
            for timestep in range(100):
                d.append(
                    {
                        "value": np.random.normal(action_values[action],1),
                        "action": action + 1          
                    }
                    )
    df = pd.DataFrame(d)
    
    fig = px.violin(df, 
                     x=df['action'], 
                     y=df['value'],
                     box = True,
                     color= df['action'],
                     labels={
                    "action": "Action",
                    "value": "Reward Distribution",
                    },
                     title='10-armed Testbed')
    
    st.plotly_chart(fig)
    
    with st.expander('See code for Violin Plot'):
        st.code(VIOLIN_PLOT_10_ARMED_TESTBED, 
                language='python')
    
    # k = 10
    # epsilons = np.array([0.001, 0.01, 0.1])
    # timesteps = 10000
    
    # bandit = create_bandit(k)
    
    # average_rewards = np.array([run_experiment(epsilons, timesteps, k, bandit) for i in range(10)]).mean(axis=0)
    
    # fig2, ax2 = plt.subplots()

    # ax2.plot(average_rewards)
    # ax2.legend(labels=['epsilon = 0.001', 'epsilon = 0.01', 'epsilon = 0.1'])
    # ax2.set_xlabel('Timesteps')
    # ax2.set_ylabel('Average Reward')
    # st.pyplot(fig2)
    
    
############################### FIGURE 2.1 ###############################
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