import heapq
from typing import Tuple, List

from src.envs.python.transportation import Transportation


class UniformCostSearch:
    """Implements the Uniform Cost Search algorithm to find the shortest path in a graph.

    Args:
        problem (Transportation): The problem instance to be solved.

    Attributes:
        problem (Transportation): The problem instance to be solved.
        src (int): The start state of the problem.
        dst (int): The end state of the problem.

    """

    def __init__(self, problem: Transportation):
        self.problem = problem
        self.src = problem.start_state
        self.dst = problem.end_state

    def search(self) -> Tuple[List[int], int]:
        """Performs the Uniform Cost Search algorithm to find the shortest path.

        Returns:
            tuple: A tuple containing the shortest path and its cost.

        """
        # Use a min heap to guarantee minimum cost to s
        queue = [(0, self.src)]

        # Store possible next states
        frontier = {self.src: 0}

        # Mark state as already visited
        explored = [self.src]

        # Keep tracking state parent
        parent = {1: None}

        # Start exploring shortest path
        print("Visited states: ", end='')
        while queue:
            # Get past cost to state
            past_cost, state = heapq.heappop(queue)
            print(f"{state}", end=' ', flush=True)

            # Backtracking states from end state
            if state == self.dst:
                paths = []
                while state is not None:
                    paths.append(state)
                    state = parent[state]

                # Reverse path
                paths = paths[::-1]

                return paths, frontier[self.dst]

            # Check cost of neighboor states
            for _, next_state, cost in self.problem.succ_and_cost(state):
                # PastCost + current cost
                new_cost = past_cost + cost

                # Add new cost and next states to queue
                if next_state not in explored or new_cost < frontier[next_state]:
                    frontier[next_state] = new_cost
                    heapq.heappush(queue, (new_cost, next_state))
                    parent[next_state] = state

                # Avoid duplication
                if next_state not in explored:
                    explored.append(next_state)


def main():
    env = Transportation(size=20)

    agent = UniformCostSearch(env)

    path, cost = agent.search()
    print()
    print(f"Path: {path}, Cost: {cost}")

    return 0


if __name__ == "__main__":
    main()
