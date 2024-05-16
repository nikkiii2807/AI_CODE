def get_neighbor(v):
    return adjacency_list[v]

def a_star(start_node,end_node):
    open_list={start_node}
    g={start_node:0}
    parent={start_node:start_node}

    while open_list:
        n=min(open_list,key=lambda a:g[a]+h[a])
        if n==None:
            print("Path not found")
            return None,float('inf')
        if n==end_node:
            path=[]
            total_cost=g[end_node]
            while parent[n]!=n:
                path.append(n)
                n=parent[n]
            path.append(start_node)
            path.reverse()
            print("Path is ",path)
            return path,total_cost
        
        open_list.remove(n)
        for m,weight in get_neighbor(n):
            temp=g.get(n,float('inf'))+weight
            if temp<g.get(m,float('inf')):
                parent[m]=n
                g[m]=temp
                open_list.add(m)

    print("Path not found")
    return None, float('inf')

adjacency_list={
    'A':[('B',4),('C',3)],
    'B':[('F',5)],
    'C': [('D', 7), ('E', 10)],
    'D': [('E', 2)],
    'F': [('G', 16)],
    'E': [('G', 5)]
}

h={
    'A':14,
    'B': 12,
    'C': 11,
    'D': 6,
    'E': 4,
    'F': 11,
    'G':0
}

path,total_cost=a_star('A','G')
if path:
    print("Total cost is: ",total_cost)
else:
    print("Not found")