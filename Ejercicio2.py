"""
El comandante de la estrella de la muerte el gran Moff Tarkin debe 
administrar las asigna- ciones de vehículos y Stromtroopers a las 
distintas misiones que parten desde la estrella de la muerte, 
para facilitar esta tarea nos encomienda desarrollar las funciones 
necesarias para gestionar esto mediante prioridades de la siguiente manera:

de cada misión se conoce su tipo (exploración, contención o ataque), 
planeta destino y general que la solicitó;
 
si la misión fue pedida por Palpatine o Darth Vader estas 
tendrán alta prioridad, sino su prioridad será baja;
 
si la misión es de prioridad alta los recursos se asignarán manualmente 
independiente- mente de su tipo;
 
si la misión es de baja prioridad se asignarán los recursos de la 
siguiente manera depen- diendo de su tipo:
 
exploración: 15 Scout Troopers y 2 speeder bike,
 
contención: 30 Stormtroopers y tres vehículos aleatorios 
AT-AT, AT-RT, AT-TE, AT-DP, AT-ST) pueden ser repetidos,
 
ataque: 50 Stormtroopers y siete vehículos aleatorios 
(a los anteriores se le suman AT-M6, AT-MP, AT-DT),

realizar la atención de todas las misiones y mostrar los 
recursos asignados a cada una, per- mitiendo agregar nuevos 
pedidos de misiones durante la atención;
 
indicar la cantidad total de recursos asignados a las misione
"""
def intercambio(vector, indice1, indice2):
    """Intercambia dos valores de la tabla."""
    vector[indice1], vector[indice2] = vector[indice2], vector[indice1]


class Heap(object):
    """Crear un montículo."""

    def __init__(self, tamanio):
        """Crea un montículo vacio."""
        self.vector = [None] * tamanio
        self.tamanio = 0


def agregar(heap, dato):
    """Agrega un dato en el montículo."""
    heap.vector[heap.tamanio] = dato
    flotar(heap, heap.tamanio)
    heap.tamanio += 1


def quitar(heap):
    """Quita el elemento en la cima del montículo."""
    intercambio(heap.vector, 0, heap.tamanio-1)
    dato = heap.vector[heap.tamanio-1]
    heap.tamanio -= 1
    hundir(heap, 0)
    return dato


def flotar(heap, indice):
    """Flota el elemento en la posición índice."""
    while(indice > 0 and heap.vector[indice][0] < heap.vector[(indice - 1) // 2][0]):
        #print('flotando', heap.vector[indice])
        padre = (indice - 1) // 2
        intercambio(heap.vector, indice, padre)
        indice = padre


def hundir(heap, indice):
    """Hunde el elemento en la posición índice."""
    hijo_izq = (indice * 2) + 1
    control = True
    while(control and hijo_izq < heap.tamanio):
        #print('hundir', heap.vector[indice])
        hijo_der = hijo_izq + 1
        aux = hijo_izq
        if(hijo_der < heap.tamanio):
            if heap.vector[hijo_der][0] < heap.vector[hijo_izq][0]:
                aux = hijo_der

        if (heap.vector[indice][0] > heap.vector[aux][0]):
            #print('se hundio')
            intercambio(heap.vector, indice, aux)
            indice = aux
            hijo_izq = (indice * 2) + 1
            #print('luego de hundir', heap.vector)
        else:
            control = False
        


def cantidad_elementos(heap):
    """Devuelve la cantidad de elementos en el montículo."""
    return heap.tamanio


def heap_vacio(heap):
    """Devuelve true si el montículo esta vacio."""
    return heap.tamanio == 0


def heap_lleno(heap):
    """Devuelve true si el montículo esta lleno."""
    return heap.tamanio == len(heap.vector)


def monticulizar(heap):
    """Transforma un vector en un mantículo."""
    for i in range(len(heap.vector)):
        flotar(heap, i)

def heapsort(heap):
    """Método de ordenamiento heapsort."""
    aux = heap.tamanio
    for i in range(heap.tamanio):
        quitar(heap)
    heap.tamanio = aux


# Cola de prioridad
def arribo(heap, dato, prioridad):
    """Arriba el dato a la cola utilizando prioridad."""
    agregar(heap, [prioridad, dato])


def atencion(heap):
    """Antiende el elemento en el frente de la cola y lo devuelve."""
    return quitar(heap)


def cambiar_prioridad(heap, indice, prioridad):
    """Cambia la prioridad de un elemento y lo acomoda en el montículo."""
    prioridad_anterior = heap.vector[indice][0]
    heap.vector[indice][0] = prioridad
    if(prioridad < prioridad_anterior):
        flotar(heap, indice)
    elif(prioridad > prioridad_anterior):
        hundir(heap, indice)

def buscar(heap, buscado):
    pos = -1
    for i in range(len(heap.vector)):
        if(heap.vector[i][1][0].info == buscado):
            pos = i
    return pos

def ins


