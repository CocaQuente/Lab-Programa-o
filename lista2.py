from datetime import datetime
from deep_translator import GoogleTranslator

tradutor = GoogleTranslator(source = 'en', target = 'pt')
DATA = datetime.now()
#Exercícios sobre os comandos de condição em python

#1. Faça um programa que leia dois valores numéricos inteiros e efetue
#   a adição, caso o resultado seja maior que 10, apresentá-lo.
def q1():
    num = []
    for i in range(0,2):
        num.append(int(input(f'{i+1}- Digite um Numero: ')))

    resultado = num[0]+num[1]

    if resultado >= 10:
        print(f'{num[0]} + {num[1]} = {resultado}')
    else:
        print('A Soma dos numeros Digitado é menor que 10')

#2. Faça um programa que leia dois valores inteiros e efetue a adição.
#   Caso o valor somado seja maior que 20, este deverá ser apresentado
#   somando-se a ele mais 8, caso o valor somado seja menor ou igual a
#   20, este deverá ser apresentado subtraindo-se 5.
def q2():
    num = []
    for i in range(0,2):
        num.append(int(input(f'{i+1}- Digite um Numero: ')))

    resultado = num[0]+num[1]

    if resultado > 20:
        print(f'{resultado} + 8 = {resultado + 8}')
    else:
        print(f'{resultado} - 5 = {resultado - 5}')

#3. Faça um programa que leia um número e imprima uma das duas mensagens:
#   "É múltiplo de 3"ou "Não é múltiplo de 3".
def q3():
    num = int(input('Digite um Numero: '))
    
    if num%3 == 0:
        print(f'{num} é múltiplo de 3')
    else:
        print(f'{num} não é múltiplo de 3')

#4. Faça um programa que leia um número e informe se ele é ou não divisível por 5.
def q4():
    num = int(input('Digite um Numero: '))

    if num%5 == 0:
        print(f'{num} é múltiplo de 5')
    else:
        print(f'{num} não é múltiplo de 5')

#5. Faça um programa que leia um número e informe se ele é divisível por 3 e por 7.
def q5():
    num = int(input('Digite um Numero: '))

    if num%3 == 0 and num%7 == 0:
        print(f'{num} é divisivel por 3 e 7')
    elif num%3 == 0:
        print(f'{num} é divisivel por 3 mas não é divisivel por 7')
    elif num%7 == 0:
        print(f'{num} é divisivel por 7 mas não é divisivel por 3')
    else:
        print(f'{num} não é divisivel por 3 e 7')

#6. A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários
#   estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
#   bruto. Faça um programa que permita entrar com o salário bruto
#   e o valor da prestação e informar se o empréstimo pode ou não ser concedido.
def q6():
    salario = float(input('Digite seu salario: '))
    prestacao = float(input('Valor da prestação: '))
    if prestacao <= 0.3 * salario:
        print(f'O emprestimo foi aprovado !')
    else:
        print('O emprestimo foi Recusado\n!- Ultrapassou 30% do salario bruto') #concertar o codigo

#7. Faça um programa que leia um número e indique se o número está compreendido
#   entre 20 e 50 ou não.
def q7():
    num = round(float(input('Digite um Numero: ')), 2)

    if num >= 20 and num <= 50:
        print(f'O Numero {num} esta entre os numeros 20 e 50')
    else:
        print(f'O Numero {num} não esta entre os numeros 20 e 50')

#8. Faça um programa que leia um número e imprima uma das mensagens:
#   "Maior do que 20", "Igual a 20"ou "Menor do que 20".
def q8():
    num = round(float(input('Digite um Número: ')), 2)

    if num > 20:
        print('maior do que 20')
    elif num == 20:
        print('Igual a 20')
    else:
        print('Menor do que 20')
#9. Faça um programa que permita entrar com o ano de nascimento da pessoa e com o
#   ano atual. O programa deve imprimir a idade da pessoa. Não se esqueça de
#   verificar se o ano de nascimento informado é válido.
def q9():
    while True:
        dataNascimento = input('Ano de Nascimento (dd/mm/aaaa): ')
        nascimento = datetime.strptime(dataNascimento, '%d/%m/%Y')

        if nascimento > DATA:
            print(f'!- Data de Nascimento {nascimento} Invalido\nData Maxima Permitida: {DATA}')
            print('\nDigite Novamente')
        else:
            break

    print(f'Idade Atual: {round((DATA - nascimento).days/365, 2)}')
