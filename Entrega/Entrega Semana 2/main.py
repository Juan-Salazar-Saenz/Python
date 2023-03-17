import Modulos.rambom as MD
import Modulos.robot as ROBOT
import Modulos.palindromos as Palindromo
import Modulos.funciones as FUNCIONES

def ejericio1():
    while True:
        try:
            posibles = ['C', 'S']
            x = input("Digite la opcion : ")
            if x in (posibles):
                y = int(input('Cantidad de veces : '))
                print("Cantidad de veces encontradas : ", MD.imprimir(x, y))
            else:
                print('valor incorrecto')
        except:
            break


def ejericio2():
    while True:
        try:
            y = int(input('Cantidad de veces : '))
            MD.imprimir2(y)
        except:
            break


def ejercicio3():
    while True:
        try:
            x = int(input("Digite la cantidad de filas : "))
            y = int(input("Digite la cantidad de columnas : "))
            ROBOT.crearMatrix(x, y)
            ROBOT.imprimirmatris()
            ROBOT.pedir()
            ROBOT.ponerasterisco(x, y)
            ROBOT.imprimirmatris()
            ROBOT.quitarasterisco(x, y)
            while True:
                try:
                    print("Selecciona un movimiento")
                    print("Derecha")
                    print("Izquierda")
                    print("Arriba")
                    print("Abajo")
                    print("")
                    m = input("")
                    if m in (ROBOT.movimientos):
                        ROBOT.moverse(m, x, y)
                        ROBOT.ponerasterisco(x, y)
                        ROBOT.imprimirmatris()
                        ROBOT.quitarasterisco(x, y)
                    else:
                        print("¡seleccion incorrecta !")
                except:
                    break
        except:
            break


def ejercicio4():
    while True:
        try:
            x = (input("Digite la palabra "))
            print ("la palabra es palindromo ",Palindromo.f(x))
        except:
            break

while True:
    try:
        posibles = ['1', '2', '3', '4', '5', '6', '7']
        print('Ejercicios')
        print('1: Cara o sello')
        print('2: Doble cara o Doble sello')
        print('3: Robot')
        print('4: Palindromo')
        print('5: Binomial')
        print('6: Poisson')
        print('7: Gaussiana')
        print(' ')
        x = input("Digite el ejericio a probar : ")
        if x in (posibles):
            if x == "1":
                print(' ')
                print(' ###Construya una  función cuyas entradas sean: ')
                print(
                    '1. Una lista con los posibles resultados de lanzar una moneda. Por ejemplo ["C","S"]')
                print('2. Un número de lanzamientos. ')
                print(' ')
                print('La función debe lanzar la moneda N veces, y al final la salida debería mostrar la fracción de caras y la fracción de sellos. ')
                print(' ')
                print('¿Qué pasa si lanza la moneda 20, 50, 100, 500 o 1000 veces?')
                print(' ')
                ejericio1()
            elif x == "2":
                print(' ')
                print(
                    'Repita el ejercicio anterior, pero esta vez, para cada uno de los valores de N, lance la moneda dos veces, y agrupe los resultados en una lista tipo ["CS","CC",...].')
                print('Al final de la rutina diga la fracción de cada resultado')
                print(' ')
                ejericio2()
            elif x == "3":
                print(' ')
                print('Imagine que tiene una cuadrícula de 3x3 donde cada cuadrado está marcado de la forma:')
                print(' ')
                print('0 1 2 ')
                print(' ')
                print('3 4 5 ')
                print(' ')
                print('6 7 8 ')
                print(' ')
                print('En cada cuadro, es posible moverse al azar a la izquierda, derecha, arriba o abajo. La regla es que si está en el extremo izquierdo, no puede moverse a la izquierda; si está arriba, no puede moverse hacia arriba, etc. ')
                print(' ')
                print('Por ejemplo, si está en 4, los posibles movimientos serían [5,1,3,7]; si está en 1, los psoibles movimientos serían [2,1,0,4], etc.')
                print(' ')
                print('Construya una rutina que muestre: ')
                print('1. Una lista de listas (o un diccionario) que muestre los posibles movimientos desde cada baldosa en el orden (derecha, arriba, izquierda, abajo). ')
                print('2. Elija un número N de movimientos.')
                print('3. Párese en una baldosa al azar. ')
                print('4. A partir de esa baldosa, muévase al azar en una dirección dada. ')
                print('5. Repita eso N veces.')
                print(' ')
                print('Al final, cuente cuántas veces pasó por cada baldosa.')
                print(' ')
                ejercicio3()
            elif x == "4":
                print(' ')
                print('Palabras palindromas')
                print(' ')
                print('"in girum imus nocte et consumimur igni", "Atar a la rata","¿Acaso hubo búhos acá?"","¿Son robos o sobornos?"","A ti no, bonita."')
                ejercicio4()
            elif x == "5":
                print(' ')
                print('**Funcion Binomial 2**')
                print('En esta función, n, p y k son los tres argumentos de la función, que representan el número de ensayos, la probabilidad de éxito en cada ensayo y el número de éxitos, respectivamente.')
                print('La función factorial() es una implementación propia de la función factorial. Esta función utiliza la recursividad para calcular el factorial de un número dado.')
                print('A continuación, la función utiliza la fórmula de la distribución binomial para calcular la probabilidad de k éxitos dados n ensayos y una probabilidad de éxito p. La fórmula incluye el cálculo del término binomial, la probabilidad de éxito y la probabilidad de fracaso.')
                print(' ')
                n = 10
                p = 0.5
                k = 5
                resultado = FUNCIONES.binomial(n, p, k)
                print(resultado) # output: 0.24609375
            elif x == "6":
                print(' ')
                print('**Funcion Poisson,**')
                print('En esta función, lam y k son los dos argumentos de la función, que representan el parámetro de la distribución Poisson y el número de eventos, respectivamente.')
                print('La función utiliza la constante matemática e (aproximadamente igual a 2.718) para calcular la función exponencial. A continuación, la función utiliza la fórmula de la distribución Poisson para calcular la probabilidad de que ocurran k eventos dados un parámetro de lam. La fórmula incluye el cálculo del factorial de k.')
                print(' ')
                lam = 2
                k = 3
                resultado = FUNCIONES.poisson(lam, k)
                print(resultado) 
            elif x == "7":
                print(' ')
                print('**Funcion Gaussiana,** ')
                print('En esta función, x, mu y sigma son los tres argumentos de la función, que representan el valor de la variable, la media y la desviación estándar de la distribución Gaussiana, respectivamente. ')
                print('La función utiliza la constante matemática pi (aproximadamente igual a 3.14159) para calcular la función de densidad de probabilidad Gaussiana. A continuación, la función utiliza la fórmula de la distribución Gaussiana para calcular la probabilidad de que x sea igual a un valor dado dado una media mu y una desviación estándar sigma. La fórmula incluye el cálculo de la exponencial y la raíz cuadrada. ')
                print(' ')
                x = 1
                mu = 0
                sigma = 1
                resultado = FUNCIONES.gaussiana(x, mu, sigma)
                print(resultado) 

        else:
            print('valor incorrecto')
    except:
        break
