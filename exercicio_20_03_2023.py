# -*- coding: utf-8 -*-
"""Exercicio_20_03_2023.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oa_7K5XvTH-vV-00tz2WiKmaC_K1mOqB

# Programa de Capacitaçao com Residência Tecnologica - PUC-Campinas/CPQD

Data(aula):20/03/2023 (aula assincrona)

Curso: Ciência (2023/1/M23111)

Aluna: Sara Bandeira Coutinho
"""

#Exercicio 8 
"""
Objetivo: Fazer a leitura do ano de construçao do imovel, do ano atual e calcular a idade do imovel e fornecer o % de desconto do IPTU. 

Entradas: Ano de construçao e ano atual em valores inteiros  
Processamento: Calculo da idade e calculo do desconto
Saida: Percentual do desconto do IPTU

"""
import datetime
from datetime import date #capturar data atual 

def main():
  #entradas
  ano_construcao = int(input("Digite o ano de construçao do imovel: "))
  ano_atual = date.today().year

  #processamento
  idade = ano_atual - ano_construcao

  #saida
  if idade < 5: 
    print("O percentual de desconto do IPTU é 0%")
  elif idade >=5 and idade < 20: 
    print("O percentual de desconto do IPTU é 15%")
  elif idade >= 20 and idade < 40: 
    print("O percentual de desconto é 25%")
  else: 
    print("O percentual de desconto e 30%")

#Ano 2022
if __name__ == "__main__": 
  main()

#Ano 2015
if __name__ == "__main__": 
  main()

#Ano 2002
if __name__ == "__main__": 
  main()

#Ano 1982
if __name__ == "__main__": 
  main()

#Exercicio 9 
""" 
Objetivo: Calcular o IMC de acordo com a tabela apresentada e emitir a classificaçao final. 

Entradas: peso e altura em reais
Processamento: calculo do IMC
Saida: classificaçao pela tabela proposta na questao 

"""

def main():
  #entradas
  peso, altura = input("Digite o peso em Kg e a altura em cm: ").split()
  peso, altura = float(peso), float(altura)/100.0 #conversao de centimetros pra metros  

  #processamento
  imc = peso / (altura**2)

  #saida
  if imc < 18.5:
    print("Baixo peso")
  elif imc >= 18.5 and imc < 25:
    print("Normal")
  elif imc >= 25 and imc < 30: 
    print("Sobrepeso")
  else:
    print("Obesidade")

# Peso 40 altura 1,65
if __name__ == "__main__":
  main()

# Peso 58 altura 1,65
if __name__ == "__main__":
  main()

# Peso 78 altura 1,65
if __name__ == "__main__":
  main()

# Peso 100 altura 1,65
if __name__ == "__main__":
  main()

#Exercicio 10

"""
Objetivo: ler 3 numeros e verificar se estao em ordem crescente

Entrada: 3 numeros inteiros
Processamento: verificar o maior e o menor e ver se estao alinhados em ordem crescente
Saida: dizer se estao alinhados ou nao

"""
def main():
  #entrada
  a, b, c = input("Digite os 3 numeros: ").split()
  a, b, c = int(a), int(b), int(c) #conversao de string para inteiro

  #processamento

  maior = max(a, b, c) #encontrando o maior
  menor = min(a, b, c) #encontrando o menor

  if (a == menor) and (c == maior): #verificando se estao em ordem crescente
    print("Os numeros estao em ordem")
  else: 
    print("Os numeros nao estao em ordem ")

#Numeros 1, 2, 3 
if __name__ == "__main__":
  main()

#Numeros 4, 2, 6 
if __name__ == "__main__":
  main()

#Exercicio 11 
 
"""
Objetivo: Calcular a média dos alunos e verificar o nivel de frequência pegando Av1 (avaliaçao 1) e Av2(avaliaçao 2) e calcular a média aritmética. Retornar o status 
do aluno na disciplina. 

Entradas: notas 1 e 2 e o percentual de frequência em float
Processamento: Calculo da média
Saida: Status do aluno na disciplina acordo com a tabela proposta na questao

"""

def main():
  #entrada
  av1, av2, frequencia = input("Digite a nota 1, a nota 2 e o % de frequência: ").split()
  av1, av2, frequencia = float(av1), float(av2), float(frequencia)
  #processamento
  media = (av1 + av2)/2

  #saida
  if frequencia < 75.0:
    print("Reprovado")
  else: 
    if media < 4: 
      print("Reprovado")
    elif media >= 4 and media < 6:
      print("Exame")
    else: 
      print("Aprovado")

#Nota 10, nota 9, % de frequencia 70%
if __name__ == "__main__":
  main()

#Nota 4, nota 2, % de frequencia 75%
if __name__ == "__main__":
  main()

#Nota 5, nota 5, % de frequencia 85%
if __name__ == "__main__":
  main()

#Nota 7, nota 9, % de frequencia 85%
if __name__ == "__main__":
  main()

#Nota 10, nota 10, % de frequencia 100%
if __name__ == "__main__":
  main()

#Exercicio 12 

"""
Objetivo: Calculo da funçao dada

Entrada: valor de x
Processamento: calculo da funçao
Saida: resultado caso x seja diferente de 0 e NAO E PERMITIDO EFETUAR A DIVISAO POR ZERO caso seja 0

Observaçoes: Maneira 1 com comandos if - else e maneira 2 com comandos try - except

"""
def main_1():
  #entrada
  x = float(input())
  #processamento

  if x != 0:
    y = ((4 * (x**2)) - (3*x) + 9)/ x
    print(y) #saida
  else:
    print("NAO E PERMITIDO EFETUAR A DIVISAO POR ZERO") #saida

# X = 0
if __name__=="__main__":
  main_1()

# X = 1
if __name__=="__main__":
  main_1()

def main_2():
  #entrada
  x = float(input())
  #processamento

  try: 
    y = ((4 * (x**2)) - (3*x) + 9)/ x
    print(y) #saida
  except ZeroDivisionError:
    print("NAO E PERMITIDO EFETUAR A DIVISAO POR ZERO") #saida

# X = 0
if __name__=="__main__":
  main_2()

# X = 1
if __name__=="__main__":
  main_2()