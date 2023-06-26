class Backtracking:
    """
    Solve a problem by backtracking.

    """
    def _backtracking(self, TP) -> tuple:
        """
        This function attempts to solve a given problem, represented by a Transition Problem (TP),
        using a backtracking algorithm. It starts from the start state of the TP, and recursively
        explores possible paths to the end state, maintaining the path and cost of the best solution
        found so far.

        Parameters
        ----------
        TP : TransitionProblem
            An instance of the TransitionProblem class representing the problem to be solved.
            The TP should have the following properties:
                - start_state: The state from which the solution path should start.
                - end_state: The state at which the solution path should end.
                - succ_and_cost(state): A method that takes a state and returns a list of
                "transition units", where each transition unit is a tuple (action, new_state, cost)
                representing a possible action at the current state, the resulting new state, and
                the cost of the action.

        Returns
        -------
        tuple
            A tuple (best_path, best_cost), where best_path is a list of transition units representing
            the best (least cost) path found from start_state to end_state, and best_cost is the total
            cost of this path. If no path is found, best_path is an empty list and best_cost is infinity.

        Raises
        ------
        Exception
            Raises an Exception if the TP object does not have the required properties.

        Test:
        ------
            from src.envs.python.transportation import Transportation
            from src.agents.backtracking import backtracking

            env = Transportation(size=4)
            agent = Backtracking()

            agent._backtracking(env)

            outup -> ([('walk', 2, 1), ('walk', 3, 1), ('walk', 4, 1)], 3)
        """
        best_cost: float = float('inf')
        best_path: list = None

        def recurse(state, history: list, total_cost: int) -> None:
            # preserve outside variables
            nonlocal best_path, best_cost

            if state == TP.end_state:

                if total_cost < best_cost:
                    best_path = history
                    best_cost = total_cost

                return

            # can return none, one or two transition units
            transition_units = TP.succ_and_cost(state)

            # go through possible transitions
            for transition_unit in transition_units:
                # get each element of transition
                action, new_state, cost = transition_unit

                # recursive call
                recurse(new_state,
                        history+[(action, new_state, cost)],
                        total_cost+cost)

        # start recursion
        recurse(TP.start_state, history=[], total_cost=0)

        return best_path, best_cost
