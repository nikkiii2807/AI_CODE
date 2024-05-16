graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['E','F','B'],
    'D':[],
    'E':[],
    'F':[]
}
visited=[]
queue=[]
def BFS(graph,start):
    if start not in visited:
        visited.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            queue.append(neighbor)
    if queue:
        BFS(graph,queue.pop(0))

start_node='A'
BFS(graph,start_node)

for node,edges in graph.items():
    if node in visited:
        print(node, 'was visited')
    else:
        print(node, 'was not visited')
[print(node,end='')for node in visited]