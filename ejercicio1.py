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

from tda_arbol_bin import crear_arbol_huffman
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

# Convertimos la tabla en un diccionario
frecuencia = {}
for i in tabla:
    frecuencia[i[0]] = i[1]

print(frecuencia)

def decodificar(cadena, arbol_huff):
    cadena_deco = ''
    raiz_aux = arbol_huff
    for bit in cadena:
        if bit == "0":
            raiz_aux = raiz_aux.izq
        elif bit == "1":
            raiz_aux = raiz_aux.der
    return cadena_deco


def codificar_caracter(raiz, caracter, codigo_actual):
        if raiz == None:
            return None
        if raiz.valor == caracter:
            return codigo_actual
        codigo_izq = codificar_caracter(raiz.izq, caracter, codigo_actual + "0")
        if codigo_izq != None:
            return codigo_izq
        codigo_der = codificar_caracter(raiz.der, caracter, codigo_actual + "1")
        return codigo_der


def codificar(cadena, arbol_huff):
    cadena_cod = ''
    for caracter in cadena:
        cadena_cod += codificar_caracter(arbol_huff, caracter, '')
    return cadena_cod

 
cadena_codificada="10001011101011000010111010001110000011011000000111100111101001011000011010011100110100010111010111111101000011110011111100111101000110001100000010110101111011111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100001100101101011100110011110100011000110000001011010111110011100"
cadena_decodificada = decodificar(cadena_codificada, crear_arbol_huffman(frecuencia))
print(cadena_decodificada)


