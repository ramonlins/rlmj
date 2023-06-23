"""
This code is a implementation of the value iteration algorithm based on stanford-cs221 course.

The lecture was taken from:
https://www.youtube.com/watch?v=9g32v7bK3Co&list=PLoROMvodv4rOca_Ovz1DvdtWuz8BfSWL2&index=20&t=140s

The enviroment was defined in /src/envs/python/dice_game.py

To test run:
    from src.envs.python.dice_game import DiceGame
    from src.agents.value_iteration import ValueIteration

    mdp = DiceGame()
    val_ite = ValueIteration(mdp)

    print(val_ite.update())
"""


class ValueIteration:
    def __init__(self, mdp):
        self.states = mdp.states
        self.actions = mdp.actions
        self.t_hash = mdp.t_hash
        self.end_state = self.states[1]

        # initialize value of policy
        self.V = {}
        for s in self.states:
            self.V[s] = 0

        # initialize value of policy
        self.Q = {}
        for s in ['in', 'end']:
            self.Q[s] = {}
            if s == 'in':
                for a in ['stay', 'quit']:
                    self.Q[s][a] = 0
            else:
                self.Q[s] = 0

    def _policy(self, s: str) -> str:
        Qs = self.Q[s]

        # NOTE: since state-acation values are zero in the beggining
        #       it will always starting with action 'stay'.
        a = max(Qs, key=Qs.get)

        return a

    def update(self, is_debug: bool = False) -> dict:
        """
        Update rule:
            if s is end_state:
                Vpi(s) = 0
            else:
                Vpi(s) = Qpi(s,a) = max_a SUM_s' T(s, a, s') * [R(s, a, s') + gamma * Vpi(s)]
        """
        # design parameters
        gamma = 0.999

        # iterate until converge
        is_iterate = True
        while is_iterate:

            if is_debug:
                print(f"State-Action Function: \n Q{self.Q}")
                print(f"State Function: \n V{self.V} \n")

            # go throught all states
            for s in self.states:
                # avoid undefined state-action in mdp
                if s != self.end_state:
                    # get action that maximize action-state value
                    a = self._policy(s)

                    all_next_states = self.t_hash[s, a].keys()

                    Qf = 0
                    for next_s in all_next_states:
                        p_t, r = self.t_hash[s, a][next_s]
                        Qf += p_t * (r + gamma * self.V[next_s])

                    self.Q[s][a] = Qf

                    # current V(in) - previous V(in)
                    e = Qf - self.V[s]

                    if e < 1e-5:
                        is_iterate = False

                    self.V[s] = Qf

        return self.V
