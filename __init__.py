# -*- coding: utf-8 -*-
#/*****************************************************\
#Codigo para resolver raices
#Elaborado por: Michael Vargas
#25/03/2016'
#/********************************************?********\

#importar librerias
from math import *
from pylab import *
#Crea variables globales
global a,b,c,fun,dfun
a=0
b=0
#crear funcion para realizar el metodo de biseccion
def metodo_biseccion(f,a,b,tol):
    c=0
    error = (tol+0.01)
    i=0
   # print("#\ta\tb\tc")
    if f(a)*f(b) < 0:
        print("   a     b      c        Fa      Fb     Fc     E")
        while error > tol:
            i=i+1
            c = (a+b)/2
            error=abs(f(c))
            print("{0:.4f}".format(a)," |{0:.4f}".format(b)," |{0:.4f}".format(c)," |{0:.4f}".format(f(a))," |{0:.4f}".format(f(b))," |{0:.4f}".format(f(c))," |{0:.4f}".format(error))
            if f(a)*f(c)<0:
                 b = c
            else:
                a = c
            raiz=c
    else:
        raiz="No hay cambio de signo, ingrese otros intervalos"
    return (raiz)
#Funcion para metodo de la secante
def metodo_secante(f,a,b,tol):
    error = (tol+0.01)
    c=0
    aux=0
    if abs(f(a)) < abs(f(b)):
        print("Se intercambiaron las variables")
        aux = a
        a = b
        b = aux
    print("\n")
    while error > tol:
        c = b - f(b)*((a-b) / (f(a)-f(b)))
        a = b
        b = c
        error = abs(f(c))
        print("{0:.4f}".format(a)," |{0:.4f}".format(b)," |{0:.4f}".format(c)," |{0:.4f}".format(f(a))," |{0:.4f}".format(f(b))," |{0:.4f}".format(f(c))," |{0:.4f}".format(error))

    raiz = c
    return (raiz)
#Funcion para metodo de Newton Rapshon
def metodo_newton(f,df,a,tol):
    if f(a) != 0 and df(a) != 0 :
        x1=0
        error=tol+0.01
        raiz=0
        while error > tol:
            x1=a
            a = a - (f(a) / df(a))
            error = abs(f(x1))
        raiz = x1
    else:
        raiz = "No converge"
    return (raiz)
#evaluar la funcion
def f(x):
    return eval(fun)
#evaluar derivada de la funcion
def df(x):
    return eval(dfun)
#Intervalos para el metodo de biseccion
def intervalos1():
    global a,b
    a=float(input("Ingrese el intervalo a: "))
    b=float(input("Ingrese el intervalo b: "))
def intervalos2():
    global a,b
    a=float(input("Ingrese el intervalo x0: "))
    b=float(input("Ingrese el intervalo x1: "))
def intervalos3():
    global dfun,a
    dfun = input("Ingrese la derivada de la funcion:")
    a=float(input("Ingrese el intervalo x0: "))

#Crea diccionario para asignar los intevarlos
intervalos = {'1':intervalos1,'2':intervalos2,'3':intervalos3}
#PROGRAMA PRINCIPAL
#Ingresar intervalos
try:
    fun=input("Ingrese la funcion:")
    tol=float(input("Tolerancia: "))
    print("Escoger un metodo")
    print("\n1.Metodo de biseccion")
    print("2.Metodo de la secante")
    print("3.Metodo de Newton")
    option=input("->")
    intervalos[option]()
except:
    print("Opcion no valida")

raiz=0
x0=a
x1=b
if option=='1':
    raiz=metodo_biseccion(f,a,b,tol)
elif option=='2':
    raiz=metodo_secante(f,a,b,tol)
elif option=='3':
    x0 = a
    x1 = a+4
    raiz = metodo_newton(f,df,a,tol)
#Solucipn
if isinstance(raiz,(int,long,float,complex)):
    print("La raiz encontrada con tolerancia",tol," es:\n ",raiz)
    #crea la grafica
    x=arange(a-5,b+5,tol*10)
    y=eval(fun)
    plot(x,y,'b-',raiz,f(raiz),'r:o')
    title(fun)
    xlabel('x')
    ylabel('y')
    text(raiz,f(raiz),' Raiz')
    grid(True)
    show()
else:
    print(raiz)
