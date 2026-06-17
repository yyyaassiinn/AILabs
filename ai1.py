from collections import deque

def dfs(graph, currentNode, visited = None):
    if visited is None:
        visited = set()
        
    if currentNode not in visited:
        visited.add(currentNode)
        print(currentNode, end=" ")
        for i in graph[currentNode]:
            dfs(graph, i,visited)
    
            
def bfs(graph, startNode):
    breadth = deque()
    visited = set()
    breadth.append(startNode)
    while breadth:
        item = breadth.popleft()
        if item not in visited:
            visited.add(item)
            print(item,end=" ")
            for i in graph[item]:
                breadth.append(i)   
    print() 
            
graph1 = {
    1:{2, 3},
    2:{4, 5},
    3:{},
    4:{},
    5:{}
}
graph2 ={
    1:{2, 3},
    2:{4},
    3:{5},
    4:{5},
    5:{4}
}
graph3 ={
    1:{2, 3},
    2:{4},
    3:{},
    4:{},
    6:{7,8},
    7:{},
    8:{}
}

print("bfs graph 1 :", end = " ")
bfs(graph1, 1)
print("dfs graph 1 :", end = " ")
dfs(graph1, 1)
print()
print("bfs graph 2 :", end = " ")
bfs(graph2, 1)
print("dfs graph 2 :", end = " ")
dfs(graph2, 1)
print()
print("bfs graph 3 (start from node 1) :", end = " ")
bfs(graph3, 1)
print("dfs graph 3 (start from node 1) :", end = " ")
dfs(graph3, 1)
print()
print("bfs graph 3 (start from node 6) :", end = " ")
bfs(graph3, 6)
print("dfs graph 3 (start from node 6) :", end = " ")
dfs(graph3, 6)
print()


