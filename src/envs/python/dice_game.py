import random


class DiceGame:
    # states : in, end
    # actions: stay, quit
    # rewards: 4  (state="in", action="stay")
    #          10 (state="in", action="quit")
    # dice   : [1,2] -> end; [3, 4, 5, 6] -> in
    def __init__(self):
        # t_hash: mdp model
        # from action-state nodes get all possible actions from next state
        # (s, a) -> (S' in (S), T in [1, 2/3, 1/3],  R in [4, 10])
        self.t_hash = {
            ("in", "stay"): {"in": (2/3, 4), "end": (1/3, 4)},
            ("in", "quit"): {"end": (1, 10)},
        }

    def step(self, state: str, policy: str) -> str:
        # check next state
        next_state = state
        reward = 4
        terminal = False

        if state == "in" and policy == "stay":
            dice_result = random.randint(1, 6)  # roll dice
            # go to end state
            if dice_result in [1, 2]:
                next_state = "end"
        # go to end state
        elif state == "in" and policy == "quit":
            next_state = "end"
            reward = 10

        if next_state == "end":
            terminal = True

        return next_state, reward, terminal, False

    def reset(self):
        return self.states[0]

    @property
    def states(self) -> list[str]:
        return ["in", "end"]

    @property
    def actions(self) -> list[str]:
        return ["stay", "quit"]
