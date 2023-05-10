from tda_cola import Cola, cola_vacia, arribo, atencion

class nodoArbol(object):

    def __init__(self, info, nrr=None):
        self.izq = None
        self.der = None
        self.info = info
        self.nrr = nrr


class nodoArbolHuffman(object):
    
    def __init__(self, valor, frecuencia):
        self.izq = None
        self.der = None
        self.valor = valor
        self.frecuencia = frecuencia

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
                    nodos.append(nodoArbolHuffman(caracter, frecuencia))
                while len(nodos) > 1:
                    nodos.sort()
                    nodo_izq = nodos.pop(0)
                    nodo_der = nodos.pop(0)
                    nodo_padre = nodoArbolHuffman(None, nodo_izq.frecuencia + nodo_der.frecuencia)
                    nodo_padre.izq = nodo_izq
                    nodo_padre.der = nodo_der
                    nodos.append(nodo_padre)
                return nodos[0]
            
    def codificar_caracter(nodo, caracter, codigo_actual):
                if nodo == None:
                    return None
                if nodo.valor == caracter:
                    return codigo_actual
                codigo_izq = Arbol.codificar_caracter(nodo.izq, caracter, codigo_actual + "0")
                if codigo_izq != None:
                    return codigo_izq
                codigo_der = Arbol.codificar_caracter(nodo.der, caracter, codigo_actual + "1")
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
                        nodo_actual = nodo_actual.izq
                    elif bit == "1":
                        nodo_actual = nodo_actual.der
                    if nodo_actual.valor != None:
                        mensaje_decodificado += nodo_actual.valor
                        nodo_actual = arbol_huffman
                return mensaje_decodificado

    

