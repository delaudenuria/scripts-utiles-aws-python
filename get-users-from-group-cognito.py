import boto3
import json

ACCESS_KEY = ''  # Acceso programático (Access Key)
SECRET_KEY = ''  # Secret Key
SESSION_TOKEN = ''  # Token de sesión 
user_pool_id = ''  # Reemplaza con tu User Pool ID
group_name = ''  # Reemplaza con el nombre del grupo

# Crear un cliente de Cognito
client = boto3.client('cognito-idp')

def list_users_in_group(user_pool_id, group_name):
    try:
        # Realizar la solicitud para obtener los usuarios en el grupo
        response = client.list_users_in_group(
            UserPoolId=user_pool_id,
            GroupName=group_name
        )

        # Guardar la respuesta en un archivo JSON
        with open(f"{group_name}.json", 'w') as file:
            json.dump(response, file, default=str, indent=4)

        print(f"Usuarios del grupo {group_name} guardados en {group_name}.json")

    except Exception as e:
        print(f"Error al obtener los usuarios: {str(e)}")

# Llamar a la función
list_users_in_group(user_pool_id, group_name)
