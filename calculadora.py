from suma_resta import sumar,restar
from multiplicacion_division import multiplicar,dividir
from raizCuadrada_potencia import raizCuadrada,potencia
comenzar=input('Deseas comenzar, ¿si o no? ')
while comenzar=='si':
    operacion=input('Qué operacion desea realizar? ')
    numero1=int(input('Ingrese el primer numero '))
    numero2=int(input('Ingrese el segundo numero '))
    def calcular():
        if operacion=='+':
            print(sumar(numero1,numero2))
        elif operacion=='-':
            print(restar(numero1,numero2))
        elif operacion=='*':
            print(multiplicar(numero1,numero2))
        elif operacion=='/':
            print(dividir(numero1,numero2))
        elif operacion=='raiz':
            print(raizCuadrada(numero1))
        elif operacion=='potencia':
            print(potencia(numero1,numero2))
    calcular()