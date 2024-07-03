import os

os.system ("cls")

print("Exemplo de While com texto")

resposta = input("Deseja calcular a soma de dois números? (SIM) ou (NÃO) - ").lower()

while resposta == "sim":
    print("=================================")
    print("Calculando a SOMA de Dois números")
    print("=================================")
    # 1 Passo - Entrada
    v1 = int(input("Digite um número: "))
    v2 = int(input("Digite um número: "))
    # 2 Passo - Processamento
    resultado = v1 + v2
    # 3 Passo - Saída
    print("O resultado é: ", resultado)
    resposta = input("Digite (SIM) para reiniciar, e (NÃO) para encerrar!").lower()

else:
    input("Pressione <ENTER> para encerrar o programa...")