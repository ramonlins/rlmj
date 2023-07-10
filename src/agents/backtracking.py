from src.envs.python.transportation import Transportation


class Backtracking:
    """
    Backtracking algorithm applied to problems such as transportation problem
    defined here as transition problems (TP).

    TransitionProblem
        Can be a instance of the transportation problem.
        The TP should have the following properties:
            - start_state: The state from which the solution path should start.
            - end_state: The state at which the solution path should end.
            - succ_and_cost(state): A method that takes a state and returns a list of
            "transition units", where each transition unit is a tuple (action, new_state, cost)
            representing a possible action at the current state, the resulting new state, and
            the cost of the action.
    """
    def __init__(self, problem):
        self.problem = problem

    def search(self) -> tuple:
        """
        This function attempts to solve a given problem, using a backtracking algorithm. It starts from the
        start state of the TP, and recursively explores possible paths to the end state, maintaining the path
        and cost of the best solution found so far.

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

        """
        best_cost: float = float('inf')
        best_path: list = None

        def recurse(state, history: list, total_cost: int) -> None:
            # preserve outside variables
            nonlocal best_path, best_cost

            if state == self.problem.end_state:

                if total_cost < best_cost:
                    best_path = history
                    best_cost = total_cost

                return

            # can return none, one or two transition units
            transition_units = self.problem.succ_and_cost(state)

            # go through possible transitions
            for transition_unit in transition_units:
                # get each element of transition
                action, new_state, cost = transition_unit

                # recursive call
                recurse(new_state,
                        history+[(action, new_state, cost)],
                        total_cost+cost)

        # start recursion
        recurse(self.problem.start_state, history=[], total_cost=0)

        return best_path, best_cost


def main():
    import time

    env = Transportation(size=9)
    agent = Backtracking(env)

    ti = time.time()
    min_cost = agent.search()

    print(min_cost)
    print(f"Time spent: {time.time() - ti:.2}")


if __name__ == "__main__":
    main()
