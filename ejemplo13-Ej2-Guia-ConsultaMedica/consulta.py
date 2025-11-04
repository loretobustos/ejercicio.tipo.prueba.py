from paciente import Paciente
class Consulta(Paciente):
    def __init__(self, id, rut,nombre, edad, sistemaSalud, medico,
                 horaAt,diaAt,diagnostico,monto):
        super().__init__(id, rut, nombre,edad, sistemaSalud, medico)
        self.horaAt=horaAt
        self.diaAt=diaAt
        self.diagnostico=diagnostico
        self.monto=monto

    def mostrarConsulta(self):
        pass

    def mostrarMedicosDeUnaEspecialidad_Forma1(self,lista):
        especialidad=input("Qué especialidad deseas buscar?: ").upper()
        print("Los médicos de la especialidad son:")
        for item in lista:
            if especialidad==item.medico.especialidad.upper():
                print("\t-",item.medico.nombre)
    
    def mostrarMedicosDeUnaEspecialidad_Forma2(self,lista):
        especialidad=input("Qué especialidad deseas buscar?: ").upper()
        listaEspecialidad=[]
        for item in lista:
            if especialidad==item.medico.especialidad.upper():
                listaEspecialidad.append(item.medico.nombre)
        return listaEspecialidad
    
    def contarMedicosDeUnaEspecialidad_Forma1(self,lista):
        especialidad=input("Qué especialidad deseas buscar?: ").upper()
        contador=0
        for item in lista:
            if especialidad==item.medico.especialidad.upper():
                contador+=1
        print("La cantidad de médicos es:",contador)

    def contarMedicosDeUnaEspecialidad_Forma2(self,lista):
        especialidad=input("Qué especialidad deseas buscar?: ").upper()
        listaEspecialidad=[]
        for item in lista:
            if especialidad==item.medico.especialidad.upper():
                listaEspecialidad.append(item.medico.nombre)
        return len(listaEspecialidad)
    
    def consultaPagoBajoPagoAlto(self,lista):
        pass
        # usar lista auxiliar y después métodos max y min
    
    def contarFonasaIsapre(self,lista):
        pass
        # usar dos contadores

    def nominaMedicoPorEspecialida(self,lista):
        pass

    
    
