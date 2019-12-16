

def suma(numUno,numDos):
    print(numUno+numDos)
def resta(numUno, numDos):
    print(numUno-numDos)
def Multiplicacion(numUno, numDos):
    print(numUno*numDos)
def division(numUno, numDos):
    print(numUno/numDos)
def exponente(numUno, numDos):
    print(pow(numUno, numDos))
def raiz(numUno, numDos):
    print(pow(numUno, 1/numDos))

while True:
    operacion = input("¿Qué operación quieres? ")
    if operacion=='suma' or operacion=="+":
        numUno = float(input("Ingresa un número: "))
        numDos = float(input("Ingresa otro número: "))
        suma(numUno, numDos)
    elif operacion=='resta' or operacion=="-":
        numUno = float(input("Ingresa un número: "))
        numDos = float(input("Ingresa otro número: "))
        resta(numUno, numDos)
    elif operacion=='Multiplicación' or operacion=="x":
        numUno = float(input("Ingresa un número: "))
        numDos = float(input("Ingresa otro número: "))
        Multiplicacion(numUno, numDos)
    elif operacion=='division' or operacion=="/":
        numUno = float(input("Ingresa un número: "))
        numDos = float(input("Ingresa otro número: "))
        division(numUno, numDos)

    elif operacion=='exponente':
        numUno = float(input("Ingresa el valor de la base: "))
        numDos = float(input("Ingresa el valor del exponente: "))
        exponente(numUno, numDos)
    elif operacion =='raiz':
        numUno = float(input("Ingresa el valor de la base: "))
        numDos = float(input("Ingresa el valor de la raiz: "))
        raiz(numUno, numDos)
    else:
        print('OK:V, la cagaste, tú')
