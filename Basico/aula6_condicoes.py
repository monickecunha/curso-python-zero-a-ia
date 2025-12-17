nota_aluno = float(input('Qual a usa nota no exame? '))

if nota_aluno >= 7:
    print('Você foi aprovado')
elif nota_aluno >= 5:
    print('Você está de recuperação')
else:
    print('Você foi reprovado')