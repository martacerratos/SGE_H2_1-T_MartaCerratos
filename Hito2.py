from tkinter import filedialog
import pandas as pd
import tkinter as tk
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Función para conectar a la base de datos MySQL
def conectar_db():
    try:
        conexion = mysql.connector.connect(
            host="localhost",       # Servidor donde está alojada la base de datos
            user="root",            # Usuario de la base de datos
            password="campusfp",    # Contraseña de la base de datos
            database="ENCUESTAS"    # Nombre de la base de datos
        )
        return conexion     # Si la conexión es exitosa, la devolvemos
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se puede conectar a la base de datos: {err}")
        return None

# Funciones para cargar los datos en los ComboBox   
def cargar_DiversionDependenciaAlcohol():
    conexion = conectar_db()
    if conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT DISTINCT DiversionDependenciaAlcohol FROM ENCUESTA")
            DiversionDependenciaAlcohol_mostrar = [str(row[0]) for row in cursor.fetchall()]
            comboDependencia['values'] = DiversionDependenciaAlcohol_mostrar
        except mysql.connector.Error as err:
            messagebox.showerror("ERROR", f"No se pueden cargar los valores de años: {err}")
        finally:
            cursor.close()
            conexion.close()

def cargar_ProblemasDigestivos():
    conexion = conectar_db()
    if conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT DISTINCT ProblemasDigestivos FROM ENCUESTA")
            ProblemasDigestivos_mostrar = [str(row[0]) for row in cursor.fetchall()]
            comboProblemDigestivo['values'] = ProblemasDigestivos_mostrar
        except mysql.connector.Error as err:
            messagebox.showerror("ERROR", f"No se pueden cargar los valores de años: {err}")
        finally:
            cursor.close()
            conexion.close()

def cargar_TensionAlta():
    conexion = conectar_db()
    if conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT DISTINCT TensionAlta FROM ENCUESTA")
            TensionAlta_mostrar = [str(row[0]) for row in cursor.fetchall()]
            comboTensionAlta['values'] = TensionAlta_mostrar
        except mysql.connector.Error as err:
            messagebox.showerror("ERROR", f"No se pueden cargar los valores de años: {err}")
        finally:
            cursor.close()
            conexion.close()

def cargar_DolorCabeza():
    conexion = conectar_db()
    if conexion:
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT DISTINCT DolorCabeza FROM ENCUESTA")
            DolorCabeza_mostrar = [str(row[0]) for row in cursor.fetchall()]
            comboDolorCabeza['values'] = DolorCabeza_mostrar
        except mysql.connector.Error as err:
            messagebox.showerror("ERROR", f"No se pueden cargar los valores de años: {err}")
        finally:
            cursor.close()
            conexion.close()

# Función para crear un nuevo cliente y guardarlo en la base de datos
def crear_cliente():
    conexion = conectar_db()  # Establecemos conexión con la base de datos
    if conexion:
        cursor = conexion.cursor()  # Creamos un cursor para ejecutar comandos SQL

        # Recogemos los datos desde los campos de entrada de la interfaz gráfica
        edad = entry_edad.get()
        Sexo = entry_sexo.get()
        BebidasSemana = entry_BebidasSemana.get()
        CervezaSemana = entry_CervezaSemana.get()
        BebidasFinSemana = entry_BebidasFinSemana.get()
        BebidasDestiladasSemana = entry_BebidasDestiladasSemana.get()
        VinosSemana = entry_VinosSemana.get()
        PerdidasControl = entry_PerdidasControl.get()
        DiversionDependenciaAlcohol = comboDependencia.get()
        ProblemasDigestivos = comboProblemDigestivo.get()
        TensionAlta = comboTensionAlta.get()
        DolorCabeza = comboDolorCabeza.get()

        try:
            # Ejecutamos una consulta SQL para insertar los datos en la tabla ENCUESTA
            cursor.execute(
                "INSERT INTO ENCUESTA(edad, Sexo, BebidasSemana, CervezasSemana, BebidasFinSemana, BebidasDestiladasSemana, VinosSemana, PerdidasControl, DiversionDependenciaAlcohol, ProblemasDigestivos, TensionAlta, DolorCabeza) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (edad, Sexo, BebidasSemana, CervezaSemana, BebidasFinSemana, BebidasDestiladasSemana, VinosSemana, PerdidasControl, DiversionDependenciaAlcohol, ProblemasDigestivos, TensionAlta, DolorCabeza)
            )
            conexion.commit()  # Confirmamos los cambios en la base de datos
            messagebox.showinfo("Correcto", "Cliente ingresado")  # Mostramos un mensaje de éxito
            mostrarClientes()  # Actualizamos la lista de clientes
        except Exception as err:
            # Si ocurre un error, mostramos un mensaje con la información del error
            messagebox.showerror("Error", f"No se puede ingresar: {err}")
        finally:
            # Cerramos el cursor y la conexión a la base de datos
            cursor.close()
            conexion.close()

