def order_vertices(graph_matrix):
    num_vertices = len(graph_matrix)
    print(str(num_vertices))
    levels = []
    
    while num_vertices > 0:
        
        current_level = []
        for vertex in range(num_vertices):
            has_incoming_arc = any(graph_matrix[i][vertex] == 1 for i in range(num_vertices))
            if not has_incoming_arc:
                current_level.append(vertex)
            
        print(current_level)
        for vertex in current_level:
            graph_matrix = [row[:vertex] + row[vertex + 1:] for row in graph_matrix]
        
        levels.append(current_level)
        num_vertices -= len(current_level)
        # print(num_vertices)
    
    return levels

# Example usage


graph_matrix = [
    [0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0,0,1,0,0],
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
a = len(graph_matrix)

ordered_levels = order_vertices(graph_matrix)
print("Ordered levels of vertices:")
# for level, vertices in enumerate(ordered_levels):
    # print(ordered_levels)