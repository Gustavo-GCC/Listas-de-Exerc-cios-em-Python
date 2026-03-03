# Declaração de variáveis 
altura: float = 0.0
largura: float = 0.0
comprimento: float = 0.0
volume: float = 0.0

# Início 

altura = float(input('Digite o valor da altura do paralelepípedo: '))
largura = float(input('Digite o valor da largura do paralelepípedo: '))
comprimento = float(input('Digite o valor da comprimento do paralelepípedo: '))

volume = altura * largura * comprimento

print('O paralelepípedo possui', volume, 'unidades cúbicas.')

# Fim