# Función para mostrar todos los clientes en la lista de la interfaz
def mostrarClientes():
    conexion = conectar_db()  # Establecemos conexión con la base de datos
    if conexion:
        cursor = conexion.cursor()  # Creamos un cursor para ejecutar comandos SQL
        try:
            lista_clientes.delete(0, tk.END)  # Borramos el contenido actual de la lista de clientes
            cursor.execute("SELECT * FROM ENCUESTA")  # Ejecutamos una consulta para obtener todos los registros
            for cliente in cursor.fetchall():
                # Añadimos cada cliente a la lista de clientes en la interfaz gráfica
                lista_clientes.insert(tk.END, cliente)
        except mysql.connector.Error as err:
            # Si ocurre un error, mostramos un mensaje con la información del error
            messagebox.showerror("Error", f"No se puede mostrar los clientes: {err}")
        finally:
            # Cerramos el cursor y la conexión a la base de datos
            cursor.close()
            conexion.close()

# Función para mostrar los datos del cliente seleccionado en los campos de texto
def seleccionarCliente(event):
    try:
        indice = lista_clientes.curselection()[0]  # Obtenemos el índice del cliente seleccionado en la lista
        cliente = lista_clientes.get(indice)  # Recuperamos los datos del cliente seleccionado

        # Actualizamos los campos de la interfaz con la información del cliente seleccionado
        entry_cod.config(state=tk.NORMAL)  # Activamos el campo "Código" para editarlo
        entry_cod.delete(0, tk.END)  # Borramos el contenido actual del campo "Código"
        entry_cod.insert(tk.END, cliente[0])  # Insertamos el código del cliente
        entry_cod.config(state=tk.DISABLED)  # Desactivamos el campo "Código" para que no se pueda modificar

        # Actualizamos el resto de los campos con la información del cliente
        entry_edad.delete(0, tk.END)
        entry_edad.insert(tk.END, cliente[1])

        entry_sexo.delete(0, tk.END)
        entry_sexo.insert(tk.END, cliente[2])

        entry_BebidasSemana.delete(0, tk.END)
        entry_BebidasSemana.insert(tk.END, cliente[3])

        entry_CervezaSemana.delete(0, tk.END)
        entry_CervezaSemana.insert(tk.END, cliente[4])

        entry_BebidasFinSemana.delete(0, tk.END)
        entry_BebidasFinSemana.insert(tk.END, cliente[5])

        entry_BebidasDestiladasSemana.delete(0, tk.END)
        entry_BebidasDestiladasSemana.insert(tk.END, cliente[6])

        entry_VinosSemana.delete(0, tk.END)
        entry_VinosSemana.insert(tk.END, cliente[7])

        entry_PerdidasControl.delete(0, tk.END)
        entry_PerdidasControl.insert(tk.END, cliente[8])

        # Establecemos los valores seleccionados de los ComboBoxes
        comboDependencia.set(cliente[9])
        comboProblemDigestivo.set(cliente[10])
        comboTensionAlta.set(cliente[11])
        comboDolorCabeza.set(cliente[12])

    except IndexError:
        # Si no hay un cliente seleccionado no hacemos nada
        pass

