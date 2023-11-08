import math    
print(math.sqrt(25))

#####################

import pandas  as pd 

data = {'Name': ["Tom","Nick",'John'],'Age':[20,21,19]}

df =  pd.DataFrame(data)
print(df)

###################### traer solo un paquete de la libreria

from math import sqrt

print(sqrt(36))


###########################################

import numpy as np 

array = np.array([1,2,3,4,5])

print(array)


##########################################
import matplotlib.pyplot as plt 

plt.plot([1,2,3,4])
plt.ylabel('algunos numeros')
plt.xlabel('los mismos numeros')
plt.show()

