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
recursos asignados a cada una, permitiendo agregar nuevos 
pedidos de misiones durante la atención;
 
indicar la cantidad total de recursos asignados a las misione
"""

import random


class Misiones(object):
    def __init__(self, tipo, planeta, general):
        self.tipo = tipo
        self.planeta = planeta
        self.general = general
        self.recursos = {}

class GrafoMisiones(object):
    def __init__(self):
        self.misiones = []

    def agregar_mision(self, mision):
        self.misiones.append(mision)

            
    def prioridad(mision):
        # Si el general es Palpatine o Darth Vader, la prioridad es alta
        if mision.general == "Palpatine" or mision.general == "Darth Vader":
            return "Alta"
        else:
            return "Baja"
        
    def asignar_recursos(mision):
        vehículos = ["AT-AT", "AT-RT", "AT-TE", "AT-DP", "AT-ST"]
        prioridad_mision = GrafoMisiones.prioridad(mision)
        if prioridad_mision == "Alta":
            # Asignar recursos manualmente
            input(f"Ingrese los recursos para la misión del general {mision.general} del tipo {mision.tipo}: ")
            mision.recursos["Stormtroopers"] = int(input("Ingrese la cantidad de Stormtroopers: "))
            mision.recursos["Scout Troopers"] = int(input("Ingrese la cantidad de Scout Troopers: "))
            mision.recursos["Speeder Bike"] = int(input("Ingrese la cantidad de Speeder Bike: "))
            mision.recursos["AT-AT"] = int(input("Ingrese la cantidad de AT-AT: "))
        else:
            # Asignar recursos automaticamente
            if mision.tipo == "Exploracion":
                mision.recursos["Scout Troopers"] = 15
                mision.recursos["Speeder Bike"] = 2
            elif mision.tipo == "Contencion":
                mision.recursos["Stormtroopers"] = 30
                for i in range(3):
                    mision.recursos[random.choice(vehículos)] = 1
            elif mision.tipo == "Ataque":
                mision.recursos["Stormtroopers"] = 50

                for i in range(7):
                    mision.recursos[random.choice(vehículos)] = 1
        return mision.recursos
    
    def mostrar_misiones(mision):
        for mision in grafo.misiones:
            print("--------------------------------------------------")
            print("Tipo: " + mision.tipo)
            print("Planeta: " + mision.planeta)
            print("General: " + mision.general)
            print("Recursos: " + str(mision.recursos))
            print("Prioridad: " + GrafoMisiones.prioridad(mision))
            print("--------------------------------------------------")




# Experimentacion
m1 = Misiones("Exploracion", "Tatooine", "Palpatine")
m2 = Misiones("Contencion", "Tatooine", "Darth Vader")
m3 = Misiones("Ataque", "Tatooine", "General Grievous")
m4 = Misiones("Exploracion", "Tatooine", "General Grievous")
m5 = Misiones("Contencion", "Tatooine", "General Grievous")
m6 = Misiones("Ataque", "Tatooine", "General Grievous")
grafo = GrafoMisiones()

grafo.agregar_mision(m1)
grafo.agregar_mision(m2)
grafo.agregar_mision(m3)
grafo.agregar_mision(m4)
grafo.agregar_mision(m5)
grafo.agregar_mision(m6)

# Asignar recursos
for mision in grafo.misiones:
    mision.recursos = GrafoMisiones.asignar_recursos(mision)

# Mostrar misiones
grafo.mostrar_misiones()

    
    