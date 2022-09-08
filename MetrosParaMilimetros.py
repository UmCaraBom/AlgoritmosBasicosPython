#criar algoritmo para fazer metros para milímetros
opcao=(input(">> Digite 1 para converter metros para milímetros ou 2 para converter milímetros para metros: "))
if opcao == "1":
    metros = float(input(">> Digite a quantidade de metros: "))
    milimetros = metros * 1000
    print("> A quantidade de milímetros é: ", milimetros)
elif opcao == "2":
    milimetros = float(input(">> Digite a quantidade de milímetros: "))
    metros = milimetros / 1000
    print("> A quantidade de metros é: ", metros)
else:
    print(">> Opção inválida!")

