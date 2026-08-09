print("\033c")
def proceso(altura,peso):
    imc=peso/(altura*altura)
    return imc

acum_imc=0
rep=0
list_imc=[]
resp=input("Desea iniciar?S/N").strip().upper()
while resp == "S":
    altura=float(input("Ingrese su altura: ").strip())
    peso=float(input("Ingrese su peso: ").strip())
    result=proceso(altura,peso)
    print(f"Su imc es de {result}")
    list_imc.append(result)
    list_imc=set(list_imc)
    resp=input("Desea ingresar otro dato?S/N").strip().upper()
    acum_imc+=result
    rep+=1
prom=acum_imc/rep
print(f"El promedio de los imc fue de {prom}")
print(f"los IMC registrados fueron {list_imc}")