#Función para actualizar un cliente
def actualizarCliente():
    conexion = conectar_db()  # Establece una conexión con la base de datos
    if conexion:
        cursor = conexion.cursor()  # Crea un cursor para ejecutar las consultas
        
        # Se recogen los datos actualizados desde los campos de entrada en la interfaz gráfica
        cod = entry_cod.get()
        edad = entry_edad.get()
        sexo = entry_sexo.get()
        BebidasSemana = entry_BebidasSemana.get()
        CervezaSemana = entry_CervezaSemana.get()
        BebidasFinSemana = entry_BebidasFinSemana.get()
        BebidasDestiladasSemana = entry_BebidasDestiladasSemana.get()
        VinosSemana = entry_VinosSemana.get()
        PerdidasControl = entry_PerdidasControl.get()
        DiversionDependenciaAlcohol = comboDependencia.get()
        ProblemasDigestivos = comboProblemDigestivo.get()
        TensionAlta = comboTensionAlta.get()
        DolorCabeza = comboDolorCabeza.get()

        try:
            # Se ejecuta una consulta SQL para actualizar el cliente en la base de datos
            cursor.execute(
                "UPDATE ENCUESTA SET edad=%s, Sexo=%s, BebidasSemana=%s, CervezasSemana=%s, BebidasFinSemana=%s, BebidasDestiladasSemana=%s, VinosSemana=%s, PerdidasControl=%s, DiversionDependenciaAlcohol=%s, ProblemasDigestivos=%s, TensionAlta=%s, DolorCabeza=%s WHERE idEncuesta=%s",
                (edad, sexo, BebidasSemana, CervezaSemana, BebidasFinSemana, BebidasDestiladasSemana, VinosSemana, PerdidasControl, DiversionDependenciaAlcohol, ProblemasDigestivos, TensionAlta, DolorCabeza, cod)
            )
            conexion.commit()  # Se confirman los cambios en la base de datos
            messagebox.showinfo("Correcto", "Cliente Actualizado correctamente")  # Muestra un mensaje de éxito
            mostrarClientes()  # Actualiza la lista de clientes en la interfaz
        except mysql.connector.Error as err:
            # En caso de error, muestra un mensaje con la descripción del error
            messagebox.showerror("Error", f"Cliente no actualizado: {err}")
        finally:
            cursor.close()  # Cierra el cursor
            conexion.close()  # Cierra la conexión con la base de datos

#Función Eliminar
def eliminarCliente():
    conexion = conectar_db()  # Establece una conexión con la base de datos
    if conexion:
        cursor = conexion.cursor()  # Crea un cursor para ejecutar las consultas
        cod = entry_cod.get()  # Obtiene el código del cliente desde el campo de entrada
        
        try:
            # Ejecuta una consulta SQL para eliminar el cliente de la base de datos
            cursor.execute("DELETE FROM ENCUESTA WHERE idEncuesta=%s", (cod,))
            conexion.commit()  # Se confirman los cambios en la base de datos
            messagebox.showinfo("Correcto", "Cliente Eliminado correctamente")  # Muestra un mensaje de éxito
            mostrarClientes()  # Actualiza la lista de clientes en la interfaz
        except mysql.connector.Error as err:
            # En caso de error, muestra un mensaje con la descripción del error
            messagebox.showerror("Error", f"Cliente no eliminado: {err}")
        finally:
            cursor.close()  # Cierra el cursor
            conexion.close()  # Cierra la conexión con la base de datos

#Función Limpiar
def limpiarCampos():
    entry_cod.config(state=tk.NORMAL)  # Habilita el campo de "Código" para editarlo
    entry_cod.delete(0, tk.END)  # Borra el contenido del campo de "Código"
    entry_cod.config(state=tk.DISABLED)  # Desactiva el campo de "Código" para que no se pueda modificar
    
    # Borra el contenido de los campos de entrada
    entry_edad.delete(0, tk.END)
    entry_sexo.delete(0, tk.END)
    entry_BebidasSemana.delete(0, tk.END)
    entry_CervezaSemana.delete(0, tk.END)
    entry_BebidasFinSemana.delete(0, tk.END)
    entry_BebidasDestiladasSemana.delete(0, tk.END)
    entry_VinosSemana.delete(0, tk.END)
    entry_PerdidasControl.delete(0, tk.END)
    
    # Restablece los ComboBoxes a su estado inicial
    comboDependencia.set("")
    comboProblemDigestivo.set("")
    comboTensionAlta.set("")
    comboDolorCabeza.set("")

