import random
import numpy as np
from GA_utils import *

def elitism(population,elitism_rate,verbose=False):
    population_size = len(population)
   
    elite_count = int(population_size*elitism_rate)
    elite_indexes = np.argsort([evaluate_fitness(chromosome) for chromosome in population] )[::-1][:elite_count]
    elite_ppulation = population[elite_indexes]
    selected_pop = np.array(elite_ppulation)

    if verbose==True:
        print(f"Elite Population : {selected_pop}")
    
    return selected_pop

def tournament(population,tounament_rate,verbose=False):
    n=len(population)
    winners=[]


    for i in range(n):
        tournament_idx=np.random.choice(np.arange(n),size=tounament_rate,replace=False)
        # print(f'tournamen idx {i} = {tournament_idx}')
        tournament_pop=population[tournament_idx]
        
        winner= max(tournament_pop,key=evaluate_fitness)
        winners.append(winner)

    if verbose==True:
        print('-'*100,'\n')
        print(f'Winners of the touenament : \n{winners}')
        print('-'*100,'\n')
        # print(f'tournamen pop {i} = {tournament_pop}')
        # print(f'The winer in  tournament {i} {tournament_idx}is = {winner}')

    return winners






