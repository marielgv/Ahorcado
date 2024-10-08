#GRUPO 4
# Mauro Antonio Chiguichon Chinchilla 202400610
# Melannie Daniela Jerónimo Sandoval 202405355
# Julián Haraldo Caceros Rac 202403934
# María Elena García Valencia 202405749
# Amanda Fabiola Martínez Mazariegos 202403453
# Estefany Nicol Castillo Retana 202400912

print(" █████╗ ██╗  ██╗ ██████╗ ██████╗  ██████╗ █████╗ ██████╗  ██████╗ ")
print("██╔══██╗██║  ██║██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔═══██╗ ")
print("███████║███████║██║   ██║██████╔╝██║     ███████║██║  ██║██║   ██║ ")
print("██╔══██║██╔══██║██║   ██║██╔══██╗██║     ██╔══██║██║  ██║██║   ██║ ")
print("██║  ██║██║  ██║╚██████╔╝██║  ██║╚██████╗██║  ██║██████╔╝╚██████╔╝ ")
print("╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ")

import random
IMAGENES_AHORCADO = ['''
 
   +---+
   |   |
       |
       |
       |
       |
 
=========''', '''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
print("Bienvenido al juego del ahorcado, listo para jugar")
print("Tu categoria a jugar es: ")
print(" █████╗ ███╗   ██╗██╗███╗   ███╗ █████╗ ██╗     ███████╗███████╗")
print("██╔══██╗████╗  ██║██║████╗ ████║██╔══██╗██║     ██╔════╝██╔════╝")
print("███████║██╔██╗ ██║██║██╔████╔██║███████║██║     █████╗  ███████╗")
print("██╔══██║██║╚██╗██║██║██║╚██╔╝██║██╔══██║██║     ██╔══╝  ╚════██║")
print("██║  ██║██║ ╚████║██║██║ ╚═╝ ██║██║  ██║███████╗███████╗███████║")
print("╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝")


def buscarpalabraaleatoria():
    nuestralistadepalabras=["delfin", "castor", "pez", "gato"] #No se debe repetir ningun caracter
    nuestrapalabraaleatoria = random.choice (nuestralistadepalabras)
    largo=len(nuestrapalabraaleatoria)
    print("La palabra tiene ", largo," caracteres")
    for i in range(0,largo):
    #  print("i i ", i)
      print (" _ " , end =" ")
        
    return nuestrapalabraaleatoria


def mostrarentablero(palabrasecreta, letrasadivinadas, dibujo, intentosresantes):
    print (dibujo[len(intentosresantes)])
    tablero = ""
    for letraingresadaporusuario in palabrasecreta:
        if letraingresadaporusuario in letrasadivinadas:
            tablero+=letraingresadaporusuario
        else:
            tablero +"_"
     
    print(tablero)

def jugarahorcado():
    palabrasecretadada = buscarpalabraaleatoria()
    strletrasadivinadaporjugador =[]
    strleteraserror=[]
    
    

    #len de las LETRAS adivinadas y len de letras incorrectas y luego mandarlas como parametros
    intentosresantes = 7

    while intentosresantes >0: 
        let=len(strletrasadivinadaporjugador)   
        
        mostrarentablero(palabrasecretadada, strletrasadivinadaporjugador,IMAGENES_AHORCADO,strleteraserror)
        strletra = str(input("Introduce una letra para seguir jugando : ")).lower()
        
        if strletra in strletrasadivinadaporjugador:
            print("Ya has ingresado esa letra, prueba otra")

            continue
        
        if strletra in palabrasecretadada:
            strletrasadivinadaporjugador.append(strletra)
            #let=len(strletrasadivinadaporjugador)
            if set(strletrasadivinadaporjugador)== set(palabrasecretadada):
                print(f"Felicidades, has adivinado la palabra, La palabra secreta era {palabrasecretadada}")
                print(" ██╗    ██╗██╗███╗   ██╗███╗   ██╗███████╗██████╗ ")
                print(" ██║    ██║██║████╗  ██║████╗  ██║██╔════╝██╔══██╗ ")
                print(" ██║ █╗ ██║██║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝ ")
                print(" ██║███╗██║██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗ ")
                print(" ╚███╔███╔╝██║██║ ╚████║██║ ╚████║███████╗██║  ██║ ")
                print("  ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ")
                print("██╗    ██╗███████╗     █████╗ ██████╗ ███████╗    ████████╗██╗  ██╗███████╗     ██████╗██╗  ██╗ █████╗ ███╗   ███╗██████╗ ██╗ ██████╗ ███╗   ██╗███████╗")
                print("██║    ██║██╔════╝    ██╔══██╗██╔══██╗██╔════╝    ╚══██╔══╝██║  ██║██╔════╝    ██╔════╝██║  ██║██╔══██╗████╗ ████║██╔══██╗██║██╔═══██╗████╗  ██║██╔════╝")
                print("██║ █╗ ██║█████╗      ███████║██████╔╝█████╗         ██║   ███████║█████╗      ██║     ███████║███████║██╔████╔██║██████╔╝██║██║   ██║██╔██╗ ██║███████╗")
                print("██║███╗██║██╔══╝      ██╔══██║██╔══██╗██╔══╝         ██║   ██╔══██║██╔══╝      ██║     ██╔══██║██╔══██║██║╚██╔╝██║██╔═══╝ ██║██║   ██║██║╚██╗██║╚════██║")
                print("╚███╔███╔╝███████╗    ██║  ██║██║  ██║███████╗       ██║   ██║  ██║███████╗    ╚██████╗██║  ██║██║  ██║██║ ╚═╝ ██║██║     ██║╚██████╔╝██║ ╚████║███████║")
                print(" ╚══╝╚══╝ ╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝       ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝")
                
                break
        else:
            intentosresantes -= 1
            strleteraserror.append(strletra)
            #leterr=len(strleteraserror)
            print(f"Tu letra es incorrecta, te quedan {intentosresantes} intentos")
            

    if intentosresantes == 0:
        print(f"Has perdido, la palabra secreta era: {palabrasecretadada}")
        print(" ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ ")
        print("██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗ ")
        print("██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝ ")
        print("██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗ ")
        print("╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║ ")
        print(" ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝ ")
          
    

jugarahorcado()








#########################################
# IMAGENES_AHORCADO = ['''
 
#    +---+
#    |   |
#        |
#        |
#        |
#        |
 
# =========''', '''
 
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========''', '''
 
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========''', '''
 
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
 
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========''', '''
 
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========''', '''
 
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========''']

# def mostrarentablero(palabrasecreta, letrasadivinadas, dibujo, intentosresantes):
#     print(dibujo[len(intentosresantes)])
#     tablero = ""
#     for letraingresadaporusuario in palabrasecreta:
#         if letraingresadaporusuario in letrasadivinadas:
#             tablero+=letraingresadaporusuario
#         else:
#             tablero +"_"
            
#     print(tablero)
# mostrarentablero("maripose","g", IMAGENES_AHORCADO,"ggg")
#  #TABLERO DEBERIA SER UN ARREGLO VACIO, VER APPEND, HACER UNA CONFIGURACION 
#  # BUSCAR PALABRA SECRETA Y POSICION DE LETRA


# #si la palabra no esta dentro de la funcion, imprimir los intentos restantes junto con el dibujo 
# #del muñequito