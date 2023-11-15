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
            if matrix[i][j] != 0 :
                outgoing[i].append(j)

                # print("on " + str(i) + "node, there is an outgoing to " + str(j) + "node")
                startVertex = i

    # print("=========================================\n")
    # print(outgoing)
    
    # startVertex = 3
    step.append(outgoing[startVertex])
    currentstep = 0
    c = 0
  
    laststep = -1    
    while notfoundPeriod: # running in step
        onestep = []
   
        # print("step -1 = " + str(step[-1]))
        # print("laststep= " + str(step[laststep][0]))
        
        for j in range(len(step[laststep])):
            # for i in range(len(step[j])):
                # print("outgoing[step[--]] = "+ str(step[j[i]]) + " - " + str(outgoing[i]))
            

            # print(str(j) + " go to " +  str(outgoing[j]))
            onestep.extend(outgoing[step[laststep][j]])
            
        # print(onestep)
        onestep = remove_duplicates(onestep)
        # print(onestep)
        step.append(onestep)
        # print(step)

        c =c + 1 


        for i in range(len(step)):
            if(has_duplicates(step)):
                notfoundPeriod = False
                # print(step)
            
            

            
    # print("\n\nNext step: " + str(step))    
    for i in range(len(step)):
        if step[i] == step[-1]:
            tmp = step[i:]
            break
        
    step = tmp[:-1]
    period = len(step) 

    return step, period
    # print(step)
    # print(str(startVertex) + ':' + str(step))

def has_duplicate(list_of_lists):
    seen_elements = set()

    for sublist in list_of_lists:
        for element in sublist:
            if element in seen_elements:
                return True
            seen_elements.add(element)
    return False

def checkIfPeriodic(matrix):
    cluster, period = PeriodicGraphMatricielle(matrix)
    new = [item for sublist in cluster for item in sublist]
    new = remove_duplicates(new)
    
    # print(len(new))
    if len(new) == len(matrix) and not has_duplicate(cluster):
        return True
    return False

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
    [1,0,0,0,0,0,0,0]
    	        # [0,0,0,0,1,0,0,1,0,0,0,1],
                # [0,0,1,1,0,0,1,0,0,0,0,0],
                # [0,0,0,0,0,1,0,0,0,0,0,0],
                #  [0,1,0,1,0,0,0,0,0,0,0,0],
                #  [0,0,0,0,0,0,0,1,0,0,0,0],
                #  [0,0,1,0,0,0,0,0,0,0,1,0],
                #  [1,0,0,0,0,0,0,0,1,0,0,0],
                #  [0,0,0,0,0,0,0,1,0,1,0,0],
                #  [0,1,0,0,0,0,1,0,0,0,0,0],
                #  [0,0,0,0,0,0,0,1,0,0,0,1],
                #  [0,0,0,0,0,0,0,0,0,0,1,0],
                #  [1,0,0,0,0,0,0,0,0,0,0,0]



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




]
sz = len(graph_matrix)

cluster, period = PeriodicGraphMatricielle(graph_matrix)

print("\nEst-ce que c'est un graphe périodique? : " + str(checkIfPeriodic(graph_matrix)))
if checkIfPeriodic(graph_matrix):
    print("\n=> Ici c'est la période de ce graphe:")
    print(str(cluster) + " = " + str(period) + "\n")
else:
    print("\n=> C'est un graphe apériodique")
