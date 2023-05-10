"""
Ejercicio 1
Desarrollar los algoritmos necesarios para generar un árbol de Huffman 
a partir de la siguiente tabla –para lo cual deberá calcular primero las 
para resolver las siguientes actividades:

1. la generación del árbol debe hacerse desde los caracteres 
de menor frecuencia hasta los de mayor, en el caso de que dos caracteres tengan la misma frecuencia, 
primero se toma el que este primero en el alfabeto, el carácter “espacio” y “coma” 
se consideraran anteúltimo y último respectivamente en el orden alfabético;
 
descomprimir los siguientes mensajes –cuyo árbol ha sido construido de la misma manera que el ejemplo visto anteriormente:
"""

from tda_arbol_bin import insertar_nodo, nodoArbolHuffman, por_nivel

def generar_arbol_huffman(tabla):
    