#10. Faça um programa que leia três números inteiros e imprima os três em ordem
#crescente.
def q10():
    numeros = []
    for i in range(0,3):
        numeros.append(int(input(f'{i+1}- Digite um Numero: ')))

    for i in range(0,3):
        for j in range(0,3):
            if numeros[i] < numeros[j]:
                auxiliar = numeros[j]
                numeros[j] = numeros[i]
                numeros[i] = auxiliar

    print(f'\n{numeros[0]} {numeros[1]} {numeros[2]}')
    
    #print(f'\n{sorted(numeros)}')
    

#11. Faça um programa que leia 3 números e imprima o maior deles.
def q11():
    numeros = []
    for i in range(0,3):
        numeros.append(float(input(f'{i+1}- Digite um Numero: ')))

    if numeros[0] > numeros[1] and numeros[0] > numeros[2]:
        print(f'O Maior Numero é: {round(numeros[0], 2)}')
    elif numeros[1] > numeros[0] and numeros[1] > numeros[2]:
        print(f'O Maior Numero é: {round(numeros[1], 2)}')
    else:
        print(f'O Maior Numero é: {round(numeros[2], 2)}')
#12. Faça um programa que leia a idade de uma pessoa e informe:
#• Se é maior de idade
#• Se é menor de idadea
#• Se é maior de 65 anos
def q12():
    idade = int(input('Digite a Idade: '))

    if idade >= 18 and idade < 65:
        print('Você é maior de Idade')
    elif idade >= 65:
        print('Você esta na melhor idade')
    else:
        print('Você e menor de Idade')


#13. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
#da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
#a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
#"Reprovado"ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
#reprovação e as demais em prova final).
def q13():
    nome = str(input('Nome do Aluno(a): '))
    prova1 = round(float(input('Nota da Primera Prova: ')), 1)
    prova2 = round(float(input('Nota da Segunda Prova: ')), 1)
    media = round((prova1 + prova2)/2, 2)

    print('\n---------------Boletin--------------')
    print(f'Aluno(a): {nome.upper()}')
    print(f'\nNOTA DA PRIMEIRA PROVA: {prova1}')
    print(f'NOTA DA PRIMEIRA PROVA: {prova2}')
    print(f'MÉDIA DO ALUNO:         {media}')
    
    if media >= 7:
        print('\n ALUNO(A) APROVADO')
    elif media > 3 and media < 7:
        print('\n ALUNO(A) EM PROVA FINAL')
    else:
        print('\n ALUNO(A) REPPROVADO')
    
    print('---------------Boletin--------------')

#14. Faça um programa que permita entrar com o salário de uma pessoa e imprima o
#desconto do INSS segundo a tabela seguir:
#Salário Faixa de Desconto
#Menor ou igual à R$600,00 Isento
#Maior que R$600,00 e menor ou igual a R$1200,00 20%
#Maior que R$1200,00 e menor ou igual a R$2000,00 25%
#Maior que R$2000,00 30%
def q14():
    salario = float(input('Digite seu salario: R$'))

    print(f'\nSalario Bruto: R${salario}')

    if salario <= 600.00:
        print('Desconto do INSS: ISENTO')
    elif salario > 600.00 and salario <= 1200.00:
        salario = round(salario - (salario * 20 / 100), 2)
        print('Desconto do INSS: -20%')
    elif salario > 1200.00 and salario <= 2000.00:
        salario = round(salario - (salario * 25 / 100), 2)
        print('Desconto do INSS: -25%')
    else:
        salario = round(salario - (salario * 30 / 100), 2)
        print('Desconto do INSS: -30%')

    print(f'\nVALOR TOTAL: R${salario}')

#15. Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o
#valor da compra for menor que R$20,00, caso contrário, o lucro será de 30%.
#Faça um programa que leia o valor do produto e imprima o valor da venda.
def q15():
    valorDoProduto = round(float(input('Valor do Produto: ')), 2)

    if valorDoProduto < 20.00:
        print(f'\nValor da Venda: {round(valorDoProduto + (valorDoProduto * 45/100), 2)}')
    else:
        print(f'\nValor da Venda: {round(valorDoProduto + (valorDoProduto * 30/100), 2)}')

