import random
import string
import os

# Colores
GREEN = '\033[0;32m'
RESET = '\033[0m'

# Mostrar banner
os.system('clear')
os.system('figlet -c "The Termux Syndicate - Generador Contraseñas"')
print(f"{GREEN}by red365{RESET}")
print("")

# Función para calcular el tamaño estimado del diccionario
def calcular_tamano(cantidad, longitud):
    # Asume un promedio de 8 bytes por contraseña
    return cantidad * longitud

# Instrucciones iniciales
print(f"{GREEN}Instrucciones:{RESET}")
print("Este script generará un diccionario de contraseñas aleatorias según las opciones que selecciones.")
print("Podrás elegir la cantidad de contraseñas, su longitud, tipo de caracteres y si deseas incluir palabras relacionadas.")
print("Asegúrate de elegir opciones que no generen contraseñas demasiado largas si es para un sistema con restricciones.")
input(f"{GREEN}Presiona Enter para continuar...{RESET}")

# Menú de opciones
print(f"{GREEN}Bienvenido al Generador de Diccionarios de Contraseñas{RESET}")
cantidad = int(input("¿Cuántas contraseñas quieres generar? "))
longitud_min = int(input("Longitud mínima de las contraseñas: "))
longitud_max = int(input("Longitud máxima de las contraseñas: "))

print("Tipos de caracteres:")
print("1) Solo números")
print("2) Solo letras")
print("3) Números y letras")
print("4) Números, letras y símbolos")
tipo = int(input("Elige el tipo de caracteres: "))
nombre_archivo = input("Nombre del archivo para guardar el diccionario: ")

# Preguntar si incluir palabras relacionadas
incluir_palabras = input("¿Quieres incluir palabras relacionadas en las contraseñas? (s/n): ").strip().lower()
palabras_relacionadas = []

if incluir_palabras == "s":
    palabras_relacionadas_input = input("Introduce las palabras relacionadas separadas por espacio: ")
    palabras_relacionadas = palabras_relacionadas_input.split()

# Determinar los caracteres a usar
if tipo == 1:
    caracteres = string.digits
elif tipo == 2:
    caracteres = string.ascii_letters
elif tipo == 3:
    caracteres = string.ascii_letters + string.digits
elif tipo == 4:
    caracteres = string.ascii_letters + string.digits + string.punctuation
else:
    print("Opción inválida")
    exit(1)

# Calcular tamaño estimado
tamano_estimado = calcular_tamano(cantidad, longitud_max)
print(f"{GREEN}Tamaño estimado del archivo: {tamano_estimado} bytes{RESET}")
print("")

# Limpiar el archivo si ya existe
with open(f"{nombre_archivo}.txt", "w") as f:
    pass

# Generar contraseñas y guardarlas en el archivo
print(f"{GREEN}Generando diccionario...{RESET}")
with open(f"{nombre_archivo}.txt", "a") as f:
    for _ in range(cantidad):
        longitud = random.randint(longitud_min, longitud_max)
        
        # Si se incluyen palabras relacionadas, las usamos en las contraseñas
        if palabras_relacionadas:
            palabra = random.choice(palabras_relacionadas)
            restante_longitud = longitud - len(palabra)
            password = palabra + ''.join(random.choice(caracteres) for _ in range(restante_longitud))
        else:
            password = ''.join(random.choice(caracteres) for _ in range(longitud))
        
        f.write(password + "\n")

print(f"{GREEN}Diccionario generado y guardado en {nombre_archivo}.txt{RESET}")
