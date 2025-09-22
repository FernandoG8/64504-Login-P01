# Sistema de Login con Tkinter y JSON  

Esta practica es una aplicación de escritorio en **Python** que implementa un sistema básico de **inicio de sesión y registro de usuarios** usando **Tkinter** para la interfaz gráfica y un archivo **JSON** como base de datos simple.  
## Pruebas de Usuario
- Deberá ejecutar python main.py
- Puede usar el siguiente Username: UsuarioPrueba
- Su contraseña es: Admin123

## Funcionalidades  
- **Registro de usuarios**  
  - Valida que la contraseña tenga al menos 8 caracteres y contenga números.  
  - Guarda las credenciales en un archivo `users_db.json`.  
  - Antes de registrar, verifica que el usuario no exista.  

- **Inicio de sesión**  
  - Verifica si el usuario existe en la base de datos.  
  - Comprueba la contraseña usando un **hash seguro SHA-256**.  
  - Si es correcto, abre un **Dashboard principal** con un mensaje de bienvenida.  

- **Gestión de usuarios**  
  - Los usuarios y contraseñas se guardan en formato JSON.  
  - Incluye funciones para guardar, cargar y comprobar existencia de usuarios.  

- **Interfaz gráfica (Tkinter (Proporcionada por el maestro))**  
  - Pantalla de inicio con campos de usuario y contraseña.  
  - Botones para **Iniciar Sesión**, **Registrarse** y **Limpiar**.  
  - Ventana de Dashboard tras login exitoso.

##  Estructura del proyecto  
- `saveJson.py` → Funciones para manejar el archivo JSON.  
- `secureHash.py` → Función para generar el hash de la contraseña con SHA-256.  
- `app.py` (principal) → Contiene la clase `LoginApp` con la interfaz Tkinter y la lógica de login/registro.  
- `users_db.json` → Archivo donde se almacenan los usuarios registrados.  

- `main.py` → Archivo que llamaremos **para ejecutar la app**.  

##  Seguridad  
- Las contraseñas **no se guardan en texto plano**, se guardan como un hash SHA-256.  


