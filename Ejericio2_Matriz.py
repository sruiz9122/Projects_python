import numpy as np
#Leer una matriz 4x4 entera y determine cuantas veces se repite ene ella el número mayor.

matriz = np.array([[19,4,5,6],
                   [7,8,9,5],
                   [6,9,8,9],
                   [9,9,9,9]])

numero_mayor = matriz[0,0]
posicion_numero_mayor =[]
orden_matriz = matriz.shape[0]
acumulador = 0

print(f"Matriz 4X4:\n{matriz}")

for i in range(orden_matriz):
    for j in range(orden_matriz):
        if numero_mayor <= matriz[i,j]:
            numero_mayor = matriz[i,j]
            posicion_numero_mayor = [(i,j)]
        elif numero_mayor == matriz[i,j]:
            posicion_numero_mayor.append((i,j))

for k in range(orden_matriz):
    for l in range(orden_matriz):
        if numero_mayor == matriz[k,l]:
            acumulador += 1


print(f"El número mayor es:\n{numero_mayor}")
print(f"Este número lo encontramos\n{acumulador}\nveces!")
