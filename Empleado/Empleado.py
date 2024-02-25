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
