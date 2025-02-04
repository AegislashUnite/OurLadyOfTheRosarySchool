import math

mode = "Default"
again = "Default"

# Funciones para calcular Areas

def square():
  length = int(input("Escribe la longitud del lado del cuadrado: "))
  width = int(input("Escribe la anchura del cuadrado: "))
  area = length * width
  print("El area del cuadrado es: " + str(area))
  mode = input("A para Areas, V para Volumenes, y F para Finalizar.")

def triangle():
  base = int(input("Escribe la base del triangulo: "))
  height = int(input("Escribe la altura del triangulo: "))
  area = (base * height) / 2
  print("El area del triangulo es: " + str(area))
  mode = input("A para Areas, V para Volumenes, y F para Finalizar.")

def circle():
  radius = int(input("Escribe el radio del circulo: "))
  area = math.pi * (radius ** 2)
  round = int(area)
  print("El area del circulo es: " + str(round))
  mode = input("A para Areas, V para Volumenes, y F para Finalizar.")

def trapezoid():
  upper = int(input("Escribe el lado superior del trapecio: "))
  lower = int(input("Escribe el lado inferior del trapecio: "))
  height = int(input("Escribe la altura del trapecio: "))
  area = ((upper + lower) / 2) * height
  print("El area del trapecio es: " + str(area))
  mode = input("A para Areas, V para Volumenes, y F para Finalizar.")

def rhombus():
  major = int(input("Escribe la diagonal mayor del rombo: "))
  minor = int(input("Escribe la diagonal menor del rombo: "))
  area = (major * minor) / 2
  print("El area del rombo es: " + str(area))
  mode = input("A para Areas, V para Volumenes, y F para Finalizar.")

# Funciones para calcular Volumenes

def cube():
  length = int(input("Escribe la longitud del lado del cubo: "))
  width = int(input("Escribe la anchura del cubo: "))
  height = int(input("Escribe la altura del cubo: "))
  volume = length * width * height
  print("El volumen del cubo es: " + str(volume))
  mode = input("A para Areas, V para Volumenes, y F para Finalizar.")

def pyramid():
  length = int(input("Esbribe la longitud de la piramide: "))
  width = int(input("Escribe la anchura de la piramide: "))
  height = int(input("Escribe la altura de la piramide: "))
  volume = ((length * width) * height) * (1 / 3)
  print("El volumen de la piramide es: " + str(volume))
  mode = input("A para Areas, V para Volumenes, y F para Finalizar.")

def cone():
  radius = int(input("Escribe el radio del cono: "))
  height = int(input("Escribe la altura del cono: "))
  volume = (math.pi * (radius ** 2)) * height / 3
  round = int(volume)
  print("El volumen del cono es: " + str(round))
  mode = input("A para Areas, V para Volumenes, y F para Finalizar.")

def sphere():
  radius = int(input("Escribe el radio de la esfera: "))
  volume = (math.pi * (radius ** 3)) * (4 / 3)
  round = int(volume)
  print("El volumen de la esfera es: " + str(round))
  mode = input("A para Areas, V para Volumenes, y F para Finalizar.")

# Mensaje de Inicio

print("Hola! Bienvenido a la Calculadora de Areas y Volumenes, ¿que quieres hacer?")

# Bucle del Programa

if mode == "Default":
   mode = input("A para Areas, V para Volumenes, y F para Finalizar.")
if mode == "A":
   print("Podemos hallar el area de cuadrados, triangulos, circulos, trapecios y rombos.")
   mode = input("Q para cuadrados, T para triangulos, C para circulos, Z para trapecios, y R para rombos.")
if mode == "V":
   print("Podemos hallar el volumen de cubos, piramides, conos y esferas.")
   mode = input("B para cubos, P para piramides, N para conos, y E para esferas.")

if mode == "Q":
   square()
if mode == "T":
   triangle()
if mode == "C":
   circle()
if mode == "Z":
   trapezoid()
if mode == "R":
   rhombus()
if mode == "B":
   cube()
if mode == "P":
   pyramid()
if mode == "N":
   cone()
if mode == "E":
   sphere()
if mode == "F":
   print("Gracias, por usar esta Calculadora.")