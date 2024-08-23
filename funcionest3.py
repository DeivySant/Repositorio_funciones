def sumalista(lista) :
    sumatoria = 0
    longitud = len(lista)
    for i in lista :
        sumatoria += i
    media = sumatoria/longitud
    return media

lista = [1,2,3,4,5,7,6]

print(f"La media de la lista es : {sumalista(lista)}")