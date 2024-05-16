import random
def fitness_function(chromosome):
    x=int("".join(map(str,chromosome)),2)
    return x**2

population_size=10
chromosome_length=10
mutation_rate=0.1
generation=200

population=[]
for _ in range(population_size):
    chromosome=[random.randint(0,1) for _ in range(chromosome_length)]
    population.append(chromosome)

for _ in range(generation):
    fitness_score=[]
    for chromosome in population:
        fitness=fitness_function(chromosome)
        fitness_score.append(fitness)

        parent=[]
        for _ in range(population_size):
            parent.append(random.choice(population))

        children=[]
        for i in range(0,len(parent),2):
            crossover_point=random.randint(0,chromosome_length-1)
            parent1=parent[i]
            parent2=parent[i+1]
            child1=parent1[:crossover_point]+parent2[crossover_point:]
            child2=parent2[crossover_point:]+parent1[:crossover_point]
            for j in range(chromosome_length):
                if random.random()<mutation_rate:
                    child1[j]^=1
                if random.random()<mutation_rate:
                    child2[j]^=1
        children.append(child1)
        children.append(child2)
    population=children

best_chromo=max(population,key=lambda a:fitness_function(a))
best_fitness=fitness_function(best_chromo)
best_x=best_fitness**0.5

print("Best chromosome:", best_chromo)
print("Best x:", best_x)
print("Best fitness:", best_fitness)

