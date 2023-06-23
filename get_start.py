import gymnasium as gym

env = gym.make("src:src/GridWorld-v0", render_mode="human")

observation, info = env.reset()

while True:
    action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        observation, info = env.reset()

env.close()
