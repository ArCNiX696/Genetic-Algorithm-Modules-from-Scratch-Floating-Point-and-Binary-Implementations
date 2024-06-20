import numpy as np 

def bitflip_mutation(chromosome,mut_rate,verbose=False):
    mutation=False
    mutated_bits=[]
    mutated_chro= chromosome.copy()

    for i in range(len(chromosome)):
        if np.random.rand()<mut_rate:
            mutation=True
            
            bit=chromosome[i]
            mutated_bit = 1 - bit
            mutated_chro[i]=mutated_bit

            #For debugging
            # print('bit:',bit)
            # print('mutated bit :',mutated_bit)

            mutated_bits.append(i)

        else:
            mutated_chro[i] = mutated_chro[i]
        
    if verbose==True and mutation == True:
        print('-'*100,'\n')
        print(f'Original Chromosome = {chromosome}\n\n')
        print(f'The mutated genes of this chromosome are in indexes = {mutated_bits}\n\n')
        print(f'Chromosome after mutation = {mutated_chro}\n\n')        
        print('-'*100,'\n')

    elif verbose==False:
        pass

    else:
        print(f'Original Chromosome = {chromosome}\n\n')
        print(f'Due the low mutation rate, there is not mutation for this Chromosome in this generation\n\n')
        print(f'Chromosome ramains the same = {mutated_chro}\n\n')    

    return mutated_chro
