"""
This code is a implementation of the policy evaluation algorithm based on stanford-cs221 course.

The lecture was taken from:
https://www.youtube.com/watch?v=9g32v7bK3Co&list=PLoROMvodv4rOca_Ovz1DvdtWuz8BfSWL2&index=20&t=140s

The enviroment was defined in /src/envs/python/dice_game.py

To test run:
    from src.envs.python.dice_game import DiceGame
    from src.agents.policy_evaluation import PolicyEvaluation

    mdp = DiceGame()
    pol_eva = PolicyEvaluation(mdp)

    print(pol_eva.update("stay"))
"""


class PolicyEvaluation:
    def __init__(self, mdp):
        self.t_hash = mdp.t_hash
        self.states = mdp.states
        self.end_state = self.states[1]

        # initialize value of policy
        self.V = {}
        for s in self.states:
            self.V[s] = 0

    def update(self, policy: str, is_debug: bool = True) -> dict:
        """
        Update rule:
            if s is end_state:
                Vpi(s) = 0
            else:
                Vpi(s) = Qpi(s,a) = SUM_s' T(s, a, s') * [R(s, a, s') + gamma * Vpi(s)]
        """
        # design parameters
        gamma = 0.999

        # iterate until converge
        is_iterate = True
        while is_iterate:

            if is_debug:
                print(f"State Function: \n V{self.V} \n")

            # go throught all states
            for s in self.states:
                # avoid undefined state-action in mdp
                if s != self.end_state:
                    all_next_states = self.t_hash[s, policy].keys()

                    Qf = 0
                    for next_s in all_next_states:
                        p_t, r = self.t_hash[s, policy][next_s]
                        Qf += p_t * (r + gamma * self.V[next_s])

                    # current V(in) - previous V(in)
                    e = Qf - self.V[s]

                    if e < 1e-5:
                        is_iterate = False

                    self.V[s] = Qf

        return self.V
