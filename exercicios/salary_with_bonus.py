sellerName = str(input())
fixedSalary = float(input())
madeInMonth = float(input())

comission = (madeInMonth * 0.15)
finalSalary = format(fixedSalary + comission, '.2f')

print(f"TOTAL = R$ {finalSalary}")