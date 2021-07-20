from function_files import save,read

#Menu
def menu():
    print("Bienvenido a su Agenda")
    print("-"*20)
    print("1. Agregar un registro")
    print("2. Mostrar un registro")
    print("0. Salir")
    print("-"*20)
    opcion = input("Ingrese una opción: ")
    continuar = True
    if opcion == "1":
        agregar_registro()
    elif opcion == "2":
        mostrar_registro()
    elif opcion == "0":
        continuar = False
    else:
        print("Ingrese una opción valida")
    return continuar


#Mostrar registros guardados
def mostrar_registro():

    personas = read()
    for i in personas:
        print("--"*10)
        for k,v in i.items():
            print(k,v, sep=": ")
        print("--"*10)



#Agregar datos
def agregar_registro():

    nombre=""
    while nombre =="":
        nombre = input("Ingrese su nombre: ").strip()
        if nombre == "": print("Ingrese su nombre correctamente")

    apellido=""
    while apellido =="":
        apellido = input("Ingrese su apellido: ").strip()
        if apellido == "": print("Ingrese su apellido correctamente")

    edad = -1
    while edad <= 17:
        try:
            edad = int(input("Ingrese su edad: "))
            if edad <= 17:
                print("Su edad debe ser igual o mayor a 18 años para registrarse")
        except:
            print("La edad debe ser un número")
    
    telefono = ""
    while len(telefono) != 9:
        telefono = input("Ingrese su telefono: ").strip()
        if len(telefono) != 9: print("El telefono debe tener largo de 9")
    
    correo = ""
    while not "@" in correo:
        correo = input("Ingrese su correo electrónico: ").strip()
        if not "@" in correo: print("El correo no es valido")
    
    #diccionario
    persona ={}
    #persona = {"nombre":nombre,"apellido":apellido}
    persona["nombre"] = nombre
    persona["apellido"] = apellido
    persona["edad"] = edad
    persona["telefono"] = telefono
    persona["correo"] = correo

    save(persona)