# Función para exportar los datos a Excel
def exportarAExcel():
    conexion = conectar_db()
    if conexion:
        cursor = conexion.cursor()
        try:
            # Ejecutar la consulta para obtener todos los datos de la tabla
            cursor.execute("SELECT * FROM ENCUESTA")
            # Obtener los datos de la base de datos
            datos = cursor.fetchall()

            # Definir los nombres de las columnas de la base de datos
            columnas = ['idEncuesta', 'edad', 'Sexo', 'BebidasSemana', 'CervezaSemana', 'BebidasFinSemana',
                        'BebidasDestiladasSemana', 'VinosSemana', 'PerdidasControl', 'DiversionDependenciaAlcohol',
                        'ProblemasDigestivos', 'TensionAlta', 'DolorCabeza']
            
            # Crear un DataFrame de pandas con los datos obtenidos
            df = pd.DataFrame(datos, columns=columnas)

            # Abrir un cuadro de diálogo para que el usuario seleccione dónde guardar el archivo
            archivo_guardar = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Archivos Excel", "*.xlsx")])

            if archivo_guardar:  # Verificar si el usuario ha seleccionado una ubicación
                # Guardar el DataFrame en un archivo Excel
                df.to_excel(archivo_guardar, index=False, engine='openpyxl')
                messagebox.showinfo("Éxito", "Datos exportados correctamente a Excel")
            else:
                messagebox.showwarning("Advertencia", "No se seleccionó ninguna ubicación para guardar el archivo")

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"No se puede exportar a Excel: {err}")
        finally:
            cursor.close()
            conexion.close()

# Función para mostrar solo las personas que tienen dolor de cabeza muy a menudo
def mostrarDolorCabeza():
    conexion = conectar_db()  # Intentamos conectar con la base de datos
    if conexion:
        cursor = conexion.cursor()  # Creamos el cursor para ejecutar la consulta
        # Realizamos una consulta que filtra las personas con "DolorCabeza" = "Muy A menudo"
        cursor.execute(" SELECT * FROM ENCUESTA WHERE DolorCabeza = 'Muy A menudo'")
        resultados = cursor.fetchall()  # Obtenemos todos los resultados de la consulta

        # Si no hay resultados, mostramos un mensaje
        if not resultados:
            messagebox.showinfo("Sin resultados", "No se encontraron personas con dolor de cabeza muy a menudo.")
        else:
            # Creamos una ventana para mostrar los resultados
            ventana_resultados = tk.Toplevel(ventana)  # Crear una nueva ventana
            ventana_resultados.title("Resultados de Dolor de Cabeza Muy A Menudo")

            # Mostramos cada registro en una fila de la ventana
            for index, resultado in enumerate(resultados, start=1):
                tk.Label(ventana_resultados, text=" | ".join(map(str, resultado))).grid(row=index, column=0)
        
        conexion.close()  # Cerramos la conexión a la base de datos

# Función para mostrar solo las personas que tienen tensión alta
def mostrarTensionAlta():
    conexion = conectar_db()  # Intentamos conectar con la base de datos
    if conexion:
        cursor = conexion.cursor()  # Creamos el cursor para ejecutar la consulta
        # Realizamos una consulta que filtra las personas con "TensionAlta" = "Sí"
        cursor.execute("SELECT * FROM ENCUESTA WHERE TensionAlta = 'Sí'")
        resultados = cursor.fetchall()  # Obtenemos todos los resultados de la consulta

        # Si no hay resultados, mostramos un mensaje
        if not resultados:
            messagebox.showinfo("Sin resultados", "No se encontraron personas con tensión alta.")
        else:
            # Creamos una ventana para mostrar los resultados
            ventana_resultados = tk.Toplevel(ventana)  # Crear una nueva ventana
            ventana_resultados.title("Resultados de Tensión Alta")

            # Mostramos cada registro en una fila de la ventana
            for index, resultado in enumerate(resultados, start=1):
                tk.Label(ventana_resultados, text=" | ".join(map(str, resultado))).grid(row=index, column=0)
        
        conexion.close()  # Cerramos la conexión a la base de datos