#16. A confederação brasileira de natação irá promover eliminatórias para o
#próximo mundial. Faça um programa que receba a idade de um nadador e imprima
#a sua categoria segundo a tabela a seguir:
#Categoria Idade
#Infantil A 5 - 7 anos
#Infantil B 8 - 10 anos
#Juvenil A 11 - 13 anos
#Juvenil B 14 - 17 anos
#Sênior maiores de 18 anos
def q16():
    idade = int(input('Idade do Nadador: '))

    if idade >= 5 and idade <= 7:
        print('Infantil A 5 - 7 anos')
    elif idade >= 8 and idade <= 10:
        print('Infantil B 8 - 10 anos')
    elif idade >= 11 and idade <= 13:
        print('Juvenil A 11 - 13 anos')
    elif idade >= 14 and idade <= 17:
        print('Juvenil B 14 - 17 anos')
    elif idade > 18:
        print('Sênior maiores de 18 anos')
    else:
        print('Idade Invalida')

#17. Depois da liberação do governo para as mensalidades dos planos de saúde,
#as pessoas começaram a fazer pesquisas para descobrir um bom plano, não
#muito caro. Um vendedor de um plano de saúde apresentou a tabela a seguir.
#Faça um programa que entre com o nome e a idade de uma pessoa e imprima o
#nome e o valor que ela deverá pagar.
#Idade Valor
#Até 10 anos R$30,00
#Acima de 10 até 29 anos R$60,00
#Acima de 29 até 45 anos R$120,00
#Acima de 45 até 59 anos R$150,00
#Acima de 59 até 65 anos R$250,00
#Maior que 65 anos R$400,00
def q17():
    nome = input('Digite o Nome: ').upper()
    idade = int(input('Digite a Idade: '))

    print(f'\nNOME: {nome}')
    if idade <= 10:
        print('Valor a pagar: R$30,00')
    elif idade >= 11 and idade <= 29:
        print('Valor a pagar: R$60,00')
    elif idade >= 30 and idade <= 45:
        print('Valor a pagar: R$120,00')
    elif idade >= 46 and idade <= 59:
        print('Valor a pagar: R$150,00')
    elif idade >= 60 and idade <= 65:
        print('Valor a pagar: R$250,00')
    else:
        print('Valor a pagar: R$400,00')

#18. Faça um programa que leia um número inteiro entre 1 e 12 e escreva o mês
#correspondente. Caso o usuário digite um número fora desse intervalo, deverá
#aparecer uma mensagem informando que não existe mês com este número.
def q18():
    #meses = ['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO',
    #         'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']
    
    #while True:
    #    mes = int(input('Digite o número do Mês: '))
    #    if mes >= 1 and mes <= 12:
    #        print(f'O mês {mes} é {meses[mes-1]}')
    #        break
    #    else:
    #        print('!- Mês não existe')

    while True:
        numeroMes = int(input('Digite o Núnero do Mes: '))

        if numeroMes < 1 or numeroMes > 12:
            print(f'!- O Mes {numeroMes} não existe\nDigite um numero entre 1 e 12')
            break

        mes = datetime.strptime(f'01/{numeroMes}/24','%d/%m/%y')
        mesExtenso = mes.strftime('%B')
        print(f'O Mes {numeroMes} é {tradutor.translate(mesExtenso)}')


#19. Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores
#para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o
#mesmo número de pontos, criar um programa que informe se uma equipe foi
#classificada, de acordo com a seguinte especificação:
#• Ler os pontos obtidos por cada jogador da equipe;
#• Mostrar esses valores em ordem decrescente;
#• Se a soma dos pontos for maior do que 100, imprimir a média aritmética entre eles,
#  caso contrário, imprimir a mensagem "Equipe desclassificada".
def q19():
    jogadoresPontos = []
    for i in range(0,3):
        jogadoresPontos.append(int(input(F'Pontos do Jogador {i+1}: ')))

    for i in range(0,3):
        for j in range(0,3):
            if jogadoresPontos[i] > jogadoresPontos[j]:
                aux = jogadoresPontos[j]
                jogadoresPontos[j] = jogadoresPontos[i]
                jogadoresPontos[i] = aux

    print('\n----------PLACAR DA EQUIPE----------')
    for i in range(0,3):
        print(f'          {i+1}° ----: {jogadoresPontos[i]}')

    somaDosPontos = jogadoresPontos[0] + jogadoresPontos[1] + jogadoresPontos[2]
    if somaDosPontos > 100:
        print(f'\nSOMA TOTAL DOS PONTOS -----: {somaDosPontos}')
        print(f'MÉDIA DA EQUIPE -----------: {round((jogadoresPontos[0] + jogadoresPontos[1] + jogadoresPontos[2])/3, 0)}')
        print('\n        EQUIPE QUALIFICADA')
    else:
        print(f'\nSOMA TOTAL DOS PONTOS -----: {somaDosPontos}')
        print(f'MÉDIA DA EQUIPE -----------: {round((jogadoresPontos[0] + jogadoresPontos[1] + jogadoresPontos[2])/3, 0)}')
        print('\n       EQUIPE DESQUALIFICADA')

