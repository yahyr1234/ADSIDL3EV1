print()
print(" === HORA DEPUES ===")
print("AUTOR: NEXUS SISTEMS")
print()
#lectura de datos
HH=int(input("Ingrese las horas (0-23)    >> "))
MM=int(input("Ingrese los minutos (0-59)  >> "))
SS=int(input("Ingrese los segundos (0-59) >> "))
N=int(input("Ingrese la cantidad de segundos a sumar (N) >> "))
#validacion
if (HH>=0 and HH<=23) and (MM>=0 and MM<=59) and (SS>=0 and SS<=59):
    #proceso
    SS=SS+N
    if (SS >= 60):
        MM = MM + (SS // 60)    #convertir segundos a minutos
        SS = SS % 60
    if (MM >= 60):
        HH = HH + (MM // 60)    #convertir minutos a horas 
        MM = MM % 60
    if (HH >= 24):
        HH = HH % 24            #adaptar la hora si pasa de 24 reinicio a 0 horas
# salida
    print()
    print(f"HORA ACTUAL ES >> {HH} : {MM} : {SS}")
    print()
else:
    print(">>> ERROR: HORA NO VALIDA <<<")
#fin
