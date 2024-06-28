
# How to install pygame in linux
# sudo apt install python3-pip
# sudo apt install python3-pygame

'''
Coment1
'''

"""
Comment2
"""

#Comment3

# """ 
# [print function]
#     --> print("your string here")
#     --> print('another string')
#     --> print("""
#     multi
#     line
#     string""")
# """

# import os modules,  os names: /// 'nt' == 'windows' /// 'posix' == 'linux/macos' ///

#########################################################

import sys
import pygame
import random
import datetime
from time import sleep
import math
pi = math.pi

# PRIMEIRO PROGRAMA PRÓPRIO

print('OLÁ MEU CARO!')
print('Escolha um número na sua mente entre 1 e 100.')
print('Não me fale ele, mantenha-o APENAS na sua mente.')
mstep1 = input('Já escolheu? Aperte enter')
print('Se escolheu, multiplique ele por 2.')
print('Use papel se você precisar.')
mstep2 = input('Não me diga o resultado, aperte enter quando você terminar')
print('Próximo passo, some 10 ao resultado da multiplicação.')
print('Não me fale o resultado.')
mstep3 = input('Conseguiu fazer a conta? Aperte enter')
print('Penúltimo passo, divida o resultado obtido por 2.')
mstep4 = input('Aperte enter quando você terminar.')
print('Chegamos ao último passo.')
print('Do resultado obtido até agora, subtraia o número que vc pensou inicialmente.')
mstep5 = input('Conseguiu? Aperte enter para eu adivinhar a resposta.')
print('O resultado final da sua conta dá 5.')
print('Matemática é magica!')
mstep6 = input('Aperte enter para rodar as lições de python')

# CURSO EM VIDEO

# AULA 04

sleep(5)
print('\n')
print('=-' * 7)
print('=-' * 5)
print('=-' * 3)
print('=-')
print('Desafio 001')
print('=-' * 7)
print('Hello, friend.')
nome = input('Me informe seu nome, por gentileza: ')
print('Prazer em te conhecer {}, eu me chamo Zahir e sou um software bem simples.'.format(nome))
print('Eu vou te perguntar alguns dados pra testar se eu estou funcionando direitinho.')

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 002')
print('=-' * 7)
print('Me informa sua data de nascimento, nessa ordem')
dia = input('Dia:')
mes = input('Mês:')
ano = int(input('Ano completo (4 digitos):'))
anoHj = 2021
idadeVc = anoHj - ano
print('A data do seu nascimento formatada ficaria {}/{}/{}.'.format(dia, mes, ano))
print('E se vc já fez aniversário está com {} anos de idade.'.format(idadeVc))

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 003')
print('=-' * 7)
idadeOutrem = int(input('Me informa a idade de qualquer outra pessoa:'))
somaIdades = idadeVc + idadeOutrem
print('Vocês dois juntos somam {} anos de idade no total.'.format(somaIdades))

print('\nDesafio003 (da aula anterior (aula 4))')

x = float(input('Digite um número real x: '))
y = float(input('Agora outro número y: '))
soma = x + y
print('A soma entre {1:2.3f} e {0:2.3f} vale aproximadamente {2:2.3f}'.format(x, y, soma))

a = float(input('Digite um número R: '))
b = float(input('Digite outro número R: '))
c = b + a
print('A soma entre {1:1.3f} e {0:1.3f} vale aproximadamente {2:1.3f}.'.format(a, b, c))

# AULA 006

print('\nPrática aula6')
n1 = input('Digite um número: ')
print(type(n1))
print(n1)
n1 = int(input('Digite ele novamente: '))
print(type(n1))
print(n1)
n1 = float(input('Digite ele mais uma vez: '))
print(type(n1))
print(n1)
n1 = bool(input('Penúltima vez, repete ele: '))
print(type(n1))
print(n1)
n1 = str(input('E agora pela última vez: '))
print(type(n1))
print(n1)

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 004')
print('=-' * 7)
n2 = input('Digite qualquer coisa: ')
print('É numérico?:', n2.isnumeric())
print('É letra?:', n2.isalpha())
print('É alfanumérico?:', n2.isalnum())
print('É maiuscula?:', n2.isupper())
print('É minúscula?:', n2.islower())
print('É digito?:', n2.isdigit())
print('É decimal?:', n2.isdecimal())
print('É identifier?:', n2.isidentifier())
print('É imprimível?:', n2.isprintable())
print('É espaço?:', n2.isspace())
print('Inicia com maiúscula?:', n2.istitle())
# print('É ASCII?:', n2.isascii())

dados = input('Digite o que você quiser: ')
print('O tipo primitivo (class) desse dado é:', type(dados))
print('Esse dado só possui espaços?', dados.isspace())
print('Esse dado só possui números?', dados.isnumeric())
print('É alfabético?', dados.isalpha())
print('É alfanumérico?', dados.isalnum())
print('São maiúsculas?', dados.isupper())
print('São minúsculas?', dados.islower())
print('Está capitalizada?', dados.istitle())
print('Procure outras definições em IDLEs e livros e seja feliz!')

