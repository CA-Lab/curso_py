#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 12:34:57 2018

@author: jmsiqueiros
"""

#Leer archivos

libro = open('Frankenstein_1818.txt')

texto = libro.readlines()

print texto[2]

print texto[2:10]

#lineas = texto[2:10]