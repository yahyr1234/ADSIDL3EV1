print()
print("=== COLEGIATURA ===")
print("AUTOR: NEXUS SISTEMS")
print()
#lectura de datos 
MATERIAS=int(input(" INGRESE EL NUMERO DE MATERIAS >>> "))
PROM=float(input(" INGRESE SU PROMEDIO COMO ALUMNO >>> "))
#validacion
if (MATERIAS>0 and PROM>0 and PROM<=20):
    #proceso
    if (PROM>=18):
       PAGO=round((MATERIAS*100)*0.75,2)
       print(" EL PAGO DE COLEGIATURA ES >> S/",PAGO)
    else:
       PAGO=round(MATERIAS*100,2)
       print(" EL PAGO DE COLEGIATURA ES >> S/",PAGO)
else:
   print("\n >>>ERROR:LAS MATERIAS TIENEN QUE SER MAYORES A 0 Y EL PROMEDIO MAYOR A 0 PERO MENOR A 21 <<< \n")
#fin