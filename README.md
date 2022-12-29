<h1 align="center"><b>Baixar YouTube amb Python</b></h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://www.gnu.org/licenses/gpl-3.0.html" target="_blank">
    <img alt="License: GPL--3+" src="https://img.shields.io/badge/License-GPL--3+-yellow.svg" />
  </a>
  <a href="https://twitter.com/miquelnebot" target="_blank">
    <img alt="Twitter: Miquel Nebot" src="https://img.shields.io/twitter/follow/miquelnebot.svg?style=social" />
  </a>
</p>
<div align="center"><img src="https://user-images.githubusercontent.com/57944755/209482485-0c04e9a6-97a2-4a57-be2f-aeecf061cd37.png"></div>

# 👁️‍🗨️ Introducció
Tot i que existeixen infinitat de solucions en línia per descarregar vídeos amb llicenciament Creative Commons des de YouTube, sempre és bona idea disposar d’un sistema senzill i sense dependència de tercers. En el següent tutorial et present com fer-ho mitjançant un mòdul de predissenyat de Python.

# 💻 Escenari
Kubuntu 22.04 LTS

# 0️⃣ Abans de començar
1. Haurem de tenir instal·lat Python en el nostre ordinador. Verificarem si disposam d'ell i la seva versió mitjançant la comanda següent a dins el Terminal (Ctrl+Alt+T): 

```console
user@kubuntu-mnebot:~$ sudo python3 -V
```
Si no el tenim instal·lat, el podem aconseguir fàcilment mitjançant la comanda:
```console
user@kubuntu-mnebot:~$ sudo apt install python3
```
2. Per a la importació del mòdul necessari (**pytube**) és imprescindible disposar al nostre ordinador de l'administrador de paquets **PIP**, per això, i si no ho hem fet amb anterioritat, l'instal·larem a través de la terminal de la següent manera:
```console
user@kubuntu-mnebot:~$ sudo apt install python3-pip
```
3. Instal·larem finalment el mòdul necessari responsable de la descàrrega i conversió del nostre vídeo:
```console
user@kubunu-mnebot:~$ sudo pip install pytube
```

# 👇 Descàrrega i execució
Copiarem el codi següent 👇 a un arxiu amb extensió **.py** al nostre ordinador (per exemple **baixar_youtube.py**). Cal informar que la descàrrega dels vídeos, per defecte, es farà al mateix directori on es trobi l’arxiu de Python, per això, hem d’assegurar-nos que disposi d’espai suficient pel seu emmagatzematge.
<p></p>📝 Descàrrega de l'arxiu .py des d'<a href="https://github.com/miquelnebotaragon/baixar_youtube_python/blob/main/baixar_youtube.py" target="_blank">aquí</a>.

# 🛰️ Baixar ràpid
En el present tutorial disposam també d'una versió ràpida per a la descàrrega dels vídeos sense missatges de confirmació i en una única instrucció a través de la consola. Baixarem l'<a href="https://github.com/miquelnebotaragon/baixar_youtube_python/blob/main/baixar_youtube_rapid.py" target="_blank">arxiu</a> **baixar_youtube_rapid.py** i l'executarem a través del terminal afegint-hi com a 1r i únic argument el vídeo a descarregar. Per exemple:
```console
user@kubuntu-mnebot:~/Downloads$ sudo python3 baixar_youtube_rapid.py https://youtu.be/i7Y7DnBx4X4
```
Cal recordar que el vídeo es descarregarà al mateix directori on tenim allotjat l'arxiu de Python (a l'exemple anterior 👆 a la carpeta de baixades). Si volem modificar aquest paràmetre, senzillament farem el canvi a la darrera línia del codi afegint la ruta completa de la nova ubicació.
 ```python
youtube_download.download('/home/mnebot/Video/descarrega_youtube')
```

# ➕ Informació
1️⃣ L'arxiu **.py** ha estat comentat al detall (#) per tal de possibilitar l'anàlisi del seu funcionament.<p></p>
2️⃣ Totes les descàrregues de vídeos de YouTube sense llicenciament Creative Commons són il·legals. Assegura't bé, abans de fer servir aquesta aplicació, que no infringeixes aquesta ni cap altra norma vigent.<p></p>
3️⃣ Aquesta aplicació ha estat creada únicament amb finalitat d'estudi i divulgació. No em faig responsable dels possibles problemes ni prejudicis que pugui provocar el seu ús.
