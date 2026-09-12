import json

try:
    with open('projetos.json', 'r') as arquivo:
        projetos= json.load(arquivo)
except FileNotFoundError:
    projetos=[]

def pedir_texto(mensagem, tipo=str):
    while True:
        valor = input(mensagem)
        if valor == '':
            print('Valor inválido!')
            continue
        try:
            return tipo(valor)
        except ValueError:
            print('Valor inválido!')

def pagamento():
    while True:
        try:
            pagamento= pedir_texto('''
                Informe o status do pagamento
                [1] Pago
                [2] Inadimplente
                [3] Parcial
                [4] Outro
    
            ''',int)
            if pagamento == 1:
                pagamento_n = 'Pago'
                return pagamento_n
            elif pagamento == 2:
                pagamento_n = 'Inadimplente'
                return pagamento_n
            elif pagamento == 3:
                pagamento_n = 'Parcial'
                return pagamento_n
            elif pagamento == 4:
                info_pagamento= input('Digite o status do pagamento\n')
                pagamento_n = info_pagamento
                return pagamento_n
            else:
                print('Valor inválido!')
                continue
        except ValueError:
            print('Valor inválido!')


def status():
    while True:
        try:        
            status= pedir_texto('''
                Escolha um status
                [1] Composição
                [2] Gravação
                [3] Mixagem
                [4] Masterização
                [5] Finalizado
                [6] Outro
            ''', int)
            if status == 1:
                status_n = 'Composição'
                return status_n
            elif status == 2:
                status_n= 'Gravação'
                return status_n
            elif status == 3:
                status_n = 'Mixagem'
                return status_n
            elif status == 4:
                status_n = 'Masterização'
                return status_n
            elif status == 5:
                status_n = 'Finalizado'
                return status_n
            elif status == 6:
                info_status= input('Digite o status\n')
                status_n = info_status
                return status_n
            else:
                print('Valor inválido!')
                continue
        except ValueError:
            print('Valor inválido!')

def add_projeto():
    nome_projeto = pedir_texto('Digite o nome do projeto\n')
    artista= pedir_texto('Digite o vulgo do artista\n')
    status_escolhido = status()
    prazo = pedir_texto('Digite a data do prazo\n')
    pagamento_escolhido= pagamento()
    projeto= {'projeto': nome_projeto,
               'artista': artista,
                'status': status_escolhido,
                'prazo': prazo,
                'pagamento': pagamento_escolhido
                }
    projetos.append(projeto)
    salvar()

def listar():
    if not projetos:
        print('Nenhum projeto cadastrado ainda.')
        return
    for j, i in enumerate(projetos, 1):
        print(f'{j} - {i["projeto"]} ({i["artista"]})')
        print(f'    Status: {i["status"]} | Prazo: {i["prazo"]} | Pagamento: {i["pagamento"]}')

def salvar():
    with open('projetos.json', 'w') as arquivo:
        json.dump(projetos,arquivo,indent=2)

def alterar_projeto():
    listar()
    try:
        numero_escolhido = int(input('Qual projeto deseja alterar? (digite o número)\n'))
        indice = numero_escolhido - 1
        projeto_escolhido = projetos[indice]

        info_projeto = int(input('''
            Qual informação deseja alterar?
            [1] Projeto
            [2] Artista
            [3] Status
            [4] Prazo
            [5] Pagamento
        '''))

        if info_projeto == 1:
            projeto_escolhido['projeto'] = input('Novo nome do projeto\n')
        elif info_projeto == 2:
            projeto_escolhido['artista'] = input('Novo artista\n')
        elif info_projeto == 3:
            projeto_escolhido['status'] = status()
        elif info_projeto == 4:
            projeto_escolhido['prazo'] = input('Novo prazo\n')
        elif info_projeto == 5:
            projeto_escolhido['pagamento'] = pagamento()
        else:
            print('Inválido')
            return
        salvar()
        print('Alterado com sucesso!')

    except (ValueError, IndexError):
        print('Valor inválido')

def apagar_projeto():
    listar()
    try:
        numero_escolhido = int(input('Qual projeto deseja apagar? (digite o número)\n'))
        indice = numero_escolhido - 1
        projeto_removido = projetos.pop(indice)
        salvar()
        print(f'Projeto "{projeto_removido["projeto"]}" removido com sucesso!')
    except (ValueError, IndexError):
        print('Valor inválido')


while True:
    print('''
        [1] Adicionar projeto
        [2] Listar projeto
        [3] Alterar status de um projeto
        [4] Apagar projeto
        [5] Sair
    ''')
    try:
        info= int(input())
        if info == 1:
            add_projeto()
        elif info== 2:
            listar()
        elif info== 3:
            alterar_projeto()
        elif info== 4:
            apagar_projeto()
        elif info==5:
            salvar()
            break
        else:
            print('Valor inválido!')
    except ValueError:
        print('Valor inválido!')
