import os

ruta = "/var/www/html/dam2526"

for directorio, subdirectorios, archivos in os.walk(ruta):
    print(f"Directorio: {directorio}")
    for sub in subdirectorios:
        print(f"  Subdirectorio: {sub}")
    for archivo in archivos:
        print(f"  Archivo: {archivo}")
