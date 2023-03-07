def metodo_dhont(nlugares, votos):
    '''
    nlugares = valor inteiro da quantidade de assentos
    votos = dicionario de valores com o somatorio dos votos totais de cada partido. ex = {'a': 655, 'b': 465, 'c': 300, 'g': 785}
    outputs = Rondas, seus respectivos votos e assentos garantidos, assim como um overview final do panorama.
    '''
    ronda = {} #cria dicionário com valores dos partidos zerados.
    for key in votos:
        ronda[key] = 0
    n_ronda = 0 #contador da ronda
    dicionario_substituto = votos.copy() # copia do dicionário para substituir o maior valor pela sua divisão.
    for i in range(nlugares): #loop para contar os assentos dentro do dicionário ronda
        lugar = max(dicionario_substituto.values()) #pega o valor maximo do dicionário copiado para contar a seleção substituir valores
        assento_selecionado = max(dicionario_substituto, key=dicionario_substituto.get) # pega a chave do valor que será contado e substituido
        if assento_selecionado in ronda: #condicional que verifica se já existir algum item dentro do dicionário ele somará + 1 valor
            ronda[assento_selecionado] += 1
        else: # condicional que se caso não exista a chave dentro da ronda, ela é criada e seu valor recebe 1 
            ronda[assento_selecionado] = 1
        dicionario_substituto[assento_selecionado] = votos[assento_selecionado]/(ronda[assento_selecionado]+1) #extrai o coeficiente de votação e o isere dentro da chave relativa.
        n_ronda +=1
        #impressão das parciais
        print(f'Ronda Número {n_ronda}: Condidato eleito do partido: {assento_selecionado}')
        for key in dicionario_substituto:
            print(f' Partido: {key} - {dicionario_substituto[key]} votos. {ronda[key]} candidato eleito.')
    resultados = list(ronda.items())
    return print(f'O numero de Candidatos dos partidos concorentes foi de {resultados}')