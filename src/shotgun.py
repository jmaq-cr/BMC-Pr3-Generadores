from random import *
import json

def shotgun(hileraBase, cantFragmentos, longFragmentos, desvLongitud, cobertura, errores, cantidadQuimeras, orientacion):
    print("")
    print("")
    print("Hilera base: ",hileraBase)
    print("Cantidad de fragmentos: ",cantFragmentos)
    print("Longitud de los fragmentos: ",longFragmentos)
    print("Desviación de la longitud: ",desvLongitud)
    print("Coberura: ",cobertura)
    print("Generar errores: ",errores)
    print("Cantidad de quimeras: ",cantidadQuimeras)
    print("Orientacion",orientacion)

    ##Genero el tamaño de los fragmentos con una distribución uniforme tomando en cuenta la desvición estándar
    tamanoFragmentos = []
    for i in range(cantFragmentos):
        tamanoFragmentos.append(int(round(uniform(longFragmentos-desvLongitud,longFragmentos+desvLongitud))))##distribucion uniforme

    

    #Se generan los frangmentos
    fragmentos = []

    if(cobertura):#Si nos piden cobertura de toda la hilera base
        if(cantFragmentos*longFragmentos < len(hileraBase)):
            print("Fragmentos insuficientes para cubrir toda la hilera base")
            return None
        else:#Si los fragmentos son suficientes para cubrir la hilera base
            index = 0
            for i in range(cantFragmentos):
                if index > (len(hileraBase)-min(tamanoFragmentos)):
                    index = randint(0,len(hileraBase)-min(tamanoFragmentos))
                newIndex = index + tamanoFragmentos[i]
                fragmentos.append(hileraBase[index:newIndex])
                index = newIndex
            print("Fragmentos: ",fragmentos)
            
    else:#Si no es necesario cubrir toda la hilera base
        for i in range(cantFragmentos):
            index = randint(0,len(hileraBase)-min(tamanoFragmentos))
            fragmentos.append(hileraBase[index:(index+tamanoFragmentos[i])])
        print("Fragmentos: ",fragmentos)

    #Se inducen errores en los fragmentos
    if(errores):
        distanciaErrores = int(round(expovariate(0.1))) #genera la distancia entre errores con distribucion exponencia
        totalLen = sum(len(f) for f in fragmentos)
        i = 0
        contError = 0
        for frag in range(len(fragmentos)):
            for i in range(len(fragmentos[frag])):
                if contError == distanciaErrores:
                    opc = randint(1,3)
                    if opc == 1:
                        alf = ["A","C","G","T"]
                        string = fragmentos[frag][:i]+alf[randint(0,3)]+fragmentos[frag][i:]
                        fragmentos.pop(frag)
                        fragmentos.insert(frag,string)                            
                    elif opc == 2:
                        alf = ["A","C","G","T"]
                        string = fragmentos[frag][:(i-1)]+alf[randint(0,3)]+fragmentos[frag][(i+1):]
                        fragmentos.pop(frag)
                        fragmentos.insert(frag,string)  
                    else:
                        string = fragmentos[frag][:(i-1)]+fragmentos[frag][(i+1):]
                        fragmentos.pop(frag)
                        fragmentos.insert(frag,string)
                    contError = 0
                else:
                    contError += 1
        print("Fragmentos con mutaciones: ",fragmentos)

    #Se generan las quimeras
    if(cantidadQuimeras > 0):
        fragTemp = []
        for i in range(len(fragmentos)):
            pos = randint(1,int(round(cantFragmentos/cantidadQuimeras))) #porcentaje de que haya una quimera dependiendo de la cantidad de fragmentos y quimeras deseadas
            if(pos == 1 and i < len(fragmentos)-1):
                fragTemp.append(fragmentos[i]+fragmentos[i+1])
            else:
                fragTemp.append(fragmentos[i])
        fragmentos = fragTemp
        print("Fragmentos con quimeras: ",fragmentos)

    #invierto algunos de los fragmentos
    if(orientacion):
        fragTemp = []
        for i in range(len(fragmentos)):
            pos= randint(1,4)
            if(pos == 1):
                fragTemp.append(fragmentos[i][::-1])
            else:
                fragTemp.append(fragmentos[i])
        fragmentos = fragTemp
        print("Fragmentos con inversiones: ",fragmentos)

    #Escribo los resutados en un archivo
    file = open('resultados.txt', 'w')
    for item in fragmentos:
        file.write("%s\n" % item)

    
    datos = {'Hilera Base': hileraBase,  'Cantidad de fragmentos': cantFragmentos, 'Longitud de Fragmentos': longFragmentos, 'Desviacion en la longitud': desvLongitud, 'Cobertura': cobertura, 'Errores': errores, 'Cantidad de quimeras': cantidadQuimeras, 'Orientacion': orientacion}
    with open('descripcion.json', 'w') as fp:
        json.dump(datos, fp)
        
##shotgun("ACGTGACGATCGATTAGGCTAGCGAGGCTAGAC",6,6,2,True,True,2,True)
