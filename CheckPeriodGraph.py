def PeriodicGraphMatricielle(matrix):
    num_nodes = len(matrix)
    # for i in range(num_nodes):
    #     print(i)
    outgoing = [[] for _ in range(num_nodes)]
    
    step = []
    notfoundPeriod = True
    for i in range(num_nodes):
        for j in range(num_nodes):
            if graph_matrix[i][j] != 0 :
                outgoing[i].append(j)

                print("on " + str(i) + "node, there is an outgoing to " + str(j) + "node")
                startVertex = i

    print("=========================================\n")
    print(outgoing)
    
    startVertex = 3
    step.append(outgoing[startVertex])
    i = 0
    c = 0
    while notfoundPeriod :
        print("outgoing[startVertex] = " + str(outgoing[startVertex]))
        for j in range(len(step[i])):
            print("step[i] = " + str(len(step[i])))
            print("j = " + str(j) + "outgoing bos j =" + str(outgoing[j]))
            step.append(outgoing[j])
        
        i = i + 1

        c = c + 1
        if(c == 10):
            notfoundPeriod = False
        
            
    print("\n\nNext step: " + str(step))    
    # print(step)
    # print(str(startVertex) + ':' + str(step))


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
    [0,0,0,0,1,0],
    [0,0,0,0,0,1],
    [0,1,0,0,0,0],
    [1,0,1,0,0,0],
    [0,0,0,1,0,1],
    [1,0,0,0,0,0]
]
sz = len(graph_matrix)

ordered_levels = PeriodicGraphMatricielle(graph_matrix)
print("Ordered levels of vertices:")
print(ordered_levels)
# for level, vertices in enumerate(ordered_levels):
    # print(ordered_levels)