#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Abans de començar haurem d'instal·lar el mòdul "pytube". 
# A un ordinador amb Linux serà fent pip install pytube des de la consola.

from pytube import YouTube

# Per tal de poder executar la instrucció de descàrrega en una única
# comanda de terminal haurem de disposar del mòdul "sys".

from sys import argv

# Variables
link = argv[1] # L'argument 1 és el link del vídeo a descarregar.
youtube = YouTube(link)

# Execució
youtube_download = youtube.streams.get_highest_resolution() # Escollir màxima resolució.
youtube_download.download('./') # Descarregar a la mateixa carpeta que l'arxiu de python.
