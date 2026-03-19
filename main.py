#Agenda de Citas con Listas Enlazadas Circulares
from datetime import datetime, timedelta


def Menu():
    print("--------------------")
    print("|  GESTOR DE CITAS  |")
    print("--------------------")

    print("1.Agregar Cita.\n2.Eliminar Cita.\n3.Mostrar Agenda.\n4.Buscar cita.\n5.Editar cita\n6.Generar reporte\n7.Salir")

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


    def Agrear_cita(self,cita, rev = None):
        nueva_cita = Nodo(cita)
        nueva_fecha = nueva_cita.dato.fecha_hora

        if self.cabeza is None:
            print("No hay citas...Agregar primera cita")
            self.cabeza =nueva_cita
            nueva_cita.siguiente = nueva_cita
            nueva_cita.anterior = nueva_cita
            return

        ultimo = self.cabeza

        if rev and rev == -1:
            while ultimo.anterior != self.cabeza:
                diferencia = abs(ultimo.dato.fecha_hora -   nueva_fecha)
                if diferencia < timedelta(hours=2):
                    print(f"\n[!] ERROR: Conflicto de horario.")
                    print(f"Ya existe una cita a las {ultimo.dato.fecha_hora.strftime('%H:%M')}.")
                    print("Debe haber un espacio de al menos 2 horas entre citas.")
                    return
                ultimo = ultimo.anterior
            nueva_cita.siguiente = ultimo
            self.cabeza.siguiente = nueva_cita
            ultimo.anterior = nueva_cita
            nueva_cita.anterior = self.cabeza
            return

        self.cola = nueva_cita

        while ultimo.siguiente != self.cabeza:
            diferencia = abs(ultimo.dato.fecha_hora - nueva_fecha)
            if diferencia < timedelta(hours=2):
                print(f"\n[!] ERROR: Conflicto de horario.")
                print(f"Ya existe una cita a las {ultimo.dato.fecha_hora.strftime('%H:%M')}.")
                print("Debe haber un espacio de al menos 2 horas entre citas.")
                return
            ultimo = ultimo.siguiente

        nueva_cita.siguiente= self.cabeza
        self.cabeza.anterior = nueva_cita
        ultimo.siguiente= nueva_cita
        nueva_cita.anterior = ultimo


    def Eliminar_cita(self, fecha_hora, ord = None):
        if self.cabeza is None:
            print("No hay citas pendientes")
            return

        fecha_hora = datetime.strptime(fecha_hora, "%Y-%m-%d %H:%M")

        if self.cabeza.dato.fecha_hora == fecha_hora:
            ant = self.cabeza.anterior
            nxt = self.cabeza.siguiente
            self.cabeza = nxt
            ant.siguiente = self.cabeza
            self.cabeza.anterior = ant
            print("Cita eliminada")
            return

        if ord and ord == -1:
            actual = self.cabeza
            found = False
            while actual.anterior != self.cabeza:
                if actual.anterior.dato.fecha_hora == fecha_hora:
                    found = True
                    break
                actual = actual.anterior

            if found:
                ant = actual.anterior
                prev = ant.anterior
                nxt = ant.siguiente
                prev.siguiente = ant.siguiente
                nxt.anterior = ant.anterior
                print(f"cita con fecha {fecha_hora} eliminada")
                return
            print("No se encontró cita con esa fecha")
            return

        actual = self.cabeza
        found = False
        while actual.siguiente != self.cabeza:
            if actual.siguiente.dato.fecha_hora == fecha_hora:
                found = True
                break
            actual = actual.siguiente

        if found:
            nxt = actual.siguiente
            actual.siguiente = nxt.siguiente
            nxt.siguiente.anterior = actual
            print(f"cita con fecha {fecha_hora} eliminada")
            return
        print("No se encontró cita con esa fecha")
        return


    def Mostrar_agenda(self, ord = None):
        if self.cabeza is None:
            print("No hay citas pendientes")
            return

        citas_hoy = []
        actual = self.cabeza
        start = actual
        is_reverse = ord == -1

        while True:
            if actual.dato.fecha_hora.strftime("%Y-%m-%d") == datetime.today().strftime("%Y-%m-%d"):
                citas_hoy.append(f"{actual.dato.nombre_paciente}|{actual.dato.fecha_hora}|{actual.dato.nombre_medico}|{actual.dato.estado}")

            actual = actual.anterior if is_reverse else actual.siguiente
            if actual == start:
                break
        if citas_hoy:
            print(" -> ".join(reversed(citas_hoy) if is_reverse else citas_hoy))
        else:
            print("No hay citas hoy")


    def buscar_cita(self, crit, s_val): #crit es el criterio de búsqueda (fecha u hora), s_val es la entrada (formato YYYY-MM-DD o HH:MM)
        if self.cabeza is None:
            print("No hay citas")
            return

        actual = self.cabeza
        found = False
        while True:
            dt = actual.dato.fecha_hora.strftime("%Y-%m-%d")
            hr = actual.dato.fecha_hora.strftime("%H:%M")
            if crit == "fecha":
                if dt == s_val:
                    found = True
                    break
            elif crit == "hora":
                if hr == s_val:
                    found = True
                    break
            else:
                print("Requisito inválido")
                return
            actual = actual.siguiente
            if actual == self.cabeza:
                break

        if found:
            print(f"Cita encontrada >:P")
            print(f"{actual.dato.nombre_paciente} | {actual.dato.fecha_hora} | {actual.dato.nombre_medico} | {actual.dato.estado}")
        else:
            print("No se encontró ninguna cita")
        return


    def editar_cita(self, c_time):
        if self.cabeza is None:
            print("No hay citas")
            return
        c_time = datetime.strptime(c_time, "%Y-%m-%d %H:%M")
        actual = self.cabeza
        while True:
            if actual.dato.fecha_hora == c_time:
                print("Cita encontrada, ingrese nuevos datos")

                nombre = input("Nuevo nombre del paciente: ")
                medico = input("Nuevo medico: ")
                tipo = input("Nuevo tipo consulta: ")
                estado = input("Nuevo estado: ")

                actual.dato.nombre_paciente = nombre
                actual.dato.nombre_medico = medico
                actual.dato.tipo_consulta = tipo
                actual.dato.estado = estado
                print("Cita editada correctamente")
                return

            actual = actual.siguiente
            if actual == self.cabeza:
                break
        print("No se encontró la cita")


    def generar_reporte(self, dia):
        if self.cabeza is None:
            print("No hay citas")
            return

        actual = self.cabeza
        found = False
        while True:
            fecha = actual.dato.fecha_hora.strftime("%Y-%m-%d")
            if fecha == dia:
                found = True
                print(f"{actual.dato.nombre_paciente} | {actual.dato.fecha_hora} | {actual.dato.nombre_medico} | {actual.dato.estado}")
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        if not found:
            print("No hay citas ese día")



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
                    try:
                        nombre = input("Ingrese nombre del paciente:")
                        fecha_hora = input("Ingrese ficha y hora de cita (formato AAAA-MM-DD HH:MM):")
                        fecha_hora = datetime.strptime(fecha_hora, "%Y-%m-%d %H:%M")
                        nombre_medico = input("Ingrese nombre de medico:")
                        tipo = input("Ingrese tipo de consulta medica:")
                        estado = "Pendiente"

                        cita = Cita(nombre, fecha_hora, nombre_medico, tipo, estado)
                        Lista.Agrear_cita(cita)
                    except ValueError:
                        print("Formato de fecha incorrecto, intente de nuevo")
                    except Exception as e:
                        print(e)

                case "2":
                    print("---ELIMINAR CITA---")
                    fecha = input("Ingrese fecha y hora de la cita a eliminar:")
                    Lista.Eliminar_cita(fecha)

                case "3":
                    print("---MOSTRAR AGENDA---")
                    Lista.Mostrar_agenda()
                    #Otro menu, busuqeda por fecha o por hora

                case "4":
                    print("---BUSCAR CITA---")
                    criterio = input("Buscar por fecha u hora:")
                    valor = input("Ingrese valor:")

                    Lista.buscar_cita(criterio, valor)

                case "5":
                    print("---EDITAR CITA---")

                    fecha = input("Ingrese fecha y hora de la cita:")
                    Lista.editar_cita(fecha)

                case "6":
                    print("---GENERAR REPORTE---")

                    dia = input("Ingrese fecha (YYYY-MM-DD):")
                    Lista.generar_reporte(dia)

                case "7":
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
                    try:
                        print("----AGREGAR CITA---")
                        nombre = input("Ingrese nombre del paciente:")
                        fecha_hora = input("Ingrese ficha y hora de cita:")
                        fecha_hora = datetime.strptime(fecha_hora, "%Y-%m-%d %H:%M")
                        nombre_medico = input("Ingrese nombre de medico:")
                        tipo = input("Ingrese tipo de consulta medica:")
                        estado = "Pendiente"

                        cita = Cita(nombre, fecha_hora, nombre_medico, tipo, estado)
                        Lista.Agrear_cita(cita, -1)
                    except ValueError:
                        print("Formato de fecha incorrecto, intente de nuevo")
                    except Exception as e:
                        print(e)

                case "2":
                    print("---ELIMINAR CITA---")
                    fecha = input("Ingrese fecha y hora de la cita a eliminar:")
                    Lista.Eliminar_cita(fecha, -1)

                case "3":
                    print("---MOSTRAR AGENDA---")
                    Lista.Mostrar_agenda(-1)
                    # Otro menu, busuqeda por fecha o por hora

                case "4":
                    print("---BUSCAR CITA---")
                    criterio = input("Buscar por fecha u hora:")
                    valor = input("Ingrese valor:")
                    Lista.buscar_cita(criterio, valor)

                case "5":
                    print("---EDITAR CITA---")
                    fecha = input("Ingrese fecha y hora de la cita:")
                    Lista.editar_cita(fecha)

                case "6":
                    print("---GENERAR REPORTE---")
                    dia = input("Ingrese fecha (YYYY-MM-DD):")
                    Lista.generar_reporte(dia)

                case "7":
                    print("Saliendo del Sistema....Hasta la proxima! :D")
                    break

                case _:
                    print("Opcion no valida....")