import random
from typing import List, Union

from src.envs.python.dice_game import DiceGame
from src.agents.policy_evaluation import PolicyEvaluation


class ModelBasedMonteCarlo:
    """
    Initializes the ModelBasedMonteCarlo class.

    Args:
        env (DiceGame): The environment for the Monte Carlo agent.
    """
    def __init__(self, env):
        self.env = env

        # Initialize MDP for estimation
        self.transitions = {}
        self.rewards = {}

    def policy(self) -> str:
        """
        Determines the action to take based on the current state.

        Returns:
            str: The action to take.
        """
        action = random.choice(self.env.actions)

        return action

    def update_transitions_and_rewards(self, episode: List[Union[str, str, str, int]]) -> None:
        """
        Updates the transition probabilities and rewards based on the given episode.

        Args:
            episode (List[Union[str, str, str, int]]): The episode containing state, action, next_state, and reward.
        """
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

    def update_transition_probabilites(self) -> None:
        """
        Updates the transition probabilities based on the recorded transitions.
        """
        for state, action in self.transitions:
            total_transitions = sum(self.transitions[(state, action)].values())
            for next_state in self.transitions[(state, action)]:
                self.transitions[(state, action)][next_state] /= total_transitions

    def update_expected_rewards(self):
        """
        Updates the expected rewards based on the recorded rewards and the number of transitions
        """
        for state, action in self.rewards:
            for next_state in self.rewards[(state, action)]:
                self.rewards[(state, action)][next_state] /= self.transitions[(state, action)][next_state]

    def policy_evaluation(self, action: str):
        """
        Performs policy evaluation to estimate the state values.

        Args:
            action (str): The action to evaluate.

        Returns:
            dict: A dictionary with state values as the keys.
        """

        gamma = 0.9999

        V = {state: 0 for state in self.env.states}

        for _ in range(100):
            for state in self.env.states:

                if (state, action) in self.transitions:
                    all_possible_next_states = self.transitions[(state, action)]

                    Q = 0
                    for next_state in all_possible_next_states:
                        transition_prob = self.transitions[(state, action)][next_state]
                        reward = self.rewards[(state, action)][next_state]
                        Q += transition_prob * (reward + gamma * V[next_state])

                    V[state] = Q
        return V


def main():
    """
    Main function to run the model-based Monte Carlo algorithm.
    """

    debug = False

    env = DiceGame()
    model_based_mc = ModelBasedMonteCarlo(env)

    eps = 10000
    for ep in range(eps):

        if debug:
            print(f"Episode {ep}:", end=' ', flush=True)

        state = env.reset()

        episode = []
        while True:
            action = model_based_mc.policy()

            next_state, reward, terminal, _ = env.step(state, action)

            episode.append([state, action, next_state, reward])

            if terminal:
                break

            state = next_state

        model_based_mc.update_transitions_and_rewards(episode)

        if debug:
            print(episode)
            print(f"Transition : {model_based_mc.transitions}")
            print(f"Acc Rewards: {model_based_mc.rewards}\n")

    model_based_mc.update_expected_rewards()
    model_based_mc.update_transition_probabilites()
    print(f"Transition Probabilites Estimated:{model_based_mc.transitions}")
    print(f"Estimated Rewards:{model_based_mc.rewards}")

    policy_evaluation = PolicyEvaluation(env)
    print(f"True Transition Probabilites and Rewards: {policy_evaluation.mdp}")

    print("Expected rewards:")
    print(model_based_mc.policy_evaluation('stay'))
    print(policy_evaluation.update("stay", False))


if __name__ == "__main__":
    main()
