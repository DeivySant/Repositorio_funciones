def cuadradolista(lista) :
    listan = []
    for i in lista :
        cuadrado = i**2
        listan.append(cuadrado)
    return listan


lista = [1,2,3,4,5,7,6]

print(f"El cuadrado de su lista es {cuadradolista(lista)}")