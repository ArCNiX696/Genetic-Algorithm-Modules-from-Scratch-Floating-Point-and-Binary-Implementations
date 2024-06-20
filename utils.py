import numpy as np

def standard_deviation(mean,x):
    n=len(x) # x is a list of sample
    sqr_differences = 0
    for i in x:
        sqr_differences = np.sum(i-mean)**2 

    if n==0.0:
        std=0.0

    else:
        std= np.sqrt(sqr_differences/ n)
    
    return std

def to_float(num=str):
    num=int(num, 2)
    return num

# def normalize(x_val,x_min,x_max):
#     return (x_val - x_min)/(x_max - x_min)
    
# number = '101111'
# print(f'{to_float(number)}')



        


    