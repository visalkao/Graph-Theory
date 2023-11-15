# check periode of graph
import numpy as np


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
            # print(matrix)
            # print("ma i = " + str(matrix[i]))
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
    while notfoundPeriod: # running in step
        onestep = []
   
        # print("step -1 = " + str(step[-1]))
        # print("laststep= " + str(step[laststep][0]))
        
        for j in range(len(step[laststep])):
            # for i in range(len(step[j])):
                # print("outgoing[step[--]] = "+ str(step[j[i]]) + " - " + str(outgoing[i]))
            

            # print(str(j) + " go to " +  str(outgoing[j]))
            onestep.extend(outgoing[step[laststep][j]])
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





# Reorder graph

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
    # print(graph)

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
  
    return levels









#Roann's code
############################################################################
# supprimer les boucles


def supprimerboucle(G):
    g=len(G)
    for i in range(g):
        if G[i][i]==1:
            G[i][i]=0
    return G

def pastransitoire(L,M): 
    return (np.sum(L)==0 or np.sum(M)==0)

def circuitgraphe(G):
    g=len(G)
    for i in range(g):
        if pastransitoire(G[i,:], G[:,i]):
            for k in range(g):
                G[i][k],G[k][i]=0,0
                
    return G


def pipeline(G):
    M=supprimerboucle(G)
    return circuitgraphe(M)
#Recherhce de tous les circuits possibles

def findCircuits(adjacency_matrix):
    n = len(adjacency_matrix)
    circuits = []

    def explore(v, path):
        if v in path:
            start = path.index(v)
            circuit = path[start:]
            if len(circuit) > 2:  # Ignore self-loops
                circuits.append(circuit)
            return

        for u in range(n):
            if adjacency_matrix[v][u] == 1:
                explore(u, path + [v])

    for i in range(n):
        explore(i, [])

    return circuits
#Algo de Malgrange 
def presencecircuit(matrice):
    return len(findCircuits(matrice)) >0


def malgrange(matrice):
    m = len(matrice)
    CFC = []
    G = np.transpose(matrice)  # Transposer la matrice pour inverser les arêtes

    def dfs(u, visited, stack):
        visited[u] = True
        for v in range(m):
            if not visited[v] and G[u][v] == 1:
                dfs(v, visited, stack)
        stack.append(u)

    def dfs_reverse(u, visited, component):
        visited[u] = True
        component.append(u)
        for v in range(m):
            if not visited[v] and matrice[u][v] == 1:
                dfs_reverse(v, visited, component)

    visited = [False] * m
    stack = []
    for u in range(m):
        if not visited[u]:
            dfs(u, visited, stack)

    visited = [False] * m
    while stack:
        u = stack.pop()
        if not visited[u]:
            component = []
            dfs_reverse(u, visited, component)
            CFC.append(component)

    return CFC

def isFC(matrice):
    if(len(malgrange(matrice))==len(matrice)):
        return True
    return False

def estarbre(G) :
    g = len(G)
    for j in range(g):
        S = 0
        for i in range (g):
            S += G[i][j]
        if S > 1 :
            return False
    return True

def extraire_sous_matrice(matrice, sommets):
    sous_matrice = [[matrice[i][j] for j in sommets] for i in sommets]
    return sous_matrice

def EtudeCFC(matrice, FC):
    checkboucle=[]
    print("\n\n")
    for i in range(len(matrice)):
        if matrice[i][i] == 1:
            checkboucle.append(i)
    # print(checkboucle)
    for i in range(len(FC)):
        afterRemoveboucle = [element for element in FC[i] if element not in checkboucle]
        if(len(afterRemoveboucle)>0):
            # print(FC[i])
            
            # print("after"+ str(FC[i]))
            submatrice = extraire_sous_matrice(matrice, afterRemoveboucle)
            # print(submatrice)
            # print(submatrice)
            cluster, period = PeriodicGraphMatricielle(submatrice)

            print("\t\tLe CFC est: " + str(afterRemoveboucle) +" a la période = " +  str(period))
         
            # print("\t\tcluster = " + str(cluster))
            
            print("\n")
        

    for i in range(len(checkboucle)):
        print("\t\tLe CFC est: [" + str(checkboucle[i]) +"] a la période = 1 parce qu'il a un boucle" )
