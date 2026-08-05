def borrarPantalla():
    print("\033c")

def ventaAutos(resp,autos,acum_pv):
    borrarPantalla()
    while resp=="S":

        marca=input("ingrese la marca del carro: ").strip().upper()
        orig=input("origen del carro: ").strip().upper()
        costo=float(input("ingrese el costo: "))

        if orig == "ALEMAN":
            impuest = .20
        elif orig == "JAPON":
            impuest= .30
        elif orig == "ITALIA":
            impuest = .15
        elif orig == "USA":
            impuest=.08
        else:
            impuest=0

        impuesto_pesos=costo*impuest
        pv=impuest+costo

        print(f'El impuesto a pagar es: {impuesto_pesos}')
        print(f'El precio de venta es: {pv}')
        autos+=1
        acum_pv+=pv
        resp=input("Desea realizar otra vez el proceso?S/N\n").strip().upper()
    return autos,acum_pv

autos=0
acum_pv=0
resp="S"
tot_autos,acum_precios=ventaAutos(resp,autos,acum_pv)
print(f'Vehiculos ingresados: {tot_autos}\nEl monto total de los precios de venta es: ${acum_precios}')
