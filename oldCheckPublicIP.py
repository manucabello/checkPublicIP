#!/usr/bin/python
# -*- coding: utf-8 -*-

# Comprobación de la IP pública y envío de correo si cambia
# www.manusoft.es

# importamos la librería necesaria para el envío de correos
import smtplib
# importamos la librería necesaria para hacer una consulta HTTP
import urllib
# importamos la librería necesaria para acceder a un fichero
import os.path as path

# Apertura del fichero con la última dirección IP pública registrada 
# Comprobamos que el fichero existe 
if path.exists('publicIPs.txt'):
        # Si el fichero existe lo abrimos en modo lectura. El atributo 'r' indica que es de solo lectura 
        archivo = open("publicIPs.txt", 'r')
else:
        # Si el archivo no existe lo creamos en modo lectura y escritura. El atributo 'w+' abre el fichero en modo lectura y escritura y, si no existe, lo crea 
        archivo = open("publicIPs.txt", 'w+')
# Obtención de la dirección IP pública actual
publicIpActual = urllib.urlopen('http://icanhazip.com').read()

# Lectura de la última dirección IP pública registrada desde el fichero
# Se leen todas las líneas del fichero quedándonos únicamente con la última
linea = archivo.readline()
publicIp = ""
while linea != '':
        publicIp = linea
        linea = archivo.readline()

# Cierre del fichero con la última dirección IP pública registrada
archivo.close()

# Si en el archivo no existe ninguna dirección IP pública registrada, o la última registrada es diferente a la actual
if publicIp == "" or publicIp != publicIpActual:
        # Guarda la dirección IP pública actual en la variable "publicIP"
        publicIp = publicIpActual
        # Escribe la dirección IP pública actual en el fichero "publicIPs.txt". El atributo 'w' abre el fichero únicamente en modo escritura y, si no existe, lo crea. Este modo s$
        archivo = open("publicIPs.txt", 'w')
        archivo.write(publicIp)
        # Cierre del fichero
        archivo.close()

        # Se envía la dirección IP pública actual por correo electrónico
        # Variable con la dirección de correo electrónico de origen
        fromAddr = '***************@gmail.com'
        # Variable con la dirección de correo electrónico de destino
        toAddr = '***************'
        # Variable con el asunto del correo electrónico
        subject = 'New public IP address'
        # Variable con el mensaje.
        msg = 'La nueva direccion IP publica es ' + publicIp
        # Variable con el correo electrónico completo
        email = """From: %s
To: %s
MIME-Version: 1.0
Content-type: text/html
Subject: %s
%s
""" %(fromAddr, toAddr, subject, msg)

        # Variable con el usuario de la dirección de correo electrónico de origen
        username = '**************@gmail.com'
        # Variable con la contraseña de la dirección de correo electrónico de origen
        password = '**********'

        # Envío del correo
        # Apertura del servidor SMTP en el servidor de correo electrónico de origen
        try:
                server = smtplib.SMTP('smtp.gmail.com:587')
                server.starttls()
                try:
                        # Inicio de sesión en el servidor de correo electrónico de origen
                        server.login(username, password)
                        try:
                                # Envío del correo electrónico
                                server.sendmail(fromAddr, toAddr, email)
                        except:
                                print('Error al enviar el correo electrónico')
                except:
                        print('Error al iniciar sesión en GMail')
                # Cierre del servidor SMTP
                server.quit()
        except:
                print('Error al iniciar el servidor SMTP')

### FIN DEL SCRIPT ###
