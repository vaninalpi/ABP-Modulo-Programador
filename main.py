#Programa de Python para simular una aplicacion de una empresa de viajes con un menu que tiene como 
# finalidad establecer las bases funcionales del sistema propuesto en la evidencia, ofreciendo un menú 
# interactivo que simula el funcionamiento deseado para una navegacion con diferentes opciones para el
# usuario, y asi poder administrar los datos a manipular.


# Para el uso de este programa lo primero que necesitamos tener es visual studio code para
# poder ejecutar el programa. El mismo puede instalarse desde su pagina oficial.
# Para tener el programa se debera descargarlo de la fuente que lo provea (en este caso un miembro del 
# grupo). Una vez descargado se debera abrir Visual Studio Code y abrir el programa previamente 
# descargado para poder ejecutarlo y comenzar a usarlo.
# Para usarlo solo deberemos darle en la opcion de Run Python File la cual se encuentra en la parte 
# superior derecha (tiene forma de triangulo) y ya comenzar a seleccionar las opciones disponibles que 
# te ofrece el programa.


# INTEGRANTES DEL GRUPO:
#Leila Selena Castillo   DNI: 43134859
#Gabriel Cavallo         DNI: 28103891
#Paulina González        DNI: 38107047
#Vanina Leticia Pi       DNI: 39908554
#Favio Villalon          DNI: 39172727