#20. O banco XXX concederá um crédito especial com juros de 2% aos seus clientes de
#acordo com o saldo médio no último ano. Faça um programa que leia o saldo médio
#de um cliente e calcule o valor do crédito de acordo com a tabela a seguir.
#O programa deve imprimir uma mensagem informando o saldo médio e o valor de
#crédito.
#Saldo Médio Percentual
#de 0 a 500 nenhum crédito
#de 501 a 1000 30% do valor do saldo médio
#de 1001 a 3000 40% do valor do saldo médio
#acima de 3001 50% do valor do saldo médio
def q20():
    saldoMedio = round(float(input('Digite o Saldo Médio do Último Ano: ')),2)

    if saldoMedio <= 500:
        credito = 0
    elif saldoMedio > 500 and saldoMedio <= 1000:
        credito = saldoMedio * 0.30
    elif saldoMedio > 1000 and saldoMedio <= 3000:
        credito = saldoMedio * 0.40
    else:
        credito = saldoMedio * 0.50

    print(f'\nSaldo Médio ---------: R${saldoMedio}')
    print(f'Valor do Crédito ----: R${round(credito, 2)}')


#21. A biblioteca de uma Universidade deseja fazer um programa que leia o nome do
#livro que será emprestado, o tipo de usuário (professor ou aluno) e possa
#imprimir um recibo conforme mostrado a seguir. Considerar que o professor
#tem dez dias para devolver o livro e o aluno só três dias.
#• Nome do livro:
#• Tipo de usuário:
#• Total de dias:
def q21():
    livro = input('Nome do Livro: ').title()
    while True:
        print('\nQuem está emprestando o livro?')
        print('1 - Professor\n2 - Estudante')
        usuario = int(input('|Digite o numero>  '))

        if usuario > 0 and usuario < 3:
            break
        else:
            print('!- Digite 1 para PROFESSOR e 2 para ALUNO')

    print('---------------RECIBO---------------')
    print(f'Nome do Livro: {livro}')
    if usuario == 1:
        print('Usuario: PROFESSOR\nTotal de Dias: 10')
    else:
        print('Usuario: ALUNO\nTotal de Dias: 3')

#22. Construa um programa que leia o percurso em quilômetros, o tipo do carro e
#informe o consumo estimado de combustível, sabendo-se que um carro tipo A faz
#12 km com um litro de gasolina, um tipo B faz 9 km e o tipo C 8 km por litro.
def q22():
    km = round(float(input('Quilometro do Percurso: ')), 2)
    tipoDoCarro = input('Tipo do Carro: ').upper()

    match tipoDoCarro:
        case 'A':
            print(f'Consumo Estimado: {round(km / 12 ,2)}l')
        case 'B':
            print(f'Consumo Estimado: {round(km / 9, 2)}l')
        case 'C':
            print(f'Consumo Estimado: {round(km / 8, 2)}l')

#23. Crie um programa que informe a quantidade total de calorias de uma refeição
#a partir da escolha do usuário que deverá informar o prato, a sobremesa, e
#bebida conforme a tabela a seguir.
#Prato  Sobremesa   Bebida
#Vegetariano    180cal Abacaxi          75cal  Chá               20cal
#Peixe          230cal Sorvete diet     110cal Suco de laranja   70cal
#Frango         250cal Mousse diet      170cal Suco de melão     100cal
#Carne          350cal Mousse chocolate 200cal Refrigerante diet 65cal
def q23():
    cardapio =[
        ['Vegetariano ---> 180cal', 'Peixe ---------> 230cal', 'Frango --------> 250cal', 'Carne ---------> 350cal'],
        ['Abacaxi -----------> 75cal ', 'Sorvete diet ------> 110cal', 'Mouse diet --------> 170cal', 'Mouse chocolate ---> 200cal'],
        ['Chá -----------------> 20cal ', 'Suco de laranja -----> 70cal ', 'Suco de melão -------> 100cal', 'Refrigerante diet ---> 65cal ']
    ]

    caloria = [
        [180, 230, 250, 350],
        [75, 110, 170, 200],
        [20, 70, 100, 65]
    ]

    lista = []

    for i in range(0,3):
        match i:
            case 0:
                print('|------ PRATO PRINCIPAL -----|')
            case 1:
                print('|----------- SOBREMESA ----------|')
            case _:
                print('|-------------- BEBIDA ------------|')
        
        for j in range(0,4):
            print(f'| {j+1}- {cardapio[i][j]} |')

        if i == 0:
            while True:
                num = int(input('Numero do Prato Principal:'))
                if num > 0 and num < 5:
                    lista.append(caloria[i][num-1])
                    break
                else:
                    print('!! NUMERO INVALIDO !!')
        elif i == 1:
            while True:
                num = int(input('Numero da Sobremesa:'))
                if num > 0 and num < 5:
                    lista.append(caloria[i][num-1])
                    break
                else:
                    print('!! NUMERO INVALIDO !!')
        else:
            while True:
                num = int(input('Numero da Bebida:'))
                if num > 0 and num < 5:
                    lista.append(caloria[i][num-1])
                    break
                else:
                    print('!! NUMERO INVALIDO !!')

    print(f'TOTAL DE CALORIAS: {lista[0] + lista[1] + lista[2]}cal')

