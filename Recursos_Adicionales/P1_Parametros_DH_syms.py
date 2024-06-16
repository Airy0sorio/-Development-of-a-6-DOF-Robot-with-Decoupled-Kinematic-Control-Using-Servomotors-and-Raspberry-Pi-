##Programa para obtener la MTH de un robot de n GDL
##Creado por:Mario Airy Hernandez Osorio
##UAQ2023-1, Robotica, Dr.Gerardo Perez Soto
##valor son los parametros de D-H vercion syms
from sympy import symbols, cos, sin, Matrix, simplify, pi

# # Definir símbolos
# t_1s, t_2s, t_3s,t_4s = symbols('th1 th2 th3 th4')
# d_1s,a_1s, a_2s,d_4s  =   symbols('l1 l2 l3 l4')
# # Definir matrices simbólicas
# alfa_1s =pi/2
# A_1s = Matrix([[cos(t_1s), -sin(t_1s)*cos(alfa_1s), sin(t_1s)*sin(alfa_1s), a_1s*cos(t_1s)],
#                [sin(t_1s), cos(t_1s)*cos(alfa_1s), -cos(t_1s)*sin(alfa_1s), a_1s*sin(t_1s)],
#                [0, sin(alfa_1s), 0*cos(alfa_1s), d_1s],
#                [0, 0, 0, 1]])

# d_2s, alfa_2s = 0, 0
# A_2s = Matrix([[cos(t_2s), -sin(t_2s)*cos(alfa_2s), sin(t_2s)*sin(alfa_2s), a_2s*cos(t_2s)],
#                [sin(t_2s), cos(t_2s)*cos(alfa_2s), -cos(t_2s)*sin(alfa_2s), a_2s*sin(t_2s)],
#                [0, sin(alfa_2s), 0*cos(alfa_2s), d_2s],
#                [0, 0, 0, 1]])

# d_3s, alfa_3s,a_3s = 0,0,pi/2
# A_3s = Matrix([[cos(t_3s), -sin(t_3s)*cos(alfa_3s), sin(t_3s)*sin(alfa_3s), a_3s*cos(t_3s)],
#                [sin(t_3s), cos(t_3s)*cos(alfa_3s), -cos(t_3s)*sin(alfa_3s), a_3s*sin(t_3s)],
#                [0, sin(alfa_3s), cos(alfa_3s), d_3s],
#                [0, 0, 0, 1]])

# a_4s, alfa_4s = 0,-pi/2
# A_4s = Matrix([[cos(t_4s), -sin(t_4s)*cos(alfa_4s), sin(t_4s)*sin(alfa_4s), a_4s*cos(t_4s)],
#                [sin(t_4s), cos(t_4s)*cos(alfa_4s), -cos(t_4s)*sin(alfa_4s), a_4s*sin(t_4s)],
#                [0, sin(alfa_4s), cos(alfa_4s), d_4s],
#                [0, 0, 0, 1]])

# #------------------------------------------------------------------------------------------------------------#
# ##descomentar si quieres ver las matrices de cada articulacion
# A_01=A_1s
# A_12=A_2s
# A_23=A_3s
# A_34=A_4s
# # A_45=A_5s
# # A_56=A_6s
# #------------------------------------------------------------------------------------------------------------#

# # Multiplicar las matrices
# A0_4 = simplify(A_1s * A_2s*A_3s*A_4s)

# # Imprimir la matriz con espacios al final de cada línea
# print("\nLa matriz simbolica es:\n")
# for i in range(A0_4.shape[0]):
#     print('[', end='')  # Inicio de la línea
#     for j in range(A0_4.shape[1]):
#         print(A0_4[i, j], end="")  # Elemento de la matriz
#         if j < A0_4.shape[1] - 1:
#             print("  |  ", end="")  # Separador entre términos
#     print(']')  # Fin de la línea

# print("\nEl vector posicion MTH0_4 es ")

# elemento_31 = A0_4[0, 3]  
# elemento_32 = A0_4[1, 3]  
# elemento_33 = A0_4[2, 3]  

# # Imprimir los elementos obtenidos
# print("Px: ", elemento_31)
# print("Py: ", elemento_32)
# print("Pz: ", elemento_33)

