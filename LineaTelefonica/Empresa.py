from LineaTelefonica import LineaTelefonica
class Empresa:
    
    '''----------------------------------------------------------------
    # atributos
    ----------------------------------------------------------------'''
    
    # Línea telefónica número 1.
    linea1 = ""
    # Línea telefónica número 2.
    linea2 = ""
    # Línea telefónica número 3.
    linea3 = ""
    
    '''----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------'''
    
    def __init__(self):
        self.linea1 = LineaTelefonica()
        self.linea2 = LineaTelefonica()
        self.linea3 = LineaTelefonica()
    #Definir estrato para cada linea
        self.linea1.definirEstrato(2)
        self.linea2.definirEstrato(5)
        self.linea3.definirEstrato(6)

        
        # TODO Parte3 PuntoA: Construir linea2 y linea3.
        
    # Retorna la l�nea 1.
    def darLinea1(self):
        return self.linea1
        # TODO Parte3 PuntoB: Completar el m�todo seg�n la documentaci�n dada.

    # Retorna la l�nea 2.
    def darLinea2(self):
        return self.linea2
        # // TODO Parte3 PuntoC: Completar el m�todo seg�n la documentaci�n dada.

    # Retorna la l�nea 3.
    def darLinea3(self):
        return self.linea3
        # // TODO Parte3 PuntoD: Completar el m�todo seg�n la documentaci�n dada.

    '''
	    # Retorna el n�mero total de llamadas realizadas.
	    # @return Total de llamadas de las tres l�neas.
	'''
    def darTotalNumeroLlamadas(self):
        # Forma1
        # return self.linea1.darNumeroLlamadas()+self.linea2.darNumeroLlamadas()+self.linea3.darNumeroLlamadas()
        Total = self.linea1.darNumeroLlamadas()+self.linea2.darNumeroLlamadas()+self.linea3.darNumeroLlamadas()
        return Total

    '''
	    # Retorna el total de minutos consumidos.
	    # @return Total de minutos de las tres l�neas.
	'''
    def darTotalMinutos(self):
        total = self.linea1.darNumeroMinutos()+self.linea2.darNumeroMinutos()+self.linea3.darNumeroMinutos()
        return total
        # TODO Parte3 PuntoF: Completar el m�todo seg�n la documentaci�n dada.

    '''
	    # Retorna el costo total de las llamadas realizadas.
	    # @return Costo total de las tres l�neas.
    '''
    def darTotalCostoLlamadas(self):
        total = self.linea1.darCostoLlamadas()+self.linea2.darCostoLlamadas()+self.linea3.darCostoLlamadas()
        return total
        # TODO Parte3 PuntoG: Completar el m�todo seg�n la documentaci�n dada.

    '''
        # Retorna el costo promedio de un minuto, seg�n los minutos consumidos. <br>
	    # @return Costo promedio por minuto.
    '''
    def darCostoPromedioMinuto(self):
        Promedio = self.darTotalCostoLlamadas()/self.darTotalMinutos()
        return Promedio
        # TODO Parte3 PuntoH: Completar el m�todo seg�n la documentaci�n dada.

    '''
        # Agrega una llamada local a la l�nea telef�nica 1 <br>
        # <b>post: </b> Se agreg� la llamada a la l�nea 1.
        # @param pMinutos N�mero de minutos de la llamada. pMinutos > 0.
    '''
    def agregarLlamadaLocalLinea1(self, pMinutos):
        self.linea1.agregarLlamadaLocal(pMinutos)

    '''
        # Agrega una llamada local a la l�nea telef�nica 2. <br>
        # <b>post: </b> Se agreg� la llamada a la l�nea 2.
        # @param pMinutos N�mero de minutos de la llamada. pMinutos > 0.
    '''
    def agregarLlamadaLocalLinea2(self, pMinutos):
        self.linea2.agregarLlamadaLocal(pMinutos)
        # TODO Parte3 PuntoI: Completar el m�todo seg�n la documentaci�n dada.

    '''
        # Agrega una llamada local a la l�nea telef�nica 3. <br>
        # <b>post: </b> Se agrega la llamada a la l�nea 3.
        # @param pMinutos N�mero de minutos de la llamada. pMinutos > 0.
    '''
    def agregarLlamadaLocalLinea3(self, pMinutos):
        self.linea3.agregarLlamadaLocal(pMinutos)
        # TODO Parte3 PuntoJ: Completar el m�todo seg�n la documentaci�n dada.

    '''
        # Agrega una llamada de larga distancia a la l�nea telef�nica 1. <br>
        # <b>post: </b> Se agrega la llamada a la l�nea 1.
        # @param pMinutos N�mero de minutos de la llamada. pMinutos > 0.
    '''
    def agregarLlamadaLargaDistanciaLinea1(self, pMinutos):
        self.linea1.agregarLlamadaLargaDistancia(pMinutos)

    '''
        # Agrega una llamada de larga distancia a la l�nea telef�nica 2. <br>
        # <b>post: </b> Se agrega la llamada a la l�nea 2.
        # @param pMinutos N�mero de minutos de la llamada. pMinutos > 0.
    '''
    def agregarLlamadaLargaDistanciaLinea2(self, pMinutos):
        self.linea2.agregarLlamadaLargaDistancia(pMinutos)
        # TODO Parte3 PuntoK: Completar el m�todo seg�n la documentaci�n dada.
    
    '''
        # Agrega una llamada de larga distancia a la l�nea telef�nica 3. <br>
        # <b>post: </b> Se agrega la llamada a la l�nea 3.
        # @param pMinutos N�mero de minutos de la llamada. pMinutos > 0.
    '''
    def agregarLlamadaLargaDistanciaLinea3(self, pMinutos):
        self.linea3.agregarLlamadaLargaDistancia(pMinutos)
        # TODO Parte3 PuntoL: Completar el m�todo seg�n la documentaci�n dada.

    '''
        # Agrega una llamada a celular a la l�nea telef�nica 1. <br>
        # <b>post: </b> Se agrega la llamada a la l�nea 1.
        # @param pMinutos N�mero de minutos de la llamada. pMinutos > 0.
    '''
    def agregarLlamadaCelularLinea1(self, pMinutos):
        self.linea1.agregarLlamadaCelular(pMinutos)

    '''
        # Agrega una llamada a celular a la l�nea telef�nica 2. <br>
        # <b>post: </b> Se agrega la llamada a la l�nea 2.
        # @param pMinutos N�mero de minutos de la llamada. pMinutos > 0.
    '''
    def agregarLlamadaCelularLinea2(self, pMinutos):
        self.linea2.agregarLlamadaCelular(pMinutos)
        # TODO Parte3 PuntoM: Completar el m�todo seg�n la documentaci�n dada.
    
    '''
        # Agrega una llamada a celular a la l�nea telef�nica 3. <br>
        # <b>post: </b> Se agrega la llamada a la l�nea 3.
        # @param pMinutos N�mero de minutos de la llamada. pMinutos > 0.
    '''
    def agregarLlamadaCelularLinea3(self, pMinutos):
        self.linea3.agregarLlamadaCelular(pMinutos)
        #TODO Parte3 PuntoN: Completar el m�todo seg�n la documentaci�n dada.
    
    '''
        # Reinicia todas las l�neas telef�nicas.
        # <b>post: </b> Se reinici� la llamada a la l�nea 1, 2 y 3. 
    '''
    def reiniciar(self):
        self.linea1.reiniciar()
        self.linea2.reiniciar()
        self.linea3.reiniciar()
        # // TODO Parte3 PuntoB: Completar el m�todo para reiniciar las lineas 2 y 3.

    '''----------------------------------------------------------------
    # Puntos de Extensi�n
    ----------------------------------------------------------------'''
    
    # M�todo para la extensi�n 1.
    # @return Respuesta 1.
    
