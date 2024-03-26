class LineaTelefonica:
    '''----------------------------------------------------------------
    # atributos
    ----------------------------------------------------------------'''
    
    # Numero de llamadas realizadas
    numeroLlamadas = ""
    
    # Numero de minutos consumidos
    numeroMinutos = ""
    
    # Costo total de las llamadas
    costoLlamadas = ""

    #Estrato de la linea telefonica
    estrato = 0

    #Descuento aplicable a las llamadas ( valor entre 0.0 y 25.5)
    descuento = 0.0

    # Cantidad de dinero disponible para gastar (prepago)
    prepago = 0.0

    #Almacenar el total de segundos 
    TotalSegundos = 0
    
    #Almacenar el costo de la llamada en dólares.
    Costollamadadolares = 0

    #Cantidad de minutos de llamadas a celular
    minutosLlamadasCelular = 0
    
    #Costo total de minutos de llamadas a celular
    costoLlamadasCelular = 0
    '''----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------'''

    # Inicializar el número de llamadas, número de minutos y costo de llamadas en 0.
    def __init__(self):
        self.numeroLlamadas = 0
        self.numeroMinutos = 0
        self.costoLlamadas = 0
        self.TotalSegundos = 0
        self.Costollamadadolares = 0
        self.costoLlamadasCelular = 0
        self.minutosLlamadasCelular = 0

    
    def reiniciar(self):
        self.numeroLlamadas = 0
        self.numeroMinutos = 0
        self.costoLlamadas = 0
        self.TotalSegundos = 0
        self.Costollamadadolares = 0
        self.costoLlamadasCelular = 0
        self.minutosLlamadasCelular = 0
    
    def convertirPesosADolares(self):
        Convertido = float(self.costoLlamadas / 3100)
        self.Costollamadadolares = Convertido
        return Convertido

        # TODO Parte2 PuntoA: Completar el método según la documentación dada.

    #Retorna el costo total de las llamadas realizadas.
    def darCostoLlamadas(self):
        return self.costoLlamadas
        # TODO Parte2 PuntoB: Completar el método según la documentación dada.
        
    # Retorna el número de llamadas realizadas por esta línea.
    def darNumeroLlamadas(self):
        return self.numeroLlamadas
        # TODO Parte2 PuntoC: Completar el método según la documentación dada.
        
    # Retorna el número de minutos consumidos.
    def darNumeroMinutos(self):
        return self.numeroMinutos
        # TODO Parte2 PuntoD: Completar el método según la documentación dada.

    # Reinicia la línea telefónica, dejando todos sus valores en cero.
    # post: El número de llamadas, número de minutos y costo de llamadas son 0.
    def reiniciar(self):
        self.numeroLlamadas = 0
        self.numeroMinutos = 0
        self.costoLlamadas = 0
        self.TotalSegundos = 0
        self.Costollamadadolares = 0

        # TODO Parte2 PuntoE: Completar el método según la documentación dada.

    # Agrega una llamada local a la línea telefónica
    # post: Se incrementá en 1 numeroDeLlamadas, se incremento numeroDeMinutos en minutos, costoLlamadas aumentá en ( minutos * 35 ).
    # :param pMinutos Número de minutos de la llamada. pMinutos >0.
    def agregarLlamadaLocal(self, pMinutos): 
        # Una llamada más
        self.numeroLlamadas += 1
        # Suma los minutos consumidos
        self.numeroMinutos += pMinutos
        # Suma el costo (costo por minuto: 35 pesos)
        self.costoLlamadas += pMinutos * 35
        DineroDisponible = self.darSaldoDisponible + self.AgregarDineroASaldo
        return DineroDisponible

    """
        Agrega una llamada de larga distancia a la línea telefónica.
        
        post: Se incrementá en 1 numeroDeLlamadas, se incremento numeroDeMinutos en minutos, costoLlamadas aumentá en ( minutos * 380 )
        
        :param pMinutos: Número de minutos de la llamada. pMinutos >0.
        """
    def agregarLlamadaLargaDistancia(self, pMinutos):
        self.numeroLlamadas += 1
        self.numeroMinutos += pMinutos
        self.costoLlamadas += pMinutos * 380

        # TODO Parte2 PuntoF: Completar el método según la documentación dada.

    '''
        Agrega una llamada a celular a la lÍnea telefónica
        post: Se incrementá en 1 numeroDeLlamadas, se incremento numeroDeMinutos en minutos, costoLlamadas aumentá en ( minutos * 999 )
        :param pMinutos Número de minutos de la llamada. pMinutos >0.
    '''
    def agregarLlamadaCelular(self, pMinutos):
        self.numeroLlamadas += 1
        self.numeroMinutos += pMinutos
        self.minutosLlamadasCelular += pMinutos
        self.costoLlamadas += pMinutos * 999
        self.costoLlamadasCelular += pMinutos * 999
        
        # TODO Parte2 PuntoG: Completar el método según la documentación dada.
    
    def darDescuento(self):
        return self.descuento
    
    def aplicarDescuento(self):
        return (self.costoLlamadas * self.descuento) / 100
    
    def darSaldoDisponible(self):
        return self.prepago
    
    def AgregarDineroASaldo(self, valor):
        self.prepago += valor
    
    def MotivarCliente(self):
        if(self.darNumeroMinutos>30):
            self.AgregarDineroASaldo + 1000 

    # Metodo que retorna el estrato de la linea.
    def darEstrato(self):
        return self.estrato
    
    def definirEstrato(self, pEstrato):
        self.estrato = pEstrato
    
    def darMinutosPorEstrato(self):
        return self.numeroMinutos * self.estrato
    
    def darMinutosLlamadasCelular(self):
        return self.minutosLlamadasCelular
    
    def darCostoLlamadasCelular(self):
        return self.costoLlamadasCelular
