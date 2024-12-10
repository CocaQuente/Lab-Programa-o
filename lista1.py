#1. Faça um programa que imprima o seu nome.
def printName():
    print('Luiz')
#2 Faça um programa que imprima o produto dos valores 30 e 27.
def printProduct():
    print(f'30 x 27 = {30*27}')

#3. Faça um programa que imprima a média aritmética entre os números 5, 8, 12.
def mediaAritmetica():
    print('A Média Aritmética de 5, 8 e 12 é: ')
    print(f'\n{(5+8+12) /3}\n')

#4. Faça um programa que leia e imprima um número inteiro.
def numeroInteiro():
    numero = int(input('Digite Um Numero: '))
    print(f'O Numero Digitado é {numero}\nE o Tipo dele é: {type(numero)}\n')

#5. Faça um programa que leia dois números reais e os imprima.
def numeroReal():
    num1 = float(input('Digite Um Numero: '))
    num2 = float(input('Digite Um Numero: '))
    print(f'Numero Digitados: {num1}, {num2}')

#6. Faça um programa que leia um número inteiro e imprima o seu
#   antecessor e o seu sucessor.
def antecessorESucessor():
    numero = int(input('Digite Um Numero: '))
    print(f'O Antecessor de é: {numero - 1}')
    print(f'O Sucessor de  é: {numero + 1}')
    print(f'resultado: {numero -1} {numero} {numero +1}')

#7. Faça um programa que leia o nome o endereço e o telefone de
#   um cliente e ao final, imprima esses dados.
def dadosDoCliente():
    print('|-------{Bem Vindo ao Mercado ZapZap}-------|')
    nome = input('|-------------:informe Seu Nome:------------|\n|> ')
    endereco = input('|----------:Informe seu Indereço:-----------|\n|> ')
    telefone = int(input('|------:Informe um numero de contato:-------|\n|> '))

    print(f'\n| Nome     : {nome}\n| Endereço : {endereco}\n| Telefone : {telefone}')

#8. Faça um programa que leia dois números inteiros e imprima a
#   subtração deles.
def subtracao():
    numero1 = int(input('Digite um Numero: '))
    numero2 = int(input('Digite um Numero: '))
    print(f'{numero1} - {numero2} = {numero1-numero2}')

#9. Faça um programa que leia um número real e imprima ¼ deste número.
def umQuarto():
    numero = float(input('Digite um Numero Real: '))
    print(f'1/4 de {numero} é : {round(numero / 4, 2)}')

#10. Faça um programa que leia três números reais e calcule a
#    média aritmética destes números. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def realAritmetica():
    numeros = []
    for i in range(0,3):
        numeros.append(float(input(f'{i + 1}- Digite um Numero: ')))
    
    print(f'O Resultado da soma Aritmetica é: {round((numeros[0] + numeros[1] + numeros[2]) /3, 2)}')

#11. Faça um programa que leia dois números reais e calcule as
#    quatro operações básicas entre estes dois números, adição,
#    subtração,multiplicação e divisão. Ao final, o programa
#    deve imprimir os resultados dos cálculos.
def operacoesBasicas():
    numeros = []
    for i in range(0,2):
        numeros.append(float(input(f'{i+1}- Digite um Numero: ')))

    print(f'  {numeros[0]} + {numeros[1]} = {round(numeros[0]+numeros[1], 2)}\n')
    print(f'  {numeros[0]} - {numeros[1]} = {round(numeros[0]-numeros[1], 2)}\n')
    print(f'  {numeros[0]} x {numeros[1]} = {round(numeros[0]*numeros[1], 2)}\n')
    print(f'  {numeros[0]} ÷ {numeros[1]} = {round(numeros[0]/numeros[1], 2)}\n')

#12. Faça um programa que leia um número real e calcule o
#    quadrado deste número. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def elevadoAoQuadrado():
    numero = float(input('Digite um Numero: '))
    print(f'O numero {numero}² é igual a {round(numero**2, 2)}')

#13. Faça um programa que leia o saldo de uma conta poupança e
#    imprima o novo saldo, considerando um reajuste de 2%.
def reajuste():
    saldo = round(float(input('Digite o Saldo R$ ')),2)
    print(f'O seu Saldo com reajuste de 2% é: {round(saldo + (saldo * 2 / 100), 2)}')

#14. Faça um programa que leia a base e a altura de um retângulo
#    e imprima o perímetro (base + altura) e a área (base * altura / 2).
def perimetroDoRetangulo():
    print('---Perimetro de um Retangulo---')

    base = float(input('Informe a Base: '))
    altura = float(input('Informe a Altura: '))

    print(f'O Perimetro do retangulo é {round(base * 2 + altura * 2, 2)}')
    print(f'A Área do Retangulo é {round(base * altura /2, 2)}')

