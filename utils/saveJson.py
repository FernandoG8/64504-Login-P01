import json
import os
import hashlib

def guardar_usuario(username, password, nombre_archivo):
    try:
        contrasena_haseada = password  # La contraseña ya viene haseada desde el componente
        # Cargar datos existentes
        if os.path.exists(nombre_archivo):
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
        else:
            datos = {}
        # Guardar/actualizar usuario
        datos[username] = contrasena_haseada
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)
        print(f"Usuario '{username}' guardado exitosamente en {nombre_archivo}")
        return True
    except Exception as e:
        print(f"Error al guardar usuario: {e}")
        return False

def cargar_usuarios(nombre_archivo):
    try:
        if not os.path.exists(nombre_archivo):
            print("El archivo no existe")
            return {}
            
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
        print(f"Datos cargados exitosamente desde {nombre_archivo}")
        return datos
    except Exception as e:
        print(f"Error al cargar: {e}")
        return {}
    
def isExist(username, nombre_archivo):
            try:
                if not os.path.exists(nombre_archivo):
                    return False
                with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                    datos = json.load(archivo)
                return username in datos
            except Exception:
                return False
# Uso de las funciones
# mi_diccionario = {"clave": "valor", "numero": 42, "lista": [1, 2, 3]}
# guardar_diccionario(mi_diccionario, "users-db.json")
# datos_cargados = cargar_diccionario("users-db.json")
# print(datos_cargados)