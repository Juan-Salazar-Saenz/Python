movimientos = ['Arriba', 'Abajo', 'Derecha', 'Izquierda']
matris = []
posicion = 0
maximo = 0
asterisco = 0
asteriscoX = 0
asteriscoY = 0


def crearMatrix(x, y):
    global maximo
    n = 0
    for i in range(x):
        filas = []
        for j in range(y):
            filas.append(n)
            n += 1
        matris.append((filas))        
    maximo = n - 1


def imprimirmatris():
    print("")
    for i in (matris):
        print(i)
    print("")


def pedir():
    global posicion
    global maximo
    print("maximo -->  ", maximo)
    numero = maximo + 1
    while numero > maximo:
        numero = int(input("posicion inicial : "))
        if numero > maximo:
            print("¡intente de nuevo!")
    print("")
    posicion = numero


def ponerasterisco(x, y):
    global asteriscoY
    global asteriscoX
    for i in range(x):
        for j in range(y):
            if posicion == matris[i][j]:
                matris[i][j] = "*"
                asteriscoX = int(i)
                asteriscoY = int(j)
                break
        if posicion == matris[i][j]:
            break


def quitarasterisco(x, y):
    for i in range(x):
        for j in range(y):
            if "*" == matris[i][j]:
                matris[i][j] = posicion
                break
        if "*" == matris[i][j]:
            break


def moverse(mover, x, y):
    global posicion
    global asteriscoY
    global asteriscoX
    if mover == "Derecha":
        if (asteriscoY+1) >= y:
            print("No se puede correr a la Derecha")
        else:
            posicion += 1
            print("Se movio a la Derecha")
    elif mover == "Izquierda":
        if (asteriscoY - 1) < 0:
            print("No se puede correr a la Izquierda")
        else:
            posicion -= 1
            print("Se movio a la Izquierda")
    elif mover == "Arriba":
        if (asteriscoX-1) < 0:
            print("No se puede correr hacia Arriba")
        else:
            posicion -= y
            print("Se movio hacia Arriba")
    elif mover == "Abajo":
        if (asteriscoX+1) >= x:
            print("No se puede correr hacia Abajo")
        else:
            posicion += y
            print("Se movio hacia Abajo")
