# Definición del diccionario de términos informáticos eddy el inge
diccionario_informatico = {
    "algoritmo": "Conjunto de instrucciones secuenciales para resolver un problema o realizar una tarea.",
    "api": "Interfaz de Programación de Aplicaciones, conjunto de reglas y herramientas para construir software.",
    "array": "Estructura de datos que contiene una colección de elementos, típicamente del mismo tipo.",
    "backend": "Parte de una aplicación que gestiona la lógica del negocio y las interacciones con la base de datos.",
    "big data": "Conjunto de datos masivos que requieren técnicas avanzadas para su análisis y procesamiento.",
    "binario": "Sistema numérico que utiliza solo los dígitos 0 y 1.",
    "bit": "Unidad básica de información en informática, puede ser 0 o 1.",
    "bug": "Error o fallo en un programa de software.",
    "byte": "Unidad de almacenamiento compuesta por 8 bits.",
    "cache": "Memoria de alta velocidad que almacena datos temporalmente para un acceso rápido.",
    "cloud computing": "Entrega de servicios de computación a través de internet.",
    "compilador": "Programa que traduce código de un lenguaje de programación a lenguaje máquina.",
    "cookie": "Pequeño archivo almacenado en el navegador del usuario para guardar información de sesión.",
    "criptografía": "Técnicas para proteger la información mediante el uso de códigos.",
    "css": "Lenguaje de hojas de estilo utilizado para describir la presentación de un documento HTML.",
    "database": "Colección organizada de datos que se puede acceder, gestionar y actualizar.",
    "depuración": "Proceso de encontrar y corregir errores en un programa de software.",
    "dns": "Sistema de Nombres de Dominio, traduce nombres de dominio a direcciones IP.",
    "firewall": "Sistema de seguridad que controla el tráfico de red entrante y saliente.",
    "framework": "Conjunto de herramientas y bibliotecas para desarrollar software de manera más eficiente.",
    "frontend": "Parte de una aplicación con la que el usuario interactúa directamente.",
    "gigabyte": "Unidad de almacenamiento equivalente a 1,024 megabytes.",
    "html": "Lenguaje de Marcado de Hipertexto, utilizado para crear páginas web.",
    "http": "Protocolo de Transferencia de Hipertexto, base de la comunicación en la web.",
    "https": "Versión segura de HTTP que utiliza cifrado para proteger la información.",
    "ide": "Entorno de Desarrollo Integrado, software que proporciona herramientas para programación.",
    "ip": "Protocolo de Internet, direcciona y enruta datos en la red.",
    "json": "Formato de intercambio de datos que es fácil de leer y escribir para humanos y máquinas.",
    "kernel": "Parte central del sistema operativo que gestiona el hardware del ordenador.",
    "lan": "Red de Área Local, conecta dispositivos en una área geográfica limitada.",
    "lenguaje de programación": "Conjunto de instrucciones y reglas utilizadas para comunicarse con una computadora.",
    "linux": "Sistema operativo de código abierto basado en Unix.",
    "malware": "Software malicioso diseñado para dañar o explotar sistemas informáticos.",
    "memoria ram": "Memoria de acceso aleatorio, utilizada por el sistema para almacenar datos temporales.",
    "método": "Función asociada a un objeto en programación orientada a objetos.",
    "nube": "Metáfora para describir la entrega de servicios de computación a través de internet.",
    "nodo": "Punto de conexión dentro de una red.",
    "open source": "Software cuyo código fuente está disponible públicamente para su uso y modificación.",
    "paralelismo": "Ejecución simultánea de múltiples tareas para mejorar el rendimiento.",
    "patch": "Actualización de software diseñada para corregir errores o mejorar funcionalidad.",
    "ping": "Herramienta de red para comprobar la conectividad entre dispositivos.",
    "pixel": "Unidad mínima de una imagen digital.",
    "protocolo": "Conjunto de reglas que determinan cómo se comunican los dispositivos en una red.",
    "python": "Lenguaje de programación interpretado, de alto nivel y con una sintaxis fácil de aprender.",
    "querencia": "Preferencia o tendencia de un usuario en términos de interacción con la tecnología.",
    "query": "Consulta para extraer información de una base de datos.",
    "recursión": "Método donde la solución de un problema depende de soluciones más pequeñas del mismo problema.",
    "router": "Dispositivo que dirige el tráfico de datos en una red.",
    "script": "Programa o secuencia de instrucciones que se ejecutan en un entorno específico.",
    "servidor": "Computadora o programa que proporciona servicios a otros dispositivos o programas en una red.",
    "sql": "Lenguaje de Consulta Estructurado, utilizado para gestionar bases de datos relacionales.",
    "ssl": "Protocolo de Seguridad de la Capa de Transporte, utilizado para cifrar comunicaciones en la web.",
    "switch": "Dispositivo que conecta múltiples dispositivos en una red y dirige el tráfico de datos.",
    "tabla hash": "Estructura de datos que asocia claves con valores utilizando una función hash.",
    "tag": "Etiqueta utilizada en lenguajes de marcado como HTML para definir elementos.",
    "tcp": "Protocolo de Control de Transmisión, garantiza la entrega fiable de datos en una red.",
    "terminal": "Interfaz de línea de comandos para interactuar con el sistema operativo.",
    "token": "Unidad de datos utilizada en la autenticación y autorización.",
    "udp": "Protocolo de Datagrama de Usuario, permite la transmisión de datos sin garantizar la entrega.",
    "ui": "Interfaz de Usuario, parte de una aplicación con la que el usuario interactúa.",
    "url": "Localizador Uniforme de Recursos, dirección que identifica un recurso en internet.",
    "usb": "Bus Universal en Serie, estándar de conexión para dispositivos periféricos.",
    "usuario": "Persona que utiliza un sistema informático o aplicación.",
    "variable": "Elemento de almacenamiento que puede contener diferentes valores durante la ejecución de un programa.",
    "virtualización": "Técnica que permite crear versiones virtuales de recursos físicos.",
    "vpn": "Red Privada Virtual, extiende una red privada a través de una red pública.",
    "websocket": "Protocolo de comunicación que permite la transmisión bidireccional de datos en tiempo real.",
    "wi-fi": "Tecnología que permite la conexión inalámbrica de dispositivos a una red.",
    "xml": "Lenguaje de Marcado Extensible, utilizado para estructurar datos.",
    "zip": "Formato de compresión de archivos que reduce el tamaño de los datos para almacenamiento o transmisión.",
    "zona dns": "Parte de la estructura DNS que contiene información sobre un dominio específico."
}

