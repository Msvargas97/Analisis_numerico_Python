# -*- coding: utf-8 -*-
#Codigo creado por Michael Vargas
#Para resolver ecuaciones lineales usando Jacobi o Gauss-Seidel
#-07/05/2016

#Importar Librerias
from math import *
from pylab import *
import numpy as np
import matplotlib.pyplot as plt

#Declaracion de variables globales
global A,b,oldx,newx,tol,size,iteraciones
#Ejemplo
# Matriz  : -5 1 -2;2 -6 1;1 2 7
#Terminos independiente: -12 11 13
#inicial 0 0 0
def metodo_jacobi():
    global A,b,oldx,newx,tol,size,iteraciones
    #Metodo de Jacobi
    #Inicializar Variables
    for i in range(size):
        b[i] =float(b[i] / A[i][i])
        newx[i] = oldx[i]
        for j in range(size):
            if j != i:
                A[i][j] = float(A[i][j] / A[i][i])
    #print(A)
    finish = False
    Flag = False
    error = 0
    while finish == False:
        iteraciones = iteraciones + 1
        text = str(iteraciones)
        if iteraciones < 10:
            text = text + ("    ")
        else:
            text = text + ("   ")
        for i in range(size):
            oldx[i] = newx[i]
            newx[i] = b[i]
        #Activa la bandera para determinar si el resultado esta por debajo de la tolerancia
        Flag = True
        for i in range(size):
            for j in range(size):
                if j != i:
                    newx[i] =  float(newx[i] - (A[i][j]*oldx[j]))
                    #Si el error es mayor en cualquiera de los errores se sigue iterando
            error = abs(newx[i]-oldx[i])
            if(error > tol ):
                Flag = False
        finish = Flag
        for i in range(size):
            text = text + "    "+(str("{0:.6f}".format(newx[i])))
       #text = text +"    " +(str("{0:.4f}".format(error)))
        print(text)
def metodo_seidel():
    global A,b,oldx,newx,tol,size,iteraciones
    #Inicializacion de variables
    for i in range(size):
        b[i] = b[i] / A[i][i]
        newx[i] = oldx[i]
        oldx[i] = 0
        for j in range(size):
            if i != j:
                A[i][j] = A[i][j]/A[i][i]
    finish = False
    Flag = False
    error = 0
    while finish == False:
        iteraciones = iteraciones + 1
        text = str(iteraciones)
        if iteraciones < 10:
            text = text + ("    ")
        else:
            text = text + ("   ")
        for i in range(size):
            newx[i] = b[i]
            for j in range(size):
                if i != j:
                    newx[i] = float(newx[i] - (A[i][j]*newx[j]))
        Flag = True
        for i in range(size):
            text = text + "    "+(str("{0:.6f}".format(newx[i])))
        print(text)
        for i in range(size):
            error = float(abs(newx[i]-oldx[i]))
            oldx[i] = newx[i]
#            print(error)
            if(error > tol):
                Flag = False
        finish = Flag


#Funcion para convertir la matriz ingresada en una lista
def stringTolist(A):
    sizeCol = 0
    rowA =[]
    colA = A.split(';')
    sizeCol = len(colA);
    for i in range(sizeCol):
        rowA.append(colA[i].split(' '))
    sizeRow=len(rowA[0])
    #print("Matrix de ",sizeCol,"x",sizeRow)
    if(sizeRow == sizeCol):
        return rowA,sizeRow
    else:
        return "La matriz no es de nxn"

#Codigo Principal
print("###############################################################################")
print("#                 Metodos iterativos:Jacobi y Gauss-Seidel                    #")
print("#                   Código Elaborado por Michael Vargas                       #")
print("#                Ingenieria Electrónica - Análisis Númerico                   #")
print("#                                 UDI 2016                                    #")
print("###############################################################################\n")
print("PARA INGRESAR UNA MATRIZ LAS FILAS SE SEPARAN POR UN ';' Ej: 1 2 3; 4 5 6; 7 8 9                   ")
A = str(input("Ingrese la matriz de coeficientes->"))
A,size = stringTolist(A)
#Si la matriz ingresada tiene el tamaño correcto de nxn
if(isinstance(A,list)):
    A = np.array(A,'float')
    print(A)
    #print(type(A))
    matrizDominante = True
    for i in range(size):
        suma = 0
        for j in range(size):
            if(i != j):
                suma = suma + abs(A[i][j])
        if(abs(A[i][i]) < suma):
             matrizDominante = False
    if matrizDominante == False:
        print("ADVERTENCIA:La matriz NO es diagonalmente dominante")
    #Vector con terminos independientes
    b = str(input("Ingrese el vector de terminos independientes->"))
    #Separar los valores del vector y guardarlo como lista
    b = b.split(' ')
    b = np.array(b,'float')
    print(b)
    #Crea el vector incial
    oldz = 0;
    oldx = str(input("Ingrese el vector con las estimaciones iniciales->"))
    oldx = oldx.split(' ')
    oldx = np.array(oldx,'float')
    print(oldx)
    #Crea un vector de tamaño
    newx = [0]*size;
    newx = np.array(newx,'float')
    tol = float(input("Tolerancia->"))
    iteraciones = 0
    metodo =  {'1':metodo_jacobi,'2':metodo_seidel}
    op = 0
    print("1.Metodo de Jacobi\n2.Metodo de Gauss-Seidel")
    while op==0:
        try:
            op = input("Selecione un metodo->")
            if op >= '1' and op <= '2':
                print("###############################################################################")
                text = "No   "
                for i in range(size):
                    text = text + "       x"+(str(i+1))+"    "
                    #text = text + "   Error"
                print(text)
                metodo[op]()
        except:
            op = 0
            print("Opcion no válida")
    print("###############################################################################")
    print("\nEl sistema converge con",iteraciones,"iteraciones, con una tolerancia de ",tol)
    print("Vector Solución->",newx)
    text = " "
    for i in range(size):
        text = 'x' + str(i+1)
        print(text,"->",newx[i])
else:
    print(A)






