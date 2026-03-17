#Agenda de Citas con Listas Enlazadas Circulares

class Nodo:
    def __init__(self,dato):
        self.dato= dato
        self.siguiente= None
        self.anterior= None


class Cita:
    def __init__(self,nombre_paciente,fecha_hora,nombre_medico,tipo_consulta,estado):
        self.nombre_paciente= nombre_paciente
        self.fecha_hora= fecha_hora
        self.nombre_medico= nombre_medico
        self.tipo_consulta= tipo_consulta
        self.estado= estado

class Agenda:
    def __init__(self):
        self.cabeza= None

def Menu():
    print("--------------------")
    print("|  GESTOR DE CITAS  |")
    print("--------------------")

    print("1.Agregar Cita2.""


    def Agrear_cita(self):
        pass

    def Eliminar_cita(self):
        pass

    def Mostrar_agenda(self):
        pass
