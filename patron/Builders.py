#patron/Builders.py
from classes.clases import *

class Builder:
    def __init__(self):
        self._esElipse = False
        
    def configBorde(self, borde_grosor:int, borde_color:int):
        self._borde_color = borde_color
        self._borde_grosor = borde_grosor
        return self
    
    def configColor(self, color:str):
        self._color_relleno = color
        return self
    
    def configPosicion(self, x: float, y: float):
        self._coord_x = x
        self._coord_y = y
        return self
        
    def configDimension(self, width: int = 50, height:int = 50):
        self._width = width
        self._height = height
        return self
    
    def esElipse(self):
        self._esElipse = True
        return self
    
    def build(self):
        variable = {
            'width':self._width,
            'height': self._height,
            'borde_grosor': self._borde_grosor,
            'borde_color':self._borde_color,
            'x': self._coord_x,
            'y': self._coord_y,
            'relleno':self._color_relleno
        }
        if self._esElipse == False:
            # return Cuadrado(width=50, height=50,
            #                 borde_grosor=self._borde_grosor, 
            #                 borde_color=self._borde_color,
            #                 x=50, y=50, 
            #                 relleno=self._color_relleno )
            # return Cuadrado(width=variable['width'], height=variable['height'],
            #                 borde_grosor=variable['borde_grosor'], 
            #                 borde_color=variable['borde_color'],
            #                 x=variable['x'], y=variable['y'], 
            #                 relleno=variable['relleno'] )
            return Cuadrado(**variable)
        else:
            return Elipse(**variable )
    # borde_grosor, borde_color, 
    #              width, height, 
    #              x, y, 
    #              relleno