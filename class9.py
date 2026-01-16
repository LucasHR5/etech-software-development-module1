# funções com argumentos nomeados vs argumentos posicionais

# Função com argumentos posicionais
#Toda a função em python começa com um def
def somarPosicional(num1, num2):
    print(f'O numero 1 tem valor: {num1}')
    print(f'O numero 2 tem valor: {num2}')
    return num1 + num2

print(somarPosicional(4, 8))