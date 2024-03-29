from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente
from CDT import CDT

class SimuladorBancario:
    """
    Atributos"""
    cedula=""
    nombre=""
    mesActual=""
    TipoCliente=""
    """----------------------------
    #1 = VIP , #2 = Platino y #3 = Normal
    -------------------------------"""
    """---------------------------
    Asociaciones
    ------------------------------"""
    corriente = CuentaCorriente()
    ahorros = CuentaAhorros()
    cdt = CDT()
    """-----------------------------
    Metodos
    ------------------------------"""
    def __init__(self, tipo_cliente):
        self.tipo_cliente = tipo_cliente
    
    def CambiarTipoCliente (self,nTipoCliente):
        self.TipoCliente = nTipoCliente
        return None
        
    def ConsignarCuentaCorriente(self, monto):
        self.corriente.ConsignarMonto(monto)
        
    def CalcularSaldoTotal(self):
     # Forma1
        return self.corriente.ConsultarSaldo()+self.ahorros.ConsultarSaldo()
        # #Forma2
        # saldoAhorros = self.ahorros.ConsultarSaldo()
        # saldoCorriente = self.corriente.ConsultarSaldo()
        # return saldoAhorros+saldoCorriente
        
    def PasarAhorrosACorriente(self):
        # forma1
        # self.corriente.ConsignarMonto(self.ahorros.ConsultarSaldo())
        # self.ahorros.RetirarMonto(self.ahorros.ConsultarSaldo())
        
        # forma 2
        # saldoAhorros = self.ahorros.ConsultarSaldo()
        # self.ConsignarCuentaCorriente(saldoAhorros)
        # self.ahorros.RetirarMonto(self, saldoAhorros)
        
        #forma 3
        saldoAhorros = self.ahorros.ConsultarSaldo()
        self.corriente.saldo += saldoAhorros
        self.ahorros.saldo = 0
    
    def ConsultarSaldoCorriente(self):
        # Aqui va el codigo del metodo
         return "Tu saldo es:"+self.Saldocorriente.ConsultarSaldo()
    
    def DuplicarAhorro(self): 
        #Forma 1
        self.ahorros.ConsignarMonto(self.ahorros.ConsultarSaldo())
        #Forma 2
        #self.ahorros.saldo *= 2

    def RetirarTodo(self, montototal):
        total = self.CalcularSaldoTotal()
        self.corriente.RetirarMonto(self.corriente.ConsultarSaldo())
        self.ahorros.RetirarMonto(self.ahorros.ConsultarSaldo())
        return "Retirarste Total: "+total

