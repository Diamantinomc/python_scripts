# Organizador de Archivos en Python

Este proyecto es un **script de automatización** en Python que organiza archivos de una carpeta según su tipo (documentos, imágenes, audios, videos, otros) y los clasifica por **año de creación**.

## 🚀 Características
- Clasifica por extensión de archivo.
- Agrupa en carpetas según el año.
- Fácil de configurar y usar.

## 🛠️ Tecnologías
- Python 3
- Librerías estándar: os, shutil, datetime

## 📂 Ejemplo de resultado

Carpeta_Organizada/

├── Documentos/

│ ├── 2024/

│ ├── informe.pdf

├── Imagenes/

│ ├── 2023/

│ ├── foto.png


## ▶️ Uso
1. Coloca tus archivos en la carpeta `archivos_desordenados/`.
2. Ejecuta:
   ```bash
   python organizador.py
3. Revisa la carpeta archivos_organizados.

## 🔮 Posibles mejoras
- Agregar logs en un archivo CSV para registrar los movimientos.
- Permitir al usuario elegir la carpeta de origen y destino desde la terminal.
- Implementar una interfaz gráfica con Tkinter o PyQt.
- Detectar duplicados y renombrarlos automáticamente.
- Añadir más categorías de archivos (ej. archivos comprimidos, código fuente).
