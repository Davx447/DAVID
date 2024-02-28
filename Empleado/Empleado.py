class Empleado:
    #Aqui va el codigo del empleado
    """-------------------------------------
    #atributos
    ----------------------------------------"""
    Nombre=""
    apellido=""
    ----------------------------------------------""
    """-----------------------------------------------
    #1 masculino y 2 femenino"
    ------------------------------------------------"""
    Sexo =0
    Salario =0
    """-----------------------------
    Asociaiones
    -----------------------------"""
    fechaNacimiento=Fecha()
    fechaIngreso=Fecha()

    '''-----------------------------------------------------------
    # Metodos
    -----------------------------------------------------------'''

    def CambiarSalario(self, nuevoSalario):
        # Aqui va el codigo de metodo
        return 0
    def CambiarEmpleado(self, nNombre, nApellido, nSexo , nSalario):
        # Aqui va el codigo del nuevo metodo
        return None  
    def ConsultarSalario(self):
        # Aqui va el codigo del metodo
        return self.Salario
    def ConsultarNombre(self):
        # Aqui va el codigo del metodo
        return self.nombre
    def ConsultarApellido(self):
        # Aqui va el codigo del metodo
        return self.apellido
def ConsultarNombreCompleto(self):
        # Aqui va el codigo del metodo
        return self.nombre +" " + self.apellido
    def AumentoSalarial(self):
        nSalario = self.salario * 0.05 
        nSalario = nSalario + self.Salario
        self.salario = nSalario
        return "El nuevo salario es de: "+self.salario
        
       def DuplicarSalario(self):
        # Aqui va el codigo
        # Forma 1
        # Self.salario = self.salario*2
        # Forma 2 pro
        self.salario *= 2
    def CalcularSalarioAnual(self):
        # Aqui va el codigo
        # self.Salario = self.salario*12
        #Forma 1
        SalarioAnual = self.salario*12
        return SalarioAnual
        #Forma 2
        # return self.salario*12
    def ConsultarDiaCumpleanio(self):
        return "El dia de su cumpleaños es: "+self.fechaNacimiento.ConsultarDia()
    def CalcularImpuesto(self):

        #forma 1
        total = self.CalularSarlarioAnual()
        return (total * 19.5) / 100
        #forma 2
        return self.CalcularSalarioAnual() * 0.195
        
    def ConsignarDinero(Self, cantidad):
        # Aqui va el codigo del metodo
        Self.salario += cantidad
        return cantidad
    def RetirarDinero(self, cantidad):
        # Aqui va el codigo del metodo
        self.Salario -= cantidad
        return cantidad
    def DarInteresMensual(self, interes):
        interes = self.salario * 0.06 
        self.salario += interes
        return "El nuevo salario es de: "+ self.salario
