Este es un repo que tiene cositas y scriptsitos que me fueron utiles alguna vez como cloud engineer. 

¡Espero que te sirva como a mi!

## get-users-from-group-cognito.py
El código consulta a **AWS Cognito** por los usuarios en un grupo y guarda la respuesta en un archivo **JSON**.

### Explicación del Código

Este código realiza lo siguiente:

1. **Conexión a AWS Cognito**:  
   Utiliza la librería `boto3` para conectarse a **AWS Cognito** y acceder a la información de usuarios en un grupo específico dentro de un **User Pool**.

2. **Obtención de Usuarios**:  
   Llama al método `list_users_in_group` para obtener los usuarios que pertenecen a un grupo específico de Cognito, usando el **User Pool ID** y el **Group Name** proporcionados.

3. **Guardado de Datos**:  
   Guarda la respuesta completa (usuarios y sus detalles) en un archivo **JSON** llamado `<group_name>.json`. Usa la función `json.dump` para serializar la respuesta.




