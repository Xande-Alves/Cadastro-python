from Pessoa import Pessoa
import unicodedata

lista = []
opcao_pesquisa = None
opcao_menu = None

def remover_acentos(texto):
    # Normaliza a string para o formato NFKD, que separa os caracteres acentuados
    texto_normalizado = unicodedata.normalize('NFKD', texto)
    # Retorna apenas os caracteres que não são acentos
    return ''.join(c for c in texto_normalizado if unicodedata.category(c) != 'Mn')

def cadastrar():
    p = Pessoa()
    p.setNome(input('Qual o seu nome?  '))
    p.setIdade(int(input('Qual a sua idade?  ')))
    p.setEndereco(input('Qual o seu endereço?  '))
    p.setCurso(input('Qual seu curso?  '))
    print('=================================================================================================\n')
    lista.append(p)

def listar():
    for p in lista:
        print(f'Nome: {p.getNome()} \nIdade: {p.getIdade()} \nEndereço: {p.getEndereco()} \nCurso: {p.getCurso()}')
        print('=================================================================================================\n')

def pesquisar():
    termo_pesquisa = None
    while True:
        opcao_pesquisa = input('Por que parâmetro deseja pesquisar? \n1 - Nome \n2 - Idade \n3 - Endereço \n4 - Curso \n')
        print('=================================================================================================\n')
        if opcao_pesquisa == '1':
            termo_pesquisa = input('Digite parte do nome que deseja pesquisar:  ')
            termo_pesquisa_normalizado = remover_acentos(termo_pesquisa)
            print('=================================================================================================\n')
            for p in lista:  
                elemento_lista_normalizado = remover_acentos(p.getNome())  
                if termo_pesquisa_normalizado.lower() in elemento_lista_normalizado.lower():
                    print(f'Nome: {p.getNome()} \nIdade: {p.getIdade()} \nEndereço: {p.getEndereco()} \nCurso: {p.getCurso()}')
                    print('=================================================================================================\n')
            break
        elif opcao_pesquisa == '2':
            termo_pesquisa = int(input('Digite a idade que deseja pesquisar:  '))
            print('=================================================================================================\n')
            for p in lista:    
                if termo_pesquisa == p.getIdade():
                    print(f'Nome: {p.getNome()} \nIdade: {p.getIdade()} \nEndereço: {p.getEndereco()} \nCurso: {p.getCurso()}')
                    print('=================================================================================================\n')
            break
        elif opcao_pesquisa == '3':
            termo_pesquisa = input('Digite parte do endereço que deseja pesquisar:  ')
            termo_pesquisa_normalizado = remover_acentos(termo_pesquisa)
            print('=================================================================================================\n')
            for p in lista:    
                elemento_lista_normalizado = remover_acentos(p.getEndereco())
                if termo_pesquisa_normalizado.lower() in elemento_lista_normalizado.lower():
                    print(f'Nome: {p.getNome()} \nIdade: {p.getIdade()} \nEndereço: {p.getEndereco()} \nCurso: {p.getCurso()}')
                    print('=================================================================================================\n')
            break
        elif opcao_pesquisa == '4':
            termo_pesquisa = input('Digite parte do nome do curso que deseja pesquisar:  ')
            termo_pesquisa_normalizado = remover_acentos(termo_pesquisa)
            print('=================================================================================================\n')
            for p in lista:    
                elemento_lista_normalizado = remover_acentos(p.getCurso())
                if termo_pesquisa_normalizado.lower() in elemento_lista_normalizado.lower():
                    print(f'Nome: {p.getNome()} \nIdade: {p.getIdade()} \nEndereço: {p.getEndereco()} \nCurso: {p.getCurso()}')
                    print('=================================================================================================\n')
            break
        else:
            print('Opção inválida!')
            print('=================================================================================================\n')
        
while True:
    opcao_menu = input('O que deseja fazer? \n1 - Cadastrar \n2 - Listar \n3 - Pesquisar \n4 - Sair  \n')
    print('=================================================================================================\n')
    if opcao_menu == '1':
        cadastrar()
    elif opcao_menu == '2':
        listar()
    elif opcao_menu == '3':
        pesquisar()
    elif opcao_menu == '4':
        print('Saindo do sistema...')
        break
    else:
        print('Opção inválida!')
        











