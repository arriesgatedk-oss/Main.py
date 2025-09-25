import os
import json
import logging
from android.permissions import request_permissions, Permission

# Configura el logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define el archivo donde se guardarán los permisos
output_file = "/sdcard/Download/permissions.json"

# Lista de permisos que vamos a solicitar
permissions_to_request = [
    Permission.CAMERA,
    Permission.READ_EXTERNAL_STORAGE,
    Permission.WRITE_EXTERNAL_STORAGE,
    Permission.RECORD_AUDIO
]

def on_permissions_result(permissions, results):
    """
    Función que se ejecuta después de que el usuario acepta o niega los permisos.
    """
    logging.info("Resultados de permisos recibidos.")
    
    # Crea un diccionario con los resultados
    permission_status = {
        perm: bool(res) for perm, res in zip(permissions, results)
    }

    # Guarda el diccionario en un archivo JSON
    with open(output_file, 'w') as f:
        json.dump(permission_status, f, indent=4)
        
    logging.info(f"Permisos guardados en: {output_file}")
    
    # Cierra la aplicación de forma segura
    import android
    android.activity.finish()

if __name__ == '__main__':
    logging.info("Iniciando solicitud de permisos...")
    request_permissions(permissions_to_request, on_permissions_result)
