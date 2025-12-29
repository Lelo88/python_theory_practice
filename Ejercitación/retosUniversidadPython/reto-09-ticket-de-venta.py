# Generación de ticket de venta. 

print("Ticket de venta")
print("----------------")

precio_leche = float(input("Precio leche: "))
precio_pan = float(input("Precio pan: "))
precio_mantequilla = float(input("Precio mantequilla: "))
descuento_porcentaje = float(input("Descuento porcentaje: "))

#calculo subtotal
subtotal = precio_leche + precio_pan + precio_mantequilla

#Aplicar descuento
descuento = subtotal * (descuento_porcentaje / 100)

#subtotal_con_descuento
subtotal_con_descuento = subtotal - descuento

#calculo con impuestos
impuestos = subtotal_con_descuento * 0.19

#calculo total
print(f'Subtotal: , $ {subtotal:.2f}')
print("Descuento: ", round(descuento,2))
print("Subtotal con descuento: ", round(subtotal_con_descuento,2))
print("Impuestos: ", round(impuestos,2))
print("Total: ", round(subtotal_con_descuento + impuestos,2))

