import os
import shutil
from datetime import datetime

# Carpeta a organizar
CARPETA_ORIGEN = "archivos_desordenados"
CARPETA_DESTINO = "archivos_organizados"

# Clasificación por tipo de archivo
CATEGORIAS = {
    "Documentos" : [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Imágenes"   : [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Audios"    : [".mp3", ".wav", ".aac", ".flac"],
    "Videos"     : [".mp4", ".avi", ".mov", ".mkv"],
    "Otros"      : []
}

def obtener_categoria(extension):
    for categoria, extensiones in CATEGORIAS.items():
        if extension.lower() in extensiones:
            return categoria
    return "Otros"

def organizar_archivos():
    if not os.path.exists(CARPETA_DESTINO):
        os.makedirs(CARPETA_DESTINO)

    for archivo in os.listdir(CARPETA_ORIGEN):
        ruta_archivo = os.path.join(CARPETA_ORIGEN, archivo)



        if os.path.isfile(ruta_archivo):
            extension = os.path.splitext(archivo)[1]
            categoria = obtener_categoria(extension)

            # Obtener año de creación del archivo
            timestamp = os.path.getctime(ruta_archivo)
            año = datetime.fromtimestamp(timestamp).year

            # Crear ruta de destino
            carpeta_categoria = os.path.join(CARPETA_DESTINO, categoria, str(año))
            os.makedirs(carpeta_categoria, exist_ok=True)

            #Mover archivo
            ruta_destino = os.path.join(carpeta_categoria, archivo)
            shutil.move(ruta_archivo, ruta_destino)
            print(f"Movido: {archivo} a {ruta_destino}")

if __name__ == "__main__":
    organizar_archivos()
    print("Organización de archivos completada.")

