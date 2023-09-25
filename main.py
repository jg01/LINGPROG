#Questao 11

var1 = int(input('Digite o primeiro número inteiro: '))
var2 = int(input('Digite o segundo numero inteiro: '))

print((var1*2)*(var2/2))

var3 = float(input('Digite o numero real: '))

print(f'{((var1*3) + var3):.4f}')

print(f'{(var3**3):.4f}')


#Questao 12

altura = float(input('Digite a altura da pessoa: '))

print('Peso ideal = '+str(72.7*altura - 58))

#Questao 13

print('Peso ideal para homens = '+str(72.7*altura - 52.8))
print('Peso ideal para mulheres = '+str(62.1*altura - 44.7))

#Questao 14

peso = float(input('Digite o peso dos peixes: '))

if peso > 50:
    excesso = peso - 50
    print(f'Voce deve pagar R${excesso*4} pelo excesso de {excesso} quilos')
else:
    print('Tudo certo, voce nao deve pagar nada.')
