def temperatura():
    #Aqui recibiria la temperatura de forma automatica al estar conectado el sensor de calor
    #Los estados del ventilador seran representados como ON = 1 y OFF = 0
    vent=0
    cal=float(input("CANTIDAD DE GRADOS: "))
    if cal>37:
        print("VENTILADOR ENCENDIDO")
        vent=vent+1
    else:
        print("VENTILADOR APANGOSE")
        vent=vent+0
#temperatura()
def humedad():
    #Se recibira la humedad de la tierra en el valor de "ml / m3" mililitros por metro cubico
    #Los tubos de riego se abriran y cerraran de forma automatica segun la situacion
    hum=float(input("Nivel de humedad en ml/m3: "))
    if hum<10:
        print("Sistema de riego activado, dispersando riego...")
    else:
        print("Sistema de riego desactivado")
humedad()
