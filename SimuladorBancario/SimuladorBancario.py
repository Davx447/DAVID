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
    def ConsignarSaldoCorriente(self, saldo):
        #Aqui va el codigo
        return self.SaldoCuentaCorriente.ConsignarValor(saldo)
    
    def CalcularSaldoTotal(self):
        #Aqui va el codigo
        SaldoTotal= self.SaldoCuentaCorriente + self.SaldoCuentaAhorros
        return "Saldo total es" + SaldoTotal
    
    def TransferirSaldoCorrienteaAhorros(self, monto):
        #Aqui va el codigo
        monto <= self.SaldoCuentaCorriente
        self.SaldoCuentaCorriente -= monto
        self.consignarSaldoAhorros(monto)
        return monto
    def ConsultarSaldoCorriente(self):
        # Aqui va el codigo del metodo
        return self.SaldoCuentaCorriente
    def RetirarTodo(self):
        # Aqui va el codigo
        SaldoRetirado = self.SaldoCuentaAhorros + self.SaldocuentaAhorros
        return "Su saldo retirado es:" + SaldoRetirado
    def DuplicarAhorro(self): 
        #Aqui va el codigo
        self.SaldoCuentaAhorros *= 2
        return self.DuplicarAhorro
