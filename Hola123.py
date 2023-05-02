Archivo = open("{NombreArchivo}, r")
LeerArchivo = Archivo.readlines()

ArchivoLista = []

for line in LeerArchivo:
    ArchivoLista.append(line)