# Función para mostrar solo las personas que NO tienen problemas digestivos
def mostrarSinProblemasDigestivos():
    conexion = conectar_db()  # Intentamos conectar con la base de datos
    if conexion:
        cursor = conexion.cursor()  # Creamos el cursor para ejecutar la consulta
        # Realizamos una consulta que filtra las personas con "ProblemasDigestivos" != "Sí"
        cursor.execute(" SELECT * FROM ENCUESTA WHERE ProblemasDigestivos != 'Sí'")
        resultados = cursor.fetchall()  # Obtenemos todos los resultados de la consulta

        # Si no hay resultados, mostramos un mensaje
        if not resultados:
            messagebox.showinfo("Sin resultados", "No se encontraron personas sin problemas digestivos.")
        else:
            # Creamos una ventana para mostrar los resultados
            ventana_resultados = tk.Toplevel(ventana)  # Crear una nueva ventana
            ventana_resultados.title("Resultados sin problemas digestivos")

            # Mostramos cada registro en una fila de la ventana
            for index, resultado in enumerate(resultados, start=1):
                tk.Label(ventana_resultados, text=" | ".join(map(str, resultado))).grid(row=index, column=0)
        
        conexion.close()  # Cerramos la conexión a la base de datos 

def filtrarClientes():
    # Obtener los valores de los filtros
    edad = entry_edad.get()
    sexo = entry_sexo.get()
    bebidas_semana = entry_BebidasSemana.get()
    cerveza_semana = entry_CervezaSemana.get()
    bebidas_fin_semana = entry_BebidasFinSemana.get()
    bebidas_destiladas_semana = entry_BebidasDestiladasSemana.get()
    vinos_semana = entry_VinosSemana.get()
    perdidas_control = entry_PerdidasControl.get()
    diversion_dependencia = comboDependencia.get()
    problemas_digestivos = comboProblemDigestivo.get()
    tension_alta = comboTensionAlta.get()
    dolor_cabeza = comboDolorCabeza.get()

    # Conectar a la base de datos
    conexion = conectar_db()
    if conexion:
        cursor = conexion.cursor()

        # Construir la consulta con condiciones dinámicas
        consulta = "SELECT * FROM ENCUESTA WHERE 1=1"  # Parte base de la consulta
        
        parametros = []  # Para almacenar los parámetros de la consulta

        # Añadir condiciones a la consulta si los filtros no están vacíos
        if edad:
            consulta += " AND edad=%s"
            parametros.append(edad)
        if sexo:
            consulta += " AND Sexo=%s"
            parametros.append(sexo)
        if bebidas_semana:
            consulta += " AND BebidasSemana=%s"
            parametros.append(bebidas_semana)
        if cerveza_semana:
            consulta += " AND CervezaSemana=%s"
            parametros.append(cerveza_semana)
        if bebidas_fin_semana:
            consulta += " AND BebidasFinSemana=%s"
            parametros.append(bebidas_fin_semana)
        if bebidas_destiladas_semana:
            consulta += " AND BebidasDestiladasSemana=%s"
            parametros.append(bebidas_destiladas_semana)
        if vinos_semana:
            consulta += " AND VinosSemana=%s"
            parametros.append(vinos_semana)
        if perdidas_control:
            consulta += " AND PerdidasControl=%s"
            parametros.append(perdidas_control)
        if diversion_dependencia:
            consulta += " AND DiversionDependenciaAlcohol=%s"
            parametros.append(diversion_dependencia)
        if problemas_digestivos:
            consulta += " AND ProblemasDigestivos=%s"
            parametros.append(problemas_digestivos)
        if tension_alta:
            consulta += " AND TensionAlta=%s"
            parametros.append(tension_alta)
        if dolor_cabeza:
            consulta += " AND DolorCabeza=%s"
            parametros.append(dolor_cabeza)

        try:
            # Ejecutar la consulta con los parámetros
            cursor.execute(consulta, tuple(parametros))
            # Obtener los resultados filtrados
            resultados = cursor.fetchall()

            # Limpiar la lista actual de clientes
            lista_clientes.delete(0, tk.END)

            # Insertar los resultados filtrados en la lista
            for cliente in resultados:
                lista_clientes.insert(tk.END, cliente)

            if not resultados:
                messagebox.showinfo("Información", "No se encontraron resultados para los filtros aplicados")

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al filtrar los datos: {err}")
        finally:
            cursor.close()
            conexion.close()

