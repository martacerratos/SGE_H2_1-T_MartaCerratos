PASOS PARA EJECUTAR EL PROGRAMA
1. Como instalar TKinter
  Primero debemos de tener Python correctamente instalado con tkinter incluido. Puedes comprobar si tiene tkinter ejecutando un "import tkinter" en la terminal de python.
2. Como instalar MySQL Workbench
   Ve a la página oficial de MySQL, selecciona la versión adecuada para tu sistema operativo y haz clic en Download.
   Realiza la instalación siguiendo las instrucciones del instalador.
3. Configurar MySQL Workbench para Conectarse a MySQL Server
   Abre MySQL Workbench e inicialo.
   Ingresa la información de tu servidor, con tu hostname, puerto, nombre de usuario y contraseña.
   Si todo lo anterior funciona correctamente, guarda la conexión y haz clic en ella para comenzar a administrar tus bases de datos.
4. Conectar la base de datos del ejercicio con MySQL Workbench
   Abrimos la aplicación y nada más iniciada le damos a File arriba a la izquierda y le damos a Open SQL Script.
   Seleccionamos la base de datos de este ejercicio y lo agregamos.
   Lo ejecutamos y ya lo tendriamos para usarlo en nuestro programa de tkinter.
5. Iniciar el programa con Visual Studio
   Abrimos Visual Studio, le damos a Archivo -> Abrir carpeta y seleccionamos la carpeta donde hayamos guardado nuestro script de python.
   En la función conectar_db debemos cambiar el host, user y password que hayamos creado anteriormente en MySQL Workbench para que se conecte con nuestras credenciales.
   Abrimos el archivo lo ejecutamos con el icono de play que nos aparece arriba a la derecha.
   Y finalmente tendríamos nuestro programa en ejecución.
