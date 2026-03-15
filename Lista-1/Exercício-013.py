# Declaração de variáveis 
alimento_em_quilos: float = 0.0
total_dias: int = 0


# Início 

alimento_em_quilos = float(input('Digite quantos quilos (kg) de alimento você possui: '))

total_dias = int(alimento_em_quilos * 20)

print('Isso significa que você terá alimento para', total_dias, 'dias.')


# Fim