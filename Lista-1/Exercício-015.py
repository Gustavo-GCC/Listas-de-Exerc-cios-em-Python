# Importação de bibliotecas
import math

# Declaração de variáveis 
c1: int = 0
c2: int = 0
h: int = 0


# Início 

c1 = int(input('Qual é o valor do PRIMEIRO cateto do triângulo retângulo? '))
c2 = int(input('Qual é o valor do SEGUNDO cateto do triângulo retângulo? '))

h = int(math.sqrt((c1*c1 + c2*c2)))

print('Logo, a hipotenusa vale', h)

# Fim