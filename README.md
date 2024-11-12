[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/U2iXA-EO)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=16811675)

 <!-- 
 Documentación para instalar y configurar el proyecto de: Javier, Alberto y Benjamín

Primer paso:
Clonar el repositorio con el comando git clone y la dirección del enlace a clonar.

Segundo paso:
Agregar un archivo .gitignore para indicarle a Git qué archivos no debe rastrear ni subir al repositorio, y un archivo .env para dejar los datos de la base de datos que se utilizarán.

Tercer paso:
Instalar Python en Visual Studio Code.

Cuarto paso:
Agregar un archivo requirements.txt para listar todas las dependencias o bibliotecas necesarias para ejecutar el proyecto.

Quinto paso:
Instalar las dependencias del archivo requirements.txt. Para hacerlo, abre requirements.txt, presiona CTRL+SHIFT+P en la barra superior y selecciona la opción “Python: Create Environment”. Después, elige la opción “venv” para crear el entorno virtual .venv. Luego, selecciona la versión de Python que tengas instalada y selecciona el archivo requirements.txt, luego da clic en "Aceptar". Esto creará el entorno virtual. Una vez instalado, verifica en el terminal (usando "Command Prompt") que aparezca (.venv).

Sexto paso:
Instalar AppServer y configurarlo con el usuario “root” y la contraseña “12345678”. Los datos de usuario y contraseña pueden ser diferentes, pero se recomienda usar estos para un entorno local de trabajo.

Séptimo paso:
Acceder a phpMyAdmin con los datos de usuario utilizados al instalar AppServer. Escribe 127.0.0.1 en la barra de búsqueda del navegador.

Octavo paso:
Crear la base de datos con el nombre que está en el archivo .env.

Noveno paso:
Crear una cuenta de usuario con el nombre y contraseña que están en el archivo .env.

Décimo paso:
Editar los privilegios del usuario creado. En la sección de bases de datos, selecciona la base creada para el proyecto, da clic en "Continuar" y luego selecciona "Todo" en los privilegios globales. Finalmente, haz clic en "Continuar". Con esto, las configuraciones de la base de datos estarán listas.

Undécimo paso:
Abrir el terminal en el proyecto y ejecutar los comandos python manage.py makemigrations y python manage.py migrate para tener los datos del proyecto en la base de datos.

Duodécimo paso:
En el terminal, abrir el proyecto con el comando python manage.py runserver. Con esto, podrás comenzar a utilizar el proyecto.
 -->