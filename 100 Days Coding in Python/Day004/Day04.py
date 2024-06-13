#Random Module
from ctypes import sizeof
import random
num_integer=random.randint(0,100)#Return a random integer betwenn [0,100]
num_float=random.random()
print(num_integer,num_float)
#Lists
A=['alpha','beta','gama','delta']
size=len(A)
print(size)
A.append('Ypsilon')#Add a single item to the end of the list.
#Nested Lists(lists within lists)
#dirty_dozen=["Strawberries","Nectarines","Apples","Grapes","Peaches","Cherries","Pears","Spinach","Kale","Tomatoes","Celery","Potatoes"]
fruits=["Strawberries","Nectarines","Apples","Grapes","Peaches","Cherries","Pears"]
vegetables=["Spinach","Kale","Tomatoes","Celery","Potatoes"]
dirty_dozen=[fruits,vegetables]
print(dirty_dozen[0][0])