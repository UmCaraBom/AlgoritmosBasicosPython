#criando algoritmo para mostrar próximo número inteiro
#n = float(input("Digite um número: "))
#print("O sucessor do número inteiro é: ", int(n+1))
#print("O antecessor do número inteiro é: ", int(n-1))

#criar classe id produto
class Produto:
    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco
    def imprimir(self):
        print (self.id, self.nome, self.preco)
class Carrinho:
    def __init__(self):
        self.produtos = []
    def adicionar(self, produto):
        self.produtos.append(produto)
    def imprimir(self):
        for produto in self.produtos:
            produto.imprimir()
    def total(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco
        return total

p1 = Produto(1, "Arroz ", 10)
p2 = Produto(2, "Feijão", 5)
p3 = Produto(3, "Macarrão", 3)

carrinho = Carrinho()
while True:
    print("--------- Menu ---------")
    print("> Digite 1 para adicionar produto")
    print("> Digite 2 para imprimir carrinho")
    print("> Digite 3 para imprimir total")
    print("> Digite 4 para sair")
    opcao = int(input())
    if opcao == 1:
        id = int(input("Digite o id do produto: "))
        if id == 1:
            print(">> "+p1.nome+"--> adicionado ao carrinho")
            carrinho.adicionar(p1)
        elif id == 2:
            print(">> "+p2.nome+" adicionado ao carrinho")
            carrinho.adicionar(p2)
        elif id == 3:
            print(">> "+p3.nome+" adicionado ao carrinho")
            carrinho.adicionar(p3)
    elif opcao == 2:
        print ("Carrinho tem:")
        carrinho.imprimir()
    elif opcao == 3:
        print(">>> Total da compra:",carrinho.total(),"R$")
    elif opcao == 4:
        print ("FIM DAS COMPRAS")
        break
    else:
        print("Opção inválida")
