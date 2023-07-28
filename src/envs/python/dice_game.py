import random


class DiceGame:
    # states : in, end
    # actions: stay, quit
    # rewards: 4  (state="in", action="stay")
    #          10 (state="in", action="quit")
    # dice   : [1,2] -> end; [3, 4, 5, 6] -> in
    #
    # Reference:
    #    The stanford-cs221 course lecture taken from:
    #    https://www.youtube.com/watch?v=aIsgJJYrlXk&list=PLoROMvodv4rOca_Ovz1DvdtWuz8BfSWL2&index=17

    def __init__(self):
        # mdp: mdp model
        # from action-state nodes get all possible actions from next state
        # (s, a) -> (S' in (S), T in [1, 2/3, 1/3],  R in [4, 10])
        self.mdp = {
            ("in", "stay"): {"in": (2/3, 4), "end": (1/3, 4)},
            ("in", "quit"): {"end": (1, 10)},
        }

    def step(self, state: str, policy: str) -> tuple[str, int, bool, bool]:
        """
        Perform a step in the environment.

        Args:
            state (str): The current state.
            policy (str): The chosen policy.

        Returns:
            tuple[str, int, bool, bool]: The next state, reward, terminal flag, and additional information.
        """
        # check next state
        next_state = state
        reward = 4
        terminal = False

        if state == "in" and policy == "stay":
            dice_result = random.randint(1, 6)  # roll dice
            # go to end state
            if dice_result in [1, 2]:
                next_state = "end"
                return next_state, reward, True, False

        # go to end state
        elif state == "in" and policy == "quit":
            next_state = "end"
            reward = 10

            return next_state, reward, True, False

        return next_state, reward, terminal, False

    def reset(self):
        return self.states[0]

    @property
    def states(self) -> list[str]:
        return ["in", "end"]

    @property
    def actions(self) -> list[str]:
        return ["stay", "quit"]
