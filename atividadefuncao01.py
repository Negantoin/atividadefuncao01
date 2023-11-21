# Escreva um programa que pergunte a quantidade de km
# percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km
# rodado.

def codigo():
    km = float(input("Digite a quantidade de quilômetros percorridos: "))
    dias = int(input("Digite a quantidade de dias passados: "))
    preco = km * 0.15 + dias * 60
    print("O preço total a se pagar é: R$", preco)

codigo()