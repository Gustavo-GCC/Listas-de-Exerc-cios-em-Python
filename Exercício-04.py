# Declaração de variáveis 
celsius: float = 0.0
fahrenheit: float = 0.0

# Início 

celsius = float(input('Qual é a temperatura em graus celsius? '))
fahrenheit = (9 * celsius + 160) / 5
print('Então essa mesma temperatura em fahrenheit é de', fahrenheit, 'graus.')

# Fim