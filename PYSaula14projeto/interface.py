from classes import *

times = {}


def ver_times() -> str:
    contador = 1
    dados = ''
    if len(times) != 0:
        for key in times.keys():
            dados += f'     {contador} - {key}\n'
            contador += 1
    dados += f'     {contador} - Cancelar'
    return dados


def verificar(num: str, analisar: int, *checar) -> bool:
    match analisar:
        case 1:
            if num[0] in ver_times():
                return True
            return False
        case 2:
            chave = nome_do_time(int(num))
            jogadores = times[chave]['Jogadores']
            for jogador in jogadores:
                if checar[0] == jogadores[jogador]['Camisa']:
                    return False
            return True


def nome_do_time(num: int) -> str:
    contador = 1
    for key in times.keys():
        if contador == num:
            return key
        contador += 1
    return 'ERRO'


while True:
    menu = input('''Informe a ação desejada:
    1 - Cadastrar time
    2 - Cadastrar jogador
    3 - Cadastrar comissão
    4 - Sair
Número correspondente à ação: ''')

    match menu:
        case '1':
            nome_time_cadastro = input('Informe o nome do novo time: ').lower().capitalize()
            cidade = input('Informe a cidade onde a sede do time está localizada: ').lower().capitalize()
            mascote = input(f'Informe o nome do mascote do {nome_time_cadastro}: ').lower().capitalize()

            time = Time(nome_time_cadastro, cidade, mascote)
            times[nome_time_cadastro] = {'Informações': {'Time': time.nome_time,
                                           'Cidade': time.cidade,
                                           'Mascote': time.nome_mascote},
                           'Jogadores': [],
                           'Acesso': time
                           }
            print(f'{nome_time_cadastro} cadastrado com sucesso!')
        case '2':
            print('Escolha entre os seguintes times para cadastrar um jogador:', ver_times(), sep='\n')
            time = input('Informe o número correspondente ao time: ')
            verificacao = verificar(time)
            str_num = int(time[0])
            if verificar:
                time_informado = nome_do_time(str_num)
                chave_time = times[time_informado]['Acesso']
                nome_jogador_cadastro = input('Informe o nome do jogador: ').lower().capitalize()
                camisa = int(input(f'Informe o número da camisa de {nome_jogador_cadastro}: '))

                jogador = Jogador(nome_jogador_cadastro, chave_time, camisa)

