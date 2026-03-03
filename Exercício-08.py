# Declaração de variáveis 
poupança: int = 0
valor_final_centavos: int = 0

# Início 

print('Digite o valor da poupança, incluindo os centavos, porém sem vírgula')
print('Exemplo: Em vez de digitar algo como "123,45", digite assim "12345"')
poupança = int(input())

valor_final_centavos = (poupança * 1013) // 1000
print(f'Após um mês de aplicação, o valor final é de {valor_final_centavos / 100:.2f}')

# Fim