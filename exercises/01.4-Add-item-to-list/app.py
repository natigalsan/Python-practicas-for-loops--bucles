#Remember import random function here:
import random

#The magic is here:
def generate_random_list():

    my_list = [4,5,734,43,45]
    
    numeros_aleatorios=random.sample(range(100), 10)

    for i in range(numeros_aleatorios):

        my_list.append(numeros_aleatorios)
        i += i
        return my_list



print(generate_random_list(my_list))