x = float(input('Digite um número Real: '))
y = float(input('Digite outro numero Real: '))
z = float(input('Digite mais um número Real: '))
print('x = {0:1.3f}'.format(x))
print('y = {0:1.3f}'.format(y))
print('z = {0:1.3f}'.format(z))
print('x + y =', x + y)
print('x - y =', x - y)
print('y - x =', y - x)
print('x * y =', x * y)
print('x ** y =', x ** y)
print('y ** x =', y ** x)
print('x / y =', x / y)
print('y / x =', y / x)
print('x // y =', x // y)
print('y // x =', y // x)
print('x % y =', x % y)
print('y % x =', y % x)
print('=' * 23)
print('Olá, ' * 3, 'meu amigo.' * 2)
nome = input('Qual é o seu nome? ')
print('Segue abaixo algumas formatações com o input dado')
print('Olá, {0:s}!'.format(nome))
print('Olá, {0:20s}!'.format(nome))
print('Olá, {0:>20s}!'.format(nome))
print('Olá, {0:<20s}!'.format(nome))
print('Olá, {0:^20s}!'.format(nome))
print('Olá, {0:=20s}!'.format(nome))
# print('Olá, {0:=>20s}!'.format(nome))
# print('Olá, {0:=<20s}!'.format(nome))
# print('Olá, {0:=^20s}!'.format(nome))
print('Olá, {0:*^20s}!'.format(nome))
print('Olá, {0:a^20s}!'.format(nome))
print('Fuchique o código', end=' >>> ')
print('pra descobrir mais')

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 005')
print('=-' * 7)
numA = int(input('Digite um número inteiro (Z): '))
suc = numA + 1
ant = numA - 1
print('Seu sucessor é {2:d}, seu antecessor é {0:d} e o número digitado foi {1:d}.'.format(ant, numA, suc))

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 006')
print('=-' * 7)
numB = float(input('Digite um número real (R) que vc conheça a raiz quadrada pra te ajudar a entender: '))
dobro = 2 * numB
triplo = 3 * numB
raiz2 = numB ** (1 / 2)
print('Seu dobro vale {0:.3f}, o triplo {1:.3f} e sua raiz aproximadamente {2:.5f}.'.format(dobro, triplo, raiz2))

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 007')
print('=-' * 7)
p1 = float(input('Quanto você tirou na P1? '))
p2 = float(input('E na optativa (P2)? '))
media = (p1 + p2) / 2
print('Sua média  é {:.1f}.'.format(media))

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 008')
print('=-' * 7)
m = float(input('Digite sua altura em metros (apenas números): '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('{0:.2f}m convertido vale {1:.0f} cm e/ou {2:.0f} mm.'.format(m, cm, mm))
print('Outras conversões: km = {0:.5f}, hm = {1:.4f}, dam = {2:.3f}, dm = {3:.1f}.'.format(km, hm, dam, dm))

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 009')
print('=-' * 7)
t = int(input('Escolha e digite um número inteiro (Z) para exibirmos sua tabuada: '))
print('#' * 15)
print('{} x {:2} = {}'.format(t, 1, t * 1))
print('{} x {:2} = {}'.format(t, 2, t * 2))
print('{} x {:2} = {}'.format(t, 3, t * 3))
print('{} x {:2} = {}'.format(t, 4, t * 4))
print('{} x {:2} = {}'.format(t, 5, t * 5))
print('{} x {:2} = {}'.format(t, 6, t * 6))
print('{} x {:2} = {}'.format(t, 7, t * 7))
print('{} x {:2} = {}'.format(t, 8, t * 8))
print('{} x {:2} = {}'.format(t, 9, t * 9))
print('{} x {:2} = {}'.format(t, 10, t * 10))
print('#' * 15)

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 010')
print('=-' * 7)
dindin = float(input('Quanto de dinheiro você tem? (se não tiver nada, invete uma quantia). R$:'))
usd = dindin / 5.35
print('Você pode comprar {:.2f} dólares.'.format(usd))

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 011')
print('=-' * 7)
print('Me indique a altura e largura de uma parede')
larg = float(input('Largura: '))
alt = float(input('Altura: '))
m2 = alt * larg
tint = m2 / 2
print('Sua parede de {0:.2f} x {1:.2f} tem {2:.1f}m².'.format(alt, larg, m2))
print('Serão necessários {0:.1f} litros de tinta para pintá-la.'.format(tint))

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 012')
print('=-' * 7)
preco = float(input('Me fale o preço de algo, R$:'))
desc = preco * (5 / 100)
precoFinal = preco - desc
print('Com desconto de 5%, ele agora custa {:.2f}.'.format(precoFinal))

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 013')
print('=-' * 7)
sal = float(input('Quanto você ganha por mês em R$:'))
aumento = sal * (15 / 100)
salFinal = sal + aumento
print('Com um aumento de 15% você passará a ganhar R${:.2f}.'.format(salFinal))

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 014')
print('=-' * 7)
e = input('Escolha uma escala de temperatura, digite C, F ou K: ')
t = float(input('Agora designe um valor numérico para {}: '.format(e)))
if e == 'C':
    f = (t * 1.8 + 32)
    k = (t + 273.15)
    print('Convertendo {0:.1f}{1:s} para Fahrenheit teremos {2:.1f}°F.'.format(t, e, f))
    print('Já se convertermos para kelvin teremos {:.2f}K.'.format(k))
elif e == 'c':
    f = (t * 1.8 + 32)
    k = (t + 273.15)
    print('Convertendo {0:.1f}{1:s} para Fahrenheit teremos {2:.1f}°F.'.format(t, e, f))
    print('Já se convertermos para kelvin teremos {:.2f}K.'.format(k))
elif e == 'F':
    c = ((t - 32) / 1.8)
    k = (c + 273.15)
    print('Convertendo {0:.1f}{1:s} para Celsius teremos {2:.1f}°C.'.format(t, e, c))
    print('Já se convertermos para kelvin teremos {:.2f}K.'.format(k))
elif e == 'f':
    c = ((t - 32) / 1.8)
    k = (c + 273.15)
    print('Convertendo {0:.1f}{1:s} para Celsius teremos {2:.1f}°C.'.format(t, e, c))
    print('Já se convertermos para kelvin teremos {:.2f}K.'.format(k))
elif e == 'K':
    c = (t - 273.15)
    f = (c * 1.8 + 32)
    print('Convertendo {0:.1f}{1:s} para Celsius teremos {2:.1f}°C.'.format(t, e, c))
    print('Já se convertermos para fahrenheit teremos {:.1f}°F.'.format(f))
elif e == 'k':
    c = (t - 273.15)
    f = (c * 1.8 + 32)
    print('Convertendo {0:.1f}{1:s} para Celsius teremos {2:.1f}°C.'.format(t, e, c))
    print('Já se convertermos para fahrenheit teremos {:.1f}°F.'.format(f))
else:
    print('Você digitou algo errado, tente novamente.')

#  AULA 08

print('\nExemplo')

i1 = int(input('Digite um número para ter a raiz quadrada dele: '))
r = math.sqrt(i1)
print('{:.3f}'.format(r))

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 015')
print('=-' * 7)
dias = int(input('Digite a quantidade de dias que o carro esteve alugado: '))
dist = float(input('Digite a quilometragem rodada pelo carro durante o aluguel: '))
custo = (dias * 60.00) + (dist * .15)
print('O total a pagar é R${0:.2f}.'.format(custo))

print('Exemplo import math')
n = float(input('Raiz de '))
r = math.sqrt(n)
print(r)

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 016')
print('=-' * 7)
nd1 = float(input('Número decimal a: '))
print('A parte inteira de a é {}'.format(int(nd1)))

nd2 = float(input('Número decimal b: '))
ni = math.floor(nd2)
print('A parte inteira dele é {}'.format(ni))

nd3 = float(input('Número decimal c: '))
nt = math.trunc(nd3)
print('A parte inteira dele é {}'.format(nt))

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 017a')
print('=-' * 7)
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
h = math.hypot(co, ca)
print('Hipotenusa = {}'.format(h))

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 017b')
print('=-' * 7)
cy = float(input('Cateto oposto: '))
cx = float(input('Cateto adjacente: '))
hz = (((cy ** 2) + (cx ** 2)) ** (1 / 2))
print('Hipotenusa = {}'.format(hz))

# python lê inputs apenas radianos, precisamos converter de graus para radianos
sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 018a')
print('=-' * 7)
angDg = float(input('Ângulo em graus: '))
dg = math.radians(angDg)
sen = math.sin(dg)
cos = math.cos(dg)
tan = math.tan(dg)
print('Sen = {:.3f}'.format(sen))
print('Cos = {:.3f}'.format(cos))
print('Tan = {:.3f}'.format(tan))

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 018b')
print('=-' * 7)
print(pi)
angRd = float(input('Ângulo em radianos: '))
rd = math.pi * angRd
dgC = math.degrees(rd)
sen = math.sin(rd)
cos = math.cos(rd)
tan = math.tan(rd)
print('Sen {0:.1f} = {1:.3f}'.format(dgC, sen))
print('Cos {0:.1f} = {1:.3f}'.format(dgC, cos))
print('Tan {0:.1f} = {1:.3f}'.format(dgC, tan))

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 019a')
print('=-' * 7)
aluno1 = str(input('\nAluno 01: '))
aluno2 = str(input('\nAluno 02: '))
aluno3 = str(input('\nAluno 03: '))
aluno4 = str(input('\nAluno 04: '))
alunos = [aluno1, aluno2, aluno3, aluno4]
sort = random.choice(alunos)
print('O sorteado foi {}'.format(sort))

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 019b')
print('=-' * 7)
enter1 = input('Aperte enter pra sortear um filho: ')
print(random.choice(['Nenhum', 'Lyan', 'Leon', 'Lucca']))

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 019c')
print('=-' * 7)
enter2 = input('\nAperte enter para sortear um nome: ')
sort = int(random.randint(1, 4))
print(sort)
if sort == 1:
    print('Ana')
elif sort == 2:
    print('Bruna')
elif sort == 3:
    print('Cíntia')
elif sort == 4:
    print('Danny')

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 020a')
print('=-' * 7)
fam1 = str(input('Nome parente 1: '))
fam2 = str(input('Nome parente 2: '))
fam3 = str(input('Nome parente 3: '))
fam4 = str(input('Nome parente 4: '))
fam5 = str(input('Nome parente 5: '))
fam6 = str(input('Nome parente 6: '))
fam7 = str(input('Nome parente 7: '))
familia = [fam1, fam2, fam3, fam4, fam5, fam6, fam7]
# random.shuffle(familia)
# ordem = random.shuffle(familia)
print(familia)

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 020b')
print('=-' * 7)
enter3 = input('Ordem aleatória dos nomes: aperte enter.')
noix = 'Traian Thomas Martina Sandra Lucia Luciano Saura'.split()
random.shuffle(noix)
# embaralhado = random.shuffle(noix)
print(noix)

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 021')
print('=-' * 7)
print('Warning: Xing stream size off by more than 1%, fuzzy seeking may be even more fuzzy than by design!')
pygame.init()
pygame.mixer.music.load('mix17.mp3')
pygame.mixer.music.play()
pygame.event.wait()

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 022')
print('=-' * 7)
nome1 = str(input('Digite o nome completo de alguém: '))
length = int(len(nome1))
spaces = int(nome1.count(' '))
letters = length - spaces
print('Total de letras = {}.'.format(letters))
print('Em maiúsculas: ', nome1.upper())
print('Em minúsculas: ', nome1.lower())
splitName = nome1.split()
print('Seu primeiro nome é {} e ele possui {} letras'.format(splitName[0], len(splitName[0])))

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 023a')
print('=-' * 7)
n09 = float(input('Digite um número entre 0 e 9999: '))
m = n09 // 1000 % 10
c = n09 // 100 % 10
d = n09 // 10 % 10
u = n09 // 1 % 10
print('{} milhar'.format(m))
print('{} centenas'.format(c))
print('{} dezenas'.format(d))
print('{} unidades'.format(u))

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 023b')
print('=-' * 7)
numero = input('Digite um número ente 0 e 9999: ')
if len(numero) == 4:
    print('{} milhar'.format(numero[0]))
    print('{} centenas'.format(numero[1]))
    print('{} dezenas'.format(numero[2]))
    print('{} unidades'.format(numero[3]))
elif len(numero) == 3:
    print('{} centenas'.format(numero[0]))
    print('{} dezenas'.format(numero[1]))
    print('{} unidades'.format(numero[2]))
elif len(numero) == 2:
    print('{} dezenas'.format(numero[0]))
    print('{} unidades'.format(numero[1]))
elif len(numero) == 1:
    print('{} unidades'.format(numero[0]))

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 024')
print('=-' * 7)
cidade = input('Escreva o nome de uma cidade: ').strip()
print(cidade)
split = cidade.upper().split()
if split[0] == 'SANTO':
    print('Essa cidade começa com a palavra Santo')
elif split[0] == 'SANTOS':
    print('Essa cidade começa com Santos, no plural, e não Santo')
else:
    cid = cidade.capitalize().split()
    print('Essa cidade não começa com Santo e sim {}'.format(cid[0]))

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 025')
print('=-' * 7)
nome2 = input('Digite outro nome completo: ').upper().strip()
print('SILVA' in nome2)
silva = nome2.find('SILVA')
print('O nome não possui Silva nele') if silva == -1 else print('O nome possui Silva nele')

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 026')
print('=-' * 7)
frase = input('Digite uma frase: ')
print(frase)
lenf = len(frase)
frase.lower().find('a')
if frase.lower().find('a') == -1:
    print('A frase não possui letras a.')
else:
    print('Comprimento da frase: {} digitos.'.format(len(frase)))
    index = int(frase.lower().find('a'))
    print('A frase possui {} letras a.'.format(frase.lower().count('a')))
    print('Sua primeira ocorrência acontece na posição {}, (índice {}).'.format(index + 1, index))
    frase_ = frase[::-1]
    index_ = int(frase_.lower().find('a'))
    lenf_ = int(len(frase_))
    print('Sua última ocorrência é na posição {} (espaços e sinais inclusos).'.format(lenf_ - index_))
#print(frase.rfind('a')
#print(frase_.rfind('a')

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 027')
print('=-' * 7)
nome3 = input('Digite outro nome completo: ')
ns = nome3.split()
print(ns[0])
print(ns[-1])

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 028')
print('=-' * 7)
print('Processando...')
sleep(5)
num_guess = random.randint(0, 5)
input_guess = int(input('Pensei em um número de 0 a 5, tente adivinhá-lo: '))
print('{}, acertou.'.format(num_guess)) if num_guess == input_guess else print('Errou! Pensei no {}.'.format(num_guess))

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 029')
print('=-' * 7)
leV = float(input('Digite a velocidade lida em km/h: '))
if leV > 80:
    multa = (leV - 80.00) * 7
    print('Você foi multado por excesso de velocidade ({:.2f} km/h).'.format(leV))
    print('Valor a pagar: R$ {:.2f}.'.format(multa))
else:
    print('Dirija com cuidado, respeite o limite de velocidade. Boa viagem.')

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 030')
print('=-' * 7)
n = float(input('Digite um número para eu falar se ele é par ou impar: '))
ua = int(n % 2)
print('Par') if ua == 0 else (print('Ímpar'))

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 031')
print('=-' * 7)
distV = float(input('Qual a distância em km da viagem realizada: '))
if distV <= 200.00:
    print('Valor a ser cobrado: R${:.2f}.'.format(distV * .5))
else:
    print('Valor a ser cobrado: R$ {:.2f}.'.format(distV * .45))

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 032a')
print('=-' * 7)
anoInput = float(input('Digite um ano qualquer: '))
biss = int(anoInput % 4)
print(biss)
print('É ano bissexto.') if biss == 0 else print('Não é ano bissexto')
# import datetime
# date.time().year

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 032b')
print('=-' * 7)
anoInput = float(input('Digite um ano qualquer: '))
biss1 = int(anoInput % 4)
biss2 = int(anoInput % 400)
biss3 = int(anoInput % 100)
print('É ano bissexto.') if biss1 == 0 and biss3 != 0 or biss2 == 0 else print('Não é ano bissexto')

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 033')
print('=-' * 7)
print('Digite 3 números quaisquer.')
nn1 = float(input('N1: '))
nn2 = float(input('N2: '))
nn3 = float(input('N3: '))
print(nn1, nn2, nn3)
if nn1 < nn2 < nn3:
    print('Maior {}, menor {}'.format(nn3, nn1))
elif nn3 < nn2 < nn1:
    print('Maior {}, menor {}'.format(nn1, nn3))
elif nn2 < nn1 < nn3:
    print('Maior {}, menor {}'.format(nn3, nn2))
elif nn3 < nn1 < nn2:
    print('Maior {}, menor {}'.format(nn2, nn3))
elif nn1 < nn3 < nn2:
    print('Maior {}, menor {}'.format(nn2, nn1))
elif nn2 < nn3 < nn1:
    print('Maior {}, menor {}'.format(nn1, nn2))
else:
    print('Fim')
# verificar quantos ifs elifs, elses, ands e ors podem existir num bloco condicional

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 034a')
print('=-' * 7)
sala = float(input('Salário do funcionário: R$'))
if sala > 1250.00:
    print('Acréscimo = {:.2f}'.format(sala * .1))
    print('Novo salário com acréscimo de 10%: R${:.2f}'.format(sala + sala * .1))
else:
    print('Acréscimo = {:.2f}'.format(sala * .15))
    print('Novo salário com acréscimo de 15%: R${:.2f}'.format(sala + sala * .15))

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 034b')
print('=-' * 7)
salb = float(input('Salário funcionário: R$'))
if salb > 1250:
    ac = salb * .1
    saln = salb + ac
else:
    ac = salb * .15
    saln = salb + ac
print('Com acréscimo de R${0:.2f}, o novo salário será R${1:.2f}'.format(ac, saln))

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 035')
print('=-' * 7)
print('Digite o comprimento de 3 retas para formar um triângulo')
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('É possível fazer um triângulo')
else:
    print('Não é possível fazer um triângulo')

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 036')
print('=-' * 7)
p = float(input('Digite o valor do imóvel: R$ '))
s = float(input('Digite seu salário líquido: R$ '))
t = int(input('Digite em quantos anos você pretende para pagar: '))
s30p = s * .3
prest = p / (t * 12)
print('Prestação mínima: R$ {:.2f} para {:d} anos:'.format(prest, t))
if prest < s30p:
    print('Seu crédito foi aprovado. Financiada em {:d} vezes de R${:.2f}'.format((t * 12), s30p))
else:
    print('Lamentamos informar que seus rendimentos estão fora do perfil de financiamento')

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 037')
print('=-' * 7)
Z1 = int(input('Digite um número inteiro: '))
cvt = int(input("""Escolha uma base para conversão:
Binário -------> 1
Octal ---------> 2
Hexadecimal ---> 3
Sua escolha ---> """))
bin1 = bin(Z1)
oct1 = oct(Z1)
hex1 = hex(Z1)
# É possivel remover os prefixos 0b, 0c e 0x com .lstrip(prefixo entre aspas)
# É possível remover tbm com fatia [2:]
print('Bin = ', bin1)
print('Oct = ', oct1) 
print('Dec = ', Z1)
print('Hex = ', hex1)
if cvt == 1:
    print('Em binário, {} = {}'.format(Z1, bin1))
elif cvt == 2:
    print('Em octal, {} = {}'.format(Z1,oct1))
elif cvt == 3:
    print('Em hexadecimal {} = {}'.format(Z1,hex1))
else:
    print('Digite um número válido para a base')

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 038')
print('=-' * 7)
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
if n1 > n2:
    print('O primeiro é maior')
elif n1 < n2:
    print('O segundo é maior')
else:
    print('São iguais')

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 039')
print('=-' * 7)
ano = int(datetime.date.today().year)
nasc = int(input('Digite o ano do seu nascimento: '))
idade = ano - nasc
print('Quem nasceu em {:d} completa {:d} anos de idade em {:d}.'.format(nasc, idade, ano))
if idade < 18:
    print('Falta {} anos para seu alistamento militar'.format(18 - idade))
elif idade > 18:
    print('Se passou {} anos do seu alistamento, procure saber se sua situação está regular'.format(idade - 18))
else:
    print('Se você completa ou já completou 18 anos esse ano, procure a junta militar mais próxima para alistastamento obrigatório')

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 040')
print('=-' * 7)
p1 = float(input('Digite a sua nota da primeira prova: '))
p2 = float(input('Digite a sua nota da segunda prova: '))
m = (p1 + p2)/2
print('Média = {:.1f}'.format(m))
if m >= 7.0:
    print('{:.1f} Aprovado'.format(m))
elif m >= 5.0 and m < 7.0:
    print('{:.1f} Recuperação'.format(m))
else:
    print('{:.f} Reprovado'.format(m))

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 041')
print('=-' * 7)
data = datetime.date.today()
ano = datetime.date.today().year
nasc = int(input('Digite o ano em que o competidor nasceu: '))
idade = ano - nasc
print(data)
if idade >=0 and idade <= 9:
    print('Categoria mirim')
elif idade > 9 and idade <= 14:
    print('Categoria infantil')
elif idade > 14 and idade <= 19:
    print('Categoria junior')
elif idade > 19 and idade <= 25:
    print('Categoria sênior')
elif idade > 25 and idade < 99:
    print('Categoria master')
else:
    print('Digite um ano válido de 4 dígitos')

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 042')
print('=-' * 7)
print('Digite 3 valores para tamanho de segmentos de retas')
r1 = float(input('Segmento 1: '))
r2 = float(input('Segmento 2: '))
r3 = float(input('Segmento 3: '))
# procurar condições p indicar se triângulo é obtuso, agudo ou retângulo
if r1 > r2 + r3 or r2 > r1 + r3 or r3 > r1 + r2:
    print('Não é possível formar nenhum triângulo')
elif r1 == r2 == r3:
    print('O triângulo formado é equilátero')
elif r1 == r2 or r2 == r3 or r1 == r3:
    print('O triângulo formado é isosceles')
elif r1 != r2 and r2 != r3 and r3 != r1:
    print('O triângulo formado é escaleno')

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 043')
print('=-' * 7)
peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso/(altura ** 2)
print('IMC = {:.1f}'.format(imc))
if 0 < imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
elif imc >=40:
    print('Obesidade mórbida')
else:
    print('Digite valores válidos')

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 044')
print('=-' * 7)
preco = float(input('Digite o preço do produto: R$ ')) 
pag = int(input("""Digite a forma de pagamento:
1 --> Dinheiro
2 --> Cheque
3 --> Cartão
Pag: """))
if pag == 3:
    par = int(input('Digite o número de parcelas (à vista = 1 parcela): '))
    if par == 1:
        preco = preco - preco * .05
        print('À vista com 5% de desconto (cartão): R$ {:.2f}.'.format(preco))
    elif par == 2:
        prest = preco / 2
        print('2 parcelas de {:.2f} com preço final de {:.2f}.'.format(prest, preco))
    elif par > 2:
        preco = preco + preco * .2
        prest = preco / par
        print('{:d} parcelas de {:.2f} com preço final de {:.2f}.'.format(par, prest, preco))
elif pag == 1 or pag == 2:
    preco = preco - preco * .1
    print('À vista com 10% de desconto (dinheiro ou cheque): R$ {}.'.format(pag, preco))
else:
    total = preco
    print('Opção inválida, tente novamente')

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 045')
print('=-' * 7)
winC = 0
winP = 0
tesComp = r"""
    |     |
    |     |
    /      \
   /       |
   \_/     /
    / /\ \/
   / /  \ \
   \/    \/
"""

tesPlay = r"""
   /\    /\
   \ \  / /
   _\ \/ /\
  /  \     \
  \        /
   \      /
   |     |
   |     |
"""

papComp = r"""
   |      |
   |      |
   /      \
  /        \
 |         |
 | | | | | |
 \_| | | | |
   | | | |_|
   |_|_|_|
"""
papPlay = r"""
    _ _ _
   | | | |_
  _| | | | |
 / | | | | |
 | | | | | |
 |         |
  \        /
   \      /
   |      |
   |      |
"""

pedComp = r"""
  |      |
  |      |
  /      \
 /        \
 \/        |
  \/ / / //
   ¯¯¯¯¯¯¯
"""

pedPlay = r"""
   _______
  /\ \ \ \\
 /\        |
 \        /
  \      /
  |      |
  |      |
"""
while winC < 4 and winP < 4:
    compChoice = random.randint(0, 2)
    inputP = (input("""
Pressione 0 para PEDRA
Pressione 1 para PAPEL
Pressione 2 para TESOURA
"""))
    play = int(inputP)
    sleep(.3)
    print('\nJo')
    sleep(.3)
    print('\nKen')
    sleep(.3)
    print('\nPô')
    if play == 0:
        if compChoice == 0:
            print(pedComp)
            print(pedPlay)
            print('=-' * 13)
            print('Empate, vamos tentar de novo')
            print('=-' * 13)
        elif compChoice == 1:
            print(papComp)
            print(pedPlay)
            winC += 1
            print('=-' * 13)
            print('Venci, quer jogar de novo?')
            print('=-' * 13)
        elif compChoice == 2:
            print(tesComp)
            print(pedPlay)
            winP += 1
            print('=-' * 13)
            print('Você venceu, meus parabéns!')
            print('=-' * 13)
    elif play == 1:
        if compChoice == 0:
            print(pedComp)
            print(papPlay)
            winP += 1
            print('=-' * 13)
            print('Você venceu, meus parabéns!')
            print('=-' * 13)
        elif compChoice == 1:
            print(papComp)
            print(papPlay)
            print('=-' * 13)
            print('Empate, vamos tentar de novo')
            print('=-' * 13)
        elif compChoice == 2:
            print(tesComp)
            print(papPlay)
            winC += 1
            print('=-' * 13)
            print('Venci, quer jogar de novo?')
            print('=-' * 13)
    elif play == 2:
        if compChoice == 0:
            print(pedComp)
            print(tesPlay)
            winC += 1
            print('=-' * 13)
            print('Venci, quer jogar de novo?')
            print('=-' * 13)
        elif compChoice == 1:
            print(papComp)
            print(tesPlay)
            winP += 1
            print('=-' * 13)
            print('Você venceu, meus parabéns!')
            print('=-' * 13)
        elif compChoice == 2:
            print(tesComp)
            print(tesPlay)
            print('=-' * 13)
            print('Empate, vamos tentar de novo')
            print('=-' * 13)
        else:
            print('Você não digitou um número válido')
    print('Placar: eu {} x {} vc'.format(winC, winP))
    print('=-' * 10)
if winC > winP:
    print('Placar final: Eu {} x {} Você.'.format(winC, winP))
    print('Venci mais rodadas. Bom jogo')
    print('=-' * 10)
elif winP > winC:
   print('Placar final: Você {} x {} Eu.'.format(winP, winC))
   print('Você é muito bom, venceu mais rodadas')
   print('=-' * 18)

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 046')
print('=-' * 7)
stt = input('\nAperte enter para iniciar contagem regressiva')
for c in range(10, -1,-1):
    print(c)
    sleep(.3)
print('=-' * 10)
print('Alahu Ahkbar')
print('=-' * 10)
sleep(2)
print("""\033[1;31m
  \\   |   /
   \\  |  /
    \\ | /
— — — × — — — 
    / | \\
   /  |  \\
  /   |   \\
\033[m""")

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 047a')
print('=-' * 7)
even = [value for value in range(2, 51, 2)]
print(even)

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 047b')
print('=-' * 7)
for even_ in range(1, 51):
    if even_ % 2 == 0:
        print(even_, end=' ')

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 048a')
print('=-' * 7)
s = 0
counter = 0
for d3 in range(1, 501):
    if d3 % 3 == 0:
        print(d3, end=' ')
        s += d3
        counter += 1
print('\nA soma dos {} múltiplos de 3 entre 1 e 500 vale {}.'.format(counter, s))

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 048b')
print('=-' * 7)
s = 0
counter = 0
for d3 in range(1, 501, 2):
    if d3 % 3 == 0:
        print(d3, end=' ')
        s += d3
        counter += 1
print('\nA soma dos ímpares {} múltiplos de 3 entre 1 e 500 vale {}.'.format(counter, s))

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 048c')
print('=-' * 7)
soma = []
counter = 0
for d3 in range(1, 501, 2):
    if d3 % 3 == 0:
        print(d3, end=' ')
        soma.append(d3)
        counter += 1
somat = sum(soma)
print('\nA soma dos ímpares {} múltiplos de 3 entre 1 e 500 vale {}.'.format(counter, sum(soma)))

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 049')
print('=-' * 7)
t = int(input('\nEscolha uma tabuada para exibir: '))
for n in range(1, 11):
    print('{} × {} = {}'.format(t, n, (t*n)))
print('Estude bastante')

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 050')
print('=-' * 7)
s = 0
print('\nDigite uma série de 6 num inteiros: ')
for i in range(1, 7):
    n = int(input('{}° num: '.format(i)))
    if n % 2 == 0:
        s += n
print('A soma apenas dos números pares totaliza {}.'.format(s))

sleep(0)
print('\n')
print('=-' * 7)
print('Desafio 051')
print('=-' * 7)
pa = float(input('\nDigite o primeiro termo de uma PA: '))
r = float(input('Digite agora a razão da PA: '))
print(pa, end = ', ')
for sum_pa in range(0, 9):
    pa += r
    print(pa, end = ', ')

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 052a')
print('=-' * 7)
p = int(input('\nDigite num p/ verificar se é primo: '))
mult = 0
for l in range(0, p):
    if p % (l+1) == 0:
        mult += 1
if mult == 2 and p != 1:
    print('É primo')
else:
    print('Não é primo')

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 052b')
print('=-' * 7)
p = int(input('\nDigite num p/ verificar se é primo: '))
mult = 0
for l in range(0, p):
    if p % (l+1) == 0:
        mult += 1
if mult == 2 and p != 1:
    print('É primo')
else:
    print('Não é primo')

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 053a')
print('=-' * 7)
pal = str(input('Tente digitar um palindromo: ')).lower().replace(' ', '')
print(pal)
if pal == pal[::-1]:
    print('É palíndromo')
else:
    print('Não é palíndromo')

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 053b')
print('=-' * 7)
pal = str(input('Tente digitar um palindromo: ')).lower().replace(' ', '')
print(pal)
for pld in range (0, len(pal)):
    if pal == pal[::-1]:
        print('É palíndromo')
    else:
        print('Não é palíndromo')

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 054')
print('=-' * 7)
ano = datetime.datetime.today().year
minor = 0
major = 0
for i in range(1, 8):
    a = int(input('Digite o {} ano de nascimento de alguém: '.format(i)))
    idade = ano - a
    if 0 <= idade < 21:
        minor += 1
    elif 21 <= idade <= 999:
        major += 1
    else:
        print('Ano inválido, use ano jápassado e com 4 dígitos')
print('{} pessoas de maior.'.format(major), end=' ')
print('{} de menor.'.format(minor))

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 055')
print('=-' * 7)
peso = []
for p in range(1, 6):
    ps = float(input('\nDigite o {} peso: '.format(p)))
    peso.append(ps)
speso = sorted(peso)
print('O maior peso é {1:.2f} e o menor {0:.2f}.'.format(speso[0], speso[-1]))

sleep(5)
print('\n')
print('=-' * 7)
print('Desafio 056')
print('=-' * 7)
olderMn = str('')
olderMa = 0
minorF = 0
agesAll = []
for i in range(1, 5):
    n = str(input('\nInsira seu nome: '))
    a = int(input('Digite sua idade: '))
    g = str(input('Selecione seu gênero: [f/m] '))        
    if g == 'm' and a > olderMa:
        olderMn = n
        olderMa = a
        agesAll.append(a)
    elif g == 'f' and a < 20:
        minorF += 1
        agesAll.append(a)
    else:
        agesAll.append(a)
    print(olderMn, olderMa)
    print('minorF =', minorF)
    print(agesAll)
print('A média de idade dos valores computados é {}.'.format((sum(agesAll)/4)))
print('Total de mulheres menor que 20 anos: {}.'.format(minorF))
if olderMa != 0:
    print('O homem mais velho tem {} anos e se chama {}.'.format(olderMa, olderMn.title()))
else:
    print('Não há pessoas do sexo masculino na lista')

sleep(2)
print('-+-' * 4)
print('Desafio 057a')
print('-+-' * 4)
male = 0
female = 0
cond = True
print('Pra sair a qualquer momento, escreva Quit')
while cond == True:
    g = str(input('Escolha um gênero: [F/M] ')).upper()
    if g == 'F':
        female += 1
    elif g == 'M':
        male += 1
    elif g == 'QUIT':
        cond = False
    else:
        print('Entrada inválida, apenas [F/M]')
        cont = str(input('Deseja continuar? [S/N] ')).upper()
        if cont == 'S':
            cond = True
        else:
            cond = False
cont = str(input('Deseja continuar? [S/N] ')).upper()
if cont == 'N':
    cond = False
print('Registrados {} mulheres e {} homens.'.format(female, male))
print('Fim de processo')

sleep(2)
print('-+-' * 4)
print('Desafio 058')
print('-+-' * 4)
numPens = random.randint(1, 1000)
print('Pensei em um número entre 1 e 1000 você pode tentar quantas vezes quiser')
cond = False
count = 0
while not cond:
    numAdv = int(input('Tente adivinhar: '))
    count += 1
    if numAdv == numPens:
        cond = True
        print('Parabéns, você acertou!')
    elif numPens < numAdv and 1 < numAdv - numPens < 10:
        print('Menor, tá pegando fogo!')
    elif numPens < numAdv and 11 < numAdv - numPens < 100:
        print('Menor, tá ficando quente.')
    elif numPens < numAdv:
        print('Menor, mas tá frio.')
    elif numPens > numAdv and 1 < numPens - numAdv < 10:
        print('Maior, tá pegando fogo!')
    elif numPens > numAdv and 11 < numPens - numAdv < 100:
        print('Maior, tá ficando quente.')
    elif numPens > numAdv:
        print('Maior, mas tá frio.')
    else:
        print('Resposta inválida, tente de novo assim mesmo')
print('{} tentativas.'.format(count))
print('Ótimo jogo !')

sleep(2)
print('-+-' * 4)
print('Desafio 059a')
print('-+-' * 4)
func = True
while func == True:
    V1 = input('Digite um valor: ')
    Op = input("""
Escolha operação:
[  +  ] Soma
[  -  ] Subtração
[  *  ] Multiplicação
[  /  ] Divisão
[  f  ] Divisão inteira
[ mod ] Resto da divisão
[  ^  ] Potência
[  r  ] Raiz
[ log ] Logaritmo
[  >  ] É maior?
[  <  ] É menor?
[  =  ] É igual?
[ new ] Novos valores
[  c  ] Limpa
[  s  ] Sair
""")
    if Op == 'c':
        break
    elif Op == 's':
        func = False
    elif Op == 'new':
        V1 = int(input('Digite o primeiro valor: '))
        V2 = int(input('Digite o segundo valor: '))
    V2 = input('Digite o segundo valor: ')
    if Op == '+':
        print(float(V1) + float(V2))
    elif Op == '-':
        print(float(V1) - float(V2))
    elif Op == '*':
        print(float(V1) * float(V2))
    elif Op == '/':
        print(float(V1) / float(V2))
    elif Op == 'f':
        print(float(V1) // float(V2))
    elif Op == 'mod':
        print(float(V1) % float(V2))
    elif Op == '^':
        print(float(V1) ** float(V2))
    elif Op == 'r':
        print(float(V1) ** (1/float(V2)))
    elif Op == 'log':
        print('Trabalhando nos detalhes')
    elif Op == '>':
        print('O primeiro valor é maior do que o segundo?', float(V1) > float(V2))
    elif Op == '<':
        print('O primeiro valor é menor do que o segundo?', (float(V1) < float(V2)))
    elif Op == '=':
        print('O primeiro valor é igual ao segundo?', (float(V1) == float(V2)))
    else:
        print('Erro de sintaxe, repita processo')
        Ipt = input('Deseja continuar operações? [s/n] ')
        if Ipt == 's':
            func = True
        else:
            func = False
print('Fim do processo')

sleep(2)
print('-+-' * 4)
print('Desafio 059b')
print('-+-' * 4)
opt = 0
while opt != 5:
    V1 = int(input('Digite o primeiro valor: '))
    V2 = int(input('Digite o segundo valor: '))
    opt = int(input("""
Escolha operação que você deseja realizar com eles:
[1] Soma
[2] Multiplicação
[3] Maior
[4] Novos valores
[5] Sair
"""))
    if opt == 1:
        print('Soma vale', V1 + V2)
    elif opt == 2:
        print('O produto vale', V1 * V2)
    elif opt == 3:
        if V1 > V2:
            print(V1, 'é maior do que', V2)
        else:
            print(V2, 'é maior do que', V1)
    elif opt == 4:
        V1 = int(input('Digite o primeiro valor: '))
        V2 = int(input('Digite o segundo valor: '))
print('Fim do processo')

sleep(2)
print('-+-' * 4)
print('Desafio 060a')
print('-+-' * 4)
fato = int(input('Digite um número p/ calcularmos seu fatorial: '))
FATO = [1]
count = fato + 1
cond = True
while cond == True:
    count -= 1
    FATO.append(count * FATO[-1])
    if count == 1:
        cond = False
print('Fatorial de {} = {}'.format(fato, FATO[-1]))
#print(count, x)
print('Fim do processo')

sleep(2)
print('-+-' * 4)
print('Desafio 060b')
print('-+-' * 4)
fto = int(input('Digite um número para calcularmos todos os fatoriais que existem até ele: '))
FTO = [1]
count = 0
cond = True
while cond == True:
    count += 1
    FTO.append(count * FTO[-1])
    if count == fto:
        cond = False
print(FTO[1:])
print('Fim do processo')

sleep(2)
print('-+-' * 4)
print('Desafio 060c')
print('-+-' * 4)
fact = int(input('Digite um número inteiro para calcularmos seu fatorial: '))
print('{}! ='.format(fact), end=' ')
f = 1
count = fact + 1
while count > 1:
    count -= 1
    f *= count
    if count > 1:
        print(count, end=' x ')
    else:
        print(count, end=' = ')
print('{}! = '.format(fact), f)

sleep(2)
print('-+-' * 4)
print('Desafio 061')
print('-+-' * 4)
print('\nVamos trabalhar com PA novamente.')
termo1 = float(input('Digite o primeiro termo da sua PA: '))
rz = float(input('Digite agora a razão dela: '))
count = 0
PA = []
PA.append(termo1)
while count < 9:
    count += 1
    PA.append(rz + PA[-1])
print('Eis os 10 primeiros termos dela')
print(PA)

sleep(2)
print('-+-' * 4)
print('Desafio 062')
print('-+-' * 4)
print('\nVamos trabalhar com PA novamente.')
termo1 = float(input('Digite o primeiro termo da sua PA: '))
rz = float(input('Digite agora a razão dela: '))
count = 0
PA = []
PA.append(termo1)
while count < 9:
    count += 1
    PA.append(rz + PA[-1])
print('Eis os 10 primeiros termos dela')
print(PA)
cond = True
while cond == True:
    opt = float(input('Gostaria de ver mais alguns termos? Quantos? '))
    if opt == 0:
        print('Fim de operação')
        break
    else:
        count = 0
        while count < opt:
            count += 1
            PA.append(PA[-1] + rz)
        print(PA)

sleep(2)
print('-+-' * 4)
print('Desafio 063')
print('-+-' * 4)
termos = int(input('Quantos termos de fibonnacci (a partir do zero) você gostaria de ver? '))
seqF = [0, 1]
count = 0
while count < termos:
    count += 1
    seqF.append(seqF[-1] + seqF[-2])
print(seqF[:-2])

sleep(2)
print('-+-' * 4)
print('Desafio 064')
print('-+-' * 4)
number = []
print('Quando quiser parar, digite 999')
cond = True
count = 0
while cond == True:
    input9 = float(input('Digite um número: '))
    count += 1
    number.append(input9)
    if input9 == 999:
        cond = False
print('Foram digitados {} números, que somam {}'.format((count - 1), sum(number[:-1])))

sleep(2)
print('-+-' * 4)
print('Desafio 065')
print('-+-' * 4)
numbers = []
cond = True
count = 0
while cond == True:
    input9 = float(input('Digite um número: '))
    count += 1
    numbers.append(input9)
    sair = str(input('Deseja continuar? [s/n] '))
    if sair == 'n':
        cond = False
    else:
        cond = True
print('O menor número é {}, o maior é {}, e a média entre a soma deles é {}.'.format(min(numbers), max(numbers), sum(numbers)/(count)))

a = float(input('Digite o termo a da eguação quadrática: '))
b = float(input('Digite o termo b da equação quadrática: '))
c = float(input('Digite o termo c da equação quadrática: '))
d = (b**2)-(4*a*c)
print(d)
if a> 0:
    if d > 0:
        R1 = (-b+(math.sqrt(d)))/(2*a)
        R2 = (-b-(math.sqrt(d)))/(2*a)
        print('As raizes da equação são {:.5f} e {:.5f}.'.format(R1, R2))
    elif d == 0:
        R = -b/2*a
        print('A raiz da equação é {:.5f}.'.format(R))
    else:
        print('Não existe raiz real.')
else:
    print('O primeiro termo (a) precisa ser maior que 0 pra ser quadrática')
print('Fim')
