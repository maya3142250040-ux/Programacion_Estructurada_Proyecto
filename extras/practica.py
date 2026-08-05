
def proceso(celcius):
    faren=(celcius*9/5)+32
    return faren

acum_faren=0
rep=0
resp=input("Desea realizar el proceso?S/N\n").upper().strip()
while resp=="S":
    celcius=float(input("Ingrese los celcius: "))
    result=proceso(celcius)
    print(f"{celcius} celcius a faren es {result}")
    resp=input("Deseas ingresar nuevos datos?S/N\n").upper().strip()
    rep+=1
    acum_faren+=result
prom=acum_faren/rep
print(f"El promedio de las operaciones fue de {prom}")

#---------------------------------------------------------------------

def proceso(kilom,litros):
	rend=kilom/litros
	return rend

acum_rend=0
rep=0
resp=input("Desea iniciar?S/N").upper().strip()
while resp =="S":
	kilom=float(input("Ingrese los kilómetros recorridos: "))
	litros=float(input("Ingrese los litros de gasolina usados: "))
	result=proceso(kilom,litros)
	print(f"El rendimiento fue de {result:.2}")
	resp=input("Desea ingresar otro dato?S/N ").upper().strip()
	rep+=1
	acum_rend+=result
prom=acum_rend/rep
print(f"El promedio de las operaciones fue de {prom}")
#---------------------------------------------------------------------
print("\033c")
def proceso(examen,tareas):
	cali_f=(examen*.70)+(tareas*0.30)
	return cali_f

acum_cal=0
rep=0
list_cali=[]
resp=input("Desea iniciar?S/N\n").strip().upper()
while resp=="S":
	examen=float(input("Ingrese su calificacion del examen: "))
	tareas=float(input("Ingrese la calificación de sus tareas: "))
	result=proceso(examen,tareas)
	print(f"Su calificación final es de {result}")
	list_cali.append(result)
	resp=input("Desea ingresar nuevos datos?S/N\n").strip().upper()
	rep+=1
	acum_cal+=result
prom=acum_cal/rep
print(f"El promedio de los resultados es de {prom}")
list_cali.sort()
list_cali.reverse()
print(f"Los promedios fueron {list_cali}")
#---------------------------------------------------------------------
print("\033c")
def proceso(masa,velo):
	energia_cine=(masa*(velo **2))/2
	return energia_cine

acum_ener=0
rep=0
list_ener=[]
true=True
while true:
	masa=float(input("ingrese la masa: "))
	velo=float(input("ingrese velocidad: "))
	result=proceso(masa,velo)
	print(f"la energía cinetica es de {result}")
	list_ener.append(result)
	resp=input("Desea ingresar otro dato?S/N").strip().upper()
	if resp == "N":
		true=False
	acum_ener+=result
	rep+=1
prom=acum_ener/rep
print(f"El promedio de los resultados es de {prom}")
list_ener.sort()
list_ener.reverse()
print(f"Los promedios fueron {list_ener}")
	