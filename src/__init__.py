from gymnasium.envs.registration import register

# TODO: This should be changed to handle multiple environments
register(
    id="src/GridWorld-v0",
    entry_point="src.envs.pygame:GridWorldEnv",
    max_episode_steps=300,
)