"""--------------------------------------
    #def metodo1(self):
    TotalMinutosPorEstrato = self.darTotalMinutosPorEstrato()
    return "Total=" + TotalMinutosPorEstrato
----------------------------------------"""
    
def metodo1(self):
        TotalMinutosACelular = self.linea1.darMinutosLlamadasCelular() + self.linea2.darMinutosLlamadasCelular() + self.linea3.darMinutosLlamadasCelular()
        return "El total de minutos a celular es=" + TotalMinutosACelular
    
    # M�todo para la extensi�n 2.
    # @return Respuesta 2.
def metodo2(self):
    ValorBono = self.aplicarDescuentoATodos()
    return "Valor del bono es=" + ValorBono

def aplicarDescuentoATodos(self):
        # Invocar el método aplicarDescuento() para cada línea de la empresa
        descuento_total = self.linea1.aplicarDescuento() + self.linea2.aplicarDescuento() + self.linea3.aplicarDescuento()
        return descuento_total

def darTotalMinutosPorEstrato(self):
        total_minutos_por_estrato = 0
        total_minutos_por_estrato += self.linea1.darMinutosPorEstrato()
        total_minutos_por_estrato += self.linea2.darMinutosPorEstrato()
        total_minutos_por_estrato += self.linea3.darMinutosPorEstrato()
        return total_minutos_por_estrato
