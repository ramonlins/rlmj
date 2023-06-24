import gymnasium as gym
from src.agents.qlearning import QL

env = gym.make("src:src/GridWorld-v0", render_mode="human", size=4)
agent = QL()
print(agent)

observation, info = env.reset()
i = 0
while True:
    action = agent.action(observation['agent'])
    next_observation, reward, terminated, truncated, info = env.step(action)

    agent.update(observation['agent'], action, reward, next_observation['agent'])

    observation = next_observation

    if terminated or truncated:
        observation, info = env.reset()
        print(f"Time spent: {i}")
        i = 0

    i += 1

env.close()
