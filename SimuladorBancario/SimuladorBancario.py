from CuentaAhorros import CuentaAhorros

class SimuladorBancario:
    """
    Atributos"""
    cedula =0
    nombre =0
    mesActual =0
    """---------------------------
    Asociaciones
    ------------------------------"""
    SaldoCuentaCorriente=0
    SaldoCuentaAhorros=0
    SaldoTotal=0
    """-----------------------------
    Metodos
    ------------------------------"""
    def ConsignarCuentaCorriente(self, Cantidaddinero):
        #Aqui va el codigo
        MontoCuentaCorriente =+ Cantidaddinero
        return 0
    
    def CalcularSaldoTotal(self):
        #Aqui va el codigo
        self.SaldoTotalotal= self.SaldoCuentaCorriente + self.SaldoCuentaAhorros
        return "Saldo total es" +self.SaldoTotal
    
    def TransferirSaldoCuentaCorrienteaCuentaAhorros(self):
        #Aqui va el codigo
        
