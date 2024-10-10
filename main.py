#saida de dados

nome = input("digite seu nome completo: ")
idade = input("digite sua idade: ")
print(f"seu nome é {nome}, você tem {idade} anos")

#operações

print("*********************************************************")

numero1 = float(input("digite um numero: "))
numero2 = float(input("digite outro numero: "))


soma= numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print("soma: ", soma)
print("subtracao: ", subtracao)
print("multiplicacao: ", multiplicacao)
print("divisao: ", divisao)


#par ou impar
print("*********************************************************")


parouimpar = int(input("digite um numero: "))
if parouimpar % 2 == 0:
    print("o numero é par")
else:
        print("o numero é impar")

#maior de tres numeros
print("*********************************************************")

num1 = int(input("digite o primeiro numero: "))
num2 = int(input("digite o segundo numero: "))
num3 = int(input("digite o terceiro numero: "))
if num1 > num2 and num1 > num3:
      print(f"o maior numero é {num1}")
elif num2 > num1 and num2 > num3:
      print(f"o maior numero é {num2}")
elif num3 > num1 and num3> num2:
      print(f"o maior numero é {num3}")

#conversao de temperatura

print("*********************************************************")


temperatura = float(input("digite a temperatura em celsius: "))
fahrenheit = (temperatura * 9/5) + 32
print(f"a temperatura em fahrenheit é {fahrenheit}")

#calculo de média
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3

if media >=7:
  print(f"a media é {media} e você está aprovado")

else:
  print(f"a media é {media} e você está reprovado")

#contagem de numeros
contagem = 0
while contagem < 10:
     print(contagem)