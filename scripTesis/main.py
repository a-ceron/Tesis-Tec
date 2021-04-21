####################################
# 
#     Ariel Cerón González
#     Intento final para terminar la tesis de licenciatura. 
#     Objetivo: Generar información de precipitación acumulada con 
#               información de datos del radar de Querétaro.
#
#      01 Marzo de 2021
#
#######################################


import libTesis as lt
import matplotlib.pyplot as plt
#from Tesis.scripTesis.libTesis import *
#import pandas as pd


#Rutas a directorios
figp= "/home/arielcg/Documentos/Tesis/imgTesis/"
qro2015= "/home/arielcg/QRO_2015/"
qro2016= "/home/amagaldi/QRO_2016/"
qro2017= "/home/amagaldi/QRO_2017/"

###
#   Formato del archivo 2015
#   RAW_NA_000_236_20150306032609
#   n= 15, antes de llegar a la fecha
#   m= 14 valores despues del _
#                  año|mes|dia|hora

data= lt.getData(qro2015,'RAW_NA_000_236_20150306032609')

#Practica con un archivo
#Lextura del primer archivo que se enceuntra en el dia 06 del mes 03
n= len(data['03']['06'])
acum= 0
for i in range(n):
    rd= lt.read(data['03']['06'][i],qro2015)
    #dBZ= lt.radarDataProcessingChain(rd)
    dBZ, vel= lt.radarDataProcessingChain(rd)
    Zc= lt.dBZ_to_Zc(dBZ,vel)
    acum += Zc
    fig = plt.figure(figsize=(10,8))
    lt.plot_ppi(fig,Zc,title="No{}".format(i),xlabel="Easting from radar (km)",ylabel="Northing from radar (km)",cmap="viridis")
    #plt.savefig(figp+"{}".format(i)+"png")
    #plt.close()
fig= plt.figure(figsize=(10,8))
lt.plot_ppi(fig,acum,title="Acum",xlabel="acum",ylabel="acum",cmap="viridis")
plt.savegif("acum.png")
