salary = float(input())
if 0 <= salary <= 400.00:
    percentual = 15
elif salary <= 800.00:
    percentual = 12
elif salary <= 1200.00:
    percentual = 10
elif salary <= 2000.00:
    percentual = 7
else:
    percentual = 4
reajuste = salary * percentual / 100
novo_salario = salary + reajuste
print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percentual} %")