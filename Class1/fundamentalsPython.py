import venv

# funções com argumentos nomeados vs argumentos posicionais

# Função com argumentos posicionais
#Toda a função em python começa com um def
def somarPosicional(num1, num2):
    print(f'O numero 1 tem valor: {num1}')
    print(f'O numero 2 tem valor: {num2}')
    return num1 + num2

# print(somarPosicional(4, 8))

def somarNomeado(num1, num2):
    print(f'O numero 1 tem valor: {num1}')
    print(f'O numero 2 tem valor: {num2}')
    return num1 + num2

# print(somarNomeado(num2=10, num1=5))

def exponenciar(base, expoente):
    return base ** expoente

# print(exponenciar(2, 3))  # Argumentos posicionais

def exponenciarNomeado(base, expoente):
    return base ** expoente

#print(exponenciarNomeado(expoente=4, base=2))  # Argumentos nomeados

#print() com argumentos extras

num1 = 10
num2 = 20
# print(num1, num2, sep=' - ', end ='\n')

# F string
print(f'O valor de num1 é {num1} e o valor de num2 é {num2}')
print('num1 é {} | num2 é {}'.format(num1, num2))

# F string nomeado
print('num1 é {n1} | num2 é {n2}'.format(n1=num1, n2=num2))

#operações aritmeticas
print(f'Soma: {num1 + num2}')
print(f'Subtração: {num1 - num2}')
print(f'Multiplicação: {num1 * num2}')
print(f'Divisão: {num1 / num2}')
print(f'Divisão inteira: {num1 // num2}')
print(f'Módulo: {num1 % num2}')

#Operações relacionais
print(f'num1 é igual a num2? {num1 == num2}')
print(f'num1 é diferente de num2? {num1 != num2}')
print(f'num1 é maior que num2? {num1 > num2}')
print(f'num1 é menor que num2? {num1 < num2}')
print(f'num1 é maior ou igual a num2? {num1 >= num2}')
print(f'num1 é menor ou igual a num2? {num1 <= num2}')

#Operações lógicas
print(f'num1 é maior que 5 e num2 é menor que 30? {num1 > 5 and num2 < 30}')
print(f'num1 é maior que 15 ou num2 é menor que 30? {num1 > 15 or num2 < 30}')
print(f'num1 não é igual a num2? {not (num1 == num2)}')