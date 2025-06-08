NOMBRE DEL PROYECTO: Sistema web de gestión de pasajes para SkyRoute

BREVE DESCRIPCIÓN: 
En este sistema las personas encargadas de gestionar las ventas de pasajes para la empresa asignada van a poder manipular los datos necesarios a través de un menú y submenús de acuerdo a lo que necesiten en el momento, para poder así concretar la acción que requieran hacer en el momento.

INTEGRANTES DEL GRUPO:
LEILA SELENA CASTILLO   DNI: 43134859
GABRIEL CAVALLO         DNI: 28103891
PAULINA GONZALEZ        DNI: 38107047
VANINA LETICIA PI       DNI: 39908554
FAVIO VILLALON	        DNI: 39172727

INSTRUCCIONES BÁSICAS DE EJECUCIÓN DEL PROYECTO:
Lo primero que se debe tener para poder ejecutar el proyecto es Visual Studio Code, para poder así abrir los archivos que dejamos a disposición en el archivo de entrega de la evidencia 3. Una vez ya con visual studio code, los archivos .py con las diferentes partes del sistema y la base de datos abiertos podemos proceder a ejecutar el sistema. Para eso vamos a ejecutar el archivo main.py que es el motor de todo el sistema, dando click en Run en la parte superior derecha de visual studio code.
Al ejecutar el main.py de nuestro sistema nos aparecerá el menú con las diferentes opciones que se pueden realizar, ya sea gestión de clientes, destinos, ventas, obtener información sobre el sistema o bien dar de baja una venta con el botón de arrepentimiento.
Al seleccionar alguna de las opciones del menú principal nos brindará otro submenú de acuerdo a la opción elegida, en donde dentro del contexto de la opción elegida nos brindara diferentes opciones para realizar.  Un ejemplo puede ser si elegimos la opción 1 de gestión de clientes, automáticamente aparecerá el submenú donde nos ofrecerá opciones como el de ver los clientes registrados, registrar un cliente, modificar uno ya existente o bien eliminar de la base de datos un cliente en particular.
En cada submenú al momento de seleccionar la acción que se desea realizar nos comenzará a pedir diferentes tipo de datos relacionados a la acción que se está llevando a cabo. En algunos seran datos nuevos o inexistentes (por ej cuando registremos un nuevo cliente a la base de datos), y en otros nos pedirá datos que ya existen dentro de la base de datos (por ej cuando debamos seleccionar un destino), por lo que a la hora de brindarle dicha información al sistema estos datos deberán ser correctos o de lo contrario generara algún error. En nuestro caso en varias sentencias para evitar que ocurran estos errores le pusimos una previa verificación para que analice la base de datos y verifique si ese dato ya existe, o bien para evitar que se duplique un dato ya existente y así respetar la estructura de nuestra base de datos.
Una vez realizada la acción que se decidió hacer y se pudo concretar correctamente (todo depende de si se brindan bien los datos que se pide en cada instancia) el sistema volverá a plasmar el menú principal, para así darle la oportunidad al usuario de seguir ejecutando acciones que sean necesarias en ese momento, o bien darle la opción de Salir del sistema de una manera correcta eligiendo la opción que se le indica.

DETALLE COMPLETO DE TODO LO QUE HAY EN EL REPOSITORIO:
main.py sin conexion a base de datos
main.py con conexion a base de datos
archivo SQL(DDL) ->ESTRUCTURACIÓN DE LA BASE DE DATOS
archivo SQL(DML) -> INSERTAR EJEMPLOS EN LAS TABLAS
archivo SQL(DML) ->CONSULTAS UTILIZANDO SELECT
Documento de etica
Estructura para proyectos ABP
archivo README.MD
Poster
Video
