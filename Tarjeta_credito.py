class TarjetaCredito:
    Todas_las_tarjetas = []

    def __init__(self, saldo_pagar=0, limite_credito=1000, intereses=1.5):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses
        TarjetaCredito.Todas_las_tarjetas.append(self)

    def compra(self, monto):
        if self.saldo_pagar + monto > self.limite_credito:
            print(f"compra de {monto} excede el limite de credito.")
        else:
            self.saldo_pagar += monto
        return self
    def pago(self, monto):
        if monto > self.saldo_pagar:
            self.saldo_pagar = 0
        else:
            self.saldo_pagar -= monto
        return self
    def cobrar_intereses(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses / 100
        return self
    def mostrar_info_tarjeta(self):
        print(f"Saldo a pagar: {self.saldo_pagar:.2f}, Límite de crédito: {self.limite_credito:.2f}, Intereses: {self.intereses:.2f}%")
        return self
    
    @classmethod
    def mostrar_todas_las_tarjetas(cls):
        for tarjeta in cls.Todas_las_tarjetas:
            tarjeta.mostrar_info_tarjeta()

tarjeta1 = TarjetaCredito(0, 5000, 1.5)
tarjeta2 = TarjetaCredito(0, 3000, 2)
tarjeta3 = TarjetaCredito(0, 1000, 3)
tarjeta1.compra(1000).compra(2000).pago(500).cobrar_intereses().mostrar_info_tarjeta()
tarjeta2.compra(500).compra(1000).compra(700).pago(300).pago(400).cobrar_intereses().mostrar_info_tarjeta()
tarjeta3.compra(200).compra(300).compra(400).compra(150).compra(100).compra(50).mostrar_info_tarjeta()

# BONUS: Mostrar información de todas las tarjetas
TarjetaCredito.mostrar_todas_las_tarjetas()