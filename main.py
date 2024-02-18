from random import choice, randint
from time import sleep

def arquivo_existe(nome):
    """
    -> Verifica se existe um arquivo de texto com o nome especificado.
    :param nome: Nome do arquivo
    :return: True se existe, False se não existe.
    """
    try:
        a = open(nome, 'rt', encoding='utf-8')  # rt = read text = Leitura de arquivo texto
        a.close()

        # Especifiquei encoding, pois os acentos não estão sendo exibidos no PyCharm.

        # Função open tenta abrir um arquivo, o 'rt' significa leitura de arquivo texto, que é read text.
        # a.close() fecha o arquivo.
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    """
    -> Cria um arquivo de texto com o nome especificado.
    :param nome: Nome do arquivo de texto
    :return: Sem retorno
    """
    try:
        a = open(nome, 'wt+', encoding='utf-8')  # wt+ = write text O + de 'wt' que cria o arquivo.
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def cadastrar(arq):
    """
    -> Insere o nome e idade de uma pessoa em um arquivo de texto.
    :param arq: Nome do arquivo em que será salvo os dados.
    :param nome: (opcional) Nome da pessoa que será salvo.
    :param idade: (opcional) Idade da pessoa que será salvo.
    :return: Sem retorno.
    """
    try:
        a = open(arq, 'at', encoding='utf-8')
    except:
        print('Houve um ERRO ao abrir o arquivo.')
    else:
        try:
            a.write(f'Nome:{nam}; Vitorias:{vit}; Dinheiro:{din};\n')
        except:
            print('Houve um ERRO ao cadastrar os dados.')
        else:
            print(f'Novo registro de {nam} adicionado.')
            a.close()


