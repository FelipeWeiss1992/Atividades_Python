from time import sleep
from random import randint

from model.pessoaFisica import PessoaFisica
from model.pessoaJuridica import PessoaJuridica

from controller.fisico import create_psf, read_psf,update_psf, delete_psf
from controller.juridico import create_pj, read_pj,update_pj, delete_pj

def menu():

    menu = 1

    while (menu != 0):

        print('-=' * 7,'Cadastro Banco', '-=' * 7)
        menu = int(input('[1] Acessar Pessoa Fisica\n[2] Acessar Pessoa Juridica\n[0] Sair\nQual opção: '))
        print()

        match menu:
            
            case 1:
                print('-=' * 7, 'Pessoa Fisica', '-=' * 7)
                menu_inicial = int(input('[1] Cadastrar Conta Pessoa Fisica\n[2] Listar Contas Pessoa Fisica\n[3] Atualizar Conta PF\n[4] Deletar Conta\nQual opção: '))
                print()
                match menu_inicial:

                    case 1:
                        pessoafisica = PessoaFisica()
                        pessoafisica.id = int(randint(1, 1000))
                        pessoafisica.titular = (input('Digite seu Nome Completo: '))
                        pessoafisica.cpf = (input('Digite seu CPF:'))
                        pessoafisica.saldo_inicial = float(input('Saldo Inicial: R$ '))
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

                    case 3:
                        pessoafisica = PessoaFisica()
                        pessoafisica.id = int(input('Digite o ID do titular para alterar dados: '))
                        pessoafisica.titular = (input('Digite seu Nome Completo: '))
                        pessoafisica.cpf = (input('Digite seu CPF:'))
                        pessoafisica.saldo_inicial = float(input('Saldo Inicial: R$ '))
                        resp_seg_tit = (input('Deseja cadastar um segundo titular: [S/N]')).upper().strip()
                        if resp_seg_tit in 'N':
                            update_psf(pessoafisica)
                            sleep(1)
                            print()
                        
                        else:
                            pessoafisica.segundo_titular = str(input('Digite o nome completo do segundo titular: '))
                            update_psf(pessoafisica)
                            sleep(1)
                            print()

                    case 4:
                        id = int(input('Digite o ID do titular: '))
                        delete_psf(id)
                        print('Deletado com Sucesso.')

            case 2:
                 print('-=' * 7, 'Pessoa Juridica', '-=' * 7)
                 menu_inicial = int(input('[1] Cadastrar Conta Pessoa Juridica\n[2] Listar Contas Pessoa Juridica\n[3] Atualizar Conta PJ\n[4] Deletar Conta\nQual opção: '))
                 print()   
                 match menu_inicial:

                    case 1:

                        pessoajuridica = PessoaJuridica()
                        pessoajuridica.id = int(randint(1, 1000))
                        pessoajuridica.titular = (input('Digite seu Nome Completo: '))
                        pessoajuridica.cnpj = (input('Digite seu CNPJ:'))
                        pessoajuridica.saldo_inicial = float(input('Saldo Inicial: R$ '))
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

                    case 3:
                        pessoajuridica = PessoaJuridica()
                        pessoajuridica.id = int(input('Digite o ID do titular para alterar dados: '))
                        pessoajuridica.titular = (input('Digite seu Nome Completo: '))
                        pessoajuridica.cnpj = (input('Digite seu CNPJ:'))
                        pessoajuridica.saldo_inicial = float(input('Saldo Inicial: R$ '))
                        resp_seg_tit = str(input('Deseja cadastar um segundo titular: [S/N]')).upper().strip()
                        if resp_seg_tit in 'N':
                            update_pj(pessoajuridica)
                            sleep(1)
                            print()
                        
                        else:
                            pessoajuridica.segundo_titular = str(input('Digite o nome completo do segundo titular: '))
                            update_pj(pessoajuridica)
                            sleep(1)
                            print()

            
                    
                    case 4:
                        id = int(input('Digite o ID do titular: '))
                        delete_pj(id)
                        print('Deletado com Sucesso.')
                        

    print('Finalizado!!!')
                    
                    




