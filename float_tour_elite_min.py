import numpy as np
import time
from utils import standard_deviation as std

class GeneticAlgorithmFloating:
    def __init__(self, population_size, chromosome_length, mutation_rate,crossover_rate, generations,tournament_size,elitism_rate):
        self.population_size = population_size
        self.chromosome_length = chromosome_length
        self.mutation_rate = mutation_rate
        self.crossover_rate=crossover_rate
        self.tournament_size=tournament_size
        self.elitism_rate=elitism_rate
        self.generations = generations
        self.x1_range = [0,1]
        self.x2_range = [0,1]
        self.best_chromosome = None
        self.best_generation = None

    def initialize_population(self):
        return np.random.uniform(low=[self.x1_range[0], self.x2_range[0]], high=[self.x1_range[1], self.x2_range[1]], size=(self.population_size, 2))

    def decode_chromosome(self, chromosome):
        return chromosome[0], chromosome[1]

    def evaluate_fitness(self, chromosome):
        x1, x2 = self.decode_chromosome(chromosome)
        value = (-1)*(x1**2 + x2**2)**0.25 * (np.sin(50*(x1**2 + x2**2)**0.1)**2 + 1)
        return value

    def selection(self, population):
        selected_population=[]

        elite_count=int(self.population_size*self.elitism_rate)
        elite_indexes = np.argsort([self.evaluate_fitness(chromosome) for chromosome in population])[::-1][:elite_count]
        elite_population = population[elite_indexes]
        selected_population.extend(elite_population)

        remaining_population=self.population_size - elite_count

        for _ in range(remaining_population):
            tournament_indexes=np.random.choice(np.arange(self.population_size),size=self.tournament_size,replace=False)
            tournament_population = population[tournament_indexes]

            winner= max(tournament_population, key=self.evaluate_fitness)
            selected_population.append(winner)
        
        return np.array(selected_population)

    def crossover(self, parent1, parent2):

        if np.random.rand()< self.crossover_rate:
            child1=np.empty_like(parent1)
            child2=np.empty_like(parent2)

            for i in range(len(parent1)):
                if np.random.rand() < 0.5:
                    child1[i]=parent1[i]
                    child2[i]=parent1[i]

                else:
                    child1[i]=parent2[i]
                    child2[i]=parent2[i]

        else:
            child1 = parent1.copy()
            child2 = parent2.copy()

        return child1, child2

    def mutate(self, chromosome):
        mutated_chromosome= chromosome.copy()
        for i in range(len(chromosome)):
            if np.random.rand() < self.mutation_rate:
                mutated_chromosome[i] += np.random.normal(-0.1,0.1)
                chromosome[i] =np.clip(mutated_chromosome[i], 0 , 1)
        return chromosome
    
    def run(self):
        start_time=time.time()
       
        population = self.initialize_population()
        best_fitness = float('-inf')

        for generation in range(self.generations):
            selected_population = self.selection(population)

            new_population = []
            for i in range(0, self.population_size, 2):
                parent1, parent2 = selected_population[i], selected_population[i+1]
                child1, child2 = self.crossover(parent1, parent2)

                child1 = self.mutate(child1)
                child2 = self.mutate(child2)

                new_population.extend([child1, child2])

            population = np.array(new_population)

            current_best_chromosome = max(population, key=self.evaluate_fitness)
            current_best_fitness = self.evaluate_fitness(current_best_chromosome)

            if current_best_fitness > best_fitness:
                best_fitness = current_best_fitness
                self.best_chromosome = current_best_chromosome
                self.best_generation = generation

        best_solution = self.decode_chromosome(self.best_chromosome)
        
        end_time=time.time()
        round_time= end_time -start_time
        
        if abs(best_fitness) > 0.00001:
            return best_solution, best_fitness, self.best_chromosome, self.best_generation,round_time

        return best_solution, best_fitness, self.best_chromosome, self.best_generation,round_time

# Parameters
population_size = 300
chromosome_length = 2
mutation_rate = 0.05
crossover_rate=1
generations = 80
tournament_size = 5
elitism_rate = 0.2  
rounds = 3
how_many=0

#----------------------- algorithm class instance -----------------------#
start_time=time.time()
ga = GeneticAlgorithmFloating(population_size, chromosome_length, mutation_rate,crossover_rate, generations,tournament_size,elitism_rate)

accum_time=[]

for i in range(rounds):
    best_solution, best_fitness, best_chromosome, best_generation, round_time = ga.run()
    # print(i)
    # print(f"Best solution: x1 = {best_solution[0]:.4f}, x2 = {best_solution[1]:.4f}")
    # print(f"Best fitness: {abs(best_fitness):.4f}")
    # print(f"Best chromosome: {best_chromosome}")
    # print(f"Found in generation: {best_generation}")
    # print('*'*50)

    if abs(best_fitness) > 0.00001:
        continue

    else:
        how_many+=1
        print(f'Round : {i}')
        print(f"Best solution: x1 = {best_solution[0]:.4f}, x2 = {best_solution[1]:.4f}")
        print(f"Best fitness: {abs(best_fitness):.4f}")
        print(f"Best chromosome: {''.join(map(str, best_chromosome))}")
        print(f"Found in generation: {best_generation}")
        print(f'The global min in round: {i} was founded in {round_time:.4f} seconds')
        print('-'*50)
        accum_time.append(round_time)

end_time=time.time()

#----------------------- algorithm Hitrate -----------------------#
if how_many == 0.0:
    hit_rate=0.0
else:
    hit_rate=(how_many/rounds)*100
#----------------------- algorithm execution time -----------------------#
execution_time= end_time -start_time

#----------------------- algorithm average time per round -----------------------#
if how_many == 0.0:
    round_avr_time=0.0

else:    
    round_avr_time=execution_time/how_many

#----------------------- algorithm Hitrate average time  -----------------------#
total_accum_time= sum(accum_time)

if how_many == 0.0:
    hit_rate_avr_time=0.0
else:
    hit_rate_avr_time=total_accum_time/how_many
hit_rate_time_std= std(hit_rate_avr_time,accum_time)


#----------------------- print algorithm metrics -----------------------#
print(f'Global min founded in {how_many} of {rounds} rounds\n')
print(f'The hit rate of the algoritm is {hit_rate}%')
print('-'*50)
print(f'The execution time of all rounds is : {execution_time:.4f} sec')
print('-'*50)
print(f'The average time per round is : {round_avr_time:.4f} sec')
print('-'*50)
# print(f'accum_time : {total_accum_time:.4f}')
# print('-'*50)
print(f'hit_rate_avr_time : {hit_rate_avr_time:.4f} sec std: {hit_rate_time_std:.6f} sec')
print('-'*50)
