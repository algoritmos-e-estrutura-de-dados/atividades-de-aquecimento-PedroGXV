a, b, c = list(map(int, input().split()))
maiorAb = ((a + b + abs(a-b)) / 2)

if (maiorAb > c):
  print(f"{maiorAb} eh o maior")
else:
  print(f"{c} eh o maior")