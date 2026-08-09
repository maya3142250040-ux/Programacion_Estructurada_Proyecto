import math
print("\033c")
def proceso(radio):
    area=math.pi*math.pow(radio,2)
    return area

acum_resul=0
rep=0
list_resul=[]
resp=input("Desea iniciar?S/N ").strip().upper()
while resp == "S":
    radio=float(input("Ingrese el radio: ").strip())
    result=proceso(radio)
    print(f"El area del circulo es de {result:.2f}")
    list_resul.append(result)
    resp=input("Desea ingresar otro dato?S/N").strip().upper()
    acum_resul+=result
    rep+=1
prom=acum_resul/rep
print(f"El promedio de las areas fue de {prom}")
list_resul.sort(reverse=True)
list_resul=tuple(list_resul)
print(f"las areas registrados fueron {list_resul}")