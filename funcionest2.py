import math
def area_circulo(radio):
    areacirculo = math.pi*(radio**2)
    return areacirculo

def volumen_cilindro(altura,radio):
    area_base = area_circulo(radio)
    volumen = area_base * altura
    return volumen

print("Vamos a calcular el area de un circulo")
radiocirculo = int(input("Introduce el radio del circulo : "))
print(f"El area de tu circulo es {area_circulo(radiocirculo)}")
alturacilindro = int(input("Introduce la altura del cilindro : "))
print(f"El volumen de tu cilindro es {volumen_cilindro(alturacilindro,radiocirculo)}")