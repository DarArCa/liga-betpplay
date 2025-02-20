import json
import os

ARCHIVO_DATOS = "datos.json"

def cargar_datos():
    if not os.path.exists(ARCHIVO_DATOS):
        return {"equipos": {}, "partidos": []}  # Asegura que sea un diccionario
    
    with open(ARCHIVO_DATOS, "r") as archivo:
        try:
            datos = json.load(archivo)
            if not isinstance(datos, dict):  # Si el archivo tiene una lista en vez de un diccionario
                return {"equipos": {}, "partidos": []}
            return datos
        except json.JSONDecodeError:
            return {"equipos": {}, "partidos": []}  # Reinicia si el JSON está corrupto

def guardar_datos(torneo):
    with open(ARCHIVO_DATOS, "w") as archivo:
        json.dump(torneo, archivo, indent=4)
