
Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- Sin funciones

print("\033c")
mul=int(input("Introduce el numero que quieras para crear la tabla de multiplicar: "))
print(f'{mul} x 1 = {mul*1}')
print(f'{mul} x 2 = {mul*2}')
print(f'{mul} x 3 = {mul*3}')
print(f'{mul} x 4 = {mul*4}')
print(f'{mul} x 5 = {mul*5}')
print(f'{mul} x 6 = {mul*6}')
print(f'{mul} x 7 = {mul*7}')
print(f'{mul} x 8 = {mul*8}')
print(f'{mul} x 9 = {mul*9}')
print(f'{mul} x 10 = {mul*10}')
print("----------Tabla terminada------------")



Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- con estructuras de control con for con decremento de 10
  2.- Sin funciones

print("\033c")
mul=int(input("Introduce el numero que quieras para crear la tabla de multiplicar: "))

for num in range(10,0,-1):
  print(f'{mul} X {num} = {mul*num}')




Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- con estructuras de control con while con incrementos de 10
  2.- Sin funciones


print("\033c")
mul=int(input("Introduce el numero que quieras para crear la tabla de multiplicar: "))
num=10 
while num <= 100:
  print(f'{mul} X {num} = {mul*num}')
  num+=10




Crear un programa que calcule e imprima cualquier tabla de multiplicar

Restricciones: 
1.- con estructuras de control con while con Decrementos de 10
2.- Sin funciones

print("\033c")
mul=int(input("Introduce el numero que quieras para crear la tabla de multiplicar: "))
num=100
while num >= 10:
  print(f'{mul} X {num} = {mul*num}')
  num-=10





Crear un programa que calcule e imprima cualquier tabla de multiplicar

  Restricciones: 
  1.- Sin estructuras de control
  2.- con funciones

print("\033c")
def process():
  print(f'{mul} x 1 = {mul*1}')
  print(f'{mul} x 2 = {mul*2}')
  print(f'{mul} x 3 = {mul*3}')
  print(f'{mul} x 4 = {mul*4}')
  print(f'{mul} x 5 = {mul*5}')
  print(f'{mul} x 6 = {mul*6}')
  print(f'{mul} x 7 = {mul*7}')
  print(f'{mul} x 8 = {mul*8}')
  print(f'{mul} x 9 = {mul*9}')
  print(f'{mul} x 10 = {mul*10}')

mul=int(input("Introduce el numero que quieras para crear la tabla de multiplicar: "))
process(mul)



Crear un programa que calcule e imprima cualquier tabla de multiplicar

Restricciones:
1.- Con estructuras de control con for con decremento de 10
2.- Con funciones

print("\033c")


def generar_tabla(tabla):
    for num in range(100, 0, -10):
        print(f'{tabla} X {num} = {tabla*num}')


mul = int(input("Introduce el numero que quieras para crear la tabla de multiplicar: "))
generar_tabla(mul)
print("-----------------Tabla terminada-----------------")