"""
The transportation problem:
    Street with blocks numbered 1 to n.
    Walking from s to s+1 takes 1 minute.
    Taking a magic tram from s to 2s take 2 minutes.
    How to travel from 1 to n in the least time

Reference:
    The stanford-cs221 course lecture taken from:
    https://www.youtube.com/watch?v=aIsgJJYrlXk&list=PLoROMvodv4rOca_Ovz1DvdtWuz8BfSWL2&index=17
"""


class Transportation:
    def __init__(self,
                 render_mode=None,
                 start_state=1,
                 size=9):
        self.state = start_state
        self.end_state = size
        self.terminated = False

        # initialize states
        self.states = [i for i in range(size)]
        # possible actions
        self.actions = ['walk', 'tram']

    def _get_obs(self):
        pass

    def _get_info(self):
        pass

    def _render_frame(self):
        pass

    def reset(self, seed=None, options=None):
        pass

    # tree-search algorithms
    def succ_and_cost(self, state: int) -> list:
        # From s -> walk -> s' (s+1), c(s,walk)=1
        #        -> tram -> s' (s*2), c(s,tram)=2
        # From any state the transition unit is always created
        transition_unit = []

        # to avoid transitions out of bound
        if state + 1 <= self.end_state:
            transition_unit.append(("walk", state + 1, 1))
        if state * 2 <= self.end_state:
            transition_unit.append(("tram", state * 2, 2))

        return transition_unit

    # mdp-based algorithms
    def step(self, action):
        next_state = None
        cost = None

        if (self.state + 1 <= self.end_state) and (action == self.actions[0]):
            next_state, cost = self.state + 1, 1

        if (self.state * 2 <= self.end_state) and (action == self.actions[1]):
            next_state, cost = self.state * 2, 2

        if next_state == self.end_state:
            self.terminated = True

        return next_state, cost, self.terminated, False, None

    def render(self):
        pass

    def close(self):
        pass
