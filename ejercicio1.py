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

class NodoHuffman(object):
    def _init_(self, valor, frecuencia):
        self.valor = valor
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None
 
class Arbol(object):
    def calcular_frecuencias(mensaje):
        frecuencias = {}
        for caracter in mensaje:
            if caracter in frecuencias:
                frecuencias[caracter] += 1
            else:
                frecuencias[caracter] = 1
        return frecuencias
    
    def construir_arbol_huffman(frecuencias):
        nodos = []
        for caracter, frecuencia in frecuencias.items():
            nodos.append(NodoHuffman(caracter, frecuencia))
        while len(nodos) > 1:
            nodos.sort()
            nodo_izquierda = nodos.pop(0)
            nodo_derecha = nodos.pop(0)
            nodo_padre = NodoHuffman(None, nodo_izquierda.frecuencia + nodo_derecha.frecuencia)
            nodo_padre.izquierda = nodo_izquierda
            nodo_padre.derecha = nodo_derecha
            nodos.append(nodo_padre)
        return nodos[0]
    
    def codificar_caracter(nodo, caracter, codigo_actual):
        if nodo == None:
            return None
        if nodo.valor == caracter:
            return codigo_actual
        codigo_izq = Arbol.codificar_caracter(nodo.izquierda, caracter, codigo_actual + "0")
        if codigo_izq != None:
            return codigo_izq
        codigo_der = Arbol.codificar_caracter(nodo.derecha, caracter, codigo_actual + "1")
        return codigo_der
    
    def codificar_mensaje(mensaje, arbol_huffman):
        mensaje_codificado = ""
        for caracter in mensaje:
            codigo = Arbol.codificar_caracter(arbol_huffman, caracter, "")
            mensaje_codificado += codigo
        return mensaje_codificado
    
    def decodificar_mensaje(mensaje_codificado, arbol_huffman):
        mensaje_decodificado = ""
        nodo_actual = arbol_huffman
        for bit in mensaje_codificado:
            if bit == "0":
                nodo_actual = nodo_actual.izquierda
            elif bit == "1":
                nodo_actual = nodo_actual.derecha
            if nodo_actual.valor != None:
                mensaje_decodificado += nodo_actual.valor
                nodo_actual = arbol_huffman
        return mensaje_decodificado
    

if __name__ == "__main__":

    frecuencias = {'A': 0.098, 'B': 0.017, 'C': 0.035, 'D': 0.026, 'E': 0.125, 'G': 0.026, 'I': 0.053, 'L': 0.053, 'M': 0.026, 'N': 0.053, 'O': 0.062, 'P': 0.035, 'Q': 0.008, 'R': 0.08, 'S': 0.035, 'T': 0.026, 'U': 0.035, 'V': 0.017, ' ': 0.15, ',': 0.017}
    mensaje_codificado1="10001011101011000010111010001110000011011000000111100111101001011000011010011100110100010111010111111101000011110011111100111101000110001100000010110101111011111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100001100101101011100110011110100011000110000001011010111110011100"
    mensaje_decodificado=Arbol.decodificar_mensaje(mensaje_codificado1,Arbol.construir_arbol_huffman(frecuencias))
    print(mensaje_decodificado)

    print("\n")
    mensaje_codificado2="0110101011011100101000111101011100110111010110110100001000111010100101111010011111110111001010001111010111001101110101100001100010011010001110010010001100010110011001110010010000111101111010"
    mensaje_decodificado2=Arbol.decodificar_mensaje(mensaje_codificado2,Arbol.construir_arbol_huffman(frecuencias))
    print(mensaje_decodificado2)

