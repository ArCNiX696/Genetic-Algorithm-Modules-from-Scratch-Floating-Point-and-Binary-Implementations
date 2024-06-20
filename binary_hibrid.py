import numpy as np
import time
from  utils import standard_deviation as std
from GA_utils import *
from GA_selection import *
from GA_crossover import *
from GA_mutation import *

class GeneticAlgorithmBinary:
    def __init__(self, population_size, chromosome_len,generations,elitism_rate,tournament_size,crossover_rate,inherited_rate,mutation_rate):
        self.population_size = population_size
        self.chromosome_len = chromosome_len
        self.generations = generations
        self.elitism_rate = elitism_rate
        self.tournament_size = tournament_size
        self.crossover_rate = crossover_rate
        self.inherited_rate=inherited_rate
        self.mutation_rate = mutation_rate
        self.best_chromosome = None
        self.best_generation = None
        self.best_fitness = []
        self.actual_fitness = []
        self.standar_devs = []

    def initialize_population(self,verbose=False):
        population = np.random.randint(2,size=(self.population_size,self.chromosome_len))

        if verbose==True:
            np.set_printoptions(threshold=np.inf)#Set print options to display all elements
            print(f'population: {population}')

        return population
    
    def run(self,verbose=True,plot=False):
        population = self.initialize_population()
        best_fitness=float('-inf')
        
        
        for generation in range(self.generations):
            next_generation=[]

            elite = elitism(population,self.elitism_rate,verbose=False)
            next_generation.extend(elite)

            selected_pop=tournament(population,self.tournament_size,verbose=False)

            for i in range(0,self.population_size,2):
                # print(f'Couple = {i}')
                parent1,parent2=selected_pop[i], selected_pop[i+1]

                child1,child2=uniform_crossover(parent1,parent2,self.crossover_rate,self.inherited_rate,verbose=False)
                # child1,child2=inter_onepoint_cross(parent1,parent2,self.crossover_rate,verbose=False)
               
                child1=bitflip_mutation(child1,0.1,verbose=False)
                child2=bitflip_mutation(child2,0.1,verbose=False)

                next_generation.extend([child1,child2])

            population = np.array(next_generation)

            current_best_chromosome = max(population , key=evaluate_fitness)
            current_best_fitness = evaluate_fitness(current_best_chromosome)
            best_fitness=abs(current_best_fitness)
            self.best_fitness.append(best_fitness)
            best_solution = decode_chromosome(current_best_chromosome)

            if verbose == True:
                print(f'Generation : {generation}\n')
                print(f'current_best_chromosome : {current_best_chromosome}\n')
                print(f'Best solution binary\nBinary chromosome x1 = {best_solution[2]}\nBinary chromosome x1 = {best_solution[3]}')
                print(f'\nBest solution float\nDecoded chromosome x1 = {best_solution[0]:.6f}\nDecoded chromosome x1 = {best_solution[1]:.6f}')
                print(f'\nFitness score = {best_fitness}')
                print('-'*100,'\n')

        if plot == True:
           plot_evolution(self.best_fitness,'Number of Generations','Fitness score','Chromosome evolution in all generations')
            
        fit_avg = fitness_avg(self.best_fitness)
        standar_dev = std(fit_avg,self.best_fitness)

        self.actual_fitness.append(fit_avg)
        self.standar_devs.append(standar_dev)

    def runs(self,runs=int,verbose=True,plot=False):

        for run in range(runs):
            self.run(verbose=False)

            if verbose == True:
                print('-'*100,'\n')
                print(f'Run : {run}\n')
                print(f'Fitness : {self.actual_fitness[run]} , std : {round(self.standar_devs[run],10)}\n')   
            print('-'*100,'\n')
            # print(f'Fitness : {self.actual_fitness} \nstd : {self.standar_devs}\n')   

        if plot == True:
            plot_evolution(self.actual_fitness,'Number of Runs','Fitness Avg score','Average fitness in all runs')
            
if __name__=='__main__': 
    population_size=100
    chromosome_len=30
    generations=10
    elitism_rate = 0.2
    tournament_size = 5
    crossover_rate = 1
    inherited_rate=0.5 #Just for some kind of crossover , it is the prob to inherited genes from each parent
    mutation_rate = 0.1
    best_chromosome = None
    best_generation = None

    #(self, population_size, chromosome_len,generations,elitism_rate,tournament_size,crossover_rate,inherited_rate,mutation_rate)
    GA=GeneticAlgorithmBinary(population_size, chromosome_len,generations,elitism_rate,tournament_size,crossover_rate,inherited_rate,mutation_rate)
    GA.run(verbose=True,plot=True)
    # GA.runs(50,plot=True)
   
