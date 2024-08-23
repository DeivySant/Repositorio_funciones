#Escribri una funcio que calcule el valor de una factura tras alicarle el valor del iva
def calcular_factura(valor,iva=21):
    total = valor + valor*(iva/100)
    return total

con_sin_iva = input("Ingrese 'SI' o 'NO' desea calcular la factura con iva: ").lower()
if con_sin_iva == "si" :
    try:
        valor = float(input("Por favor ingrese el valor de la factura : "))
        iva = int(input("Por favor ingrese el valor del iva : "))
        print(f"El valor total de la factura es {calcular_factura(valor,iva)}")
    except Exception as e:
        print("Valores no validos",e)

elif con_sin_iva == "no":
    try:
        valor = float(input("Por favor ingrese el valor de la factura : "))
        print(f"El valor total de la factura es {calcular_factura(valor)}")
    except Exception as e:
        print("Valores no validos", e)

else :
    print("Opcion no valida")