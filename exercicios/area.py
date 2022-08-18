import math

a = float(input())
b = float(input())
c = float(input())

triangleArea = (a * c) / 2
print(f"TRIANGULO: {triangleArea}")

circleArea = math.pi * math.pow(c, 2)
print(f"CIRCULO: {circleArea}")

if (a > b):
  biggestArea = a
  smallestArea = b
else:
  biggestArea = b
  smallestArea = a

trapArea = ((biggestArea + smallestArea) * c) / 2
print(f"TRAPEZIO: {trapArea}")

quadArea = math.pow(b, 2)
print(f"QUADRADO: {quadArea}")

retArea = a * b
print(f"RETANGULO: {retArea}")