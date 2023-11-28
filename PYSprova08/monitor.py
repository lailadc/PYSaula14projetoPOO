from sistema import *

correcao = input('Digite seu nome: ').title()
print(f"Tenha uma ótima correção, {correcao} XD\n")
limpar = '\n'
encerrar = False                                                            # Variável para sair do loop principal
while True:
    if encerrar:                                                            # Se verdadeira encerra
        break
    print(50*'-')
    identificacao = input('Identificações:\n'
                          '    1. Administração\n'
                          '    2. Cliente\n'
                          'Informe o número equivalente à sua identificação: ')

    match identificacao:
        # ADMINISTRADOR DA LOJA ONLINE
        case '1':
            usuario = input(
                'Informe o usuário do InfinityApp: '
            ).lower()
            if 'dev' not in usuario:                                        # IDENTIFICAÇÃO FALHOU
                print(2 * limpar, 'Usuário inválido!', 3 * limpar)
                continue
            else:                                                           # IDENTIFICAÇÃO VERIFICADA
                print(f"{10*limpar}Bem vinde ao sistema da loja, {correcao}!")
                while True:                                                 # LOOP SECUNDÁRIO - SISTEMA DA LOJA
                    acao = input(f'{6*"-"}  SISTEMA DA LOJA  {6*"-"}\n'
                                 f'    1. Cadastrar produto\n'
                                 f'    2. Atualizar produto\n'
                                 f'    3. Deletar produto\n'
                                 f'    4. Voltar menu funcionário/cliente\n'
                                 f'    5. Encerrar correção\n'
                                 f'Informe o número correspondente à ação desejada: ')
                    match acao:
                        # CADASTRAR NOVO PRODUTO
                        case '1':
                            nome_cadastro = input(
                                'Informe o nome do produto: '
                            ).capitalize()
                            preco_unitario = float(
                                input(
                                    f'Informe o preço unitário de {nome_cadastro}:\nR$ '
                                ).replace(',', '.')
                            )
                            print(cadastrar_produto(nome_cadastro, preco_unitario))

                        # ATUALIZAR PRODUTO EXISTENTE
                        case '2':
                            print(ver_produtos())
                            produto_atualizar = input('Informe o produto que deseja atualizar: ')

                            if tipo_numerico(produto_atualizar):
                                produto_atualizar = int(produto_atualizar)
                                if 0 < produto_atualizar <= len(produtos):

                                    nome_atualizar = produtos[produto_atualizar - 1][0]
                                    preco_atualizar = produtos[produto_atualizar - 1][1]
                                    opcao = input(f'Opções de atualização:\n'
                                                  f'    1. Apenas nome de {nome_atualizar}\n'
                                                  f'    2. Apenas valor unitário de {nome_atualizar}\n'
                                                  f'    3. Substituir {nome_atualizar}\n'
                                                  f'    4. Cancelar\n'
                                                  f'Informe o número equivalente à ação desejada: ')
                                    while (opcao not in '1234'
                                           or len(opcao) != 1):                         # LOOP TERCIÁRIO - VERIFICAÇÃO DE ERRO
                                        print('Opção inválida!')
                                        opcao = input(f'Opções de atualização:\n'
                                                      f'    1. Apenas nome de {nome_atualizar}\n'
                                                      f'    2. Apenas valor unitário de {nome_atualizar}\n'
                                                      f'    3. Substituir {nome_atualizar}\n'
                                                      f'    4. Cancelar\n'
                                                      f'Informe o número equivalente à ação desejada: ')
                                    match opcao:
                                        # ATUALIZAR NOME SEM MUDAR PREÇO
                                        case '1':
                                            nome_atualizado = input(
                                                f'Informe o novo produto de R$ {preco_atualizar:.2f}: '
                                            ).capitalize()
                                            print(atualizar_produto(produto_atualizar, nome_atualizado))

                                        # ATUALIZAR PREÇO SEM MUDAR NOME
                                        case '2':
                                            preco_atualizado = float(
                                                input(
                                                    f'Informe o novo preço unitário de {nome_atualizar}:\nR$ '
                                                ).replace(',', '.')
                                            )
                                            print(atualizar_produto(produto_atualizar, preco_atualizado))

                                        # ATUALIZAR TANTO NOME QUANTO PREÇO
                                        case '3':
                                            nome_atualizado = input(
                                                f'Informe o novo produto para substituir {nome_atualizar}: '
                                            ).capitalize()
                                            preco_atualizado = float(
                                                input(
                                                    f'Informe o preço unitário de {nome_atualizado}:\nR$ '
                                                ).replace(',', '.')
                                            )
                                            print(
                                                atualizar_produto(produto_atualizar,
                                                                  nome_atualizado,
                                                                  preco_atualizado)
                                            )
                                        # CANCELAR OPERAÇÃO
                                        case '4':
                                            print(10 * limpar)
                                            continue
                                else:
                                    print(2*limpar, "Opção inválida!", 3*limpar)
                                    continue

                        # DELETAR PRODUTO
                        case '3':
                            print(ver_produtos())
                            produto_deletar = int(input('Informe o produto que deseja deletar: '))
                            print(deletar_produto(produto_deletar))

                        # SAIR DO SISTEMA DA LOJA
                        case '4':
                            print(10*limpar)
                            break

                        # ENCERRAR PROGRAMA
                        case '5':
                            print(10*limpar)
                            encerrar = True
                            break

                        # TRATAMENTO DE ERROS
                        case _:
                            print('Opção inválida!', 3*limpar)
                            continue
                    print(10 * limpar)

        # SITE DE COMPRAS
        case '2':
            print(f'{3*limpar}Seja bem-vinde, {correcao}! Boas compras :)')
            while True:
                acao = input(f'{10 * "-"}  AÇÕES  {10 * "-"}\n'
                             f'    1. Adicionar ao carrinho\n'
                             f'    2. Remover do carrinho\n'
                             f'    3. Ver carrinho\n'
                             f'    4. Voltar ao primeiro menu\n'
                             f'    5. Finalizar compra\n'
                             f'Informe o número equivalente à ação desejada: ')
                match acao:
                    # ADICIONAR AO CARRINHO
                    case '1':
                        print(ver_produtos())
                        produto_add = input('Informe o número equivalente ao produto desejado: ')

                        if tipo_numerico(produto_add):
                            num_prod = int(produto_add)
                            if num_prod > len(produtos):
                                print('Produto inexistente.')
                                continue
                            else:

                                nome_prod = nome_produto(num_prod)
                                qntd_add = input(f'Informe a quantidade de {nome_prod} deseja comprar: ')

                                if tipo_numerico(qntd_add):
                                    qntd_add = int(qntd_add)
                                    print(adicionar_ao_carrinho(num_prod, qntd_add))
                                else:
                                    print(adicionar_ao_carrinho(num_prod))
                                    print('Porém não foi possível identificar a quantidade, '
                                          'então apenas uma unidade foi adicionada.')
                        else:
                            print(10*limpar)
                            continue

                    # REMOVER DO CARRINHO
                    case '2':
                        print(ver_carrinho())
                        produto_remover = input('Informe o número equivalente ao produto que deseja remover: ')

                        if tipo_numerico(produto_remover):
                            produto_remover = int(produto_remover)
                            nome_prod_rmv = informacoes(produto_remover)
                            if nome_prod_rmv in carrinho:
                                if carrinho[nome_prod_rmv] > 1:
                                    qntd_remover = input(
                                        f'Informe quantos itens de {nome_prod_rmv} deseja remover do carrinho: '
                                    )
                                    if tipo_numerico(qntd_remover):
                                        qntd_remover = int(qntd_remover)
                                        print(remover_item(produto_remover, qntd_remover))
                                    else:
                                        print(remover_item(produto_remover))
                                        print('Porém não foi possível identificar a quantidade, '
                                              'apenas uma unidade foi removida')
                                else:
                                    print(remover_item(produto_remover))
                            else:
                                print(nome_prod_rmv)
                        else:
                            print("Não foi possível identificar o produto.")
                            continue

                    # VER CARRINHO
                    case '3':
                        print(ver_carrinho())
                        print(2*limpar)
                        continue

                    # FECHAR SITE
                    case '4':
                        print(10*limpar)
                        break

                    # ENCERRAR PROGRAMA
                    case '5':
                        print(10*limpar)
                        encerrar = True
                        print(f'Obridade e volte sempre, {correcao}!')
                        print('Correção encerrada.')
                        break
                    case _:
                        print('Opção inválida!')
                print(10*limpar)
        case _:
            print(2*limpar, 'Opção inválida!', 3*limpar)
            continue
    print(20 * limpar)

print(f'Espero que tenha gostado, {correcao} ^^\n'
      f'Agora vá lá e aperte naquele 1 verdinho com gosto pra me dar 10 😜')