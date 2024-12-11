import boto3
import json
from datetime import datetime

# Configuración directamente en el código
OUTPUT_FILE = ''  # El archivo CSV donde se guardarán los usuarios
ACCESS_KEY = ''  # Acceso programático (Access Key)
SECRET_KEY = ''  # Secret Key
SESSION_TOKEN = ''  # Token de sesión si usas credenciales temporales (opcional)

# Crear un cliente de Cognito
client = boto3.client('cognito-idp')

# Parámetros
user_pool_id = ''  # Reemplaza con tu User Pool ID
group_name = ''  # Reemplaza con el nombre del grupo

def list_users_in_group(user_pool_id, group_name):
    try:
        # Realizar la solicitud para obtener los usuarios en el grupo
        response = client.list_users_in_group(
            UserPoolId=user_pool_id,
            GroupName=group_name
        )

        # Función para convertir datetime a string
        def convert_datetime(obj):
            if isinstance(obj, datetime):
                return obj.isoformat()  # Convertir datetime a formato string
            raise TypeError("Type not serializable")

        # Guardar la respuesta en un archivo JSON, usando el conversor para datetime
        with open(f"{group_name}.json", 'w') as file:
            json.dump(response, file, default=convert_datetime, indent=4)
        # Genera un archivo con el mismo nombre del grupo
        print(f"Usuarios del grupo {group_name} guardados en {group_name}.json")

    except Exception as e:
        print(f"Error al obtener los usuarios: {str(e)}")

# Llamar a la función
list_users_in_group(user_pool_id, group_name)
