#!/usr/bin/python
# -*- coding: utf-8 -*-

#################################################
##                                             ##
## Script para obtener la dirección IP pública ##
##               www.manusoft.es               ##
##                                             ##
#################################################

# Importamos la librería necesaria para hacer una consulta HTTP
import urllib

def getPublicIP():
	return urllib.urlopen('http://icanhazip.com').read()

print (getPublicIP())
