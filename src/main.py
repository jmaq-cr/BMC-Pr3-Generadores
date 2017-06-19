from src.generadorHilera import *
from src.utilitario import *
from src.shotgun import *


def main():
    salir = False
    global lista
    global HileraBase
    global repeat
    global repeatOriginal
    global cantRepeat
    cantRepeat = 0


    while salir == False:


        print("1. Cargar hilera")
        print("2. Generar hilera Random")
        print("3. Generar hilera Bases desiguales")
        print("4. Generar Repeat")
        print("5. Generar Repeat Sistema")
        print("6. Insertar Repeat en la Hilera")
        print("7. Insertar Repeat en la Hilera Random")
        print("8. Modificar Repeat")
        print("9. Inserta Repeat con Errores")
        print("10. Generar Archivos")
        print("11. Shotgun")
        opc = str(input(">>"))
        if opc == "1":
            hileraBase = cargarHilera()
            print(hileraBase)
        elif opc == "2":
            tamano=int(input("Ingrese el tamano de la hilera"))
            hileraBase = generarRandom(tamano)
            print(hileraBase)
        elif opc == "3":
            baseA = float(input("Ingrese el valor para la base A"))
            baseG = float(input("Ingrese el valor para la base G"))
            baseT = float(input("Ingrese el valor para la base T"))
            baseC = float(input("Ingrese el valor para la base C"))
            tamano = float(input("Ingrese el tamano de la hilera"))
            hileraBase=generarBases(baseA,baseG,baseT,baseC,tamano)
            print(hileraBase)

        elif opc == "4":
            repeat=cargarHilera()
            repeatOriginal=repeat
            print(repeat)

        elif opc == "5":
            k = int(input("Ingrese el tamaño del repeat"))
            print(hileraBase)
            repeat=fuenteRepeatRandom(hileraBase,k)
            repeatOriginal=repeat
            print(repeat)

        elif opc == "6":
            posRepeat = int(input("Ingrese la posicion donde iniciará el repeat"))
            distancia = int(input("Ingrese la distancia entre los repeat"))
            cantidadRepeat = int(input("Ingrese la cantidad de repeat"))
            hileraResultado=insertarRepeatUser(hileraBase, repeat, posRepeat, distancia, cantidadRepeat)
            print("Hilera Base: "+ hileraBase)
            print("Hilera Repeat: " + repeat )
            print("Resultado: "+hileraResultado)
        elif opc == "7":
            hileraResultado=insertarRepeatRandom(hileraBase, repeat,0)
            print("Hilera Base: "+ hileraBase)
            print("Hilera Repeat: " + repeat )
            print("Resultado: "+hileraResultado)

        elif opc == "8":

            salirAux = False
            lista = []
            listaR=[]

            cantRepeat = int(input("Ingrese la cantidad de repeat"))
            i = 0
            while i < cantRepeat:
                lista.append(repeat)
                i = i + 1
            while salirAux == False:


                print("1. Modificar Repeat Insert")
                print("2. Modificar Repeat Cambia Base")
                print("3. Modificar Repeat Elimina")
                print("4. Orientacion Inversa")
                print("5. Salir")
                print()
                opcAux = str(input(">>"))


                if opcAux == "1":
                    print(repeatOriginal)
                    print(lista)
                    lista=mutaciones(lista,1)
                    print(lista)
                    print("Resultado: ", lista)
                elif opcAux == "2":
                    lista = mutaciones(lista, 2)
                    print("Resultado: " , lista)
                elif opcAux == "3":
                    lista = mutaciones(lista, 3)
                    print("Resultado: ", lista)
                elif opcAux == "4":
                    if len(lista)>0:
                        print(lista)
                        posicionRandom = randint(0, len(lista) - 1)
                        valorInvertido=reverse(lista[posicionRandom])
                        lista[posicionRandom]=valorInvertido
                        print(lista)
                        print(valorInvertido)
                elif opcAux == "5":
                    print(len(lista))
                    salirAux = True
        elif opc == "9":
            if (lista!=[]):
                posRepeat = int(input("Ingrese la posicion donde iniciará el repeat"))
                distancia = int(input("Ingrese la distancia del repeat"))
                deseaPalindromo=int(input ("Desea Palindromo [1/0]"))
                if deseaPalindromo== 1:
                    palin = palindromo(lista)
                    result=insertarRepeatError(hileraBase, posRepeat, palin, distancia, len(lista))
                    print(hileraBase)
                    print(palin)
                    print("Resultado: " + result)
                else:
                    result = insertarRepeatError(hileraBase, posRepeat, lista, distancia, len(lista))
                    print(hileraBase)
                    print("Resultado: " + result)
            else:
                print("Debe de ingresar al menos una modificacion en el repeat")

        elif opc == "11":
            print("Cargue su hilera:")
            hileraBase = cargarHilera()
            cantFragmentos = int(input("Cantidad de fragmentos: "))
            longFragmento = int(input("Longitud del fragmento: "))
            desvLongitud = int(input("Desviación estándar de la longitud: "))
            cobertura = False
            bool = str(input("Los fragmentos deben abarcar toda la hilera base? S/N  "))
            if(bool == "S" or bool == "s"):
                cobertura = True
            errores = False
            bool = str(input("Deben haber errores(inserción, borrado y cambio)? S/N  "))
            if (bool == "S" or bool == "s"):
                errores = True
            quimeras = int(input("Cantidad de quimeras: "))
            inversiones = False
            bool = str(input("Deben haber inversiones y complementos? S/N  "))
            if (bool == "S" or bool == "s"):
                inversiones = True
            shotgun(hileraBase,cantFragmentos,longFragmento,desvLongitud,cobertura,errores,quimeras,inversiones)

        elif opc == "#salir":
            salir = True


main()