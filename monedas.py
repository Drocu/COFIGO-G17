#PROGRAMA PARA CONVERTIR MONEDAS POR EL TIPO DE CAMBIO
#SOLES A DOLARES Y VICEVERSA
# ENTRADA
opcion = 0
while(opcion != 3):
    print(""" 
    =============================================
            CONVERTIDOR DE MONEDAS VERSION 1.0
    =============================================
    OPCION 1 : CONVERTIR DE SOLES A DOLARES
    OPCION 2 : CONVERTIR DE DOLARES A SOLES
    =============================================
    """)
    opcion = int(input("Ingrese una opcion segun el menu: "))
    #PROCESO
    if(opcion == 1):
        #CONVERTIR DE SOLES A DOLARES
        montoOrigen = float(input("Ingrese monto en soles: "))
        montoDestino = montoOrigen /  3.8
        monedaDestino = "dolares"
    elif(opcion == 2):
        #CONVERTIR DE DOLARES A SOLES
        montoOrigen = float(input("Ingrese monto en dolares: "))
        montoDestino = montoOrigen * 3.9
        monedaDestino = "soles"
    elif(opcion == 3):
        print("ADIOS !!!")
    else:
        print("debe ingresar una opcion valida...")

    #SALIDA
    if(opcion <= 2 and opcion >= 1):
        print(" El monto en " + monedaDestino + "es " + str(montoDestino))