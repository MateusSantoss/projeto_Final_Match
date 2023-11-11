
print("------CALCULADORA DE META FINANCEIRA------\n")
print("Bem vindo a calculadora financeira, aqui você poderá simular quanto tempo você levará pra juntar aquela graninha!\n")
input("Presionse a tecla enter pra continuar...\n")


valorDesejado = float(input('Qual é a sua meta financeira?: '))
economiaMensal = float(input("Quanto você está disposto a guardar mensalmente?: "))

tempoPraAtingir = int(valorDesejado / economiaMensal)


print("Guardando {}$ todos os meses você levará {} meses para atingir a sua meta: ". format(economiaMensal, tempoPraAtingir))

