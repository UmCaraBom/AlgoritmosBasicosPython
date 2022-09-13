#criar entrada para quantidade de cigarros fumados por dia
cigarros = int(input(">> Digite a quantidade de cigarros fumados por dia: "))
#criar entrada para quantidade de anos fumando
anos = int(input(">> Digite a quantidade de anos fumando: "))
#calcular dias de vida perdidos
diasPerdidos = int((anos * 365) * (cigarros * 10 / 1440))
#mostrar dias de vida perdidos
print("> A quantidade de dias de vida perdidos é: ", diasPerdidos,"dias")
