# Criação de dicionários a partir de listas usando a função zip

a = ['cor', 'preco.', 'quantidade', 'unidade']
b = ['verde', 10.5, 20, 'kg']

c = dict(zip(a, b))

d = {
    'cor': 'verde',
    'preco': 10.5,
    'quantidade': 20,
}