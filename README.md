# Proyecto-algorimos-2324-3-Kevin-R
Proyecto: Euro 2024 ⚽
Te han contratado para el desarrollo de un nuevo proyecto, un sistema para
vender los tickets de la Eurocopa Alemania 2024. Este sistema servirá para la venta
de entradas, restaurantes, registrar asistencia y más.
El sistema consta de seis (6) módulos fundamentales:
1. Gestión de partidos y estadios
2. Gestión de venta de entradas
3. Gestión de asistencia a partidos
4. Gestión de restaurantes
5. Gestión de venta de restaurantes
6. Indicadores de gestión (estadísticas)
Nota: Revise la información importante en observaciones
Gestión de partidos y estadios
Este módulo permitirá a los usuarios administrar los equipos, enfrentamientos
y los estadios en donde ocurrirán; para eso tendrás que tener en cuenta, que la
información será dada a través de una API, (ver observaciones). Con esta
información deberán desarrollar lo siguiente:
1. Registrar los equipos con la información proveniente de la API, es importante
que se guarden los siguientes datos:
a. El nombre del país
b. Su código FIFA
c. El grupo en el que se encuentra
2. Registrar los estadios con la información proveniente de la API, es importante
que se guarden los siguientes datos:
a. El nombre
b. La Ubicación
3. Registrar los partidos con la información proveniente de la API, es importante
que se guarden los siguientes datos:
a. Equipo local (debe ser una referencia al objeto)
b. Equipo visitante (debe ser una referencia al objeto)
c. Fecha y hora
d. Estadio (debe ser una referencia al objeto)
4. Se deberá poder realizar la búsqueda de los partidos en función de los
siguientes filtros:
a. Buscar todos los partidos de un país
b. Buscar todos los partidos que se jugarán en un estadio específico
c. Buscar todos los partidos que se jugarán en una fecha determinada
Gestión de venta de entradas
Los organizadores de la Euro 2024 necesitarán un sistema para administrar
las ventas de sus entradas; para esto necesitará solicitar los siguientes datos:
1. Datos del cliente:
a. Nombre del cliente
b. Cedula
c. Edad
d. Partido que desea comprar ticket (para esto se deberá mostrar toda la
información de los partidos)
e. Tipo de entrada que desea comprar
i. Si es General: solo podrá ver el partido en su asiento y su
precio es de $35
ii. Si es VIP; podrá disfrutar del restaurante del estadio, es decir
podrá adquirir productos de dicho restaurante. El precio de una
entrada VIP es de $75
2. Luego el sistema deberá arrojarle un mapa del estadio, el cual el cliente
podrá seleccionar un asiento, si el asiento está ocupado deberá notificarle al
cliente que seleccione otro.
3. Por último le aparecerá el costo de la entrada según los siguientes casos:
a. si su cédula es un número vampiro su entrada tiene un 50% de
descuento y se le notificara al cliente
b. Las entradas hay que sumarle el 16% del impuesto del valor agregado
(IVA)
4. Luego deberá mostrar un mensaje indicando al cliente su asiento, costo (con
información del subtotal, descuento, IVA y Total) y si desea proceder a pagar
la entrada, de ser así, se ocupa el asiento y se muestra un mensaje de pago
exitoso.
Gestión de asistencia a partidos
En la Euro 2024, las entradas se compra con anticipación a los partidos, por
lo que es posible que las personas no puedan asistir al partido, o que el por el
contrario el partido esté lleno y se falsifiquen boletos; por tal razón el equipo de
seguridad necesita de un módulo que les permita revisar si los boletos son válidos
para ello deberá:
1. Validar la autenticidad del boleto con el código único del mismo
a. Si el boleto es auténtico deberá modificar la asistencia del partido
2. Un boleto puede ser falso si el código presentado no coincide con los códigos
del sistema o si el código ya fue utilizado, es decir, un boleto con ese mismo
código ya se usó para entrar al estadio
Gestión de restaurantes
En la Euro 2024 se necesitará un sistema para administrar su restaurante
para sus clientes más importantes (VIP), esto debe tener las siguientes
funcionalidades:
1. Al tener que guardar el producto en su estructura de datos local, luego de
haberla descargado del API, deberá guardar
a. Nombre del alimento/bebida.
b. Clasificación (alimento o bebida).
i. Si es bebida se debe registrar si es alcohólica o no. Si es
alimento se debe guardar si es de empaque o de preparación.
c. Precio (se le deberá sumar el 16% del IVA).
2. Buscar productos por nombre, tipo, o rango de precio.
Gestión de venta de restaurantes
Para la venta en el restaurante se necesitará que el cliente ya haya comprado
una entrada VIP, esto se validará con su cédula, si es así se procederá de la
siguiente manera:
1. Se guardan los datos del cliente:
a. Cedula.
b. Comida(s) que desee comprar
i. Si la edad el cliente es menor a 18 años no podrá comprar
bebidas alcohólicas
2. Luego deberá mostrarle los productos que desea comprar con el monto total,
siguiendo los siguientes casos:
a. Si la cédula es un número perfecto obtendrá un 15% de descuento.
3. Por último, si el cliente desea proceder con la compra, se le mostrará un
mensaje de pago exitoso con un resumen de su compra donde se muestre el
monto con su subtotal, descuento y total.
4. Se debe restar del inventario la cantidad de productos que el cliente compró
Indicadores de gestión (Estadísticas)
Toda empresa necesita evaluar su gestión y ver que le está funcionando y
que no, para eso es importante un módulo de estadísticas que le indique a los
organizadores de Euro 2022 lo siguiente:
1. ¿Cuál es el promedio de gasto de un cliente VIP en un partido (ticket +
restaurante)?
2. Mostrar tabla con la asistencia a los partidos de mejor a peor, mostrando el
nombre del partido (nombre de los equipos), estadio en donde se juega,
boletos vendidos, personas que asistieron y la relación asistencia/venta
3. ¿Cuál fue el partido con mayor asistencia?
4. ¿Cuál fue el partido con mayor boletos vendidos?
5. Top 3 productos más vendidos en el restaurante.
6. Top 3 de clientes (clientes que más compraron boletos)
7. Realizar gráficos con dichas estadísticas con las librerías de matplotlib o
Bokeh (Bono).
Observaciones
● Euro 2024 posee una API en donde podrás obtener toda su información:
○ Documentación:https://github.com/Algoritmos-y-Programacion/api-pro
yecto
○ Endpoints:
■ Equipos:https://raw.githubusercontent.com/Algoritmos-y-Progra
macion/api-proyecto/main/teams.json
■ Estadios:https://raw.githubusercontent.com/Algoritmos-y-Progr
amacion/api-proyecto/main/stadiums.json
■ Partidos:https://raw.githubusercontent.com/Algoritmos-y-Progra
macion/api-proyecto/main/matches.json
● La API tiene que funcionar como una opción de pre-cargado de datos antes
de empezar a usar el programa, es decir esta opción crea el estado inicial del
programa, posteriormente no se debe usar la API a menos que se quiera
borrar los datos y cargar su estado inicial
● Se deben usar los conceptos de programación orientado a objetos
● Antes de realizar el código, es imperante que realicen un diagrama de
clases y que la implementación de su proyecto sea uno a uno con el
diagrama
● Se evaluará que el código este comentado (docstring)
● Se evaluará que el sistema contenga validaciones
● Se deberán guardar datos en un archivo TXT para preservar los datos
● El proyecto deberá ser entregado en GitHub más tardar el 30 de junio de
2024 a las 11:59PM
