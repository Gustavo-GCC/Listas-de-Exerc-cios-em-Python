# Declaração de variáveis 
p: int = 0
s: int = 0
t: int =0


# Início 

p = int(input('Qual é o valor do PRIMEIRO ângulo do triângulo? '))
s = int(input('Qual é o valor do SEGUNDO ângulo do triângulo? '))

t = 180 - (p + s)

print(f'Portanto, pode-se afirmar que o valor do TERCEIRO ângulo é de {t}°')

# Fim