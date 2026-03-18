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
    def __init__(self,nombre_paciente,fecha_hora,nombre_medico,tipo_consulta, estado):
        self.nombre_paciente= nombre_paciente
        self.fecha_hora= fecha_hora
        self.nombre_medico= nombre_medico
        self.tipo_consulta= tipo_consulta
        self.estado= estado

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

    def Eliminar_cita(self, fecha_hora, ord = None):
        if self.cabeza is None:
            print("No hay citas pendientes")
            return

        if self.cabeza.dato.fecha_hora == fecha_hora:
            self.cabeza = None
            print("Cita atendida")

        actual = self.cabeza
        found = False
        while actual.siguiente != self.cabeza:
            if actual.siguiente.dato.fecha_hora == fecha_hora:
                found = True
                break
            actual = actual.siguiente

        if found:
            prev = actual.anterior
            nxt = actual.siguiente
            prev.siguiente = actual
            nxt.anterior = actual
            print(f"cita con fecha {fecha_hora} eliminada")
            return
        print("No se encontró cita con esa fecha")
        return


    def Mostrar_agenda(self, ord = None):
        if self.cabeza is None:
            print("No hay citas pendientes")
            return

        actual = self.cabeza
        if ord and ord == -1:
            while True:
                c_time, hoy = None, None
                try:
                    hoy = datetime.today().date()
                    c_time = datetime.strftime(actual.dato.fecha_hora, "YYYY-MM-DD")
                except:
                    pass
                if c_time and hoy and c_time == hoy:
                    print(f"{actual.dato.nombre_paciente}|{actual.dato.fecha_hora}|{actual.dato.nombre_medico}|{actual.dato.estado}", end="")
                actual = actual.anterior
                if actual != self.cabeza:
                    print(end = " -> ")
                if actual.anterior == self.cabeza.anterior:
                    break
            return

        while True:
            c_time, hoy = None, None
            try:
                hoy = datetime.today().date()
                c_time = datetime.strftime(actual.dato.fecha_hora, "YYYY-MM-DD")
            except:
                pass
            if c_time and hoy and c_time == hoy:
                print(f"{actual.dato.nombre_paciente}|{actual.dato.fecha_hora}|{actual.dato.nombre_medico}|{actual.dato.estado}",end="")
            actual = actual.siguiente
            if actual != self.cabeza:
                print(end=" -> ")
            if actual.siguiente == self.cabeza.siguiente:
                break
        return

    def buscar_cita(self, crit, s_val): pass #crit es el criterio de búsqueda (fecha u hora), s_val es la entrada (formato YYYY-MM-DD o HH:MM)


    def atender_cita(self, c_time): pass

    def generar_reporte(self, dia): pass




Lista= Agenda()
while True:
    print("---SELECCIONE EL TIPO DE RECORRIDO DE LA AGENDA---")
    print("1.Cabeza y Siguiente\n2.Cola y Anterior")
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