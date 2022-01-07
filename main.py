print("si")

#variables

texto = "Si"
nombre = "erxsto"
altura ="1.65"
year = 2022

print("Si o no?", texto, "Mi nombre es", nombre, "y mido", altura ,"estamos en el año" , year)
print("Si o no? " + texto + " Mi nombre e s" + nombre + " y mido " + altura + " estamos en el año " + str(year))
print(f"{texto}, {nombre}, {altura}, {year}")

#Entradas

#pregunta = input("¿Cuál es tu nombre?")
#print("Hola"+ pregunta)

#condiciones
'''
altura = int(input("¿Cuál es tu altura?"))
if altura >= 180:
    print("Eres una persona alta"); def unafunction:
else:
    print("Eres una persona bajita ")
'''
    #funciones
"""
var_altura = int(input("¿Cuál es tu altura?"))

def mostrarAltura(altura):

    if altura >= 180:
        resultado = "Eres una persona alta"
    else:
        resultado = "Eres una persona bajita "
    
    return resultado

print(mostrarAltura(var_altura))
"""
#listas
personas = ["Victor", "Paco", "Erasto"]
print(personas[0])

for persona in personas:
    print(persona)