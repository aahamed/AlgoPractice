"""
Author: Aadil Ahamed
dijkstras.py: Implementation of dijkstra's algorithm
"""

import Queue


def dijkstras(graph, source):
    count = 0
    dist_from_src = []
    pq = Queue.PriorityQueue()
    for node in graph:
        dist_from_src.append(None)
    dist_from_src[source] = 0
    pq.put((0, source))
    while not pq.empty():
        count += 1
        min_tuple = pq.get()
        node = min_tuple[1]
        distance = min_tuple[0]
        dist_from_src[node] = distance
        for neighbor in graph[node]:
            if dist_from_src[neighbor[0]] is None:
                pq.put((distance + neighbor[1], neighbor[0]))

    return dist_from_src
