from enum import Enum
"""----------------------------------------------------------------
# Enumeraciones
----------------------------------------------------------------"""
class Tipo(Enum):
    """----------------------------------------------------------------
    # Enumeraciones para los tipos de productos
    ----------------------------------------------------------------"""
    
    PAPELERIA = 1
    SUPERMERCADO = 2
    FARMACIA = 3

class Producto:
    _subsidio = False
    """-----------------------------------------------------------------
    #Constantes
    -----------------------------------------------------------------"""
    __IVAPAPELERIA= 0.16
    __IVASUPERMERCADO= 0.04
    __IVAFARMACIA= 0.12
    PRECIO_MAXIMO= 500000

    """------------------------------------------------------------------
    # Atributos
    -------------------------------------------------------------------"""
    __nombre = None
    __tipo = Enum ('Tipo',{'PAPELERIA','SUPERMERCADO','FARMACIA'})
    __valorUnitario = 0.0
    __cantidadBodega = 0
    __cantidadMinima = 0
    __cantidadUnidadesVendidas = 0

    """------------------------------------------------------------------
    # Metodos
    ------------------------------------------------------------------"""
    def getnombre(self):
        return self.__nombre
    def gettipo(self):
        return self.__tipo
    def getvalorUnitario(self):
        return self.__valorUnitario
    def getcantidadBodega(self):
        return self.__cantidadBodega
    def getcantidadMinima(self):
        return self.__cantidadMinima
    def getcantidadUnidadesVendidas(self):
        return self.__cantidadUnidadesVendidas
    
