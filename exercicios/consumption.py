distanceTraveled = int(input())
spentFuel = float(input())

averageConsumption = distanceTraveled / spentFuel

print(f"{format(averageConsumption, '.3f')} km/l")