def generarGrafico():
    # Recoger los resultados filtrados de la lista de clientes
    resultados_filtrados = [lista_clientes.get(i) for i in range(lista_clientes.size())]

    if not resultados_filtrados:
        messagebox.showinfo("Información", "No hay datos filtrados para generar el gráfico.")
        return

    # Crear las listas con los datos para el gráfico
    edades = [str(cliente[1]) for cliente in resultados_filtrados]
    bebidas_semana = [int(cliente[3]) for cliente in resultados_filtrados]
    cerveza_semana = [int(cliente[4]) for cliente in resultados_filtrados]
    bebidas_destiladas = [int(cliente[6]) for cliente in resultados_filtrados]
    vinos_semana = [int(cliente[7]) for cliente in resultados_filtrados]

    # Crear la nueva ventana para mostrar el gráfico
    ventana_grafico = tk.Toplevel(ventana)
    ventana_grafico.title("Gráfico de Consumo de Bebidas")

    # Crear el gráfico según la selección del usuario
    tipo_grafico = comboGrafico.get()
    fig, ax = plt.subplots(figsize=(9, 4))

    if tipo_grafico == "Barras":
        # Crear barras
        ax.bar(edades, bebidas_semana, label="Bebidas por semana")
        ax.bar(edades, cerveza_semana, label="Cervezas por semana", alpha=0.7)
        ax.bar(edades, bebidas_destiladas, label="Bebidas destiladas por semana", alpha=0.5)
        ax.bar(edades, vinos_semana, label="Vinos por semana", alpha=0.3)
    elif tipo_grafico == "Líneas":
        # Crear líneas
        ax.plot(edades, bebidas_semana, label="Bebidas por semana", marker='o')
        ax.plot(edades, cerveza_semana, label="Cervezas por semana", marker='x')
        ax.plot(edades, bebidas_destiladas, label="Bebidas destiladas por semana", marker='^')
        ax.plot(edades, vinos_semana, label="Vinos por semana", marker='s')
    elif tipo_grafico == "Circular":
        # Crear gráfico circular (solo para una categoría)
        total_bebidas = sum(bebidas_semana)
        ax.pie([total_bebidas, sum(cerveza_semana), sum(bebidas_destiladas)], 
               labels=["Bebidas por semana", "Cervezas", "Destiladas"], autopct='%1.1f%%')

    ax.set_ylabel('Cantidad')
    ax.set_xlabel('Edad')
    ax.set_title('Gráfico de Consumo de Bebidas')
    ax.legend()

    # Mostrar el gráfico en la nueva ventana
    canvas = FigureCanvasTkAgg(fig, ventana_grafico)
    canvas.get_tk_widget().pack()
    canvas.draw()

#Crear ventana con titulo
ventana = tk.Tk()
ventana.title("Gestión de Encuestas")

#Campos a rellenar
tk.Label(ventana, text="Código: ").grid(row=0, column=0, padx=5, pady=3, sticky="e")
entry_cod = tk.Entry(ventana, state=tk.DISABLED)
entry_cod.grid(row=0, column=1)

tk.Label(ventana, text="Edad: ").grid(row=1, column=0, padx=5, pady=3, sticky="e")
entry_edad = tk.Entry(ventana)
entry_edad.grid(row=1, column=1)

tk.Label(ventana, text="Sexo: ").grid(row=2, column=0, padx=5, pady=3, sticky="e")
entry_sexo = tk.Entry(ventana)
entry_sexo.grid(row=2, column=1)

tk.Label(ventana, text="Num Bebidas por Semana: ").grid(row=3, column=0, padx=5, pady=3, sticky="e")
entry_BebidasSemana = tk.Entry(ventana)
entry_BebidasSemana.grid(row=3, column=1)

tk.Label(ventana, text="Num Cervezas por Semana: ").grid(row=4, column=0, padx=5, pady=3, sticky="e")
entry_CervezaSemana = tk.Entry(ventana)
entry_CervezaSemana.grid(row=4, column=1)

tk.Label(ventana, text="Num Bebidas por Fin de Semana: ").grid(row=5, column=0, padx=5, pady=3, sticky="e")
entry_BebidasFinSemana = tk.Entry(ventana)
entry_BebidasFinSemana.grid(row=5, column=1)

tk.Label(ventana, text="Num Bebidas Destiladas por Semana: ").grid(row=6, column=0, padx=5, pady=3, sticky="e")
entry_BebidasDestiladasSemana = tk.Entry(ventana)
entry_BebidasDestiladasSemana.grid(row=6, column=1)

