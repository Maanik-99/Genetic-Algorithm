import random

class GA:
    def __init__(self, T, k):
        self.target = T
        self.k = k
        self.population_size = 20
        self.max_generations = 100
        self.mutation_rate = 0.2
        self.population = []
        self.found = False
        self.solution = None
        self.run()

    def run(self):
       
        self.population = [[random.randint(0, 9) for _ in range(self.k)] for _ in range(self.population_size)]
        
        for generation in range(self.max_generations):
           
            fitness = []
            for individual in self.population:
                current_sum = individual[0] + individual[1]
                fitness.append(abs(current_sum - self.target))
            
            for i in range(self.population_size):
                if fitness[i] == 0:
                    self.found = True
                    self.solution = self.population[i]
                    break
            
            if self.found:
                break
            
         
            parents = []
            for _ in range(self.population_size):
                
                idx1, idx2 = random.sample(range(self.population_size), 2)
                parent = self.population[idx1] if fitness[idx1] <= fitness[idx2] else self.population[idx2]
                parents.append(parent)
            
           
            new_population = []
            for i in range(0, self.population_size, 2):
                parent1 = parents[i]
                parent2 = parents[i+1] if (i+1) < self.population_size else parents[0]
                crossover_point = random.randint(1, self.k - 1)
                child1 = parent1[:crossover_point] + parent2[crossover_point:]
                child2 = parent2[:crossover_point] + parent1[crossover_point:]
                new_population.extend([child1, child2])
          
            for individual in new_population:
                for j in range(self.k):
                    if random.random() < self.mutation_rate:
                        individual[j] = random.randint(0, 9)
            
            self.population = new_population
        
        if self.found:
            print(" ".join(map(str, self.solution)))
        else:
          
            best_fitness = min(fitness)
            best_index = fitness.index(best_fitness)
            print(" ".join(map(str, self.population[best_index])))

T = int(input("Enter the target value: "))
k = int(input("Enter the length: "))
ga = GA(T, k)
