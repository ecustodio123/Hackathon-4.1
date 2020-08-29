import json
from time import sleep
from Es import Cursos

data = {}
data['estudiantes_creados'] = []
data_1 = {}
data_1['docentes_creados'] = []

notas = []

class Estudiante():
    def __init__(self, dni, nombre, edad, cargo):
        self.dni = dni
        self.nombre = nombre
        self.edad = edad
        self.cargo = cargo

    def configurar_estudiante(self):
        print(""""\n Por favor indique si usted es Alumno o Docente\n
                1) Alumno
                2) Docente\n""")
        cargo = input("> ")
        if cargo == "1":
            cargo = "Alumno"
            self.crear_estudiante(cargo)
        elif cargo == "2":
            cargo = "Docente"
            self.crear_estudiante(cargo)
        else:
            print("\nOpción no valida")

    def crear_estudiante(self, cargo):
        dni = input("\nPor favor introduzca su DNI: ")
        nombre = input("\nPor favor introduzca su Nombre: ")
        edad = input("\nPor favor introduzca su Edad: ")
        nuevo_estudiante = Estudiante(dni,nombre,edad,cargo)
        datos = {
                "DNI" : nuevo_estudiante.dni,
                "Nombre" : nuevo_estudiante.nombre,
                "Edad" : nuevo_estudiante.edad,
                "Cargo" : nuevo_estudiante.cargo
            }
        self.guardar_estudiante(datos)

        print(f"\nSe ha registrado a {nombre}")
        

    def guardar_estudiante(self, datos):

        notas = []

        if (datos['Cargo'] == "Alumno"):
            
            cant_notas = int(input("Por favor introduzca la cantidad de notas que va ingresar en el curso: "))
            
            for i in range(cant_notas):

                nota = int(input(f"Por favor ingrese la nota {i + 1}: "))
                notas.append(nota)
            
            nota_promedio = sum(notas) / len(notas)

            print(notas)

            del datos['Cargo']

            notas_dicc = {
                "Notas" : notas,
                "Nota Maxima" : max(notas),
                "Nota Minima" : min(notas),
                "Nota Promedio" : nota_promedio
            }

            data["estudiantes_creados"].append(datos)
            data["estudiantes_creados"].append(notas_dicc)
            
            est = data["estudiantes_creados"]
            # est = (f"-Alumno->   DNI:{datos['DNI']}, Nombre: {datos['Nombre']}, Edad: {datos['Edad']}, Notas: {notas}, Maxima nota: {max(notas)}, Minima nota: {min(notas)}, Promedio:{nota_promedio}")
            archivo = open("alumnos.json", "w")
            json.dump(est, archivo, indent=4)

        elif(datos['Cargo'] == "Docente"):

            print("\nPor favor introduzca la opción del curso en el cual se desea asignar:\n")

            for i in range(len(Cursos)):
                print(f"{i +1}) -> {Cursos[i]}")

            opcion_curso = int(input("\n> "))

            for i in range(len(Cursos)):
                if(opcion_curso == i+1):
                    curso = Cursos[i]
                    print(curso)

            del datos['Cargo']

            curso_dicc = {
                "Curso" : curso
            }

            data_1["docentes_creados"].append(datos)
            data_1["docentes_creados"].append(curso_dicc)
            doc = str(data_1["docentes_creados"])
            # print(doc)
            # archivo = open("docente.txt", "a+")
            # archivo.write(f"-Docente: {datos['DNI']}, {datos['Nombre']}, {datos['Edad']}\n")
            # archivo.write(doc)
            doc = data_1['docentes_creados']
            archivo = open("docentes.json", "w")
            json.dump(doc, archivo, indent=4)
    
    def cargar_personajes(self):
        try:
            archivo = open("alumnos.json")
            data["estudiantes_creados"] = json.load(archivo)
            # print(data["estudiantes_creados"])
        except FileNotFoundError:
            print("\nCreando Registro de Alumnos")
            sleep(1)
            archivo = open("alumnos.json", "a+")
        except json.decoder.JSONDecodeError:
            print("\nNo hay alumnos creados aún en nuestra base de datos")
        
        try:
            archivo = open("docentes.json")
            data_1["docentes_creados"] = json.load(archivo)
            # print(data_1["docentes_creados"])
        except FileNotFoundError:
            print("\nCreando Registro de Docentes")
            sleep(1)
            archivo = open("docentes.json", "a+")
        except json.decoder.JSONDecodeError:
            print("\nNo hay docentes creados aún en nuestra base de datos")
        pass

    def interfaz(self):
        while True:
            print("""\n¡Bienvenido al colegio Pachaqtec! Por favor indique que desea hacer?
            1) Registrarse en nuestra base de datos
            2) Ver la base de datos de Alumnos/Profesores
            2) Salir del programa\n""")
            opcion = input("> ")
            if opcion == "1":
                self.configurar_estudiante()
            elif opcion == "2":
                print("\nGracias por usar esta aplicacion")
                sleep(2)
                quit()
            else:
                print("\nHas introducido una opción erronea")


class Iniciar(Estudiante):
    def __init__(self):
        self.cargar_personajes()
        self.interfaz()

Iniciar()