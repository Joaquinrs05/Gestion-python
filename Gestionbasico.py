#Programa gestion colegio


#Para que sirve cada cosa: 
# {} Sirve para indicar la posicion.
#pop Sirve para quitar un objeto/cosa de una lista
#Format Sirve para añadir a una cadena un tipo en particular de dato

# Inicializar la lista vacía
lista_asignaturas = []

# Bucle  del programa
while True:
    # Mostrar el menú
    print("Menú: ")
    print("A) Vaciar Lista")
    print("B) Añadir Asignatura")
    print("C) Borrar Asignatura")
    print("D) Mostrar Asignatura")
    print("E) Mostrar Lista")
    print("F) Ordenar Lista A-Z")
    print("G) Ordenar Lista Z-A")
    print("H) Mostrar Número De Asignaturas")
    print("I) Mostrar Todas Las Asignaturas")
    print("X) Salir Del Programa")

    # Elegir una opción
    opcion = input("Selecciona una opción: ")
    
    #opcion A
    #La opcion A vacia toda la lista
    if opcion =="A" or opcion == "a":
        lista_asignaturas=[]
        print("La lista está vacía")
    
    #Opcion B
    #La opcion B añade asignaturas a la lista
    elif opcion =="B" or opcion=="b":
        Asignatura = input("Añade una asignatura: ")
        Maestro = input("Añade un maestro: ")
        clase = input("Añade una clase: ")
        lista_asignaturas2=[Asignatura, Maestro, clase]
        lista_asignaturas.append(lista_asignaturas2)
        print("Has añadido una asignatura")
    
    #Opcion C
    #La opcion C borra una asignatura de la lista usando Pop
    elif opcion == "C" or opcion=="c":
        # Borrar un elemento de la lista
        if len(lista_asignaturas) > 0:
            posicion = int(input("Ingresa la posición del elemento a borrar (0 - {}): ".format(len(lista_asignaturas)-1)))
            if 0 <= posicion < len(lista_asignaturas2):
                respuesta = print('¿Estas seguro de borrar la asignatura?(S/N)')
                respuesta2= input('S/N: ')
                if respuesta2== 'S':
                    elemento_borrado = lista_asignaturas.pop(posicion)
                    print("Se ha borrado el elemento '{}' de la lista.".format(elemento_borrado))
                elif print== 'N' :
                        print("La lista no ha cambiado")
            else:
                print("Posición inválida. Por favor, selecciona una posición válida.")
        else:
            print("La lista está vacía. No se puede borrar ningún elemento.")
            
    
    elif opcion == "D" or opcion=="d":
        # Mostrar un elemento de la lista
        if len(lista_asignaturas) > 0:
            posicion = int(input("Ingresa la posición del elemento a mostrar (0 - {}): ".format(len(lista_asignaturas)-1)))
            if 0 <= posicion < len(lista_asignaturas):
                print("Elemento en la posición {}: {}".format(posicion, lista_asignaturas[posicion]))
            else:
                print("Posición inválida. Por favor, selecciona una posición válida.")
        else:
            print("La lista está vacía. No hay elementos para mostrar.")
    
    
    elif opcion == "E" or opcion=="e":
        # Mostrar la lista completa
        if len(lista_asignaturas) > 0:
            print("Lista completa: ")
            for i, elemento in enumerate(lista_asignaturas):
                print("· {}: {}".format(i, elemento))
        else:
            print("La lista está vacía.")
            
    
    #Ordena la lista mediante al fundion sort
    elif opcion == "F" or opcion== "f":
        lista_asignaturas.sort()
        print (lista_asignaturas)
    
    #Muestra la lista empezando por el final gracias a la funcion Reverse
    elif opcion== "G" or opcion=="g":
        lista_asignaturas.reverse()
        print(lista_asignaturas)
        
    #Muestra cuantas asignaturas hay en la lista
    elif opcion== "H" or opcion== "h":
        print("Hay un total de ", len(lista_asignaturas), "asignaturas")
        
    #Muestra que asignaturas hay en la lista
    elif opcion== "I" or opcion== "i":
        for stade in range(len(lista_asignaturas)):
            print(lista_asignaturas[stade][0])
    #Cierra el programa
    elif opcion == "X" or opcion == "x":
        print("Se acabó el día")
        break
    
    else:
        print("Esa opción es incorrecta")
