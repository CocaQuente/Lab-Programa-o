def area(largura, altura):
    return largura*altura

def volume(largura, profundidade, altura):
    return area(largura, profundidade) * altura

print(area(2,3))
print(volume(2, 3, 5))

def areaUser(largura, altura):
    print(f'A área é {largura*altura}')

areaUser(largura = int (input('Digite a largura: ')), altura = int (input('Digite a altura: ')))