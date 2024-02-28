from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente
from CDT import CDT

class SimuladorBancario:
    """
    Atributos"""
    cedula =0
    nombre =0
    mesActual =0
    """---------------------------
    Asociaciones
    ------------------------------"""
    SaldoCuentaCorriente= CuentaCorriente ()
    SaldoCuentaAhorros= CuentaAhorros ()
    CDT = CDT ()
    """-----------------------------
    Metodos
    ------------------------------"""
    def ConsignarCuentaCorriente(self, Cantidaddinero):
        #Aqui va el codigo
        MontoCuentaCorriente =+ Cantidaddinero
        return 0
    
    def CalcularSaldoTotal(self):
        #Aqui va el codigo
        SaldoTotal= self.SaldoCuentaCorriente + self.SaldoCuentaAhorros
        return "Saldo total es" +self.SaldoCuentaAhorros + self. SaldoCuentaAhorros
    
    def TransferirSaldoCuentaCorrienteaCuentaAhorros(self):
        #Aqui va el codigo
