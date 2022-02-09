import streamlit as st
import numpy as np 
import pandas as pd 
import plotly.express as px 
from CodeSnippets import VIOLIN_PLOT_10_ARMED_TESTBED

def show():
    
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
    
