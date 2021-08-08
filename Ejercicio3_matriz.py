import numpy as np
#Leer una matriz 3X4 entera y determinar en que posiciones exactas se encuentran los números pares

matriz = np.array([[2,7,8,3],
                   [3,10,15,20],
                   [22,80,5,36]])

orden_matriz = matriz.shape[0]
numero_par=matriz[0,0]
posicion_numero_par=[]

print(matriz)

for i in range (orden_matriz):
    for j in range (orden_matriz+1):
        if matriz[i,j]%2 == 0:
            numero_par = matriz[i,j]
            posicion_numero_par = [(i,j)]
            print(f'El número {numero_par} es par y está en la posición {posicion_numero_par}')
