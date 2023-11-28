from base_dados import *


def ver_produtos() -> str:
    tab = '\t'
    mostrar = f"\n\n{8*'-'}  PRODUTOS À VENDA  {8*'-'}"
    escolha = 1
    for produto in produtos:
        palavra = len(produto[0])//4
        preco = produto[1]
        mostrar += f"\n{escolha}. {produto[0]}:{(5-palavra)*tab}R$ {preco:.2f}"
        escolha += 1
    return mostrar


def nome_produto(produto: int) -> str:
    return produtos[produto-1][0]


def informacoes(produto: int) -> str:
    """Função destinada a uso interno do programa"""
    contar = 0
    if produto > len(carrinho):
        return '\nProduto não encontrado...'
    for key in carrinho.keys():
        if produto == contar:
            return key
        contar += 1
    return '\nProduto não encontrado...'


def tipo_numerico(num_txt: str) -> bool:
    num = True
    if len(num_txt) == 0:
        num = False
    for char in num_txt:
        if char not in '0123456789':
            num = False
            break
    return num


def calcular_total():
    carrinho['TOTAL'] = 0
    total = 0
    for item in carrinho:
        for prod in produtos:
            if item == prod[0]:
                total += carrinho[item] * prod[1]
                break
    carrinho['TOTAL'] = total


# ----------  APENAS FUNCIONÁRIOS TÊM ACESSO A ESSAS FUNÇÕES  ----------


def cadastrar_produto(nome: str, preco_unitario: float) -> str:
    for produto in produtos:
        if nome.capitalize() == produto[0]:
            return '\nProduto já existente.'
    produto = (nome.capitalize(), preco_unitario)
    produtos.append(produto)
    return '\nProduto cadastrado com sucesso!'


def atualizar_produto(produto: int, *novos_dados) -> str:
    if produto < 1 or produto > len(produtos):                    # Checando se a opção é inválida
        return '\nProduto não encontrado'
    indice = produto - 1
    if len(novos_dados) == 1:                                     # Verificando o tamanho da tupla *args
        if type(novos_dados[0]) == str:                         # Verificando o tipo de dado
            novo_nome = novos_dados[0]                                    # Guardando novo nome se string
            preco_un = produtos[indice][1]
            produtos[indice] = (novo_nome, preco_un)                      # Atualizando apenas o nome
        elif type(novos_dados[0]) == float:                           # Verificando o tipo de dado
            nome = produtos[indice][0]
            novo_preco_un = novos_dados[0]                                # Guardando novo preço se número
            produtos[indice] = (nome, novo_preco_un)                      # Atualizando apenas o preço
        else:                                                         # Verificando o tipo de dado
            return 'Inválido!'                                            # Descartando qualquer outro tipo
    elif len(novos_dados) > 2:                                    # Verificando o tamanho da tupla  |  Descartando se >2
        return 'Inválido!\nInforme apenas o novo nome e/ou o preço unitário ao tentar novamente.'
    elif len(novos_dados) == 0:                                   # Verificando o tabanho da tupla  |  Descartando se 0
        return 'Inválido!\nInforme pelo menos o novo nome ou o novo preço unitário ao tentar novamente.'
    else:                                                         # Verificando o tamanho da tupla
        novo_nome = ''                                                # Inicializando variáveis se 2
        novo_preco_un = 0
        for tipo in novos_dados:                                      # Percorrendo a tupla *args
            if type(tipo) == str:                                   # Verificando o tipo de dado
                novo_nome = tipo                                              # Armazenando se string
            elif type(tipo) == float:                # Verificando o tipo de dado
                novo_preco_un = tipo                                          # Armazenando se número
            else:                                                         # Verificando o tipo de dado
                return '\nAlgum dos novos dados inseridos é inválido!'        # Descartando qualquer outro tipo
            produtos[indice] = (novo_nome, novo_preco_un)            # Atualizando produto na lista
    return '\nProduto atualizado com sucesso!'


def deletar_produto(produto: int) -> str:
    if produto > len(produtos) or produto < 1:
        return '\nProduto não encontrado.'
    produtos.pop(produto - 1)
    return '\nProduto deletado com sucesso.'


# ---------------  CLIENTES TAMBÉM PODEM USAR ESSAS FUNÇÕES  ---------------


def adicionar_ao_carrinho(produto: int, quantidade: int = 1) -> str:
    total = carrinho['TOTAL']
    nome = produtos[produto-1][0]
    preco_un = produtos[produto-1][1]
    total += preco_un * quantidade
    if nome in carrinho:
        quantidade += carrinho[nome]
    carrinho.update([(nome, quantidade), ('TOTAL', total)])
    return '\nProduto adicionado com sucesso!'


def ver_carrinho() -> str:
    calcular_total()
    num_prod = 1
    mostrar = f"\n\n{10*'-'}  MEU CARRINHO  {10*'-'}\n"
    for key in carrinho.keys():
        if key == 'TOTAL':
            continue
        preco_un = 0
        for produto in produtos:
            if key == produto[0]:
                preco_un = produto[1]
                break
        mostrar += f"{num_prod}. {key}  ->  {carrinho[key]} x  R$ {preco_un:.2f}\n"
        num_prod += 1
    mostrar += 35*'-'
    mostrar += f"\nTOTAL:  R$ {carrinho['TOTAL']:.2f}\n\n"
    return mostrar


def remover_item(produto: int, quantidade: int = 1) -> str:
    key = informacoes(produto)
    if key in carrinho:
        if carrinho[key] == quantidade:
            carrinho.pop(key)
            return '\nProduto removido com sucesso.'
        carrinho[key] -= quantidade
        return '\nItens removidos com sucesso.'
    return key


if __name__ == '__main__':
    print('Tudo testado e redondo ^^')
