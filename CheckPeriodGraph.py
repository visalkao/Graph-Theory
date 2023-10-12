def PeriodicGraphMatricielle(matrix):
    num_nodes = len(matrix)
    # for i in range(num_nodes):
    #     print(i)
    for i in range(num_nodes):
        print(i)    
    


graph_matrix = [
    [0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,1,0,0,0,0,0],
    [0,0,1,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [1,1,0,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0,1],
    [0,0,0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,1,0]
]
sz = len(graph_matrix)

ordered_levels = PeriodicGraphMatricielle(graph_matrix)
print("Ordered levels of vertices:")
print(ordered_levels)
# for level, vertices in enumerate(ordered_levels):
    # print(ordered_levels)