#24. A polícia rodoviária resolveu fazer cumprir a lei e vistoriar veículos para
#cobrar dos motoristas o DUT. Sabendo-se que o mês em que o emplacamento do
#carro deve ser renovado é determinado pelo último número da placa do mesmo,
#faça um programa que, a partir da leitura da placa do carro, informe o mês
#em que o emplacamento deve ser renovado.
def q24():
    placa = input('Digite a Placa: ').upper()
    ultimoNumero = int(placa[len(placa)-1])

    if ultimoNumero == 0:
        print('O Emplacamento deve ser renovado em Janeiro')
    elif ultimoNumero == 1:
        print('O Emplacamento deve ser renovado em Fevereiro')
    elif ultimoNumero == 2:
        print('O Emplacamento deve ser renovado em Março')
    elif ultimoNumero == 3:
        print('O Emplacamento deve ser renovado em Abril')
    elif ultimoNumero == 4:
        print('O Emplacamento deve ser renovado em Maio')
    elif ultimoNumero == 5:
        print('O Emplacamento deve ser renovado em Junho')
    elif ultimoNumero == 6:
        print('O Emplacamento deve ser renovado em Julho')
    elif ultimoNumero == 7:
        print('O Emplacamento deve ser renovado em Agosto')
    elif ultimoNumero == 8:
        print('O Emplacamento deve ser renovado em Setembro')
    elif ultimoNumero == 9:
        print('O Emplacamento deve ser renovado em Outubro')
    else:
        print('!! MES INVALIDO !!')
    
#25. A prefeitura contratou uma firma especializada para manter os níveis de
#poluição considerados ideais para um país do 1º mundo. As indústrias,
#maiores responsáveis pela poluição, foram classificadas em três grupos.
#Sabendo-se que a escala utilizada varia de 0,05 e que o índice de poluição
#aceitável é até 0,25, fazer um programa que possa imprimir intimações de
#acordo com o índice e a tabela a seguir:
#Índice Indústrias que receberão intimação
#0,3 1º grupo
#0,4 1º e 2º grupos
#0,5 1º, 2º e 3º grupos
def q25():
    indicePoluicao = round(float(input(' Informe Indice da Poluição: ')), 2)

    if indicePoluicao == 0.5:
        print('Intimar as industrias do 1°, 2° e 3° grupos')
    elif indicePoluicao == 0.4:
        print('Intimar as industrias do 1° e 2° grupos')
    elif indicePoluicao == 0.3:
        print('Intimar as industrias do 1° grupo')
    elif indicePoluicao <= 0.25:
        print('Nivel de Poluição Aceitavel')
    else:
        print('Nivel de Poluição Fora dos Limites Conhecidos')


while True:
    atividade = input('Qual Atividade Deseja Executar? ').strip()
    execute = eval(atividade + '()')

    continua = input('Você Deseja Continuar (sim/não)? ')
    if continua == 'yes' or continua == 'y' or continua == 'sim' or continua == 's':
        print('OK DIGITE...')
    elif continua == 'no' or continua == 'n' or continua == 'não' or continua == 'nao':
        print('!- ATÉ A PROXIMA')
        break
    else:
        print('!- RESPOSTA INCORRETA, DIGITE SIM OU NÃO')
#q1()
#q2()
#q3()
#q4()
#q5()
#q6()
#q7()
#q8()
#q9()
#q10()
#q11()
#q12()
#q13()
#q14()
#q15()
#q16()
#q17()
#q18()
#q19()
#q20()
#q21()
#q22()
#q23()
#q24()
#q25()