"""
print("\033c")
respuesta="si"
num_trabajadores=0
acum_sueldos=0

while respuesta=="si":
    nombre=input("ingrese el nombre del trabajador: ")
    num_horas=int(input("ingrese el numero de horas trabajadas: "))
    sueldo=int(input("ingrese el sueldo: "))
    
    if num_horas==10:
        aumento=20
    elif num_horas==15:
        aumento=30
    elif num_horas==20:
        aumento=15
    elif num_horas>=25:
        aumento=8
    respuesta=input("¿desea realizar otro registro SI/NO?")

    num_trabajadores+=1
    acum_sueldos+=1
    sueldo_neto=sueldo*acum_sueldos
    sueldo_hora=sueldo+sueldo*aumento


print(f"el sueldo a pagar es de: {sueldo_hora}")
print(f"el numero de trabajadores ingresados es de: {num_trabajadores}")
print(f"el sueldo neto es de: {sueldo_neto}")
"""

def sueldoTrabajadores(horas_trab,sueldo):
    sueldo_base=sueldo*horas_trab   
    return sueldo_base


print("\033c")
trabajadores=0
acum_sueldo_neto=0
opc="S"
while opc=="S":
    nombre=input("Nombre: ")
    horas_trab=int(input("Horas trabajadas: "))
    sueldo=float(input("Sueldo por Horas trabajadas: "))
    aumento=0
    sueldo_base=sueldoTrabajadores(horas_trab,sueldo)

    if horas_trab==10:
        aumento=0.20
    elif horas_trab==15:
        aumento=0.30
    elif horas_trab==20:
        aumento=0.15
    elif horas_trab>25:
        aumento=0.08
        
    aumento_pagar=aumento*sueldo_base
    suel_neto=sueldo_base+aumento_pagar
    
    trabajadores+=1
    acum_sueldo_neto+=suel_neto
    
    print(f"El aumento es: {aumento_pagar}\n Y el sueldo neto cobrado es: {suel_neto}")
    
    opc=input("¿Desea ingresar mas trabajadores (S/N)").upper().strip()
print(f"El total de trabajadores es: {trabajadores}\nY monto total del sueldo neto cobrado es: {acum_sueldo_neto}")