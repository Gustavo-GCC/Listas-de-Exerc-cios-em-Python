# Declaração de variáveis 
t: float = 0.0
d: float = 0.0
v: float = 0.0
l: float = 0.0


# Início 

t = float(input('Quanto tempo, em horas, durará a viagem? '))
v = float(input('E qual será a sua velocidade média? '))

d = v * t
l = d / 12

print(f'Então tenha em mente que você gastará {l:.2f} litros de combustível no total.')

# Fim