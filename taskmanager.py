import os
import getpass

usuarios = [{'nome': 'Leandro Marinho', 'email': 'lelemarinho300@gmail.com', 'senha': 'M@rinh0@1706'}]
tarefas = [{'titulo': 'Tarefa', 'descricao': 'Descrição da Tarefa', 'datacriacao': 'Data da Tarefa', 'dataconclusao': 'Prazo de Conclusão'}]
  
def exibir_opcoes():
    '''Esta função exibe a lista de opções disponíveis no menu principal
    
    Output:
    -Lista com as opções disponíveis no programa.
    '''
    print('1. Cadastrar novo usuário')
    print('2. Editar dados cadastrais')
    print('3. Listar usuários cadastrados')
    print('4. Fazer login')

def escolher_opcao():
    '''Esta função permite o usuário selecionar entre um novo cadastro ou acessar o seu gerenciador'''

    try:
        opcao_escolhida = int(input('\nDigite a opção desejada: '))
        if opcao_escolhida == 1:
            cadastro_de_usuarios()
        elif opcao_escolhida == 2:
            editar_dados_acesso()
        elif opcao_escolhida == 3:
            listar_usuarios()
        elif opcao_escolhida == 4:
            acesso_usuario()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def cadastro_de_usuarios():
    '''Essa função receberá os dados do usuário para cadastro
    
    Inputs:
    - Nome
    - Email
    - Senha
    
    Outputs:
    - Mensagem exibindo dados cadastrados com sucesso.
    '''
    os.system('cls')
    exibir_subtitulo('Cadastrar usuários')
    nome_usuario = input('Digite o seu nome de Cadastro: ')
    email_usuario = input('\nDigite o seu e-mail de cadastro: ')
    senha_usuario = input('\nDigite uma senha: ')
    dados_do_usuario = {'nome' :nome_usuario, 'email' :email_usuario, 'senha' :senha_usuario}
    usuarios.append(dados_do_usuario)
    print(f'\nSeja bem vindo(a), {nome_usuario}')
    voltar_ao_menu_principal()

def editar_dados_acesso():
    '''Menu que edita os dados pessoais do usuário
    
    Inputs:
    - E-mail de Cadastro (Para validação)
    - Informações editadas (Para atualização dos Dados)

    Outputs:
    - Confirmação de e-mail encontrado
    - Dados Atualizados
    '''
    os.system('cls')
    exibir_subtitulo('Editar Informações Pessoais')

    email_pessoal = input('Digite o E-mail cadastrado: ')

    for usuario in usuarios:
        if 'email' in usuario and usuario['email'] == email_pessoal:
            # Mostra as informações atuais do usuário
            print('\nDados do usuário:')
            print(f'Nome de Usuário: {usuario['nome']}')
            print(f'E-mail Cadastrado: {usuario['email']}\n')

            # Solicita as novas informações
            novo_nome = input('Digite o nome de usuário (Pressione Enter para manter a informação atual): ')
            novo_email = input('Digite o E-mail (Pressione Enter para manter a informação atual): ')
            nova_senha = getpass.getpass('Digite a senha de acesso (Pressione Enter para manter a informação atual): \n')

            # Atualiza as informações de acesso
            usuario['nome'] = novo_nome if novo_nome else usuario['nome']
            usuario['email'] = novo_email if novo_email else usuario['email']
            usuario['senha'] = nova_senha if nova_senha else usuario['senha']

            print(f'\nOs dados do usuário {novo_nome} foram alterados com sucesso!\n')
            voltar_ao_menu_principal()
            return

    print(f'\nO usuário {email_pessoal} não foi encontrado!')
    voltar_ao_menu_principal()

def autenticar_usuario(usuario, senha_digitada):
    '''Função para autenticar o usuário'''
    if usuario['senha'] == senha_digitada:
        return True
    else:
        return False

