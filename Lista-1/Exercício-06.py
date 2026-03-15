# Declaração de variáveis 
x: float = 0.0
y: float = 0.0
z: float = 0.0

# Início 

x = float(input('Digite um valor para x: '))
y = float(input('Digite um valor para y: '))

z = x
x = y
y = z

print('Com a troca feita, o valor de x agora é', x, 'e de y é', y)

# Fim