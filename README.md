# checkPublicIP
Script en Python para comprobar que la dirección IP pública no ha cambiado.

La utilidad de este pequeño programa es para el caso en el que tengamos los puertos de nuestro router redirigidos a algún servicio de alguno de los equipos conectados a él (servidor web, conexin ssh...) para acceder a él desde un equipo externo a nuestra red. Lo más habitual es que tengamos nuestra dirección IP pública dinámica, por lo que nos resultaría muy útil conocer en cada momento cuál es dicha dirección IP para poder acceder siempre a nuestro servicio.

Este conjunto de scripts/módulos en python nos permiten comprobar cuál es la dirección IP pública de nuestro router, compararla con la obtenida en la última comprobación y, si ha cambiado, recibir un correo electrónico con la nueva dirección IP.

Lo ideal sería programar el script principal para que se ejecute de forma automática cada X tiempo. Por ejemplo, haciendo uso de la herramienta "cron" de Linux.

Podéis ver un tutorial sobre cómo hacerlo con un código similar al de este repositorio en: http://www.manusoft.es/comprobar-automaticamente-la-direccion-ip-publica-de-nuestra-raspberry-pi/


* El envío de correo solamente es posible desde una dirección de GMail.
