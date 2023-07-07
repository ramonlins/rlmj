import random
from typing import List, Union

from src.envs.python.dice_game import DiceGame


class ModelBasedMonteCarlo:
    def __init__(self, env):
        self.actions = env.actions
        # Initialize MDP for estimation
        self.transitions = {}
        self.rewards = {}

    def policy(self, state: str) -> str:
        if state == 'in':
            action = self.actions[random.randint(0, len(self.actions) - 1)]
        else:
            action = 'quit'

        return action

    def update_transitions_and_rewards(self,
                                       episode: List[Union[str, str, str, int]]
                                       ) -> dict:
        for state, action, next_state, reward in episode:
            # Compute the number of times a chance node transition occurs
            if (state, action) not in self.transitions:
                self.transitions[(state, action)] = {}

            if next_state not in self.transitions[(state, action)]:
                self.transitions[(state, action)][next_state] = 1
            else:
                self.transitions[(state, action)][next_state] += 1

            # Compute the cummulative rewards (return) from transitions
            if (state, action) not in self.rewards:
                self.rewards[(state, action)] = {}

            if next_state not in self.rewards[(state, action)]:
                self.rewards[(state, action)][next_state] = reward
            else:
                self.rewards[(state, action)][next_state] += reward

    def update_transition_probabilites(self):
        for state, action in self.transitions:
            total_transitions = sum(self.transitions[(state, action)].values())
            for next_state in self.transitions[(state, action)]:
                self.transitions[(state, action)][next_state] /= total_transitions

    def update_expected_rewards(self):
        for state, action in self.rewards:
            for next_state in self.rewards[(state, action)]:
                self.rewards[(state, action)][next_state] /= self.transitions[(state, action)][next_state]


def main():
    env = DiceGame()
    agent = ModelBasedMonteCarlo(env)

    eps = 10000
    for ep in range(eps):

        print(f"Episode {ep}:", end=' ', flush=True)

        state = env.reset()
        episode = []
        while True:
            action = random.choice(env.actions)

            next_state, reward, terminal, _ = env.step(state, action)

            episode.append([state, action, next_state, reward])

            if terminal:
                break

            state = next_state

        agent.update_transitions_and_rewards(episode)

        print(episode)
        print(f"Transition : {agent.transitions}")
        print(f"Acc Rewards: {agent.rewards}\n")

    agent.update_expected_rewards()
    agent.update_transition_probabilites()
    print(f"Transition Probabilites Estimated:{agent.transitions}")
    print(f"Expected Rewards:{agent.rewards}")


if __name__ == "__main__":
    main()

