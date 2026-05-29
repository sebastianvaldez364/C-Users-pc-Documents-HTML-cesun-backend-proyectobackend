#classes/clases.py
from p5 import *

class Borde:
    def __init__(self, grosor, color):
        self.grosor = grosor
        self.color = color

    def __str__(self):
        return f"grosor = {self.grosor}, color = {self.color}"


class Dimension:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"width = {self.width}, height = {self.height}"


class Posicion:
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

    def __str__(self):
        return f"x = {self.coord_x}, y = {self.coord_y}"

#La clase Cuadrado, Cambió a clase Figura
class Figura:
    def __init__(self, 
                 borde_grosor, borde_color, 
                 width, height, 
                 x, y, 
                 relleno, borde:Borde=None):

        if borde is None:
            self.borde = Borde(borde_grosor, borde_color)
        else:
            self.borde = borde
            
        self.dimension = Dimension(width, height)
        self.posicion = Posicion(x, y)

        self.color_relleno = relleno

        # velocidad en x y y
        self.vel_x = 3
        self.vel_y = 2

    def __str__(self):

        return f"""
        Borde: {self.borde}
        Dimension: {self.dimension}
        Posicion: {self.posicion}
        Color relleno: {self.color_relleno}
        """

    def dibujar(self):

        stroke_weight(self.borde.grosor)
        stroke(self.borde.color)

        fill(self.color_relleno)

        rect(
            self.posicion.coord_x,
            self.posicion.coord_y,
            self.dimension.width,
            self.dimension.height
        )

    # def desplazar_rebotar(self, max_x=600, max_y=600):
    def desplazar_rebotar(self, max_x:int=600, max_y:int=600):

        #para mover en x
        self.posicion.coord_x += self.vel_x

        # para mover en y
        self.posicion.coord_y += self.vel_y

        # rebote horizontal
        #if self.posicion.coord_x <= 0 or self.posicion.coord_x + self.dimension.width >= 600:
        if self.posicion.coord_x <= 0 or self.posicion.coord_x + self.dimension.width >= max_x:

            self.vel_x *= -1

        # rebote vertical
        if self.posicion.coord_y <= 0 or self.posicion.coord_y + self.dimension.height >= max_y:

            self.vel_y *= -1
            
class Cuadrado(Figura):
    ...

class Elipse(Figura):
    def dibujar(self):

        stroke_weight(self.borde.grosor)
        stroke(self.borde.color)

        fill(self.color_relleno)

        ellipse(
            self.posicion.coord_x,
            self.posicion.coord_y,
            self.dimension.width,
            self.dimension.height
        )
    
if __name__ == "__main__":

    cuadrado = Cuadrado(2, "#000000", 50, 50, 10, 10, "#463932")

    print(cuadrado)