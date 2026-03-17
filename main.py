#Agenda de Citas con Listas Enlazadas Circulares

from datetime import datetime


def Menu():
    print("--------------------")
    print("|  GESTOR DE CITAS  |")
    print("--------------------")

    print("1.Agregar Cita.\n2.Eliminar Cita.\3.Mostrar Agenda.\n4.Mostrar Agenda.\n5.Salir")

    print("---" * 30)

class Nodo:
    def __init__(self,dato):
        self.dato= dato
        self.siguiente= None
        self.anterior= None


class Cita:
    def __init__(self,nombre_paciente,fecha_hora,nombre_medico,tipo_consulta):
        self.nombre_paciente= nombre_paciente
        self.fecha_hora= fecha_hora
        self.nombre_medico= nombre_medico
        self.tipo_consulta= tipo_consulta
        self.estado= ""

class Agenda:
    def __init__(self):
        self.cabeza= None
        self.cola = None

    def Agrear_cita(self,cita):
        nueva_cita= Nodo(cita)

        if self.cabeza is None:
            print("No hay citas...Agregar primera cita")
            self.cabeza =nueva_cita
            nueva_cita.siguiente = nueva_cita
            return

        ultimo= self.cabeza

        while ultimo != self.cabeza:
            ultimo = ultimo.siguiente

        nueva_cita.siguiente= self.cabeza
        ultimo.siguiente= nueva_cita

    def Eliminar_cita(self):
        pass

    def Mostrar_agenda(self):
        pass

Lista= Agenda()
while True:
    print("---SELECCIONE EL TIPO DE RECORRIDO DE LA AGENDA---")
    print("1.Cabeza y Cola\n2.Cola y Anterior")
    option= input("Ingrese una opcion:")

    match option:
        case "1":
            print("---CABEZA Y COLA---")

            Menu()
            opcion= input("Ingrese una opcion:")

            match opcion:
                case "1":
                    print("----AGREGAR CITA---")
                    nombre = input("Ingrese nombre del paciente:")
                    fecha_hora = input("Ingrese ficha y hora de cita:")
                    nombre_medico = input("Ingrese nombre de medico:")
                    tipo = input("Ingrese tipo de consulta medica:")
                    estado = "Pendiente"

                    cita = Cita(nombre, fecha_hora, nombre_medico, tipo, estado)
                    Lista.Agrear_cita(cita)

                case "2":
                    print("---ELIMINAR CITA---")

                case "3":
                    print("---MOSTRAR AGENDA---")
                    #Otro menu, busuqeda por fecha o por hora

                case "4":
                    print("---BUSCAR CITA---")

                case "5":
                    print("Saliendo del Sistema....Hasta la proxima! :D")
                    break

                case _:
                    print("Opcion no valida....")
        case "2":
            print("---COLA Y ANTERIOR---")

            Menu()
            opcion = input("Ingrese una opcion:")

            match opcion:
                case "1":
                    print("----AGREGAR CITA---")
                    nombre = input("Ingrese nombre del paciente:")
                    fecha_hora = input("Ingrese ficha y hora de cita:")
                    nombre_medico = input("Ingrese nombre de medico:")
                    tipo = input("Ingrese tipo de consulta medica:")
                    estado = "Pendiente"

                    cita = Cita(nombre, fecha_hora, nombre_medico, tipo, estado)
                    Lista.Agrear_cita(cita)

                case "2":
                    print("---ELIMINAR CITA---")

                case "3":
                    print("---MOSTRAR AGENDA---")
                    # Otro menu, busuqeda por fecha o por hora

                case "4":
                    print("---BUSCAR CITA---")

                case "5":
                    print("Saliendo del Sistema....Hasta la proxima! :D")
                    break

                case _:
                    print("Opcion no valida....")