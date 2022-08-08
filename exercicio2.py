print('Sequência de Fibonacci')
apres =print('O programa contém uma sequência de fibonacci com 20 termos')
cliente=(int(input('Digite um número para saber se contém na sequência de fibonacci: ')))
n = int(20)
termo1 = 0
termo2 = 1
cont = 3
lista = [termo1,termo2]
while cont <= n:
    termo3 = termo1 + termo2
    
    termo1 = termo2
    termo2 = termo3
    lista.append(termo3)
    cont +=1
   
if cliente in lista:
    print(f'O número {cliente} está na sequência de fibonacci !')
else:
    print(f'O número {cliente} não está na sequência de fibonacci.')    


r=input('Você quer ver a sequência de fibonacci ? Responda com S/N: ')
resposta=r.strip()

if resposta == 'S'or resposta == 's':
    print(lista)
elif resposta == 'N'or resposta == 'n':
    print('Ok, tenha um bom dia !')    