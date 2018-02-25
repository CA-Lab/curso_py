#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 19:57:55 2018

@author: jmsiqueiros
"""

#Escribir archivos

texto = ['mi','perro','Juno', 'es', 'un', 'destructor']

outfile = open('/Users/jmsiqueiros/Dropbox/salida.txt', 'w')

#
outfile.writelines(texto)

outfile.close()