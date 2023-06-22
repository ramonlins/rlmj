"""
This code is a implementation of the policy evaluation algorithm based on stanford-cs221 course.

The enviroment was defined in /src/envs/python/dice_game.py

The lecture was taken from:
https://www.youtube.com/watch?v=9g32v7bK3Co&list=PLoROMvodv4rOca_Ovz1DvdtWuz8BfSWL2&index=20&t=140s
"""
class PolicyEvaluation:
    def __init__(self, mdp):
        self.t_hash = mdp.t_hash
        self.states = mdp.states
        self.end_state = self.states[1]

        # initialize value of policy
        self.V = {}
        for state in self.states:
            self.V[state] = 0

    def update(self, policy: str, max_it: int = 100) -> dict:
        """
        Update rule:
            if s is end_state:
                Vpi(s) = 0
            else:
                Vpi(s) = Qpi(s,a) = SUM_s' T(s, a, s') * [R(s, a, s') + gamma * Vpi(s)]
        """
        # design parameters
        gamma = 1

        # TODO: Iterate until converge
        for _ in range(max_it):
            # go throught all states
            for s in self.states:
                # avoid undefined state-action in mdp
                if s != self.end_state:
                    all_next_states = self.t_hash[s, policy].keys()

                    Vf = 0
                    for next_s in all_next_states:
                        p_t, r = self.t_hash[s, policy][next_s]
                        Vf += p_t * (r + gamma * self.V[next_s])

                    self.V[s] = Vf

        return self.V
