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
                    nodo_padre.izquierda = nodo_izq
                    nodo_padre.derecha = nodo_der
                    nodos.append(nodo_padre)
                return nodos[0]
            
def codificar_caracter(nodo, caracter, codigo_actual):
                if nodo == None:
                    return None
                if nodo.valor == caracter:
                    return codigo_actual
                codigo_izq = codificar_caracter(nodo.izquierda, caracter, codigo_actual + "0")
                if codigo_izq != None:
                    return codigo_izq
                codigo_der = codificar_caracter(nodo.derecha, caracter, codigo_actual + "1")
                return codigo_der
            
def codificar_mensaje(mensaje, arbol_huffman):
                mensaje_codificado = ""
                for caracter in mensaje:
                    codigo = codificar_caracter(arbol_huffman, caracter, "")
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

    

def inorden(raiz):
    if(raiz is not None):
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)


def postorden(raiz):
    if(raiz is not None):
        postorden(raiz.der)
        print(raiz.info)
        postorden(raiz.izq)

def preorden(raiz):
    if(raiz is not None):
        print(raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)


def por_nivel(raiz):
    cola = Cola()
    arribo(cola, raiz)
    while(not cola_vacia(cola)):
        nodo = atencion(cola)
        print(nodo.info)
        if(nodo.izq is not None):
            arribo(cola, nodo.izq)
        if(nodo.der is not None):
            arribo(cola, nodo.der)


def busqueda(raiz, buscado):
    if(raiz is not None):
        if(raiz.info == buscado):
            return raiz
        else:
            if(raiz.info > buscado):         
                return busqueda(raiz.izq, buscado)
            else:
                return busqueda(raiz.der, buscado)


def busqueda_nario(raiz, buscado, pos):
    if(raiz is not None):
        if(raiz.info == buscado):
            pos.append(raiz)
            return
        busqueda_nario(raiz.izq, buscado, pos)
        busqueda_nario(raiz.der, buscado, pos)


def busqueda_proximidad(raiz, buscado):
    if(raiz is not None):
        if(raiz.info[0:len(buscado)] == buscado):
            print(raiz.info)
        busqueda_proximidad(raiz.izq, buscado)
        busqueda_proximidad(raiz.der, buscado)


def arbol_vacio(raiz):
    return raiz is None


def remplazar(raiz):
    """Determina el nodo que remplazará al que se elimina."""
    aux = None
    if(raiz.der is None):
        aux = raiz
        raiz = raiz.izq
    else:
        raiz.der, aux = remplazar(raiz.der)
    return raiz, aux


def eliminar_nodo(raiz, clave):
    x = None
    if(raiz is not None):
        if(clave < raiz.info):
            raiz.izq, x = eliminar_nodo(raiz.izq, clave)
        elif(clave > raiz.info):
            raiz.der, x = eliminar_nodo(raiz.der, clave)
        else:
            x = raiz.info
            if(raiz.izq is None):
                raiz = raiz.der
            elif(raiz.der is None):
                raiz = raiz.izq
            else:
                raiz.izq, aux = remplazar(raiz.izq)
                raiz.info = aux.info
    return raiz, x


def hijo_der(arbol):
    if(arbol.der is None):
        print(arbol.der)
    else:
        print(arbol.der.info)

def hijo_izq(arbol):
    if(arbol.izq is None):
        print(arbol.izq)
    else:
        print(arbol.izq.info)




def contar(raiz, cp, ci):
    if(raiz is not None):
        if(raiz.info % 2 == 0):
            cp += 1
        else:
            ci += 1
        cp, ci = contar(raiz.izq, cp, ci)
        cp, ci = contar(raiz.der, cp, ci)
    return cp, ci

# cantp, canti = contar(arbol, cantp, canti)
# print(cantp, canti)


def contar_repetidos(raiz, buscado, cant):
    if(raiz is not None):
        if(raiz.info == buscado):
            cant += 1
            cant = contar_repetidos(raiz.der, buscado, cant)
        else:
            cant = contar_repetidos(raiz.izq, buscado, cant)
    return cant

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