def acesso_usuario():
    
    os.system('cls')
    exibir_subtitulo('Acesse o Sistema')
    email_usuario_busca = input('Digite o seu e-mail: ')
    usuario_encontrado = False

    try:
        for usuario in usuarios:
            if email_usuario_busca == usuario['email']:
                usuario_encontrado = True
                tentativas = 3
                while tentativas > 0:
                    senha_digitada = getpass.getpass (f'\nDigite a sua senha, {email_usuario_busca}: ')

                    if autenticar_usuario(usuario, senha_digitada):
                        print(f'\nBem-vindo(a), {email_usuario_busca}!')
                        main_tarefas()
                        return
                    else:
                        tentativas -= 1
                        print(f'Senha incorreta: restam {tentativas} tentativas.\n')
                print('Número máximo de tentativas atingido! Acesso negado!\n')
                return
        if not usuario_encontrado:
            print(f'\nO e-mail {email_usuario_busca} não foi encontrado em nossa base de dados\n')
            voltar_ao_menu_principal()

    except:
        voltar_ao_menu_principal()

def listar_usuarios():
    os.system('cls')
    exibir_subtitulo('Usuários Listados')
    for usuario in usuarios:
        nome_do_usuario = usuario['nome']
        email_do_usuario = usuario['email']
        print(f'- {nome_do_usuario} | {email_do_usuario}')
    voltar_ao_menu_principal()

def exibir_opcoes_logado():
    '''Esta função exibe a lista de opções disponíveis no menu principal após o usuário se logar
    
    Output:
    -Lista com as opções disponíveis no programa.
    '''
    print('1. Criar uma nova tarefa')
    print('2. Listar tarefas')
    print('3. Editar tarefa')
    print('4. Excluir tarefa')
    print('5. Sair')

def escolher_opcao_logado():
    '''Esta função permite o usuário selecionar entre um novo cadastro ou acessar o seu gerenciador'''

    try:
        opcao_escolhida = int(input('\nDigite a opção desejada: '))
        if opcao_escolhida == 1:
            criar_tarefa()
        elif opcao_escolhida == 2:
            visualizar_tarefa()
        elif opcao_escolhida == 3:
            editar_tarefa()
        elif opcao_escolhida == 4:
            excluir_tarefa()
        elif opcao_escolhida == 5:
            main()
        else:
            opcao_invalida_logado()
    except:
        opcao_invalida_logado()

def criar_tarefa():
    os.system('cls')
    exibir_subtitulo('Criar uma nova tarefa')
    nome_da_tarefa = input('Digite o título da sua tarefa: ')
    descricao_tarefa = input('\nDigite a descrição da tarefa: ')
    sem_prazo = input('\nDeseja definir um prazo para a tarefa? (S/N)?').lower()
    if sem_prazo == 's':
        data_de_criação = input('\nDigite a data de início da tarefa: ')
        prazo_de_conclusão = input('\nDigite o prazo para conclusão da tarefa: ')
    else:
        data_de_criação = 'Indeterminado'
        prazo_de_conclusão = 'Indeterminado'
    dados_da_tarefa = {'titulo':nome_da_tarefa, 'descricao':descricao_tarefa, 'datacriacao': data_de_criação, 'dataconclusao':prazo_de_conclusão}
    tarefas.append(dados_da_tarefa)
    print(f'\nA tarefa {nome_da_tarefa} foi incluída com sucesso!')
    voltar_ao_menu_principal_logado()

def editar_tarefa():
    os.system('cls')
    exibir_subtitulo('Editar Tarefa')

    for tarefa in tarefas:
        titulo_tarefa = tarefa['titulo']
        print(f'Tarefa: {titulo_tarefa}')

    titulo_tarefa = input('Digite o título da tarefa que deseja editar: ')

    for tarefa in tarefas:
        if 'titulo' in tarefa and tarefa['titulo'] == titulo_tarefa:
            # Mostra as informações atuais da tarefa
            print('\nInformações atuais da tarefa:')
            print(f'Título: {tarefa["titulo"]}')
            print(f'Descrição: {tarefa["descricao"]}')
            print(f'Data de criação: {tarefa["datacriacao"]}')
            print(f'Prazo para conclusão: {tarefa["dataconclusao"]}\n')

            # Solicita as novas informações
            novo_titulo = input('Novo título (pressione Enter para manter o atual): ')
            nova_descricao = input('Nova descrição (pressione Enter para manter a atual): ')
            nova_data_criacao = input('Nova data de criação (pressione Enter para manter a atual): ')
            novo_prazo_conclusao = input('Novo prazo para conclusão (pressione Enter para manter o atual): ')

            # Atualiza as informações da tarefa
            tarefa['titulo'] = novo_titulo if novo_titulo else tarefa['titulo']
            tarefa['descricao'] = nova_descricao if nova_descricao else tarefa['descricao']
            tarefa['datacriacao'] = nova_data_criacao if nova_data_criacao else tarefa['datacriacao']
            tarefa['dataconclusao'] = novo_prazo_conclusao if novo_prazo_conclusao else tarefa['dataconclusao']

            print('\nTarefa atualizada com sucesso!\n')
            voltar_ao_menu_principal_logado()
            return

    print(f'Tarefa com título "{titulo_tarefa}" não encontrada.\n')
    voltar_ao_menu_principal_logado()

