opcao = 0
while opcao != 9:
    print('\033[1;35mBem vindo(a) ao APP WILLOW. Temos diversos serviços para sua navegação.\033[1;31m')
    print('''    [ 1 ] Jo Ken Po
    [ 2 ] Calculadora de Câmbio DOLAR X REAL
    [ 3 ] Player de Música
    [ 4 ] Conversor de temperaturas Celsius X Fahrenheit
    [ 5 ] Ident. Ano Bissexto
    [ 6 ] Gerador de P.A.
    [ 7 ] Calculadora de Economia de Tinta
    [ 8 ] Jogo de Advinhação
    [ 9 ] EXIT''')
    opcao = int(input('\033[1;35mQual é a sua opção?\033[1;31m>>>> '))
    if opcao == 1:
        from random import choice
        from time import sleep

        options = ['pedra', 'papel', 'tesoura']
        computer = choice(options)
        print('*||x' * 20)
        print('\033[1;34mVamos jogar JoKenPo')
        jogador = input('\033[1;34mEscolha entre pedra, papel e tesoura >>>\033[m ').lower()
        if jogador not in options:
            print('\033[1;31mEscolha inválida! Tente novamente!')
        else:
            print('*||x'*10)
            print('JO')
            sleep(0.5)
            print('KEN')
            sleep(0.5)
            print('PO')
            sleep(0.5)
            print('*||x'*10)
            sleep(0.5)
            if jogador == computer:
                print('\033[1;35mEmpate!\033[m')
            elif (jogador == 'tesoura' and computer == 'papel') or (jogador == 'pedra' and computer == 'tesoura') or (jogador == 'papel' and computer == 'pedra'):
                print(f'\033[1;35mVocê jogou {jogador} e o computador jogou {computer}. \n VOCÊ VENCEU!!!\033[m')
            else:
                print('\033[1;33mVocê jogou {} e o computador jogou {}.Você perdeu!\033[m'.format(jogador, computer))
        print('')
    if opcao == 2:
        print ('''\033[1;33m[ 1 ] CÂMBIO REAL para DÓLAR\n[ 2 ] CÂMBIO DÓLAR para REAL''')
        cambio = int(input('Escolha sua opção de câmbio >>> '))
        if cambio == 1:
            n1 = float(input('Quanto dinheiro você tem na carteira agora? R$ '))
            d = 5.87
            dolar = n1 / d
            print('\033[mConvertendo seus \033[1;35mR$ {:.2f}\033[m em dólares, hoje você tem somente \033[1;35mUS${:.2f}\033[m, SEU POBRE!!! <(°:°)>'.format(n1, dolar))
        print('')
        if cambio == 2:
            n1 = float(input('How many dollars do you have in your account? US$ '))
            r = 5.71
            real = n1 * r
            print('\033[mYou have got \033[1;35m{:.2f} BRL\033[m today. \nHave a nice day!'. format(real))
        print('')
    if opcao == 3:
        import pygame

        pygame.init()
        pygame.mixer.music.load('music002.mp3')
        pygame.mixer.music.play()
        input()
        pygame.event.wait()
        print('')
    if opcao == 4:
        print('''\033[1;33m[ 1 ] Conversão ºC para ºF\n[ 2 ] Conversão ºF para ºC''')
        option = int(input('Qual é a sua opção?>>>> \033[m'))
        if option == 1:
            Temperatura = float(input('Qual é a temperatura do ambiente em ºCelsius? '))
            Fahrenheit = Temperatura * 9 / 5 + 32
            print('A temperatura é de \033[1;36m{:.2f}ºF.\033[m'.format(Fahrenheit))
            print('')
        else:
            Temperatura = float(input('Qual é a temperatura do ambiente em ºFahrenheit? '))
            Celsius = (Temperatura - 32) * 5/9
            print('A temperatura é de \033[1;36m{:.2f}ºC.\033[m'.format(Celsius))
            print('')
    if opcao == 5:
        from datetime import date

        ano = int(input('\033[1;35mQue ano você quer analisar? Coloque um valor 0 para analisar o ano atual '))
        if ano == 0:
            ano = date.today().year
        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:  # é bom prestar atenção nos iguais
            print('\033[1;33mO ano {} É um ano bissexto \033[m'.format(ano))
        else:
            print('\033[1;33mO ano {} NÃO é um ano bissexto.\033[m'.format(ano))
        print('')
    if opcao == 6:
        primeiro = int(input('\033[1;33mDigite o primeiro termo de uma PA: '))
        raz = int(input('\033[1;34mDigite a razão dessa PA: '))
        pa = 0  # contador de termos gerados
        mais = 10  # inicialmente, vamos gerar 10 termos
        total = 0  # total de termos
        while mais != 0:
            total += mais  # atualiza o total de termos que já foram solicitados
            while pa <= total:  # enquanto o contador de termos gerados for menor que o total
                print('\033[1;38m', primeiro + pa * raz, end=' >> ')  # calcula o termo atual da PA
                pa += 1
            print('PAUSA')
            mais = int(input('\033[1;33mDigite um novo termo. Caso queira sair, digite 0: '))
        print( )
        print('\033[1;36mOperação finalizada com total de {} termos.'.format(total))
        print( )
    if opcao == 7:
        b = float(input('\033[1;36mQual é o tamanho, em metros, da base da parede? '))
        c = float(input('\033[1;36mQual é o tamanho, em metros, da altura da parede? '))
        a = b * c
        cor = (input('\033[1;37mQual é a cor da tinta? '))
        t = a / 2
        print('\033[1;33mComo a parede tem {} m², será necessário {} l de tinta {} para pintar sua parede! ECONOMIZE!!'.format(a, t,cor))
        print('')
    if opcao == 8:
        from random import randint

        print('\033[1;37m=-=-' * 23)
        print('\033[1;35mSou seu computador... \n     mas agora eu estou entediado. Vamos jogar advinhação?')
        print('\033[1;37m=-=-' * 23)
        # Gera um número aleatório entre 0 e 10
        computador = randint(0, 10)
        # Inicializa o contador de tentativas
        tentativas = 0
        max_tentativas = 5  # Limite de tentativas
        # Loop principal do jogo
        acertar = False
        while tentativas < max_tentativas and not acertar:
            # Incrementa o contador de tentativas
            tentativas += 1
            # Solicita a entrada do jogador
            jogador = int(input(f'\033[1;35mTentativa {tentativas}/{max_tentativas} - Adivinhe o número entre 0 e 10: '))
            # Verifica se o jogador acertou
            if jogador == computador:
                acertar = True
                print('\033[1;36mParabéns, você venceu!')
            elif jogador < computador:
                print('\033[1;33mMais... tente novamente! :) ')
            elif jogador > computador:
                print('\033[1;34mMenos... tente outra vez! :) ')
        print('+_+' * 10)
        if acertar:
            print('\033[1;35mFinalmente você acertou!')
        else:
            print(f'\033[1;35mFim das tentativas! O número era {computador}. Boa sorte na próxima vez!')
        print('+_+' * 10)
        # AQUI o contador de tentativas será utilizado. Por isso ele foi importante.
        print('\033[1;36mJogador, você fez {} tentativas.'.format(tentativas))
        print('')
    if opcao == 9:
        from time import sleep
        print('\033[1;33mFinalizando...')
        print('+=+=' * 10)
        for c in range (3, 0, -1):
            print(c, ' >> ', end=' ')
            sleep(0.5)
        print('\033[1;32m;) Au revoir! \n Obrigado por interagir. Volte sempre!\033[m')








