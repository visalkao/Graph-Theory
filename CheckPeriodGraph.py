def has_duplicates(lst):
    seen = set()
    for item in lst:
        # Convert the list to a tuple, which is hashable
        item_tuple = tuple(item)
        if item_tuple in seen:
            return True
        seen.add(item_tuple)
    return False

def remove_duplicates(lst):
    seen = set()
    result = []

    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)

    return result

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
    currentstep = 0
    c = 0
    # while notfoundPeriod :
    #     print("outgoing[startVertex] = " + str(outgoing[startVertex]))
    #     for j in range(len(step[i])):
    #         print("step[i] = " + str(len(step[i])))
    #         print("j = " + str(j) + "outgoing bos j =" + str(outgoing[j]))
    #         step.append(outgoing[j])
        
    #     i = i + 1

    #     c = c + 1
    #     if(c == 10):
    #         notfoundPeriod = False
        # this is comment code     
    laststep = -1    
    while notfoundPeriod and c < 5: # running in step
        onestep = []
   
        print("step -1 = " + str(step[-1]))
        print("laststep= " + str(step[laststep][0]))
        
        for j in range(len(step[laststep])):
            # for i in range(len(step[j])):
                # print("outgoing[step[--]] = "+ str(step[j[i]]) + " - " + str(outgoing[i]))
            

            # print(str(j) + " go to " +  str(outgoing[j]))
            onestep.extend(outgoing[step[laststep][j]])
        onestep = remove_duplicates(onestep)
        print(onestep)
        step.append(onestep)
        print(step)

        c =c + 1 
        # comment end here
    # seen = set(tuple(move) for move in outgoing)  # Keep track of seen moves to check for duplicates
    # c = 0
    # while notfoundPeriod and c < 5:  # running in step
    #     onestep = []

    #     print("step -1 =", step[-1])

    #     for j in range(len(step[-1])):
    #         for i in range(len(step[step[-1][j] - 1])):
    #             print("outgoing[step[--]] =", step[step[-1][j] - 1][i], "-", outgoing[i])

    #         print(str(j) + " go to " + str(outgoing[j]))
    #         onestep.append(outgoing[j])

    #     c += 1

        for i in range(len(step)):
            if(has_duplicates(step)):
                notfoundPeriod = False
                print(step)
            
            

            
    print("\n\nNext step: " + str(step))    
    period = len(step) -1

    return step, period
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
    # [0,0,0,0,1,0],
    # [0,0,0,0,0,1],
    # [0,1,0,0,0,0],
    # [1,0,1,0,0,0],
    # [0,0,0,1,0,1],
    # [1,0,0,0,0,0]
    [0,1,0,1,0,0,0,0],
    [0,0,1,0,0,0,0,0],
    [0,0,0,0,1,1,0,0],
    [0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,1,0],
    [1,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0],
]
sz = len(graph_matrix)

cluster, period = PeriodicGraphMatricielle(graph_matrix)
print("Ordered levels of vertices:")
print(str(cluster) + " = " + str(period))
# for level, vertices in enumerate(ordered_levels):
    # print(ordered_levels)