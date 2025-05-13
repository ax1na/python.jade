#jade rojas
#12-5-25
# La clase TarjetaCredito debe tener un saldo_pagar.
# Cuando se crea una nueva instancia de TarjetaCredito se da el monto,
# de lo contrario el saldo_pagar se establece como $0. 
# La tarjeta debe tener también un límite de crédito, 
# que se va a proporcionar en la creación de la instancia. 
# Por último, la tarjeta de crédito tendrá intereses, 
# los cuales deben guardarse como decimales; por ejemplo: 
#     si tiene 2% de interés, se guardará 0.02.
# Esta información también debe enviarse al crear la instancia.

class TarjetaCredito:
    def __init__(self, saldo_pagar=0, limite_credito=1000, intereses=0.02):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses
    
    def compra(self, monto):
        if self.saldo_pagar + monto <= self.limite_credito:
            self.saldo_pagar += monto
            print(f"Compra de ${monto} realizada. Saldo a pagar: ${self.saldo_pagar}")
        else:
            print("Límite de crédito excedido. Compra no autorizada.")

    def pago(self, monto):
        if monto > self.saldo_pagar:
            print(f"El pago de ${monto} excede el saldo a pagar de ${self.saldo_pagar}")
        else:
            self.saldo_pagar -= monto
            print(f"Pago de ${monto} realizado. Nuevo saldo: ${self.saldo_pagar}")

    def mostrar_info_tarjeta(self):
        print("=== Información de la Tarjeta ===")
        print(f"Saldo a pagar: ${self.saldo_pagar}")
        print(f"Límite de crédito: ${self.limite_credito}")
        print(f"Tasa de interés: {self.intereses * 100}%")

    def cobrar_interes(self):
        interes = self.saldo_pagar * self.intereses
        self.saldo_pagar += interes
        print(f"Se cobró un interés de ${interes}")
        print(f"Nuevo saldo a pagar: ${self.saldo_pagar}")

