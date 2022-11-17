'''Na pasta model crie um documento com namespace main.py e realize as importacoes
from model.pessoaFisica import PessoaFisica
from model.pessoaJuridica import PessoaJuridica
from controller.saudacao import saudacao
from controller.juridico import create_pj, read_pj
from controller.fisico import create_psf, read_psf
Crie uma funcao menu()
Dentro da função menu() crie uma variável com nome de menu recebendo valor 1
Crie um while, abrindo parênteses  atribua à variável menu diferente de zero.
Crie um print descritivo solicitando ao usuário para digitar a opção desejada
Crie uma variável menu_inicial recebendo um int() e dentro do int um input solicitando ao usuário opção 1 ou opção 2, estas opções devem ser relacionadas à pessoa física e pessoa jurídica.
Crie um match recendo a variável menu_incial:
Crie um case 1: opção de escolha para pessoa física.
Crie um case 2: opção de escolha para pessoa física

dentro do case 1: crie uma variável menu recebendo um int() e dentro do int, um input solicitando ao usuário opção 1 ou opção 2, estas opções devem estar relacionadas a criar conta de pessoaFísica ou listar conta 
Crie um case 1: opção de escolha para Criar conta pessoaFísica
Crie um case 2: opção de escolha para listar contas pessoaFísica
Dentro do case 1: crie uma variável de referência ao objeto de PessoaFisica()
Chame cada atributos da nossa classe através da variável de referência do objeto e insira input solicitando dados para o cadastro.
Crie um if condicional solicitando se deseja cadastrar um segundo_titular.
Chame a função create_psf() e passe a variável de objeto
Dentro do case 2: chame a função read_psf()'''
from time import sleep
from model.pessoaFisica import PessoaFisica
from model.pessoaJuridica import PessoaJuridica

from controller.fisico import create_psf, read_psf
from controller.juridico import create_pj, read_pj

def menu():

    menu = 1

    while (menu != 0):

        print('-=' * 10,'Cadastro Banco', '-=' * 10)
        menu = int(input('[1] Acessar Pessoa Fisica\n[2] Acessar Pessoa Juridica\n[0]Sair\nQual opção: '))

        match menu:
            
            case 1:
                menu_inicial = int(input('[1] Cadastrar Conta Pessoa Fisica\n[2] Listar Contas Pessoa Fisica\nQual opção: '))

                match menu_inicial:

                    case 1:

                        pessoafisica = PessoaFisica()
                        pessoafisica.titular = (input('Digite seu Nome Completo: '))
                        pessoafisica.cpf = (input('Digite seu CPF:'))
                        pessoafisica.saldo_inicial = int(input('Saldo Inicial: '))
                        resp_seg_tit = (input('Deseja cadastar um segundo titular: [S/N]')).upper().strip()
                        if resp_seg_tit in 'N':
                            create_psf(pessoafisica)
                            sleep(1)
                            print()
                        else:
                            pessoafisica.segundo_titular = str(input('Digite o nome completo do segundo titular: '))
                            create_psf(pessoafisica)
                            sleep(1)
                            print()

                    case 2:
                        print('-=' * 10, 'Contas PF Cadastradas', '-=' * 10)
                        read_psf()
                        sleep(1)
                        print()
            case 2:
                 menu_inicial = int(input('[1] Cadastrar Conta Pessoa Juridica\n[2] Listar Contas Pessoa Juridica\nQual opção: '))

                 match menu_inicial:

                    case 1:

                        pessoajuridica = PessoaJuridica()
                        pessoajuridica.titular = (input('Digite seu Nome Completo: '))
                        pessoajuridica.cnpj = (input('Digite seu CNPJ:'))
                        pessoajuridica.saldo_inicial = int(input('Saldo Inicial: '))
                        resp_seg_tit = str(input('Deseja cadastar um segundo titular: [S/N]')).upper().strip()
                        if resp_seg_tit in 'N':
                            create_pj(pessoajuridica)
                            sleep(1)
                            print()
                        else:
                            pessoajuridica.segundo_titular = str(input('Digite o nome completo do segundo titular: '))
                            create_pj(pessoajuridica)
                            sleep(1)
                            print()

                    case 2:
                        print('-=' * 10, 'Contas PJ Cadastradas', '-=' * 10)
                        read_pj() 
                        sleep(1)
                        print()
                        

        print('Finalizado!!!')
                    
                    




