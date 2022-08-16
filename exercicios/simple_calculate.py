from types import SimpleNamespace

product1 = SimpleNamespace()
product1.code = int(input())
product1.unitsNumber = int(input())
product1.unitPrice = float(input())

product2 = SimpleNamespace()
product2.code = int(input())
product2.unitsNumber = int(input())
product2.unitPrice = float(input())

valorPagar = (product1.unitsNumber * product1.unitPrice) + (product2.unitsNumber * product2.unitPrice)

print(f"VALOR A PAGAR: {valorPagar}")