def visualizar_tarefa():
    os.system('cls')
    exibir_subtitulo('Tarefas Criadas')
    for tarefa in tarefas:
        titulo_tarefa = tarefa['titulo']
        descricao_tarefa = tarefa['descricao']
        data_criacao = tarefa['datacriacao']
        data_conclusao = tarefa['dataconclusao']
        print(f'Tarefa: {titulo_tarefa}')
        print(f'Descrição da tarefa: {descricao_tarefa}')
        print(f'Data da criação: {data_criacao}')
        print(f'Prazo para conclusão: {data_conclusao}\n')
    voltar_ao_menu_principal_logado()

def excluir_tarefa():
    os.system('cls')
    exibir_subtitulo('Excluir tarefa')

    for tarefa in tarefas:
        titulo_tarefa = tarefa['titulo']
        print(f'Tarefa: {titulo_tarefa}')

    titulo_tarefa = input('\nDigite o nome da tarefa que deseja excluir: ')

    for tarefa in tarefas:
        if 'titulo' in tarefa and tarefa['titulo'] == titulo_tarefa:

            #Mostra as informações da tarefa
            print('\nInformações atuais da tarefa:')
            print(f'Título: {tarefa['titulo']}')
            print(f'Descrição: {tarefa['descricao']}')
            print(f'Data de Criação: {tarefa['datacriacao']}')
            print(f'Prazo para conclusão: {tarefa['dataconclusao']}')

            #Confirmação do Usuário
            confirmacao = input(f'Tem certeza que deseja excluir a tarefa {titulo_tarefa}? (S/N): ').lower()

            #Exclui ou Não a partir da confirmação
            if confirmacao == 's':
                tarefas.remove(tarefa)
                print(f'A tarefa {tarefa['titulo']} foi excluída com sucesso!')
            else:
                print('Exclusão cancelada. \n')
            voltar_ao_menu_principal_logado()
            return
        
    print(f'Tarefa {titulo_tarefa} não foi encontrada em nossa base.')
    voltar_ao_menu_principal_logado()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def opcao_invalida():
    '''Exibe a mensagem opção inválida e retorna ao menu principal
    
    Outputs:
    
    -Retorna ao menu principal
    '''
    print('\nOpção inválida!\n')
    voltar_ao_menu_principal()

def opcao_invalida_logado():
    '''Exibe a mensagem opção inválida e retorna ao menu principal
    
    Outputs:
    
    -Retorna ao menu principal
    '''
    print('\nOpção inválida!\n')
    voltar_ao_menu_principal_logado()

def voltar_ao_menu_principal():
    input('\nPressione uma tecla para voltar ao Menu Principal: ')
    main()

def voltar_ao_menu_principal_logado():
    input('\nPressione uma tecla para voltar ao Menu Principal: ')
    main_tarefas()

def exibir_nome_programa():
    '''Essa função é responsável por exbir o nome do programa que estamos trabalhando'''
    print('''𝔾𝕖𝕣𝕖𝕟𝕔𝕚𝕒𝕕𝕠𝕣 𝕕𝕖 𝕋𝕒𝕣𝕖𝕗𝕒𝕤
      ''')

def main():
    '''Função principal que inicia o programa'''
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

def main_tarefas():
    '''Função principal que inicia o programa após logado'''
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes_logado()
    escolher_opcao_logado()

if __name__ == '__main__':
    main()

if __name__ == '__main_tarefas__':
    main_tarefas()
