print()
print(" ===== TRIBUTOS ===== ")
print(" AUTOR: NEXUS SISTEMS ")
print()
#lectura de datos
EDAD=int(input(" INGRESE SU EDAD >> "))
INGRESO=float(input(" INGRESE SUS INGRESOS MENSUALES >> S/"))
#validacion
if (EDAD>0 and INGRESO>0):
   #proceso
   if(EDAD>=18 and INGRESO>=3000):
       IMPUESTO=round((INGRESO*0.05),2)
       print("EL IMPUESTO ES >> S/",IMPUESTO)
       print(" >>> TRIBUTAR <<< ")
   else:
       print(" >>> NO TRIBUTAR <<< ")
else:
    print("\n >>> ERROR: LA EDAD Y LOS INGRESOS DEBEN SER POSITIVOS <<< \n")
#fin