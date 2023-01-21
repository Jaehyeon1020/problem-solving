def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n-1):
        now = get_smallest_node()
        visite[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]

            fi cost < distance[j[0]]:
            distance[j[0]] = cost
