#criar entrada para km percorridos no carro
km = float(input(">> Digite a quantidade de km percorridos: "))
#criar entrada para dias de aluguel do carro
dias = int(input(">> Digite a quantidade de dias de aluguel: "))
#calcular o valor a pagar
valor = (km * 0.15) + (dias * 60)
#mostrar o valor a pagar
print("> O valor a pagar é: ", valor,"R$")