def mostrar_menu():
    """
    Muestra el menú principal del Diccionario Informático de eddy el inge.

    Opciones:
    1. Buscar término: Permite al usuario buscar un término que desea en el diccionario.
    2. Acerca de: Muestra información acerca del diccionario.
    3. Salir: Finaliza el programa o salida del diccionario.
    """
    print("\nBienvenido al Diccionario Informático eddy el inge") #se muestra en pantalla el mensaje de bienvenido al diccionario
    print("1. Buscar término") #se muestra en pantalla la opcion uno que es buscar el termino
    print("2. Acerca de") #se muestra en pantalla la opcion dos que es acerca de
    print("3. Salir") #se muestra en pantalla la opcion de salir

def buscar_termino():
    """
    Permite al usuario buscar un término que desea en el diccionario.

    La función sigue ejecutándose hasta que el usuario ingresa 'salir'.
    Si el término no se encuentra en el diccionario, se le indica al usuario.
    """
    while True:
        termino = input("\nIngrese el término que desea buscar en nuestro diccionario, eddy el inge (o 'salir' para regresar al menú): ").strip().lower()
        
        if termino == 'salir':
            break

        if termino in diccionario_informatico:
            print(f"{termino.capitalize()}: {diccionario_informatico[termino]}\n") #se muesta en pantalla el termino de busqueda en el diccionario
        else:
            print("Término no encontrado. Intente nuevamente.\n") #se muestra en pantalla el mensaje del termino que no se a encontrado 

def acerca_de():
    """
    Muestra información acerca del Diccionario Informático eddy el inge.

    Esta información incluye la versión actual y el propósito del diccionario que se lleva.
    """
    print("\nDiccionario Informático del inge eddy v1.0") #se muestra en pantalla el mensaje del diccionario y una version para guiarse
    print("Este diccionario fue desarrollado para ayudar a los usuarios o personas para a entender términos básicos de informática con el diccionario del eddy el inge.") #se muestra en pantalla el mensaje sobre el proposito la cual se lleva acabo

while True:
    mostrar_menu() #se muestra el menu de las opciones
    opcion = input("\nSeleccione una opción: ").strip() #muestra la opcion para seleccionar

    if opcion == '1':
        buscar_termino() #se busca el termino
    elif opcion == '2':
        acerca_de() #se busca el acerca de
    elif opcion == '3':
        print("Gracias por usar el Diccionario Informático del inge eddy. ¡Hasta pronto niños, jovenes y padres!") #se muestra en pantalla a la hora de dar la opcion 3 se muestra un mensaje agradecimiento
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.") #se muestra en pantalla el mensaje de las opciones 

