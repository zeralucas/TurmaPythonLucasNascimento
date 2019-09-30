print("="*60)

salario = float(input("{} Digite o salario liquido: ".format(" "*5)))

print("{} O salario liquido é: R${:.2f}".format(" "*5, salario))
print("{} Gastos e: R${:.2f}".format(" "*5, salario*0.5))
print("{} Investimentos LP: R${:.2f}".format(" "*5, salario*0.2))
print("{} Ivenstimentos CP: R${:.2f}".format(" "*5, salario*0.1))
print("{} Livre : R${:.2f}".format(" "*5, salario*0.2))


print("="*60)