# print("\nLa matriz de Rotacion es:\n")
# # Obtener la submatriz 3x3
# R3_6 = A0_4.extract(range(3), range(3))
# for i in range(R3_6.shape[0]):
#     print('[', end='')  # Inicio de la línea
#     for j in range(R3_6.shape[1]):
#         print(R3_6[i, j], end="")  # Elemento de la matriz
#         if j < R3_6.shape[1] - 1:
#             print("  |  ", end="")  # Separador entre términos
#     print(']')  # Fin de la línea
# print("\n")
#-----------------------------------------------------------------------------#

##Intento de Version optimizada
from sympy import symbols, cos, sin, Matrix, simplify, pi
import os
import numpy as np
def clear_console():
    #para windows
        _ = os.system('cls')
clear_console()
# Definir símbolos
thetas = symbols('th1 th2 th3 th4 th5 th6')
lengths = symbols('l1 l2 l3 l4 l5 l6 l7 l8 l9 l10')

# Definición de parámetros de articulaciones (t, d, a, alfa) para cada articulación
DH = [
    {"t": thetas[0], "d": lengths[0], "a": 0, "alfa":pi/2},
    {"t": thetas[1], "d": 0, "a": lengths[1], "alfa":0},
    {"t": thetas[2], "d": 0, "a": 0, "alfa":pi/2},
    {"t": thetas[3], "d": lengths[2], "a": 0, "alfa": -pi/2},
    #{"t": thetas[3], "d": lengths[3], "a": 0, "alfa": -pi/2}
]
i=1
# Definir matrices simbólicas
As = []
for i in range(len(DH)):
    dh_params = DH[i]
    t, d, a, alfa = dh_params['t'], dh_params['d'], dh_params['a'], dh_params['alfa']
    A = Matrix([
        [cos(t), -sin(t)*cos(alfa), sin(t)*sin(alfa), a*cos(t)],
        [sin(t), cos(t)*cos(alfa), -cos(t)*sin(alfa), a*sin(t)],
        [0, sin(alfa), cos(alfa), d],
        [0, 0, 0, 1]
    ])
    As.append(A)

# Multiplicar las matrices
A0_n = simplify(As[0])
for i in range(1, len(As)):
    A0_n = A0_n * As[i]

print("Bienvenido\nEl programa te entregara los siguientes resultados del Robot de n GDL\n")
print("1. Parametros de DH ingresados\n2. La MTH simbolica\n3. El vector Posicion P:\n4. La matriz de rotacion R: ")
print("\n-----------------------------------------------------------------------\n")
print("1. Parametros de DH")

# Imprimir la cabecera
print(f"{'art':<5} | {'thi':<10} | {'d i':<10} | {'ai':<10} | {'alfai':<10} |")
print("-" * 60)

# Imprimir tabla de valores
i = 1
for item in DH:
    print(f"{i:<5} | {str(item['t']):<10} | {str(item['d']):<10} | {str(item['a']):<10} | {str(item['alfa']):<10} |")
    i += 1


print("\n-----------------------------------------------------------------------")

#matrices de tranformacion homogenia una a una
print("\n2. MTH de cada articulación\n")
i = 0
for A in As:
    print(f"MTH_{i + 1}:")
    print(np.array(A.tolist()),"\n")
    i += 1
print("\n-----------------------------------------------------------------------")
A0_n=simplify(A0_n)
print("3. La matriz simbolica es:\n",f"MTH0_{i}:")
for i in range(A0_n.shape[0]):
    print(' [', end='')  # Inicio de la línea
    for j in range(A0_n.shape[1]):
        print(A0_n[i, j], end="")  # Elemento de la matriz
        if j < A0_n.shape[1] - 1:
            print("  |  ", end="")  # Separador entre términos
    print(']')  # Fin de la línea

print("\n-----------------------------------------------------------------------")
# Extraer elementos de la matriz
print(f"\n3. El vector posición MTH0_{i+1} es:\nP:")
print("Px:", A0_n[0, 3])
print("Py:", A0_n[1, 3])
print("Pz:", A0_n[2, 3])
print("\n----------------------------------------------------------------------")
print(f"\n4.La matriz de Rotacion de MTH0_{i+1} es:\nR:")
# Obtener la submatriz 3x3
R = A0_n.extract(range(3), range(3))
for i in range(R.shape[0]):
    print('[', end='')  # Inicio de la línea
    for j in range(R.shape[1]):
        print(R[i, j], end="")  # Elemento de la matriz
        if j < R.shape[1] - 1:
            print("  |  ", end="")  # Separador entre términos
    print(']')  # Fin de la línea

print("\n-----------------------------Fin del programa-----------------------------")
print("-"*30+"Creado por MAHO"+"-"*30)
