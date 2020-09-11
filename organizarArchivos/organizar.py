__Author__="Julian Guillermo Zapata Rugeles"

"""
Este script se distribuido con licencia GPL. Puedes modificarlo , compartirlo y realizar tus propias versiones.
para mas información sobre la licencia pública general GNU GPL https://www.gnu.org/licenses/licenses.es.html
https://www.gnu.org/licenses/gpl-3.0.html GPL3
colaboremos con el movimiento de software libre para un mundo mejor.

El objetivo de este script es organizar el directorio.


11 septiembre 2020 : cambio ---> añadido reconocimiento de plataforma.
"""

menu="""                             _              _
  ___  _ __ __ _  __ _ _ __ (_)______ _  __| | ___  _ __
 / _ \| '__/ _` |/ _` | '_ \| |_  / _` |/ _` |/ _ \| '__|
| (_) | | | (_| | (_| | | | | |/ / (_| | (_| | (_) | |
 \___/|_|  \__, |\__,_|_| |_|_/___\__,_|\__,_|\___/|_|
           |___/

                 Bienvenido Nuevamente

"""
import os
import os.path
import sys
import platform

MOVER="mv" # comando linux , se cambiará a move si se detecta la plataforma windows
PLATAFORMA=platform.system() # retorna la plataforma
NOMBRE_ARCHIVO=sys.argv[0] # determina el nombre del archivo python en ejecución para evitar su movimiento
EXEPCIONES=[] #añada aquí archivos que no se moveran. ejemplo : EXEPCIONES=["mi_archivo.txt","mi_archivo2.mp3" etc ... ]

class Organizador(object):
    """ Métodos para ordenar el directorio """

    def __init__(self):
        super(Organizador).__init__()
        try:
            self.archivosEnDirectorio=os.listdir() # retorna una lista con los archivos y sus formatos
            self.diccionario={}
        except Exception as e:
            print(e," <-- error")

    def crearCarpeas(self):
        print("\n --------------------- creacion de carpetas --------------------------")
        for extenciones in self.diccionario.keys():
            if os.path.isdir(extenciones):
                print("{} -> omitido ( ya existe ) ".format(extenciones))
            else:
                os.system("mkdir {}".format(extenciones))
                print("{} -> directorio creado ".format(extenciones))

    def eliminarEspacios(self):
        for archivos in self.archivosEnDirectorio:
            try:
                if not os.path.isdir(archivos):
                    sinEspacios=archivos.replace(" ","\ ")
                    self.archivosEnDirectorio.remove(archivos)
                    self.archivosEnDirectorio.append(sinEspacios)
            except Exception as e:
                pass

    def moverArchivos(self):
        try:
            self.archivosEnDirectorio.remove(NOMBRE_ARCHIVO)
            for archivos_omitir in EXEPCIONES:
                try:
                    self.archivosEnDirectorio.remove(archivos_omitir)
                except Exception as e:
                    pass
        except Exception as e:
            raise
        print("\n --------------------- movimientos --------------------------")
        for elementosAmover in self.archivosEnDirectorio:
            try:
                file=elementosAmover.split(".")
                os.system("{} {} {}/".format(MOVER,elementosAmover,file[1]))
                print("se movió  {}  print(PLATAFORMA)-->  {}/".format(elementosAmover,file[1]))
            except Exception as e:
                pass # omitidos

    def ordenar(self):
        for documentos in self.archivosEnDirectorio:
            try:
                extencionDocumento=documentos.split(".")
                if len(extencionDocumento)!=1:
                    if extencionDocumento[1] not in self.diccionario:
                        self.diccionario[extencionDocumento[1]]=1
                    else:
                        self.diccionario[extencionDocumento[1]]+=1
            except Exception as e:
                raise
        #print(menu.replace("{}",os.popen("date").read())) # DESCOMENTAR PARA LINUX
        print(menu)
        print("# Encontré las siguientes extenciones para ordenarlas :")
        contador=1
        for extenciones , cantidades in self.diccionario.items():
            print("{} --> Extención {}  {} ".format(contador,extenciones,cantidades))
            contador+=1

        print("\nPara continuar Presiona ENTER o CTRL+C para salir")
        print("Crearé los directorios y moveré los archivos por ti.\n")

        contador=str(input("continuar ? >> ")) # variable reciclada.
        if contador=="":
            return True

if __name__ == '__main__':
    #os.system("clear") # refrescar la pantalla de terminal
    if PLATAFORMA=="Windows":
        MOVER="move"
    session=Organizador()
    validacionContinuar=session.ordenar() # retorna True Explicitamente. Enter representa cadena vacía-
    if validacionContinuar:
        session.crearCarpeas()
        session.eliminarEspacios()
        session.moverArchivos()
