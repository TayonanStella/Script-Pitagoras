from time import sleep


def mostrarlinha(valor):
    tam = ('\033[33m=\033[m'*valor)
    print(tam)


def mostrarmsg(msg):
    tam = len(msg)+4
    print('\033[33m=\033[m'*tam)
    print(f'  \033[31m{msg}\033[m')
    print('\033[33m=\033[m'*tam)
    sleep(1.5)


def calcarea():
    mostrarmsg('Você escolheu o cálculo de área')
    sleep(0.5)
    largura = float(input('digite a largura em metros '))
    comprimento = float(input('digite o comprimento em metros '))
    res = comprimento*largura
    return res


def calcvolume():
    mostrarmsg('você escolheu o cálculo de volume')
    sleep(0.5)
    largura = float(input('digite a largura em metros '))
    comprimento = float(input('digite o comprimento em metros '))
    altura = float(input('digite a altura em metros '))
    res = (largura*comprimento)*altura
    return res


def calcmédia():
    mostrarmsg('Você escolheu cálculo de média')
    somageral = 0
    opvezes = int(input('de quantos valores deseja obter a média '))
    for r in range(0, opvezes):
        valorDeEntrada = float(input(f'divite o {r+1}º valor '))
        somageral += valorDeEntrada
    res = somageral/opvezes
    return res


def fibonacci():
    mostrarmsg('Você escolheu números fibonacci')
    while True:
        opcaotermos = str(input('Quantos termos deseja? ')).strip()
        if opcaotermos.isnumeric():
            opcaotermos = int(opcaotermos)
            break
        print('use apenas numeros inteiros')
    cont = atual = anterior = 0
    res = [1]
    while(cont < opcaotermos):
        if cont == 0:
            res.append(1)
            atual = 1
            anterior =1
        if cont > 0:
            atual += anterior
            anterior = atual - anterior
            res.append(atual)
        cont += 1
    return res



mostrarmsg('BEM VINDO AO PITÁGORAS')
while True:
    print('[1] Cálculo de área\n'
          '[2] Cálculo de volume\n'
          '[3] Cálculo de média aritmética\n'
          '[4] Números fibonacci\n'
          '    Enter pra sair')
    mostrarlinha(26)
    while True:
        opçãodeop = str(input('escolha entre 1 e 4: ')).strip()
        if opçãodeop == '':
            print('você escolheu sair ')
            sleep(0.5)
            break
        if opçãodeop in '1234':
            opçãodeop = int(opçãodeop[0])
            break
        print('digite um número de 1 a 4')
    if opçãodeop == '':
        break
    if opçãodeop == 1:
        área = calcarea()
        mostrarmsg(f'A medida corresponde à {área} mts²')
    if opçãodeop == 2:
        volume = calcvolume()
        mostrarmsg(f'A medida corresponde à {volume} mts³')
    if opçãodeop == 3:
        média = calcmédia()
        mostrarmsg(f'A média dos valores digitados é {média}')
    if opçãodeop == 4:
        seqfibo = fibonacci()
        mostrarmsg(f'A sequencia fibonacci solicitada é {seqfibo}')
    while True:
        resp = str(input('deseja continuar? S/n ')).strip().upper()
        if resp in 'SN ':
            break
        print('ERRO! use somente S ou N')
    if resp == 'N' or opçãodeop == '':
        break
print('\033[4:31mObrigado por usar o pitágoras\nVolte sempre!\033[m')


