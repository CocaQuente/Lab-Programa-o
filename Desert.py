def int_input(valor):
    while True:
        try:
            num = int(input(valor))
        except ValueError:
            print('!- Valor Invalido: O Valor Não É Do Tipo Inteiro')
        except:
            print('!- Erro Desconhecido, Tente Novamente.')
        else:
            return num
        
def float_input(valor):
     while True:
        try:
            num = float(input(valor))
        except ValueError:
            print('!- Valor Invalido: O Valor Não É Do Tipo Float')
        except:
            print('!- Erro Desconhecido, Tente Novamente.')
        else:
            return num
        