# def order_graph(adj_matrix):
#     def dfs(node):
#         visited[node] = True
#         for neighbor in range(num_nodes):
#             if adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
#                 dfs(neighbor)
#         ordered_nodes.append(node)

#     num_nodes = len(adj_matrix)
#     visited = [False] * num_nodes
#     ordered_nodes = []

#     for node in range(num_nodes):
#         if not visited[node]:
#             dfs(node)
#     print(ordered_nodes[::-1])
#     return ordered_nodes[::-1]  

# Example usage
from collections import deque

def order_graph_by_level(adj_matrix):
    # print(adj_matrix)
    num_nodes = len(adj_matrix)
    indegrees = [0] * num_nodes 
    # print("indegree" + str(indegrees))
    levels = []  
    graph = {} 


    for i in range(num_nodes):
        graph[i] = []
        for j in range(num_nodes):
            if adj_matrix[i][j] == 1:
                graph[i].append(j)
                indegrees[j] += 1
    print(graph)
    # print("indegree" + str(indegrees))


    queue = deque()
    for i in range(num_nodes):
        if indegrees[i] == 0:
            queue.append((i, 0))
    # print(queue)
    # print("queue: " + str(queue))
    while queue:
        node, level = queue.popleft()
        # print("node = "+str(node) + " goes6 to level = " + str(level))
       
        if level == len(levels):
            levels.append([node])
        else:
            levels[level].append(node)

        for neighbor in graph[node]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append((neighbor, level + 1))
        # print(levels)
  
    return levels

graph_matrix = [
    # [0,0,0,0,0,0,0,1,0,0,0],
    # [0,0,0,1,0,0,0,0,0,0,1],
    # [0,0,0,0,0,0,0,0,1,0,0],
    # [0,0,0,0,0,1,0,0,0,0,0],
    # [0,0,1,0,0,0,0,1,0,0,0],
    # [0,0,0,0,0,0,0,0,0,0,0],
    # [1,1,0,1,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,1,0,1],
    # [0,0,0,0,0,0,0,0,0,1,0],
    # [0,0,0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,1,0,0,0,1,0]
    # [0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],
    # [1,1,1,0,0,0,0,1,0,0,0,0,0,0,0],
    # [1,0,0,1,0,0,1,0,0,0,0,0,0,0,0],
    # [0,0,1,0,1,1,0,0,0,0,0,0,0,0,0],
    # [0,0,1,0,1,0,0,0,0,0,0,0,0,1,1],
    # [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
    # [0,0,0,0,0,1,0,0,0,0,0,1,0,0,0],
    # [0,0,0,0,0,0,1,0,0,1,1,0,0,0,0],
    # [0,0,0,0,0,0,0,1,0,1,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],
    # [0,0,0,0,0,0,1,0,0,0,1,0,0,0,0],
    # [0,0,0,0,0,1,1,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
    # [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]

    [0,0,0,1,0,0,0,0,0],
    [0,0,0,0,1,1,0,0,0],
    [0,0,0,0,0,1,0,0,0],
    [0,1,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,1,1,0],
    [0,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]
# print(graph_matrix)
sz = len(graph_matrix)

ordered_levels = order_graph_by_level(graph_matrix)
print("Il y a " + str(len(ordered_levels)) + " niveaux : ")
print(ordered_levels)
