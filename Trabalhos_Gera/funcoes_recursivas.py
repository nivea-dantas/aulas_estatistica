#imports
import numpy as np
from itertools import permutations
from itertools import combinations
import xlwt

def chama_menu(menu):
    if menu == 1:
        print('Você escolheu identificar os numeros primos.')
        return retorno_funcao1()
    elif menu == 2:
        print('Você escolheu Número de Representações')
        return retorno_funcao2()
    elif menu == 3:
        print('Você escolheu a Conjectura de Collatz')
        return retorno_funcao3()


#função numero primo - recursiva
def numero_primo(numero, i=2):
    if numero == i:
        return True
    elif numero % i == 0:
        return False
    return numero_primo(numero, i+1)

# FUnção recursiva  Numero Primo
def retorno_funcao1():
    n = int(input('Digite um número qualquer:'))
    retorno = numero_primo(n)
    print('A afirmação é',retorno)

#função representação
def representacao(n,p):
    termos = list(np.arange(1,n ** (1/p))**p)
    resultados=[]
    for i in range(len(termos)):
        combinacoes = list(combinations(termos, i+1))
        sequencias_possiveis = list(set(combinacoes))
        for y in range(len(sequencias_possiveis)):
                if sum(sequencias_possiveis[y])==n:
                    resultados.append(sequencias_possiveis[y])
    return resultados

#recursiva de representação
def retorno_funcao2():
    n = int(input('Informe o valor do denominador:'))
    p = int(input('Informe o valor do expoente:'))
    resultado = representacao(n,p)
    if len(resultado) != 0:
        print('O número de termos possíveis é',len(resultado[0]))
    elif len(resultado) == 0:
        print('Não existe possibilidades possíveis para a representação')
    
#função collatz - main
def collats(n):
    cont = [n]
    if n == 1:
        return cont
    elif n % 2 == 0:
        cont.extend(collats(int(n/2)))
    else:
        cont.extend(collats(int(3*n+1)))
    return cont

#recursiva
def retorno_funcao3():
    n = int(input('Digite qualquer valor:'))
    RETORNO = collats(n)[-1] == 1
    print('A afirmação é',RETORNO)


print('#####################################')
print('#                MENU               #')
print('#####################################')
print('\n')
print('1 - Verifica Primo')
print('2 - Número de Representações')
print('3 - Conjectura Collatz')
print('\n')


if __name__ == "__main__":
    menu = int(input('Insira a opção desejada:'))
    funcao = chama_menu(menu)
    