def ler_arquivo(arq):
    """
    -> Lê o conteúdo de um arquivo de texto.
    :param nome: Nome do arquivo de texto.
    :return: Sem retorno.
    """
    try:
        a = open(arq, 'rt', encoding='utf-8')
    except:
        print('Erro ao abrir o arquivo.')
    else:
        banner('Ranking')

        # print(a.readlines())
        # Mostra o conteúdo inteiro do arquivo de texto em uma única linha, inclusive com as quebras
        # de linha (\n).

        # print(a.read())
        # Mostra o conteúdo inteiro do arquivo formatado com as quebras de linha.

        for linha in a:
            dado = linha.split(';')  # Separa a linha por ponto e vírgula.
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}, {dado[1]}, {dado[2]}')
    finally:
        a.close()


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mErro! Digite um numero inteiro valido\033[m.')
            continue
        else:
            return n


def ini():
    print(f'\033[1;32m_________________________________________________________________\033[m')
    print(f'\033[1;32m___{nam.center(59)}___\033[m')
    print(f"{gam.center(65)}")
    print(f'Total na Carteira  R${din},00       Valor da aposta: R$ {apt},00 ')
    print(f'Vitorias:{vit}      Empates:{dwr}      Derrotas:{der}')
    print(f'\033[1;32m_________________________________________________________________\033[m')


def apresentacao(nome):
    global nam
    nam = str(input('Qual seu nome? or [Enter]: '))
    if nam == '':
        nam = 'Anonimo'
    banner(f'Boa Sorte, {nam}!')


def contarcartas():
    r = len(lista_de_cartas)
    mensagem(f'Restam {r} cartas.')


def aposta():
    global din
    global apt
    mensagem(f'Voce possui R${din} em sua carteira.')
    while True:
        apt = leiaInt('Qual sua aposta?: ')
        if apt > din:
            print('\033[31mOperação invalida\033[m')
        else:
            din -= apt
            break
    return apt


def exibe_pillha():
    print(f'Cartas na pilha: ', end='')
    for i in lista_de_cartas:
        print(f'[{i}]', end=' ')
    print()


def sorteia():
    sort = choice(lista_de_cartas)
    lista_de_cartas.remove(sort)
    return int(sort)


def banner(msg):
    barra = 65
    print('_' * barra)
    print(f'\033[34m{msg.center(barra)}\033[m')
    print('_' * barra)


def msg_derrota(msg):
    barra = 65
    print(f'\033[1;31m-\033[m' * barra)
    print(f'\033[1;31m{msg.center(barra)}\033[m')
    print(f'\033[1;31m-\033[m' * barra)


def msg_vitoria(msg):
    barra = 65
    print(f'\033[1;32m-\033[m' * barra)
    print(f'\033[1;32m{msg.center(barra)}\033[m')
    print(f'\033[1;32m-\033[m' * barra)


def mensagem(msg):
    barra = 65
    print(f'\033[33m{msg.center(barra)}\033[m')


def mensagem_d(msg):
    barra = 65
    print(f'\033[1;37m{msg.center(barra)}\033[m')


def jogar():
    global der, jog
    cont = 5
    while cont >= 0:
        # ---(Verifica se passou dos 21 pontos)------------------------------------------------------------------
        if jog > 21:
            #msg_derrota('Voce perdeu: Pontuação acima de 21.')
            #der += 1
            break
        # ------------------------------------------------------------------------------------------------------
        res = str(input('[S para SIM/D para NÃO]: ')).upper()
        if res == 'D':
            mensagem(f'Sua pontuação na rodada foi de {jog}')
            break
        elif res == 'S':
            cont -= 1
            r = sorteia()
            jog += r
            mensagem(f'Carta sorteada: {r} Total Pontos: {jog} ')


def jogar_dealer():
    global dea, vit
    dea = 0
    cont = 2
    if jog < 21:
        while cont >= 0:
            # ---(Verifica se passou dos 21 pontos)-----------------------------------------------------------------
            if dea > 21:
                #msg_vitoria(f'Voce Venceu: Dealer {dea} pontos.')
                #vit += 1
                break
            # ------------------------------------------------------------------------------------------------------
            if dea < 16:
                banner(f'Dealer retirando cartas ...')
                sleep(1)
                r = sorteia()
                dea += r
                cont -= 1
                mensagem_d(f'Dealer possui {dea} pontos.')
                sleep(1)
            else:
                if dea < jog:
                    msg_derrota(f'Total de pontos na rodada:Dealer {dea}')
                    msg_vitoria(f'Total de pontos na rodada:{nam} {jog}')
                else:
                    msg_derrota(f'Total de pontos na rodada:{nam} {jog}')
                    msg_vitoria(f'Total de pontos na rodada:Dealer {dea}')
                break


def resultado():
    global vit, der, dwr, din, apt
    if jog == 21:
        apt2 = apt* 2
        mensagem(f'Voce fez 21 pontos e recebe bonus de {apt*2}')
        din += apt2
    if jog >= 22:
        msg_derrota(f'Voce perdeu!')
        der += 1
    elif dea >= 22:
        msg_vitoria(f'Voce venceu!')
        vit += 1
        din += apt * 2
    else:
        if jog > dea:
            msg_vitoria(f'Voce venceu a rodada')
            vit += 1
            din += apt * 2
        elif dea > jog:
            msg_derrota(f'Dealer Venceu a Rodada!')
            der += 1
        else:
            msg_vitoria('DRaw gaME')
            dwr += 1
            din += apt


#programa principal
#----------(declaracao de variaveis)------------------------------------------------------------
nam = ''
gam = 'BlAcK jAcK'
jog = dea = 0
din = 15
vit = der = cnt = dwr = apt = 0
#----------(listas total de 52 cartas do blackjack)----------------------------------------------
lista_de_cartas = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13',
                   '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13',
                   '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13',
                   '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
#----------(bloco de inicio)----------------------------------------------------------------------
arq = 'ranking.txt'

if not arquivo_existe(arq):
    criar_arquivo(arq)

banner(f'Bem vindo ao {gam}')
apresentacao(nam)
#----------(Estrutura de Loop)--------------------------------------------------------------------
while True:
    cartas = len(lista_de_cartas)
    if din <= 0:
        msg_derrota('Game Over - Acabaram seus créditos.')
        ini()
        cadastrar(arq)
        ler_arquivo(arq)
        break
    if cartas < 5:
        banner('Fim de jogo. Acabaram as cartas para uma nova rodada!')
        ini()
        cadastrar(arq)
        ler_arquivo(arq)
        break
    banner("Iniciando a rodada")
    aposta()
    ini()
    sleep(2)
    r = sorteia()
    jog = r
    mensagem(f'A carta retirada foi {r}')
    banner('Deseja retirar outra carta?')
    #---------------(Definicao de Jogada do Usuario)------------------------------------------------
    jogar()
    #---------------(Definicao de Jogada do Dealer)-------------------------------------------------
    jogar_dealer()
    #---------------(Verificando vencedor)----------------------------------------------------------
    resultado()
    ini()
    contarcartas()