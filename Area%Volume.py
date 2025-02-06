import math

# Mensaje de Inicio

print("Hola! Bienvenido a la Calculadora de Areas y Volumenes, ¿que quieres hacer?")

# Programa Principal

def calculator():
    while True:

        # Funciones para calcular Areas

        def square():
            length = int(input("Escribe la longitud del lado del cuadrado: "))
            width = int(input("Escribe la anchura del cuadrado: "))
            area = length * width
            print("El area del cuadrado es: " + str(area))
            mode = int(input("1 para Areas, 2 para Volumenes, 3 para Salir. "))

        def triangle():
            base = int(input("Escribe la base del triangulo: "))
            height = int(input("Escribe la altura del triangulo: "))
            area = (base * height) / 2
            print("El area del triangulo es: " + str(area))
            mode = int(input("1 para Areas, 2 para Volumenes, 3 para Salir. "))

        def circle():
            radius = int(input("Escribe el radio del circulo: "))
            area = math.pi * (radius ** 2)
            round = int(area)
            print("El area del circulo es: " + str(round))
            mode = int(input("1 para Areas, 2 para Volumenes, 3 para Salir. "))

        def trapezoid():
            upper = int(input("Escribe el lado superior del trapecio: "))
            lower = int(input("Escribe el lado inferior del trapecio: "))
            height = int(input("Escribe la altura del trapecio: "))
            area = ((upper + lower) / 2) * height
            print("El area del trapecio es: " + str(area))
            mode = int(input("1 para Areas, 2 para Volumenes, 3 para Salir. "))

        def rhombus():
            major = int(input("Escribe la diagonal mayor del rombo: "))
            minor = int(input("Escribe la diagonal menor del rombo: "))
            area = (major * minor) / 2
            print("El area del rombo es: " + str(area))
            mode = int(input("1 para Areas, 2 para Volumenes, 3 para Salir. "))

        def polygone():
            sides = int(input("Escribe la cantidad de lados del poligono: "))
            apothem = int(input("Escribe el apotema del poligono: "))
            long = int(input("Escribe el largo de los lados del poligono: "))
            area = ((apothem * long)/2) * sides
            print("El area del poligono es: " + str(area))

        # Funciones para calcular Volumenes

        def cube():
            length = int(input("Escribe la longitud del lado del cubo: "))
            width = int(input("Escribe la anchura del cubo: "))
            height = int(input("Escribe la altura del cubo: "))
            volume = length * width * height
            print("El volumen del cubo es: " + str(volume))
            mode = int(input("1 para Areas, 2 para Volumenes, 3 para Salir. "))

        def pyramid():
            length = int(input("Esbribe la longitud de la piramide: "))
            width = int(input("Escribe la anchura de la piramide: "))
            height = int(input("Escribe la altura de la piramide: "))
            volume = ((length * width) * height) * (1 / 3)
            print("El volumen de la piramide es: " + str(volume))
            mode = int(input("1 para Areas, 2 para Volumenes, 3 para Salir. "))

        def cone():
            radius = int(input("Escribe el radio del cono: "))
            height = int(input("Escribe la altura del cono: "))
            volume = (math.pi * (radius ** 2)) * height / 3
            round = int(volume)
            print("El volumen del cono es: " + str(round))
            mode = int(input("1 para Areas, 2 para Volumenes, 3 para Salir. "))

        def sphere():
            radius = int(input("Escribe el radio de la esfera: "))
            volume = (math.pi * (radius ** 3)) * (4 / 3)
            round = int(volume)
            print("El volumen de la esfera es: " + str(round))
            mode = int(input("1 para Areas, 2 para Volumenes, 3 para Salir. "))

        mode = int(input("1 para Areas, 2 para Volumenes, 3 para Salir. "))

        if mode == 1:
            print("Podemos hallar el area de cuadrados, triangulos, circulos, trapecios y rombos. ")
            mode2 = int(input("1 para cuadrados, 2 para triangulos, 3 para circulos, 4 para trapecios, 5 para rombos, y 6 para poligonos. "))
        elif mode == 2:
            print("Podemos hallar el volumen de cubos, piramides, conos y esferas. ")
            mode2 = int(input("7 para cubos, 8 para piramides, 9 para conos, y 0 para esferas. "))

        elif mode2 == 1:
            square()
        elif mode2 == 2:
            triangle()
        elif mode2 == 3:
            circle()
        elif mode2 == 4:
            trapezoid()
        elif mode2 == 5:
            rhombus()
        elif mode2 == 6:
            polygone()
        elif mode2 == 7:
            cube()
        elif mode2 == 8:
            pyramid()
        elif mode2 == 9:
            cone()
        elif mode2 == 0:
            sphere()
        elif mode == 3:
            print("Gracias por usar esta calculadora.")
            break

calculator()