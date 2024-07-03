import os

os.system ("cls")

print("=================================")
print("Exibindo um intervalo de Números")

# 1 Passo - Entrada
print("=================================")
inicio = int(input("Digite o inicio do intervalo: "))
fim    = int(input("Digite o fim do intervalo:    "))
print("=================================")

if inicio < fim:
    while inicio <= fim:    
        print("Números: ", inicio)
        inicio = inicio + 1
    else:
        print("==================================")
        input("Pressione <ENTER> para encerrar...")

else:
    while fim <= inicio:
        print("Número: ", fim)
        fim = fim + 1
print("==================================")
input("Pressione <ENTER> para encerrar...")