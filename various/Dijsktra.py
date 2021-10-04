def is_int(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def matrix(dim, element):
    matrix = [[element for column in range(dim)] for row in range(dim)]
    return matrix

def min_distance(dist, visited, dim):
    min = 99999999
    min_index = -1
    for v in range(dim):
        if dist[v] < min and visited[v] is False:
            min = dist[v]
            min_index = v
    return min_index

def dijkstra(start, dim, matrix, nodes):
    dist = [99999999] * dim
    visited = [False] * dim
    path = [''] * dim
    dist[start] = 0
    for i in range(dim):
        u = min_distance(dist, visited, dim)
        visited[u] = True
        for v in range(dim):
            if matrix[u][v] > 0 and visited[v] is False and dist[v] > dist[u] + matrix[u][v]:
                dist[v] = dist[u] + matrix[u][v]
                if path[v] == '':
                    if len(path[u]) < 4:
                        path[v] += path[u] + nodes[u] + "->" + nodes[v]
                    else:
                        path[v] += path[u] + "->" + nodes[v]
                else:
                    if len(path[u]) < 4:
                        path[v] += path[u] + nodes[u] + "->" + nodes[v]
                    else:
                        path[v] = ''
                        path[v] += path[u] + "->" + nodes[v]
    return dist, path

yesno = input("\nWant to make your own graph? [y/n] (enter n to use the default-homework): ")

if yesno == 'n':
    v = 8
    nodes = ['H', 'A', 'B', 'C', 'D', 'E', 'F', 'S']
    homework_matrix = [[0, 3, 2, 5, 0, 0, 0, 0],
                      [3, 0, 0, 0, 3, 0, 0, 0],
                      [2, 0, 0, 0, 1, 6, 0, 0],
                      [5, 0, 0, 0, 0, 2, 0, 0],
                      [0, 3, 1, 0, 0, 0, 4, 0],
                      [0, 0, 6, 2, 0, 0, 1, 4],
                      [0, 0, 0, 0, 4, 1, 0, 2],
                      [0, 0, 0, 0, 0, 4, 2, 0]]

    distances_list, path = dijkstra(0, v, homework_matrix, nodes)
    print("\nShortest path from Home to School is: ", distances_list[7])
    print("Path: ", path[7])

if yesno == 'y':
    nodes = []
    while True:
        v = input("How many nodes: ")
        if is_int(v):
            v = int(v)
            break
    for node in range(v):
        node_name = input("Name of node "+str(node+1)+": ")
        nodes.append(node_name)
    print("Your set of nodes: ")
    for node in nodes:
        print(node)
    default_matrix = matrix(v, -1)
    distances_matrix = matrix(v, 0)
    path_matrix = matrix(v, '')
    for node in nodes:
        for neigh in nodes:
            if default_matrix[nodes.index(neigh)][nodes.index(node)] != -1:
                default_matrix[nodes.index(node)][nodes.index(neigh)] = default_matrix[nodes.index(neigh)][nodes.index(node)]
            else:
                if node != neigh:
                    while True:
                        d = input("Distance from \""+node+"\" to \""+neigh+"\" (if its not his neighbour enter 0): ")
                        if is_int(d):
                            d = int(d)
                            break
                    default_matrix[nodes.index(node)][nodes.index(neigh)] = d
                if node == neigh:
                    default_matrix[nodes.index(node)][nodes.index(neigh)] = 0
    for i in range(v):
        distances_matrix[i], path_matrix[i] = dijkstra(i, v, default_matrix, nodes)
    while True:
        while True:
            startt = input("Starting node: ")
            if startt in nodes:
                break
        while True:
            end = input("End node: ")
            if end in nodes:
                break
        print("\nShortest path from "+startt+" to "+end+" is: ", distances_matrix[nodes.index(startt)][nodes.index(end)])
        print("It goes: ", path_matrix[nodes.index(startt)][nodes.index(end)])
        close = input("\nType 'x' to close or any other key to repeat getting start-end node distance: ")
        if close == 'x':
            break