tk.Label(ventana, text="Num Vinos por Semana: ").grid(row=7, column=0, padx=5, pady=3, sticky="e")
entry_VinosSemana = tk.Entry(ventana)
entry_VinosSemana.grid(row=7, column=1)

tk.Label(ventana, text="Num Perdidas de control: ").grid(row=8, column=0, padx=5, pady=3, sticky="e")
entry_PerdidasControl = tk.Entry(ventana)
entry_PerdidasControl.grid(row=8, column=1)

tk.Label(ventana, text="Diversion Dependencia Alcohol: ").grid(row=9, column=0, padx=5, pady=3, sticky="e")
comboDependencia = ttk.Combobox(ventana, state="readonly")
comboDependencia.grid(row=9, column= 1, padx=5, pady=3)

tk.Label(ventana, text="Problemas Digestivos: ").grid(row=10, column=0, padx=5, pady=3, sticky="e")
comboProblemDigestivo = ttk.Combobox(ventana, state="readonly")
comboProblemDigestivo.grid(row=10, column= 1, padx=5, pady=3)

tk.Label(ventana, text="Tension Alta: ").grid(row=11, column=0, padx=5, pady=3, sticky="e")
comboTensionAlta = ttk.Combobox(ventana, state="readonly")
comboTensionAlta.grid(row=11, column= 1, padx=5, pady=3)

tk.Label(ventana, text="Dolor Cabeza: ").grid(row=12, column=0, padx=5, pady=3, sticky="e")
comboDolorCabeza = ttk.Combobox(ventana, state="readonly")
comboDolorCabeza.grid(row=12, column= 1, padx=5, pady=3)

#Botones
tk.Button(ventana, text="Ingresar", command=crear_cliente, font=("Arial", 10), width=15 ).grid(row=14, column=0, padx=5, pady=3)
tk.Button(ventana, text="Actualizar", command=actualizarCliente, font=("Arial", 10), width=15).grid(row=14, column=1, padx=5, pady=3)
tk.Button(ventana, text="Eliminar", command=eliminarCliente, font=("Arial", 10), width=15).grid(row=15, column=0, padx=5, pady=3)
tk.Button(ventana, text="Limpiar", command=limpiarCampos, font=("Arial", 10), width=15).grid(row=15, column=1, padx=5, pady=3)
tk.Button(ventana, text="Filtrar", command=filtrarClientes, font=("Arial", 10), width=15).grid(row=16, column=0, padx=5, pady=3)
tk.Button(ventana, text="Exportar Excel", command=exportarAExcel, font=("Arial", 10), width=15).grid(row=16, column=1, padx=5, pady=3)
tk.Button(ventana, text="Mostrar todo", command=mostrarClientes, font=("Arial", 10), width=15).grid(row=17, column=1, padx=5, pady=3)
tk.Button(ventana, text="Personas Dolor Cabeza", command=mostrarDolorCabeza, font=("Arial", 10), width=18).grid(row=17, column=0, padx=5, pady=3)
tk.Button(ventana, text="Tensión Alta", command=mostrarTensionAlta, font=("Arial", 10), width=15).grid(row=18, column=1, padx=5, pady=3)
tk.Button(ventana, text="Sin problemas digestivos", command=mostrarSinProblemasDigestivos, font=("Arial", 10), width=18).grid(row=18, column=0, padx=5, pady=3)

comboGrafico = ttk.Combobox(ventana, values=["Barras", "Líneas", "Circular"], state="readonly")
comboGrafico.set( "Elige el tipo de gráfico")
comboGrafico.grid(row=19, column= 0, padx=5, pady=3)

tk.Button(ventana, text="Generar Gráfico", command=generarGrafico, font=("Arial", 10), width=15).grid(row=19, column=1, padx=5, pady=3)

#Box de texto
lista_clientes =tk.Listbox(ventana, width=100, height=10)
lista_clientes.grid(row=20, column=0, columnspan=2)
lista_clientes.bind("<<ListboxSelect>>", seleccionarCliente)

#Iniciar funciones
mostrarClientes()
cargar_DiversionDependenciaAlcohol()
cargar_ProblemasDigestivos()
cargar_TensionAlta()
cargar_DolorCabeza()

#Inicia el bucle principal
ventana.mainloop() 