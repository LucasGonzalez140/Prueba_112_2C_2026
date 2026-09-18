cargo_fijo = 7000
costo_m3 = 200

tipo_cliente = input("Ingrese el tipo de cliente (residencial, comercial, industrial): ").lower()
consumo_m3 = int(input("Ingrese el consumo en m3: "))
impuesto_iva = 0.21
bonificacion = 0
recarga = 0
descuento = 0
costo_consumo = consumo_m3 * costo_m3

if tipo_cliente == "residencial":
    if consumo_m3 <= 30:
        bonificacion += 0.10
    elif consumo_m3 > 80:
        recarga += 0.15

if tipo_cliente == "residencial" and costo_consumo < 35000:
    descuento += 0.05
    

if tipo_cliente == "comercial":
    if consumo_m3 > 300:
        bonificacion += 0.12
    elif consumo_m3 > 150:
        recarga += 0.08
    elif consumo_m3 < 50:
        recarga += 0.05

if tipo_cliente == "industrial":
    if consumo_m3 > 1000:
        bonificacion += 0.30
    elif consumo_m3 > 500:
        bonificacion += 0.20
    elif consumo_m3 < 200:
        recarga += 0.10

subtotal_costo = cargo_fijo + costo_consumo - (costo_consumo * descuento)
costo_final = subtotal_costo + (costo_consumo * recarga) - (costo_consumo * bonificacion)
total_costo = costo_final + (costo_final * impuesto_iva)    

print(f"Descuento aplicado: {descuento * 100:.2f}%") if descuento > 0 else print("No se aplicó descuento.")
print(f"El costo subtotal del servicio es: {subtotal_costo:.2f} pesos")
print(f"Bonificación aplicada: {bonificacion * 100:.2f}%") if bonificacion > 0 else print("No se aplicó bonificación.")
print(f"Recarga aplicada: {recarga * 100:.2f}%") if recarga > 0 else print("No se aplicó recarga.")
print(f"El costo final del servicio es: {costo_final:.2f} pesos")
print(f"Total a pagar: {total_costo:.2f} pesos (IVA incluido)")








