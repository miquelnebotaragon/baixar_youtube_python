#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Abans de començar haurem d'instal·lar el mòdul "pytube". 
# A un ordinador amb Linux serà fent pip install pytube des de la consola.

from pytube import YouTube


while True: 
# Mentre es compleixi que la variable consentiment sigui "Y" el programa continuarà endavant, 
# si es dona qualsevol altra resultat, tornarà al principi.
        
    link = input("Enganxa l\'enllaç del vídeo a descarregar:\n") # Introducció Variable 1. Enllaç del vídeo.
    youtube = YouTube(link) # Variable automàtica 2. Vídeo de YouTube.
    
    print("\n · Títol: ",'\033[92m'+youtube.title+'\033[0m') # Informació 1 rebuda des de l'objecte "YouTube" del mòdul "pytube".
    print(" · Autor/a: ",'\033[92m'+youtube.author+'\033[0m') # Informació 2 rebuda des de l'objecte "YouTube" del mòdul "pytube".
    
    consentiment = input("\nÉs aquest el vídeo que vols descarregar? Y/n  ") # Introducció Variable 3. Pregunta consentiment informació.

    if consentiment == "Y" or consentiment == "y" or consentiment == "": # Sempre i quan consentiment sigui "Y" o "y" o intro descarregarà.
        print("Has de tenir paciència, depenent del tamany del vídeo pot trigar uns instants...")
        youtube_down = youtube.streams.get_highest_resolution()
        youtube_down.download('./') # D'aquesta manera deixarà el vídeo a la mateixa carpeta on tenim l'arxiu de Python.
        print("El vídeo s'ha descarregat amb èxit!")
        break