#15. Faça um programa que leia o valor de um produto, o percentual
#    do desconto desejado e imprima o valor do desconto e o valor
#    do produto subtraindo o desconto.
def descontoDeProduto():
    produto = float(input('Digite o valor do Produto: '))
    desconto = int(input('Digite a porcentagem do desconto: '))
    
    print(f'\nValor Sem desconto --------: {produto}')
    print(f'Porcentual do desconto ----: {desconto}%')
    print(f'Valor Com Desconto --------: {round(produto - (produto * desconto /100) ,2)}')

#16. Faça um programa que calcule o reajuste do salário de um
#    funcionário. Para isso, o programa deverá ler o salário atual
#    do funcionário e ler o percentual de reajuste. Ao final imprimir
#    o valor do novo salário.
def calculoDeReajuste():
    salario = float(input('Digite seu salario atual: '))
    reajuste = int(input('Porcentual de reajuste: '))

    print(f'O salario que antes era de {salario}')
    print(f'Com {reajuste}% de reaujuste\nAgora seu salario é {round(salario + (salario * reajuste /100) ,2)}')
          
#17. Faça um programa que calcule a conversão entre graus centígrados
#    e Fahrenheit. Para isso, leia o valor em centígrados e calcule
#    com base na fórmula a seguir. Após calcular o programa deve
#    imprimir o resultado da conversão.
#    F = (9 x C + 160) / 5
def converterCentigrados():
    centigrados = int(input('Informe a temperatura em centigrados: '))
    print(f'A temperatura convertida para Fahrenheit é {(9 * centigrados + 160) /5}')

#18. Faça um programa que calcule a quantidade de litros de combustível
#    consumidos em uma viagem, sabendo-se que o carro tem autonomia de
#    12 km por litro de combustível. O programa deverá ler o tempo
#    decorrido na viagem e a velocidade média e aplicar as fórmulas:
#    D = T x V       L = D / 12
#    Em que:
#    • D = Distância percorrida em horas
#    • T = Tempo
#    • V = Velocidade média
#    • L = Litros de combustível consumidos
#    Ao final, o programa deverá imprimir a distância percorrida e a
#    quantidade de litros consumidos na viagem.
def quantidadeDelitros():
    tempo = float(input('Digite o tempo decorrido: '))
    velocidade = int(input('Digite a Velocidade Média: '))
    distancia = tempo * velocidade /60

    print(f'A Distância percorrida foi de {distancia}km')
    print(f'A quantidade de Litros Consumidos foi de {distancia/12}l')

#19. Faça um programa que calcule o valor de uma prestação em atraso.
#    Para isso, o programa deve ler o valor da prestação vencida, a
#    taxa periódica de juros e o período de atraso. Ao final, o
#    programa deve imprimir o valor da prestação atrasada, o período
#    de atraso, os juros que serão cobrados pelo período de atraso, o
#    valor da prestação acrescido dos juros. Considere juros simples.
def prestacaoEmAtraso():
    prestacaoVencida = float(input('Digite o valor da prestação vencida: '))
    taxaDeJuros = float(input('Digite a taxa periódica de juros: '))
    periodoDeAtraso = int(input('Digite o período de atraso: '))

    juros = prestacaoVencida * (periodoDeAtraso * taxaDeJuros / 100)
    valorTotal = prestacaoVencida + juros

    print(f'Valor da Prestação Vencida --------------: {round(prestacaoVencida ,2)}')
    print(f'Periodo de Atraso -----------------------: {periodoDeAtraso} meses')
    print(f'juros Cobrado Pelo Periodo de Atraso ----: {round(juros ,2)}')
    print(f'\nValor total da Prestação em atraso ----: {round(valorTotal ,2)}')


#20. Faça um programa que efetue a apresentação do valor da conversão
#    em real (R$) de um valor lido em dólar (US$). Para isso, será
#    necessário também ler o valor da cotação do dólar.
def dolarEmReal():
    cotacao = float(input('Digite a cotação do Dolar: '))
    real = round(float(input('Digite o Valor R$ ')) ,2)

    print(f'O Valor convertido em Dolar: US${round(real * cotacao ,2)}')

while True:
    questao = int(input('Questão a ser executada: '))
    match questao:
        case 1:
            printName()
        case 2:
            printProduct()
        case 3:
            mediaAritmetica()
        case 4:
            numeroInteiro()
        case 5:
            numeroReal()
        case 6:
            antecessorESucessor()
        case 7:
            dadosDoCliente()
        case 8:
            subtracao()
        case 9:
            umQuarto()
        case 10:
            realAritmetica()
        case 11:
            operacoesBasicas()
        case 12:
            elevadoAoQuadrado()
        case 13:
            reajuste()
        case 14:
            perimetroDoRetangulo()
        case 15:
            descontoDeProduto()
        case 16:
            calculoDeReajuste()
        case 17:
            converterCentigrados()
        case 18:
            quantidadeDelitros()
        case 19:
            prestacaoEmAtraso()
        case 20:
            dolarEmReal()
        case _:
            break
