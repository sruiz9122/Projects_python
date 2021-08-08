#1. Leer una matriz de 4X4 y determinar 
#en que posición está el mayor
numFilas = int(input('Ingrese número de filas:'))
numColumnas = int(input('Ingrese número de columnas:'))

mat = [] * numFilas
for i in range (numFilas):
    a = [0] * numColumnas
    mat.append(a)

for i in range(numFilas):
    for j in range(numColumnas):
        mat[i][j] = int(input(f'Posición [{i},{j}]:\n'))

mayor = mat[0][0]
posFila = 0
posColumna = 0

for i in range(numFilas):
    for j in range(numColumnas):
        if mat[i][j] > mayor:
            mayor = mat[i][j]
            posFila = i
            posColumna = j

print(f'En la matriz de tamaño {numFilas} X {numColumnas}: {mat}')
print(f'El número mayor es: {mayor} \nY está en la posición: [{posFila}, {posColumna}]')

