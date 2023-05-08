estoque = {'tomate': [1000, 2.59],
           'alface': [500, 0.99],
           'batata': [2000, 1.89]}

produto = str(input('Digite o produto: '))
qtd = int(input('Digite a quantidade disponível: '))

venda = []
venda.append([produto,qtd])

total = 0

print('Vendas: \n')

while produto not in estoque:
    print('Produto não existe')
    produto = str(input('Digite o produto: '))
    qtd = int(input('Digite a quantidade disponível: '))


for operação in venda:
    preço = estoque[produto][1]
    custo = preço * qtd
    print('{},{},{},{}'.format(produto,qtd,preço,custo))
    estoque[produto][0] = estoque[produto][0] - qtd
    total = total + custo
    print('Custo total: {} \n'.format(total))
    print('Estoque: \n')

for chave, dados in estoque.items():
    print('Descrição: {}'.format(chave))
    print('Quantidade: {}'.format(dados[0]))
    print('Preço: {}\n'.format(dados[1]))

