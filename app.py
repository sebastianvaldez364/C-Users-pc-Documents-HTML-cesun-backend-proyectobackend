from p5 import *
from classes.clases import *
from patron.Builders import Builder

cuadrado = None
elipse = None
cuadrado3 = None
elipse3 = None
figuras = []

MAX_WIDTH = 800
MAX_HEIGHT = 700


def setup():
    global cuadrado
    global cuadrado3
    global elipse
    global elipse3
    global MAX_WIDTH
    global MAX_HEIGHT
    size(MAX_WIDTH, MAX_HEIGHT)
    
    figuras.append(crearFigura(0, 50,50))
    figuras.append(crearFigura(1, 100,200))
    

def draw():
    background(220)
    
    for figura in figuras:
        interactuarFig(figura)
    
    
def interactuarFig(figura:Figura):
    figura.dibujar()
    figura.desplazar_rebotar(max_y=MAX_HEIGHT)

def crearFigura(tipo: int, x:float, y:float):
    if tipo ==0:
        return Builder().configBorde(2,"#000000").configColor("#463932").configDimension(50,50).configPosicion(x,y).build()
    else:
        return Builder().configBorde(4,"#000000").configColor("#12B85D").configDimension(50,50).configPosicion(x,y).esElipse().build()
# def interactuar(cuadrado:Cuadrado):
#     cuadrado.dibujar()
#     cuadrado.desplazar_rebotar(max_y=MAX_HEIGHT)
    

# def interactuarCirculo(elipse:Elipse):
#     elipse.dibujar()
#     elipse.desplazar_rebotar(MAX_WIDTH, MAX_HEIGHT)

run()