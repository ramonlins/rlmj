from src.envs.python.transportation import Transportation


class DynamicProgramming:
    """Dynamic Programming

        Traverse forward until find end state.
        Get minimum future cost over transitions (action, next_state, cost):
            iterate over transitions
                Compute future cost backwards until find a transition
        Repeat steps until find minimum cost

    """

    def __init__(self, problem):
        # init cache to store future state cost
        self.cache = {}
        self.problem = problem
        self.is_debug = False

    # traverse states until find end state
    def search(self, state):
        # Work as non-local variable inside recurse function
        cache = {}

        def _future_cost(state):
            # Base case
            if state == self.problem.end_state:
                return 0

            # Since the minimum cost over states are the same:
            #   c(s=2,a='T') = 2
            #   c(s=2,a='w') = 2
            # The values can be store in memory, avoiding unnecessary
            if state in cache:
                return cache[state]

            # Compute future cost:
            transition_units = self.problem.succ_and_cost(state)

            # Traverse until find end state.
            # Compute future cost backwards:
            #   future_cost(s) = min_a {cost(s, a) + future_cost(s')}
            #                  = 0 if current state is a end state
            # until find next transition.
            # After iterate over transitions, get minimum cost
            # Repeat steps until find minimum cost
            future_cost = min(cost + _future_cost(next_state)
                              for _, next_state, cost in transition_units)

            # Store in
            cache[state] = future_cost

            if self.is_debug:
                print(future_cost)

            return future_cost

        return _future_cost(state)


def main():
    import time

    env = Transportation(size=100)
    agent = DynamicProgramming(env)

    ti = time.time()
    min_cost = agent.search(env.start_state)

    print(min_cost)
    print(f"Time spent: {time.time() - ti:.2}")


if __name__ == "__main__":
    main()
