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

ATTEMPT_AT_SARSA = """
action_space = [0,1,2,3]

alpha = 0.1
epsilon = 0.01
gamma = 0.9
num_episodes = 10

policy = np.random.rand(env.observation_space.n, len(action_space))

def epsilon_greedy(state, epsilon):
  if np.random.rand() < 1-epsilon + (epsilon/4):
    action = np.argmax(Q[state,:])
  else:
    action = np.random.choice(k)
  return action

def sarsa(alpha, epsilon, num_episodes, gamma):
  # Initialization of Q[s,a]
  Q = np.random.rand(env.observation_space.n, len(action_space))

  for episode in range(num_episodes):
    starting_state = env.reset()
    action = epsilon_greedy(starting_state, epsilon)
    
    finished = False
    while not finished:
      next_state, reward, finished, _ = env.step(action)
      next_action = epsilon_greedy(next_state, epsilon)
      Q[state, action] += alpha*(reward + gamma*Q[next_state, next_action] - Q[state, action])      
      state = next_state
      action = next_action
  return Q 
  """