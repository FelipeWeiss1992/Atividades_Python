from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica

pessoafisica = PessoaFisica('Felipe', '986.576.695-09', 5000)
print()

print('-=' * 10, 'PessoaFisica Inicial', '-=' * 10)
print(pessoafisica,'\n')
pessoafisica.segundo_titular = 'Maiara'
print('-=' * 10, 'PessoaFisica alterações', '-=' * 10)
print(pessoafisica, '\n')
pessoajuridica = PessoaJuridica('Coferpan', '09.897.564/0001-34', 10000)
print()

print('-=' * 10, 'PessoaJuridica Inicial', '-=' * 10)
print(pessoajuridica, '\n')

pessoajuridica.segundo_titular = 'Fermisul'
print('-=' * 10, 'PessoaJuridica alterações', '-=' * 10)
print(pessoajuridica)
