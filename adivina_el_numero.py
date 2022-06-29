import random 
#Nos da acceso a todo el módulo

def adivina_el_numero(x):
    
    print("•.................................•")
    print("      Bienvenido(a)! Juguemos!     ")
    print("•.................................•")
    print("Tienes que adivinar el número que elige la computadora.")
    
    
    numero_elegido_por_computadora = random.randint(1, x) #Número aleatorio entre 1 y x. 
    numero_ingresado_por_usuario = 0
    
    #Necesitamos repetir una cantidad x de veces que se repita. 
    #No sabemos cuanto demorará el usuario.
    while numero_ingresado_por_usuario != numero_elegido_por_computadora:
        #El usuario ingresa el número
        numero_ingresado_por_usuario = int(input(f"Adivina un número entre 1 y {x}: ")) #f-string reemplazar el valor de una variable o expresion

        if numero_ingresado_por_usuario < numero_elegido_por_computadora:
            print("Sigue intentando. Éste número es muy pequeño. ")
        elif numero_ingresado_por_usuario > numero_elegido_por_computadora:
            print("Sigue intentando. Éste número es muy grande. ")

    print(f"Felicitaciones, adivinaste! El número {numero_elegido_por_computadora} es el elegido por la computadora ☻")


adivina_el_numero(100)

#Llamamos a la función y establecemos el máximo del rango 