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

from tda_arbol_bin import insertar_nodo, nodoArbolHuffman, por_nivel, calcular_frecuencia
# Cargamos los datos con las frecuencias
tabla = [
    ['A',0.098],
    ['B',0.017],
    ['C',0.035],
    ['D',0.026],
    ['E',0.125],
    ['G',0.026],
    ['I',0.053],
    ['L',0.053],
    ['M',0.026],
    ['N',0.053],
    ['O',0.062],
    ['P',0.035],
    ['Q',0.008],
    ['R',0.080],
    ['S',0.035],
    ['T',0.026],
    ['U',0.035],
    ['V',0.017],
    [' ',0.150],
    [',',0.017]
]

# Genero un diccionaro en blanco 
dic = {}

# Generamos un bosuqe ahorra vacio
bosque = []

for elemento in tabla:
    nodo = nodoArbolHuffman(elemento[0], elemento[1])
    bosque.append(nodo)

while(len(bosque) > 1):
    elemento1 = bosque.pop(0)
    elemento2 = bosque.pop(0)
    nodo = nodoArbolHuffman('', elemento1.valor+elemento2.valor)
    nodo.izq = elemento1
    nodo.der = elemento2
    bosque.append(nodo)

def generar_tabla(raiz, dic, cadena=''):
    if(raiz is not None):
        if(raiz.izq is None):
            dic[raiz.info] = cadena
            #print(raiz.info, cadena)
        else:
            cadena += '0'
            generar_tabla(raiz.izq, dic, cadena)
            cadena = cadena[0:-1]
            cadena += '1'
            generar_tabla(raiz.der, dic, cadena)


def decodificar(cadena, arbol_huff):
    cadena_deco = ''
    raiz_aux = arbol_huff
    pos = 0
    while(pos < len(cadena)):
        if(cadena[pos] == '0'):
            raiz_aux = raiz_aux.izq
        else:
            raiz_aux = raiz_aux.der
        pos += 1
        if(raiz_aux.izq is None):
            cadena_deco += raiz_aux.info
            raiz_aux = arbol_huff
        cadena_deco
    return cadena_deco

def codificar_caracter(caracter, arbol_huff):
    cadena_cod = ''
    raiz_aux = arbol_huff
    while(raiz_aux.info != caracter):
        if(raiz_aux.izq is not None):
            if(caracter in raiz_aux.izq.info):
                cadena_cod += '0'
                raiz_aux = raiz_aux.izq
            else:
                cadena_cod += '1'
                raiz_aux = raiz_aux.der
    return cadena_cod

def codificar(cadena, arbol_huff):
    cadena_cod = ''
    for caracter in cadena:
        cadena_cod += codificar_caracter(caracter, arbol_huff)
    return cadena_cod



