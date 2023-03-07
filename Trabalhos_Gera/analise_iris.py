#imports bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#carga de dados
df = pd.read_csv('Iris.csv', sep= ',')


# Funções de plots

def retorno_funcao3(): #retorna o plot do gráfico de pizza
    species = list(df['Species'].unique())
    species_size = list(df['Species'].value_counts())
    figura, ax = plt.subplots()
    figura.set_size_inches(10, 10)
    ax.pie(species_size, labels=species, autopct='%1.2f', startangle=90)
    ax.axis('equal')
    plt.show()

def retorno_funcao4(): #retorna o plot do gráfico de dispersão
    Setosa = df[df['Species'] == 'Iris-setosa']
    Versicolor = df[df['Species'] == 'Iris-versicolor']
    Virginica = df[df['Species'] == 'Iris-virginica']
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 10)
    ax.scatter(Versicolor['PetalLengthCm'], Versicolor['PetalWidthCm'], label='Versicolor').set_facecolor('green')
    ax.scatter(Setosa['PetalLengthCm'], Setosa['PetalWidthCm'], label='Setosa').set_facecolor('blue')
    ax.scatter(Virginica['PetalLengthCm'], Virginica['PetalWidthCm'], label='Virginica').set_facecolor('red')
    ax.set_xlabel('Petal Length (cm)')
    ax.set_ylabel('Petal Width (cm)')
    ax.set_title('Tamanho das pétalas Íris')
    ax.legend(loc='lower right')
    plt.show()


def chama_menu(menu): #chama a seleção de menus
    if menu == 1:
        return print('Formato dos dados:\n',df.shape,'\n \nPrimeiras linhas:\n', df.head())
    elif menu == 2:
        return print(df.describe())
    elif menu == 3:
        return retorno_funcao3()
    elif menu == 4:
        return retorno_funcao4()

#inicio do programa
print('#####################################')
print('#                MENU               #')
print('#####################################')
print('\n')
print('1 - Formato dos dados e primeiras linhas')
print('2 - Estatística')
print('3 - Frequência das espécies')
print('3 - Relação entre comprimeiro e largura das pétalas')
print('\n')


#função main
if __name__ == "__main__":
    menu = int(input('Insira a opção desejada:'))
    funcao = chama_menu(menu)