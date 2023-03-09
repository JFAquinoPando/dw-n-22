"""
Si el monto total de la compra excede de 500000 la empresa
tendrá la capacidad de invertir de su propio dinero un 55% del
monto de la compra, pedir prestado al banco un 30% y el resto lo
pagará solicitando un crédito al fabricante.
------------------------------
Si el monto total de la compra no excede de 500000 la empresa
tendrá capacidad de invertir de su propio dinero un 70% y el
restante 30% lo pagará solicitando crédito al fabricante.
------------------------------
El fabricante cobra por concepto de intereses un 20% sobre la
cantidad que se le pague a crédito
"""
montoCompra = int(input("Favor ingresar el monto de la compra: "))
if montoCompra > 500000:
    dineroPropio = 55/100
    banco = 30/100
    creditoFabricante = 1 - (dineroPropio + banco)
else:
    dineroPropio = 70/100
    banco = 0
    creditoFabricante = 1 - dineroPropio

creditoFabricanteInteres = creditoFabricante * 1.2

print("dineroPropio %",dineroPropio * 100)
print("banco %",banco * 100)
print("creditoFabricante %",creditoFabricante * 100)
print("creditoFabricanteInteres %",creditoFabricanteInteres *100)

# montoTotalPago = (dineroPropio * montoCompra) + (banco * montoCompra) + (creditoFabricanteInteres * montoCompra)
montoTotalPago = montoCompra * (dineroPropio + banco + creditoFabricanteInteres)
print("Inversion de dinero propio:", dineroPropio * montoCompra)
print("Pedido al banco:", banco * montoCompra)
print("Credito solicitado al fabricante", creditoFabricante * montoCompra)
print("Monto a estar abonando al fabricante (20% sobre el credito)", creditoFabricanteInteres * montoCompra)
print("Monto total a pagar:", montoTotalPago)