import heapq
from typing import Tuple, List

from src.envs.python.transportation import Transportation


class AStarSearch:
    """Implements the Uniform Cost Search algorithm to find the shortest path in a graph.

    Args:
        problem (Transportation): The problem instance to be solved.

    Attributes:
        problem (Transportation): The problem instance to be solved.
        src (int): The start state of the problem.
        goal (int): The end state of the problem.

    """

    def __init__(self, problem: Transportation):
        self.problem = problem
        self.src = problem.start_state
        self.goal = problem.end_state

    def search(self) -> Tuple[List[int], int]:
        """Performs the A Star Search algorithm to find the shortest path.

        Returns:
            tuple: A tuple containing the cost and the shortest path sequence.
        """

        # Assume that the max cost from a given state to the end is two
        def heuristic(state, goal):
            if state == goal:
                return 0
            return 2

        # Use a min heap to guarantee minimum cost for state
        queue = [(0, self.src)]
        heapq.heapify(queue)

        # Store all the possible next states
        frontier = {self.src: 0}

        # Mark the state as already visited
        explored = [self.src]

        # Keep tracking state parent for backtracking path
        parent = {1: None}

        # Start exploring shortest path
        print("Visited states: ", end='')
        while queue:
            # Get past cost to state
            _, state = heapq.heappop(queue)

            print(f"{state}", end=' ', flush=True)

            # Backtracking states from end state
            if state == self.goal:
                paths = []
                while state is not None:
                    paths.append(state)
                    state = parent[state]

                # Reverse path
                paths = paths[::-1]

                return paths, frontier[self.goal]

            # Check cost of neighboor states
            for _, next_state, cost in self.problem.succ_and_cost(state):
                # PastCost + c(s, a)
                # NOTE: The heuristic costs in queue are not the same as real past cost in frontier
                #       this is why path_cost changes in relation to ucs algorithm.
                path_cost = frontier[state] + cost

                # Add new cost and next states to queue
                if next_state not in explored or path_cost < frontier[next_state]:
                    frontier[next_state] = path_cost

                    path_cost_future = path_cost + heuristic(next_state, self.goal)
                    #path_cost_h = path_cost + 0

                    heapq.heappush(queue, (path_cost_future, next_state))

                    parent[next_state] = state

                # Avoid duplication
                if next_state not in explored:
                    explored.append(next_state)


def main():
    env = Transportation(size=10)

    agent = AStarSearch(env)

    path, cost = agent.search()
    print()
    print(f"Path: {path}, Cost: {cost}")

    return 0


if __name__ == "__main__":
    main()
