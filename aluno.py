numero = int(1,2,3,4,5,6,7,8,9,10)
#escolha o aluno que você quer colocar a sua nota.
aluno = input("digite o nome do aluno que voce quer colocar a nota: ",numero)

#escolha a nota de bimestre para este aluno.
nota1 = input('qual será a nota do aluno ??:')
print('a nota do aluno será:'+ nota1)

nota2 = input('qual será a nota do 2ºbimestre do aluno ??:')
print('a nota do aluno será:'+ nota2)

#notas final da prova do aluno.
notaPF = input('qual será a nota final da prova do aluno ??: ')
print("a nota final da prova será: " + notaPF)

#as somas das notas para as medias finais.

notaMP = int(nota1) + int(nota2) + int(notaPF)
notaMF = float(notaMP / 3)

#menssagem final.

print('a media final do ' + aluno + ' será a nota '  + str(notaMF))

if aluno == numero:
   print("erro ao digitar o nome !!!")
else:
   print("nome errado")

   