from consulta import Consulta
from medico import Medico
lista=[]
c=Consulta(1,"11-1","Renato",20,"Fonasa",Medico("Chapatin 1","General"),
           "09:00","30-10-2025","Estado Gripal",15000)
lista.append(c)
c=Consulta(2,"22-2","Juan",30,"Fonasa",Medico("Chapatin 2","Oftalmólogo"),
           "10:00","10-09-2025","Miopía",20000)
lista.append(c)
c=Consulta(3,"33-3","Adrian",50,"Isapre",Medico("Chapatin 3","General"),
           "11:00","15-10-2025","Estado Gripal",25000)
lista.append(c)
c=Consulta(4,"44-4","Isidora",40,"Isapre",Medico("Chapatin 4","Traumatólogo"),
           "12:00","22-10-2025","Esguince",5000)
lista.append(c)
c=Consulta(5,"55-5","Jego",65,"Fonasa",Medico("Chapatin 5","Geriatra"),
           "13:00","03-11-2025","Artrosis",18000)
lista.append(c)

#c.mostrarMedicosDeUnaEspecialidad_Forma1(lista)
#listaEspecialidad=c.mostrarMedicosDeUnaEspecialidad_Forma2(lista)
#print("Los doctores son:",listaEspecialidad)
# c.contarMedicosDeUnaEspecialidad_Forma1(lista)
