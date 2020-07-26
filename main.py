##
##  UNIVERSIDAD DEL VALLE DE GUATEMALA
##  GRÁFICAS POR COMPUTADORA
##  SECCIÓN 20
##
##  SR3: Obj Models
##  LUIS PEDRO CUÉLLAR - 18220
##

from gl import Render, color

title = "---    ESCRITOR DE MODELOS OBJ    ---\n"
main_menu = """Opciones:
        1. Cambiar color de fondo (default = negro)
        2. Cambiar color de líneas (default = blanco)
        3. Graficar una mascarilla
        4. Graficar unos lentes
        5. Graficar un carro
        6. Salir
        """

wants_to_continue = True
option = 0
r = 0
g = 0
b = 0
are_values_ok = False

filename = "output.bmp"

r = Render(10000, 5000)

print(title)
while(wants_to_continue):
    print(main_menu)
    option = input("        Ingrese la opción que desea realizar: ")
    option = int(option)

    ##  changes the background color of the image
    if(option == 1):
        is_values_ok = False

        ## ask the values for the rgb and check that they are valid
        while(is_values_ok == False):
            r = input("Ingrese el valor r del color deseado (de 0 a 1): ")
            r = float(r)
            g = input("Ingrese el valor g del color deseado (de 0 a 1): ")
            g = float(g)
            b = input("Ingrese el valor b del color deseado (de 0 a 1): ")
            b = float(b)

            if((r < 0 or r > 1) or (g < 0 or g > 1) or (b < 0 or b > 1)):
                print("\nPor favor escoger valores entre 0 y 1\n")
            else:
                is_values_ok = True

                ##  changes the background color of the image
                render.glClearColor(r, g, b)

    ##  changes the color of the lines
    elif(option == 2):
        is_values_ok = False

        ## ask the values for the rgb and check that they are valid
        while(is_values_ok == False):
            r = input("Ingrese el valor r del color deseado (de 0 a 1): ")
            r = float(r)
            g = input("Ingrese el valor g del color deseado (de 0 a 1): ")
            g = float(g)
            b = input("Ingrese el valor b del color deseado (de 0 a 1): ")
            b = float(b)

            if((r < 0 or r > 1) or (g < 0 or g > 1) or (b < 0 or b > 1)):
                print("\nPor favor escoger valores entre 0 y 1\n")
            else:
                is_values_ok = True

                ##  changes the color of the lines
                render.glColor(r, g, b)

    ##  draws a face mask
    elif(option == 3):
        r.loadModel('./models/mask.obj', (5000, 2300), (300, 300))
        r.glFinish(filename)
        print("Termiado!\nPara ver todas las líneas, hacerle zoom a la imagen! \n")

    ##  draws a sunglasses
    elif(option == 4):
        r.loadModel('./models/Glasses.obj', (2200, 1500), (65, 65))
        r.glFinish(filename)
        print("Termiado!\n")

    ##  draws an f1 car
    elif(option == 5):
        r.loadModel('./models/f1.obj', (5000, 2300), (750, 750))
        r.glFinish(filename)
        print("Termiado!\n")
        print("Termiado!\nPara ver todas las líneas, hacerle zoom a la imagen! \n")

    ##  exits the program
    elif(option == 6):
        wants_to_continue = False
        print("BYEEE")
        
    else:
        print("Por favor escoja una opción válida!")
