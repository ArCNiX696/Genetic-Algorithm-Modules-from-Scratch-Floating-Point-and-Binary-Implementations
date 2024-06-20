import numpy as np
import matplotlib.pyplot as plt
from utils import to_float

############### Plug the Function here ###############
def function(x1,x2,max=True):
    if max == True:
        return (x1**2 + x2**2)**0.25 * (np.sin(50*(x1**2 + x2**2)**0.1)**2 + 1)
    
    return (-1)*(x1**2 + x2**2)**0.25 * (np.sin(50*(x1**2 + x2**2)**0.1)**2 + 1)
    
#Separeate each chromosome into 2 binary chro
def decode_chromosome(chromosome):
    # print('chro:', chromosome)
    # exit()
    chromosome_len=len(chromosome)
    # print('chr len', chromosome_len)
    # exit()
    x1_binary= chromosome[:int(chromosome_len/2)]
    x2_binary= chromosome[int(chromosome_len/2):]
    # print(f'x1_bin {x1_binary} , x2_bin {x2_binary}')
    # exit()

    #To float then Normalize 
    x1 = to_float("".join(map(str,x1_binary))) / (2**(len(x1_binary))-1)
    x2 = to_float("".join(map(str,x2_binary))) / (2**(len(x2_binary))-1)
    # print(f'x1_bin {x1_binary} , x2_bin {x2_binary}')
    # print(f'x1 {x1} , x2 {x2}')
    # exit()
    return x1,x2,x1_binary,x2_binary

#Pass the x1,x2 chromosomes to the function to evaluate
def evaluate_fitness(chromosome,vebose=False):
    x1,x2,x1_binary,x2_binary=decode_chromosome(chromosome)
    
    value = function(x1,x2)

    if vebose==True:
        print('-'*100,'\n')
        print(f'x_1_binary: {x1_binary}\nx_2_binary: {x2_binary}\n')
        print(f'x1 : {x1}\nx2 : {x2}\n\nChromosome fitness score : {value}\n')
        print('-'*100)
    
    return value

def fitness_avg(fitness_scores):
    n = len(fitness_scores)
    # print('this is len',len(fitness_scores))
    ft = sum(fitness_scores)
    favg =  ft / n

    return favg

########### PLOT FUNCTIONS ##########

def plot_evolution(data,x_label=str,y_label=str,title=str):
    plt.figure(figsize=(8, 8))  # Definir el tamaño de la figura

    # Graficar los datos
    plt.plot(data, color='blue', linewidth=2)

    # Etiquetas y título
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    # Mostrar la gráfica
    plt.grid(True)  # Agregar cuadrícula
    plt.show()

    
        
    