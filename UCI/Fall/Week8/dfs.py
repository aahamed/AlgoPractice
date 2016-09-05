__author__ = 'aahamed'


class DFS(object):
    def __init__(self, graph, source):
        self.visited = [False for _ in range(len(graph))]
        self.parent = [None for _ in range(len(graph))]
        self.visited[source] = True
        self.dfs(graph, source)

    def dfs(self, graph, source):
        for neighbor in graph[source]:
            if not self.visited[neighbor]:
                self.visited[neighbor] = True
                self.parent[neighbor] = source
                self.dfs(graph, neighbor)

    def has_path_to(self, v):
        return self.visited[v]

    def path_to(self, v):
        res = [v]
        parent = self.parent[v]
        while parent is not None:
            res.append(parent)
            parent = self.parent[parent]
        return res