# Función para gestionar los clientes
def gestionar_clientes():
    while True:
        print("""\n>>> Gestión de Clientes<<<
        1. Ver clientes  
        2. Registrar cliente
        3. Modificar cliente
        4. Eliminar cliente
        5. Volver al Menú Principal""")
       
        try:
            opcion_funcion = int(input("Seleccione una opción: "))
            if opcion_funcion == 1:
                print("Mostrando lista de clientes...")
                print("Clientes mostrados correctamente.")
                break
            elif opcion_funcion == 2:
                razon_social=input("Ingrese la razon social del cliente: ")
                cuit_cliente=input("Ingrese el CUIT del cliente: ")
                contacto_cliente=input("Ingrese el correo del contacto: ")
                print(f""">>Cliente registrado como:
            \nRazon Social: {razon_social}
            \nCUIT: {cuit_cliente}
            \nCorreo de contacto: {contacto_cliente}
             """)
                break
            elif opcion_funcion == 3:
                cuit_cliente=input("Ingrese el CUIT del cliente que desea modificar: ")
                print("Modificando cliente...")
                print(f"Cliente con CUIT:{cuit_cliente} modificado correctamente.")
                break
            elif opcion_funcion == 4:
                cuit_cliente=input("Ingrese el CUIT del cliente que desea elimiar: ")
                print("Eliminando cliente...")
                print(f"Cliente con CUIT:{cuit_cliente} eliminado correctamente.")
                break
            elif opcion_funcion == 5:
                print("Regresando al menú principal...")
                break
            else:
                print("Opción fuera de rango. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

# Función para gestionar los destinos
def gestionar_destinos():
    while True:
        print("""\n>>> Gestión de Destinos<<<
        1. Registrar destino
        2. Modificar destino
        3. Eliminar destino
        4. Volver al Menú Principal""")
        
        try:
            opcion_funcion = int(input("Seleccione una opción: "))
            if opcion_funcion == 1:
                id_destino=input("Ingrese el ID del destino: ")
                ciudad_destino=input("Ingrese la ciudad del destino: ")
                pais_destino=input("Ingrese el pais del destino: ")
                costo_destino=input("Ingrese el costo de base del destino: ")
                print(f""">>Destino registrado como:
                \nID: {id_destino}     
                \nCiudad: {ciudad_destino}
                \nPais: {pais_destino}
                \nCosto base del viaje:  {costo_destino}
                """)
                break
            elif opcion_funcion == 2:
                id_destino=input("Ingrese el ID del destino que desea modificar: ")
                print(f"Modificando destino {id_destino}")
                print("Destino modificado correctamente.")
                break
            elif opcion_funcion == 3:
                id_destino=input("Ingrese el ID del destino que desea elimiar: ")
                print(f"Eliminando destino {id_destino}")
                print("Destino eliminado correctamente.")
                break
            elif opcion_funcion == 4:
                print("Regresando al menú principal...")
                break
            else:
                print("Opción fuera de rango. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

# Función para gestionar las ventas
def gestionar_ventas():
    while True:
        print("""\n>>> Gestión de Ventas<<<
        1. Registrar venta
        2. Ver estado de la venta
        3. Volver al Menú Principal""")
        
        try:
            opcion_funcion = int(input("Seleccione una opción: "))
            if opcion_funcion == 1:
                cuit_cliente=input("Ingrese el CUIT del cliente que realiza la compra: ")
                id_destino=input("Ingrese el ID del destino: ")
                fecha_venta=input("Ingrese la fecha de venta: ")
                print(f""">>Se registra nueva venta:
                \nCliente: {cuit_cliente}
                \nDestino: {id_destino}
                \nFecha de la venta: {fecha_venta}
                \nID de la venta:
                """)
                break
            elif opcion_funcion == 2:
                id_venta=input("Ingrese el ID de la venta que desea ver el estado: ")
                print(f"El estado de la venta: {id_venta}, es _______")
                break
            elif opcion_funcion == 3:
                print("Regresando al menú principal...")
                break
            else:
                print("Opción fuera de rango. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

# Función para consultar las ventas
def consultar_ventas():
    while True:
        print("""\n>>> Consulta de Ventas<<< 
        1. Consultar ventas
        2. Volver al Menú Principal""")
        
        try:
            opcion_funcion = int(input("Seleccione una opción: "))
            if opcion_funcion == 1:
                print("Mostrando historial de ventas...")
                break
            elif opcion_funcion == 2:
                print("Regresando al menú principal...")
                break
            else:
                print("Opción fuera de rango. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

# Función para acceder al botón de arrepentimiento
def boton_arrepentimiento():
    while True:
        print("""\n>>> Botón de Arrepentimiento<<<
        1. Cancelar compra
        2. Volver al Menú Principal""")
        
        try:
            opcion_funcion = int(input("Seleccione una opción: "))
            if opcion_funcion == 1:
                id_venta=input("Ingrese el ID de la venta que desea cancelar: ")
                print(f"Cancelando compra con el ID: {id_venta}")
                break
            elif opcion_funcion == 2:
                print("Regresando al menú principal...")
                break
            else:
                print("Opción fuera de rango. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

# Función para mostrar el reporte general
def ver_reporte_general():
    while True:
        print("""\n>>> Reporte General<<<
        1. Ver reporte general
        2. Volver al Menú Principal""")
        
        try:
            opcion_funcion = int(input("Seleccione una opción: "))
            if opcion_funcion == 1:
                print("Mostrando reporte general...")
                break
            elif opcion_funcion == 2:
                print("Regresando al menú principal...")
                break
            else:
                print("Opción fuera de rango. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

# Función para mostrar acerca del sistema
def acerca_del_sistema():
    while True:
        print("""\n>>> SkyRoute - Sistema de Gestión de Pasajes<<<
        Versión 1.0
        Desarrollado por -nombre integrantes-
        \n1. Volver al Menú Principal""")
        
        try:
            opcion_funcion = int(input("Seleccione una opción: "))
            if opcion_funcion == 1:
                print("Regresando al menú principal...")
                break
            else:
                print("Opción fuera de rango. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

#funcion para mostrar el menu
def mostrar_menu():
    print("""\n--- Menú Principal ---
1. Gestionar Clientes
2. Gestionar Destinos
3. Gestionar Ventas
4. Consultar Ventas
5. Botón de Arrepentimiento
6. Ver Reporte General
7. Acerca del Sistema
8. Salir""")


import sys


#aca comienza el programa
print("---Bienvenido a la web de SkyRoute---")
while True:
    eleccion = input("¿Desea ver nuestro menú? (SI / NO): ").upper()
    if eleccion in ["SI", "NO"]:
        break
    else:
        print("Por favor, ingrese una opción válida (SI / NO).")

if eleccion == "NO": #verificamos que quiere ver el menu
    print("Te esperamos la próxima.")
    sys.exit()

while True:  # Bucle principal del menu
    mostrar_menu()
    try:
        opcion = int(input("Seleccione una opción (1-8): "))  #aseguramos que ingrese un num entero
        if opcion == 1:
            gestionar_clientes()
        elif opcion == 2:
            gestionar_destinos()
        elif opcion == 3:
            gestionar_ventas()
        elif opcion == 4:
            consultar_ventas()
        elif opcion == 5:
            boton_arrepentimiento()
        elif opcion == 6:
            ver_reporte_general()
        elif opcion == 7:
            acerca_del_sistema()
        elif opcion == 8:
            print("Gracias por utilizar nuestro servicio")
            break
        else:
            print("Opcion invalida.")   
    except ValueError:
        print(" Error: Por favor, ingrese un número válido.")  


