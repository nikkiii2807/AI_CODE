import random
[[1,1,1],
 [1,1,1],
 [1,1,1]]

def aco(num_cities,distances,num_ants,max_iterations):
    pheromones=[[1 for _ in range(num_cities)]for _ in range(num_cities)]
    best_cost=999999
    best_sol=[]

    for _ in range(max_iterations):
        solutions=[]

        for _ in range(num_ants):
            sol=list(range(num_cities))
            random.shuffle(sol)
            cost=sum(distances[sol[i]][sol[(i+1)% len(sol)]] for i in range(len(sol)))
            solutions.append((sol,cost))

        solutions.sort(key=lambda x:x[1])
        

        if solutions[0][1] < best_cost:
            best_sol,best_cost=solutions[0]

        for sol,cost in solutions:
            for i in range(len(sol)):
                citya,cityb=sol[i],sol[(i+1)%len(sol)]
                pheromones[citya][cityb]+=1/cost

    return best_sol,best_cost

num_cities=4
distances=[
    [0,10,15,20],
    [10,0,35,25],
    [15,35,0,30],
    [20,25,30,0]
]
num_ants=10
max_iterations=100
best_sol,best_cost=aco(num_cities,distances,num_ants,max_iterations)
print("Best sol is: ",best_sol)
print('Best cost is: ',best_cost)