#criar entrada de preço e desconto e calcule o novo preço
preco = float(input(">> Digite o preço do produto: "))
desconto = float(input(">> Digite o desconto: "))
novoPreco = preco - (preco * desconto / 100)
print("> O novo preço é: ", novoPreco,"R$")