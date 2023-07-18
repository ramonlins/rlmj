import random
from collections import defaultdict

from src.envs.python.dice_game import DiceGame


class ModelFreeMonteCarlo:
    def __init__(self, env):
        self.states = env.states
        self.actions = env.actions
        self.max_steps = 100
        self.values = defaultdict(float)
        self.counts = defaultdict(float)

    def policy(self):
        action = random.choice(self.actions)

        return action

    def run(self, episode):
        episode_reward = 0
        for state, action, reward in episode:
            episode_reward += reward  # Compute cumulative reward

            self.values[(state, action)] += episode_reward  # Add to value function
            self.counts[(state, action)] += 1  # Increment counter

    def action_value(self, state, action):
        # Value of action on average
        key = (state, action)
        if self.counts[key] > 0:
            return self.values[key] / self.counts[key]
        else:
            return 0.0


def main():
    env = DiceGame()
    agent = ModelFreeMonteCarlo(env)

    debug = False
    eps = 10000
    for _ in range(eps):

        buffer = []
        state = 'in'
        steps = 0
        while True:
            #action = agent.policy()

            action = 'stay'  # Similar to Policy Evaluation

            next_state, reward, terminal, _ = env.step(state, action)

            if debug:
                if steps == 0:
                    print(f"{state},{action},{reward},{next_state}", end='')
                else:
                    print(f",{action},{reward},{next_state}", end='')

            buffer.append([state, action, reward])

            state = next_state

            steps += 1

            if terminal:
                break

        if debug:
            print()

        agent.run(buffer)

    for state in env.states:
        for action in env.actions:
            key = (state, action)
            if key in agent.values:
                print(f"s={state}, a={action}: {agent.action_value(state, action)}")


if __name__ == "__main__":
    main()
