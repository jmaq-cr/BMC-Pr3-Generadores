def cargarHilera():
    texto = ""
    tipo = str(input("1. Texto\n2. Archivo\n>>"))
    if tipo == "1":
        texto = str(input("Ingrese su cadena:\n>>"))
        return texto
    elif tipo == "2":
        direc = str(input("Ingrese la dirección de su archivo:\n>>"))
        try:
            file = open(direc,"r")
            texto = file.read()
            return texto
        except:
            print("Dirección no encontrada")
    else:
        print ("Opción no válida")
        return texto

