import tkinter as tk
import subprocess
import os

# Función para ejecutar un script de Python
def ejecutar_script(script):
    try:
        # Usa subprocess para ejecutar el script y esperar a que termine
        subprocess.run(["python", script])
    except Exception as e:
        print(f"Error ejecutando {script}: {e}")

# Función para volver al menú principal
def volver_al_menu():
    for widget in root.winfo_children():
        widget.destroy()
    crear_menu_principal()

# Función para crear el menú principal
def crear_menu_principal():
    opciones = [
        ("Pagina", "app.py"),
        ("Convertir un archivo a audio", "archivo_audio.py"),
        ("Chat GPT", "chat.py"),
        ("Chunking", "chunking.py"),
        ("Convertir archivo .py a ejecutable", "ejecutable.py"),
        ("Grabar audio y convertirlo a texto", "Grbacion.py"),
        ("grabar audio, pasarlo a texto y reproducirlo", "reconocedor.py"),
        ("detector de sentimientos", "sentimientos.py"),
        ("Convertir un texto a audio", "Texto_audio.py")
    ]
    
    tk.Label(root, text="Seleccione una opción", font=("Helvetica", 16)).pack(pady=20)
    
    for opcion, script in opciones:
        tk.Button(root, text=opcion, command=lambda script=script: [ejecutar_script(script), volver_al_menu()]).pack(pady=5)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Menú Principal")
root.geometry("400x400")

crear_menu_principal()

root.mainloop()
