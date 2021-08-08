#Mi primer programa en python
print('Hola mundo')

x=1
y=2
z=3

#Salida de Datos
n=x+y+z
print('El resultado de la suma es: ', n)
n=n*x
print('El resultado de la multiplicación es: ', n)
n=n-n-n
print('El resultado de la resta es: ', n)
n=n*2
print('Hola','nose')
print('Hola', end='')
print('nose')
print('Hola','nose',sep=',')
print('Hola','\n nose que',sep=',')#El \ Salto de linea
print(f'prueba de imprimir un valor dentro de un string {n}')
variableconcate = """Hola
diablo"""
print(variableconcate)

#Elevado a la n potencia
e=2**n
print(f"2 elevado a la {n} es igua a: \n" , e)


#Entrada de datos
nombre=input("Ingrese Nombre: \n")
apellido=input("Ingrese apellido: \n")
edad=int(input(f"Ahora {nombre} ingrese su edad: \n"))
datoUsr= print('ingreso su nombre: ', nombre,'\n Ingreso su apellido: ',apellido, '\n Ingreso su edad: ', edad)
año=int(input('Ingrese el año actual \n'))
nacimiento = año - edad
print(f'Usted nació en el año: \n {nacimiento}')

