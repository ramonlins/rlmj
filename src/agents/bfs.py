from collections import deque


class BFS:
    def __init__(self):
        self.adj_list = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F', 'G'],
            'D': [],
            'E': [],
            'F': [],
            'G': []
        }

    def search(self):
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
                childs = self.adj_list[node]
                visited.append(node)

                # Put child node into queue
                for child in childs:
                    queue.append(child)
                    # Extend child to path
                    paths[child] = paths[node] + [child]

        return paths


def main():
    agent = BFS()

    print(agent.search())

if __name__ == "__main__":
    main()
