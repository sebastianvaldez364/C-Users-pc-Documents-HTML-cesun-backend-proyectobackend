from p5 import *
from classes.clases import *
from patron.Builders import Builder
import random

cuadrado = None
elipse = None
cuadrado3 = None
elipse3 = None
figuras = []

MAX_WIDTH = 800
MAX_HEIGHT = 700


def colorRandom():
    return "#{:02X}{:02X}{:02X}".format(
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )


def setup():
    global cuadrado
    global cuadrado3
    global elipse
    global elipse3
    global MAX_WIDTH
    global MAX_HEIGHT

    size(MAX_WIDTH, MAX_HEIGHT)

    for i in range(10):

        tipo = random.randint(0, 1)

        x = random.randint(50, MAX_WIDTH - 50)
        y = random.randint(50, MAX_HEIGHT - 50)

        figuras.append(
            crearFigura(tipo, x, y)
        )


def draw():
    background(220)

    for figura in figuras:
        interactuarFig(figura)


def interactuarFig(figura: Figura):
    figura.dibujar()
    figura.desplazar_rebotar(max_y=MAX_HEIGHT)


def crearFigura(tipo: int, x: float, y: float):
    if tipo == 0:
        return Builder().configBorde(
            2, "#000000"
        ).configColor(
            colorRandom()
        ).configDimension(
            50, 50
        ).configPosicion(
            x, y
        ).build()
    else:
        return Builder().configBorde(
            4, "#000000"
        ).configColor(
            colorRandom()
        ).configDimension(
            50, 50
        ).configPosicion(
            x, y
        ).esElipse().build()


run()