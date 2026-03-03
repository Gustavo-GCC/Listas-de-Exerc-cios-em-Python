# Importação de bibliotecas
import math

# Declaração de variáveis 
a: float = 0.0
b: float = 0.0
c: float = 0.0
x: float = 0.0
DISCRIMINANTE: float = 0.0


# Início 

a = float(input('Qual é o valor do coeficiente quadrático? '))
b = float(input('Qual é o valor do coeficiente linear? '))
c = float(input('Qual é o valor do termo independente? '))
DISCRIMINANTE = math.pow(b, 2) - 4*a*c

# COMO O ENUNCIADO DIZ QUE HÁ DUAS RAÍZES, LOGO O DISCRIMINANTE É POSITIVO #

x = ((-b) - math.sqrt(DISCRIMINANTE)) / 2*a
print('A primeira raiz vale', x)

x = ((-b) + math.sqrt(DISCRIMINANTE)) / 2*a
print('E a segunda raiz vale', x)

# Fim