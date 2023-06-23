class Transportation:
    def __init__(self, size=9):
        self.start_state = 1
        self.end_state = size
        self.terminated = False

    # tree-search algorithms
    def succ_and_cost(self, state: int) -> list:
        # From s -> walk -> s' (s+1), c(s,walk)=1
        #        -> tram -> s' (s*2), c(s,tram)=2
        # From any state the transition unit is always (action, next_state, cost)
        transition_unit = []

        # to avoid transitions out of bound
        if state + 1 <= self.end_state:
            transition_unit.append(("walk", state + 1, 1))

        if state * 2 <= self.end_state:
            transition_unit.append(("tram", state * 2, 2))

        return transition_unit


def backtracking(TP):
    # TODO: Keep traking of path, choose best one based on minimum total cost;
    def recurse(state):
        if state == TP.end_state:
            return

        # can return none, one or two transition units
        transition_units = TP.succ_and_cost(state)

        for transition_unit in transition_units:
            print(transition_unit)
            action, new_state, cost = transition_unit

            # recursive call
            recurse(new_state)

    recurse(TP.start_state)

    return 1


def main():
    result = backtracking(Transportation(size=4))
    print(result)


if __name__ == "__main__":
    main()
