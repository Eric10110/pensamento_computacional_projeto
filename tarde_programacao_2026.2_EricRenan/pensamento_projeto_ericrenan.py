'''
>>progeto industria de automoveis
'''



# Ufa, quebrei a maldição 
# print('olá, Mundo!')

print('-' * 48 + '\n')
print('Bem-vindo ao Sistema de vendas-industria de automoveis\n')
print('1 - Cadastrar produto')
print('2 - listar produtos')
print('3 - Realizar venda ') 
print('4 - Buscar veiculos')
print('5 - Buscar pelo ano')
print('6 - Lista de financiamentos')
print('7 - Estoque')
print('8 - Agenda de visitas')
print('9 - Sobre')
print('0 - Sair do Sistema')
print('\n------------------------------------------------------\n')

opcao_definida = int(input('Digite a opção desejada: '))
if opcao_definida == 1: 
    print('Cadastrando produtos...')
elif opcao_definida== 2:
    print('Lista de produtos...')
elif opcao_definida == 3:
    print('Realizando vendas...')
elif opcao_definida == 4:
    print('Buscando veiculos...')
elif opcao_definida == 5:
    print('Buscar pelo ano...')
elif opcao_definida == 6:
    print('Listando financiamentos...')
elif opcao_definida == 7:
    print('Lista de estoque...')
elif opcao_definida == 8:
    print('Agenda de visitas...')
elif opcao_definida == 9:
    print('Sobre o sistema')