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