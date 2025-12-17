def saudacao(): # Exemplo simples
    print('Olá!')
    
saudacao()

def saudacaoComNome(nome): # Exemplo com parâmetro
    print(f'Olá, {nome}')
    
saudacaoComNome('Monicke')

def somar(num1, num2): # Com contas
    return num1 + num2

conta = somar(5, 6)
print(conta)