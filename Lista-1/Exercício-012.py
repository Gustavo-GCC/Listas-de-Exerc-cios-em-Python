# Declaração de variáveis 
ano_nascimento: int = 0.0
ano_atual: int = 0.0
idade_atual: int = 0.0
idade_futura: int = 0.0


# Início 

ano_nascimento = int(input('Digite em que ano você nasceu: '))
ano_atual = int(input('Digite em que ano estamos: '))

idade_atual = ano_atual - ano_nascimento
idade_futura = idade_atual + 17

print('Você tem', idade_atual, 'anos e terá', idade_futura, 'daqui 17 anos.')

# Fim