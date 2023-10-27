
## import librerias ##

import pandas as pd
import seaborn as sns 
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt 

## se leen los datos ## 

datos = pd.read_csv(r"C:\Users\ViG\Desktop\NHANES.csv")
datos.head()

grafico =pd.crosstab(datos.Gender,datos.HomeOwn)
grafico_porcentuales = grafico.apply(lambda x:(x*100) / sum(x), axis =1)
grafico_porcentuales.plot.barh(stacked= True)

##Planteamiento de Hipotesis, aplicando la estadistica Inferencial" para infereir en
## en los datos, se crea la hipotesis nula y la hipotesis alternativa
## se busca rechazar la hipotesis nula 

## Se seleccionan las variables a trabajar## 

analisis = datos.loc[datos['HomeOwn'].isin(['Own','Rent'])
                     ,['Gender','HomeOwn']]
analisis.head()

## Se define funcion para permutaciones
## Permutaciones realizan un proceso iterativo de muestreo, asumiendo 
## que el muestreo es aleatorio 

def permutation_sample(data1,data2):
    """Genera una muestra permuta a partit de dos conjuntos de datos."""
    
    ##Concatenar Los conjuntos de datos : data
    data = np.concatenate((data1,data2))
    
    
    ##Permutar el arreglo concatenado : datos permutados
    permuted_data = np.random.permutation(data)
    
    ##Dividir el arreglo permutado en dos:
    perm_sample_1 = permuted_data[:len(data1)]
    perm_sample_2 = permuted_data[len(data1):]
    
    return perm_sample_1, perm_sample_2 

## Generate permutation samples

perm_sample_1, perm_sample_2 = permutation_sample(
    datos.loc[datos['Gender'] == 'male', ['HomeOwn']],
    datos.loc[datos['Gender'] == 'female',['HomeOwn']])
    
### Se crea la funcion para definir la diferencia entre proporciones###


def diff_of_props(data_1,data_2,value):
    
    """Diferencia entre los promedios de dos arreglos"""
    
 ## Se calcula la diferencia entre las proporciones de datos 1 y datos 2: diff

diff = np.mean(data_1[:,0] == value) - np.mean(data_2[:,0] == value)

return diff

result = diff_of_props(data_1, data_2, some_value)

    
    
    
    
    
    
    