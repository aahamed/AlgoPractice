from collections import deque


class BFS(object):
    def __init__(self, graph, source):
        self.visited = []
        self.next_visit = deque()
        self.parent = []
        self.dist_to = []
        self.source = source
        self.bfs(graph, source)

    def bfs(self, graph, source):
        for i in range(len(graph)):
            self.visited.append(False)
            self.parent.append(None)
            self.dist_to.append(None)
        self.next_visit.append(source)
        self.visited[source] = True
        self.dist_to[source] = 0
        while len(self.next_visit) > 0:
            curr_node = self.next_visit.popleft()
            for neighbor in graph[curr_node]:
                if not(self.visited[neighbor]):
                    self.next_visit.append(neighbor)
                    self.visited[neighbor] = True
                    self.parent[neighbor] = curr_node
                    self.dist_to[neighbor] = self.dist_to[curr_node] + 1

    def has_path_to(self, v):
        return self.visited[v]

    def path_to(self, v):
        if not(self.visited[v]):
            return None
        res = [v]
        t = v
        while self.parent[t] is not None:
            res.append(self.parent[t])
            t = self.parent[t]
        return res

    def distance_to(self, v):
        return self.dist_to[v]