######################################################################




# Input graph 
matrice = [
    # to test CFC
    # [0,0,0,0,1,0,0,1,0,0,0,1],
    #               [0,0,1,1,0,0,1,0,0,0,0,0],
    #              [0,0,0,0,0,1,0,0,0,0,0,0],
    #              [0,1,0,1,0,0,0,0,0,0,0,0],
    #              [0,0,0,0,0,0,0,1,0,0,0,0],
    #              [0,0,1,0,0,0,0,0,0,0,1,0],
    #              [1,0,0,0,0,0,0,0,1,0,0,0],
    #              [0,0,0,0,0,0,0,0,0,1,0,0],
    #              [0,1,0,0,0,0,1,0,0,0,0,0],
    #              [0,0,0,0,0,0,0,1,0,0,0,1],
    #              [0,0,0,0,0,0,0,0,0,0,1,0],
    #              [1,0,0,0,0,0,0,0,0,0,0,0]
    
    
    # to test non circuit + non arbo
    # [0,0,0,1,0,0,0,0,0],
    # [0,0,0,0,1,1,0,0,0],
    # [0,0,0,0,0,1,0,0,0],
    # [0,1,0,0,1,0,0,0,0],
    # [0,0,0,0,0,0,1,0,0],
    # [0,0,0,0,0,0,1,1,0],
    # [0,0,0,0,0,0,0,0,1],
    # [0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0]




    #graph FC + periodic
    # [0,0,0,0,1,0],
    # [0,0,0,0,0,1],
    # [0,1,0,0,0,0],
    # [1,0,1,0,0,0],
    # [0,0,0,1,0,1],
    # [1,0,0,0,0,0]

    #to test arborescence
    [0, 1, 1, 0, 0],
[0, 0, 0, 1, 1],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0]


]



matriceinNumpy=np.array(matrice)
# print(isFC(matriceinNumpy))
# print(malgrange(matriceinNumpy))

# # print(graph_matrix)
# sz = len(graph_matrix)

# ordered_levels = order_graph_by_level(graph_matrix)
# print("Il y a " + str(len(ordered_levels)) + " niveaux : ")
# print(ordered_levels)



print("========================================================================\n")
print("\t\tGraph entrée\t:")
for i in range(len(matrice)):
    print("\t"+str(matrice[i]))
print("\n\n\t\tPrésence d'un circuit?\n")
#Circuit
if(presencecircuit(matriceinNumpy)):
    print("\t\tOui\n")
    print("\tCe sont les circuits dans ce graph: ")
    for i in range(len(findCircuits(matriceinNumpy))):
        print("\t\t"+str(findCircuits(matriceinNumpy)[i]))
    
    print("\n\n\t\tC'est un graph Fortement Connexe? ")
    #FC
    if(isFC(matriceinNumpy)):
        print("\t\tOui\n")
        print(malgrange(matriceinNumpy))
        print("C'est un graph périodique?\n")
        if(checkIfPeriodic(matrice)):
            print("\t\tOui")
            PeriodicGraphMatricielle(matrice)
        else:
            print("Non c'est le graph apériodique")
    else:
        print("\t\tNon")
        # print(malgrange(matriceinNumpy))
        EtudeCFC(matriceinNumpy, malgrange(matriceinNumpy))
        # print("m "+ str(malgrange(matriceinNumpy)))
else:
    print("\t\tNon")
    print("\t\tOrdonne le graph: \n")
    ordered_levels = order_graph_by_level(matrice)
    print("\t\tIl y a " + str(len(ordered_levels)) + " niveaux : ")
    print("\t\t"+str(order_graph_by_level(matrice)))
    print("\t\tEst-ce que c'est un graphe arborescence?   \t" + str(estarbre(matriceinNumpy)))