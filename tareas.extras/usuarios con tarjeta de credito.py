#jade rojas
#12-5-25

from tarjetacredito import TarjetaCredito

class Usuario:
    def __init__(self, nombre, tarjeta=None):
        self.nombre = nombre
        self.tarjeta = tarjeta if tarjeta else TarjetaCredito()
        
    def hacer_compra(self, monto):
        self.tarjeta.compra(monto)
        return self
    
    def pagar_tarjeta(self, monto):
        self.tarjeta.pago(monto)
        return self
    
    def mostrar_saldo_usuario(self):
        print(f"=== Información de {self.nombre} ===")
        self.tarjeta.mostrar_info_tarjeta()
        return self

# Versión BONUS con múltiples tarjetas:
class UsuarioMultiplesTarjetas:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tarjetas = {} 
        
    def agregar_tarjeta(self, nombre_tarjeta, tarjeta=None):
        self.tarjetas[nombre_tarjeta] = tarjeta if tarjeta else TarjetaCredito()
        
    def hacer_compra(self, monto, nombre_tarjeta):
        if nombre_tarjeta in self.tarjetas:
            self.tarjetas[nombre_tarjeta].compra(monto)
        else:
            print(f"No se encontró la tarjeta {nombre_tarjeta}")
        return self
    
    def pagar_tarjeta(self, monto, nombre_tarjeta):
        if nombre_tarjeta in self.tarjetas:
            self.tarjetas[nombre_tarjeta].pago(monto)
        else:
            print(f"No se encontró la tarjeta {nombre_tarjeta}")
        return self
    
    def mostrar_saldo_usuario(self):
        print(f"=== Información de {self.nombre} ===")
        for nombre_tarjeta, tarjeta in self.tarjetas.items():
            print(f"\nTarjeta: {nombre_tarjeta}")
            tarjeta.mostrar_info_tarjeta()
        return self
