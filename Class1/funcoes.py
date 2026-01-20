# parametros vs argumentos

def funcaoComParametro(parametro1, parametro2):
    print(f'Parametro 1: {parametro1}') 

funcaoComParametro('valor1', 'valor2')  # argumentos

# args e kwargs
def funcaoComArgs(*args, **kwargs):
    print('Argumentos posicionais (args):')
    for arg in args:
        print(arg)
    print('Argumentos nomeados (kwargs):')
    for key, value in kwargs.items():
        print(f'{key}: {value}')

funcaoComArgs(1, 2, 3, nome='Lucas', idade=30)
