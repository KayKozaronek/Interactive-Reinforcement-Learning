import numpy as np 
import matplotlib.pyplot as plt 
  
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