import json

#save
def save(persona):
    # "a" -> append: si el archivo existe se agrega al final
    archivo = open("registros.json","a")
    #convertir el diccionario a json y escribirlo en el archivo
    archivo.write(f"{json.dumps(persona)}\n")
    archivo.close()

#read
def read():
    archivo = open("registros.json", "r")
    # personas -> lista
    # l -> cada linea del archivo que contiene los registros
    personas = [ json.loads(l.strip()) for l in archivo.readlines() ]
    archivo.close()
    return personas

