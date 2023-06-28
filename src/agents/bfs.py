from collections import deque


def bfs(adj_list):
    # root node
    root_node = 'A'

    # init
    queue = deque()
    queue.append(root_node)
    visited = []
    paths = {}

    # Extend elements instead of strings
    paths[root_node] = [root_node]
    while queue:
        node = queue.popleft()

        # Avoid visited nodes
        if node not in visited:
            childs = adj_list[node]
            visited.append(node)

            # Put child node into queue
            for child in childs:
                queue.append(child)
                paths[child] = paths[node] + [child]

    return paths


def main():
    adj_lst = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': [],
        'E': [],
        'F': [],
        'G': []
    }

    print(bfs(adj_lst))


if __name__ == "__main__":
    main()
