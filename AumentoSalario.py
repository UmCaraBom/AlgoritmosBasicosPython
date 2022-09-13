#criar programa que calcule aumento de salário de acordo com o percentual
salario = float(input(">> Digite o salário: "))
percentual = float(input(">> Digite o percentual de aumento: "))
aumento = salario * percentual / 100
novoSalario = salario + aumento
print("> O aumento é: ", aumento,"R$")
print("> O novo salário é: ", novoSalario,"R$")
