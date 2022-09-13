#criar entrada de saldo e calcule ajuste de saldo de 1%
saldo = float(input(">> Digite o saldo: "))
ajuste = saldo * 1 / 100
novoSaldo = saldo + ajuste
print("> O ajuste é: ", ajuste,"R$")
print("> O novo saldo é: ", novoSaldo,"R$")
