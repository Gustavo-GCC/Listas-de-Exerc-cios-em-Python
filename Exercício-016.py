# Declaração de variáveis 
horas_trabalhadas: float = 0.0
valor_hora: float = 0.0
desconto: float = 0.0
dependentes: float = 0.0
salário_líquido: float = 0.0
salário_bruto: float = 0.0
salário_final: float = 0.0


# Início 

horas_trabalhadas = float(input('Você trabalho quantas horas neste mês? '))
valor_hora = float(input('Quanto você ganha por hora? '))
desconto = float(input('Em porcentagem, quanto é descontado do seu salário bruto? '))
dependentes = float(input('E quantos dependentes você tem? '))

salário_bruto = horas_trabalhadas * valor_hora
salário_líquido = salário_bruto - (salário_bruto * desconto / 100)
salário_final = salário_líquido + dependentes * 100

print(f'Então você receberá R$ {salário_final:.2f}')

# Fim