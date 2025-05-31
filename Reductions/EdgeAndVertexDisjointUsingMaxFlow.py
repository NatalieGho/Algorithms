import networkx as nx
def DisjointStuff(mod, vert, elems): #this is the method that does not work lol
    new_elems = []
    for i in range(len(elems)):
        if i % 2 == 0:
            new_elems.append(elems[i])
        else:
            new_elems.append(elems[i] + "*")
    for i in range(vert):
        firstthing = str(i)
        nextthing = firstthing + "*"
        new_elems.append(nextthing)
        new_elems.append(firstthing)
    EdgeDisjointStuff(mod, vert, new_elems)
def EdgeDisjointStuff(mod, vert, listofstuff):
    G = nx.DiGraph()
    for i in range(0, len(listofstuff)-1, 2):
        value = str(listofstuff[i])
        valueplusone = str(listofstuff[i + 1])
        G.add_edge(value, valueplusone)
        nx.set_edge_attributes(G,{(value, valueplusone): 1}, "capacity")
    doingMaxFlow(mod, vert, G)
def doingMaxFlow(mod, vert, graph):
    sink = str(vert - 1)
    if mod=="V":
        sink = str(vert-1) + "*"
    flow_value, flow_dict = nx.maximum_flow(graph, "0", sink, flow_func=nx.algorithms.flow.edmonds_karp)
    print(str(flow_value))
    lists = extract_paths(flow_dict,"0",sink)
    for i in range(len(lists)):
        for j in range(len(lists[i])):
            thing = lists[i][j].replace("*", "")
            if mod=="E":
                print(thing, end=" ")
            else:
                if j==(len(lists[i])-1):
                    print(thing, end=" ")
                elif thing == lists[i][j]:
                    print(thing, end=" ")
        print()
    print()
    # print(answer)

def extract_paths(flow_dict, source, target):
    paths = [] #creating a list that keeps all the lists of the answers
    while True:
        onepath= [] #creating a small path where keeping track of current dfs path
        currnode = source #starting at the source every single time
        visited = list() #keeping track off all the ones you have aready seen at each step
        while currnode != target:  #while you haven't reached the end
            visited.append(currnode) #add the current node to nodes you have already seen
            onepath.append(currnode) #add the current node to the current path to later add to final list of paths
            next_node = None #setting up the local variable for this
            for nextnode, flow in flow_dict[currnode].items(): #looking at all the possible other edges
                if flow>0 and nextnode not in visited:  #if the flow greater than zero and the next node has not already been seen
                    next_node = nextnode #set the value
                    break
            if next_node is None: #if no next node exists that fits those conditions, there is not a path to the terminus node
                break #exit this inner loop and try again to find an augmenting path from start to end
            flow_dict[currnode][next_node] -= 1 #updating the edge so not looked at again
            currnode = next_node #updating the current node to the next one since it is a valid way to the next node
        if currnode==target:  #if the current node is the target, means you have found a path with flow to the terminus
            onepath.append(target) #add the current node to the pat
            paths.append(onepath) #add the finished path to the list of all paths
        else:
            break #otherwsie you do not have a valid path, so try again in the while loop
    return paths #returning the overall answer in this

test_cases = int(input())
for _ in range(test_cases):
    v, e, mode = input().split()
    vertices = int(v)
    edges = int(e)
    elements = input().split(" ")
    # print("Graph: " + str(_))
    if mode.lower() == "e":
        EdgeDisjointStuff(mode, vertices, elements)
    elif mode.lower() =="v":
        DisjointStuff(mode, vertices, elements)
