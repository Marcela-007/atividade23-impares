#Faça um programa que calcule a soma entre todos os números que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.
soma = 0 
contador = 0
for item in range(0,500):
  if item % 3 == 0:
    contador += 1
    print(f'A soma de todos os valores é {item}')
    soma = soma+item
    print(soma)