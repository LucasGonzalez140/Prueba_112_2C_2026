cant_horas = int(input("Ingrese la cantidad de horas trabajadas: "))
valor_hora = float(input("Ingrese el valor por hora: "))

sueldo = cant_horas * valor_hora
obra_social = sueldo * 0.03
jubilacion = sueldo * 0.11
sueldo_bruto = sueldo - (obra_social + jubilacion)
bono_navideño = sueldo_bruto * 0.10
sueldo_neto = sueldo_bruto + bono_navideño

print(sueldo)
print(obra_social)
print(jubilacion)
print(bono_navideño)
print(sueldo_neto)
