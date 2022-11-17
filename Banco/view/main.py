from time import sleep
from model.pessoaFisica import PessoaFisica
from model.pessoaJuridica import PessoaJuridica

from controller.fisico import create_psf, read_psf
from controller.juridico import create_pj, read_pj

def menu():

    menu = 1

    while (menu != 0):

        print('-=' * 7,'Cadastro Banco', '-=' * 7)
        menu = int(input('[1] Acessar Pessoa Fisica\n[2] Acessar Pessoa Juridica\n[0] Sair\nQual opção: '))
        print()

        match menu:
            
            case 1:
                print('-=' * 7, 'Pessoa Fisica', '-=' * 7)
                menu_inicial = int(input('[1] Cadastrar Conta Pessoa Fisica\n[2] Listar Contas Pessoa Fisica\nQual opção: '))
                print()
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
                 print('-=' * 7, 'Pessoa Juridica', '-=' * 7)
                 menu_inicial = int(input('[1] Cadastrar Conta Pessoa Juridica\n[2] Listar Contas Pessoa Juridica\nQual opção: '))
                 print()   
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
                        print('-=' * 7, 'Contas PJ Cadastradas', '-=' * 7)
                        read_pj() 
                        sleep(1)
                        print()
                        

    print('Finalizado!!!')
                    
                    




