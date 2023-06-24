class Transportation:
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
    def __init__(self, start_state=1, size=9):
        self.start_state = start_state
        self.end_state = size
        self.terminated = False

    # tree-search algorithms
    def succ_and_cost(self, state: int) -> list:
        """
        Compute the possible transitions from a given state.

        This method takes a state (represented as an integer) and computes the possible transitions
        to new states, along with the cost of each transition. There are two possible actions from
        any state: "walk" to the next state (state+1) with a cost of 1, and "tram" to the doubled
        state (state*2) with a cost of 2.

        Parameters
        ----------
        state : int
            The current state, represented as an integer.

        Returns
        -------
        list
            A list of transition units, where each transition unit is a tuple (action, next_state, cost)
            representing a possible action from the current state, the resulting new state, and the cost
            of the action. The list will be empty if there are no valid transitions from the current state
            (i.e., if the current state is the end state).
        -------
        # Example:
        #   s -> walk -> s' (s+1), c(s,a=walk)=1
        #     -> tram -> s' (s*2), c(s,a=tram)=2
        # any state the transition unit is always (action, next_state, cost)
        """
        transition_unit = []

        # to avoid transitions out of bound
        if state + 1 <= self.end_state:
            transition_unit.append(("walk", state + 1, 1))

        if state * 2 <= self.end_state:
            transition_unit.append(("tram", state * 2, 2))

        return transition_unit
