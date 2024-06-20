import numpy as np
    
def single_crossover(parent1,parent2,crossover_rate,verbose=False):
    chromosome_len=len(parent1)

    if np.random.rand() < crossover_rate:
            crossover_point= np.random.randint(1, chromosome_len)

            child1=np.concatenate((parent1[:crossover_point],parent2[crossover_point:]))
            child2=np.concatenate((parent2[:crossover_point],parent1[crossover_point:]))

    else:
        child1=parent1.copy()
        child2=parent2.copy()

    if verbose==True:
        print('-'*100,'\n')
        print(f'\nParent1 = {parent1}\nParent2 = {parent2}\n')
        print(f'crosover_point = {crossover_point}\n')
        print(f'child1 = {child1}\nchild2 = {child2}')
        print('-'*100,'\n')

    return child1,child2

def uniform_crossover(parent1,parent2,cross_rate,inherited_rate,verbose=False):
    parent1_bits=[]
    parent2_bits=[]
    crossover=False

    if np.random.rand()<cross_rate:
          crossover=True
          
          child1=np.empty_like(parent1)
          child2=np.empty_like(parent2)

          for i in range(len(parent1)):
               prob=np.random.rand()
               
               if prob < inherited_rate:
                child1[i]=parent1[i]
                child2[i]=parent1[i]

                parent1_bits.append(i)

               else:
                child1[i]=parent2[i]
                child2[i]=parent1[i]

                parent2_bits.append(i)

    else:
        child1=parent1.copy()
        child2=parent2.copy()

    if verbose==True and crossover==True:
        print('-'*100,'\n')
        print(f'\nParent1 = {parent1}\nParent2 = {parent2}\n')
        print(f'Bits inherited by\nparent 1 are in indexes = {parent1_bits}\nparent 2 are in indexes = {parent2_bits}\n')
        print(f'child1 = {child1}\nchild2 = {child2}\n')
        print('-'*100,'\n')

    elif verbose == False:
        pass

    else:
        print('-'*100,'\n')
        print(f'\nParent1 = {parent1}\nParent2 = {parent2}\n')
        print(f'\nNo crossover in this generation due a low crossover rate, so parents become children for the next generation\n')
        print(f'child1 = {child1}\nchild2 = {child2}')
        print('-'*100,'\n')
        
    return child1,child2

def inter_onepoint_cross(parent1,parent2,cross_rate,verbose=False):
    n=len(parent1)
    m=len(parent2)
    

    if np.random.rand() < cross_rate:
        cross_point1=np.random.randint(1,n)
        cross_point2=np.random.randint(1,m)

        child1=np.concatenate((parent1[cross_point1:],parent1[:cross_point1]))
        child2=np.concatenate((parent2[cross_point2:],parent2[:cross_point2]))
    
    else:
        child1 = parent1.copy()
        child2 = parent2.copy()


    if verbose == True:
        if verbose==True:
            print('-'*100,'\n')
            print(f'\nParent1 = {parent1}\nParent2 = {parent2}\n')
            print(f'crosover_point 1 for child 1 = {cross_point1}\n')
            print(f'crosover_point 2 for child 2 = {cross_point2}\n')
            print(f'child1 = {child1}\nchild2 = {child2}')
            print('-'*100,'\n')

    return child1,child2



        

            


    

     
    
 
        

    
                 

                 

                
                 
                 
                 
          
      

    
        




    




    