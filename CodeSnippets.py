VIOLIN_PLOT_10_ARMED_TESTBED = """num_random = 2
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
                })
                
df = pd.DataFrame(d)

fig = px.violin(df, 
                x=df['action'], 
                y=df['value'],
                box=True,
                color=df['action'],
                labels={
                    "action": "Action",
                    "value": "Reward Distribution",
                },
                title='10-armed Testbed')            
"""

SIMPLE_BANDIT_ALG = """action_space = [0,1,2,3]
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
"""