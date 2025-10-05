# Tarea: Trabajo con Archivos de Texto en Python
# Autor: Alan
# Descripción: Programa que crea un archivo de texto con notas personales, luego las lee y muestra en pantalla.

# --- ESCRITURA DEL ARCHIVO ---
# Crea un nuevo archivo llamado "my_notes.txt" y escribe tres notas personales
with open("my_notes.txt", "w") as archivo:
    archivo.write("1. Tengo clases en la universidad.\n")
    archivo.write("2. Tengo una cita médica en la tarde.\n")
    archivo.write("3. Ir al gimnasio después de estudiar.\n")

print("Archivo 'my_notes.txt' creado y escrito correctamente.\n")

# --- LECTURA DEL ARCHIVO ---
# Abre el archivo en modo lectura y muestra el contenido línea por línea
with open("my_notes.txt", "r") as archivo:
    print("Contenido del archivo:")
    for linea in archivo:
        print(linea.strip())

print("\nArchivo cerrado correctamente.")
