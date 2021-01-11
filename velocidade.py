
   
while True:
    try:
        print('digite 6 para notas de provas')
        print('digite 5 para jogar o jogo de pedra, papel e tesoura')
        print('digite 4 banco')
        print('digite 3 para triangulo retangulo ')
        print('digite 2 para jogar rpg')
        nice = float(input('digite 1 para saber velocida media, 1.1 para distancia,1.2 para tempo'))
    
    except:
        print('XXXXXXXXXXXXXXXXXX')
        print('erro')
        print('xxxxxxxxxxxxxxxxxx')
        nice = float(input('digite 1 para saber velocida media, 1.1 para distancia,1.2 para tempo'))
    try:
        while nice ==6:
            alunos = 10
            media = []
            for i in range(1,alunos+1):
                nota = 0
                for j in range (1,5):
                    nota += float(input('digite a nota %i de 4 do alunos %i de %i :'%(j,i,alunos)))
                nota = nota/4
                media.append(nota)
            cont = 0
            for a in media:
                if a >= 7:
                    cont = cont + 1

            print(media)
            print('quantidade de alunos q tiraram 7 ou mais na media',cont)


            print('digite 6 para notas de provas')
            print('digite 5 para jogar o jogo de pedra, papel e tesoura')
            print('digite 4 banco')
            print('digite 3 para triangulo retangulo ')
            print('digite 2 para jogar rpg')
            nice = float(input('digite 1 para saber velocida media, 1.1 para distancia,1.2 para tempo'))
            
        while nice ==4:
            asdf = 0
            while asdf == 0:
                try:
                    s = int(input('saque seu dinheiro'))
                except:
                    print('erro')

                if s == 0:
                    print('digite 6 para notas de provas')
                    print('digite 5 para jogar o jogo de pedra, papel e tesoura')
                    print('digite 4 banco')
                    print('digite 3 para triangulo retangulo ')
                    print('digite 2 para jogar rpg')
                    asdf = 1
                    nice = float(input('digite 1 para saber velocida media, 1.1 para distancia,1.2 para tempo'))
                     
                nota_cem = s // 100
                s = s % 100

                nota_cinquenta = s // 50
                s = s % 50

                
                

                nota_dez = s // 10
                s = s % 10

                nota_cinco = s // 5
                s = s % 5

                nota_dois = s // 2
                s = s % 2

                nota_um = s // 1

                if nota_cem > 0:
                    print(nota_cem,'nota(s) de cem reais')

                if nota_cinquenta > 0:
                    print(nota_cinquenta,'nota(s) de cinquenta reais')

                

                if nota_dez > 0:
                    print(nota_dez,'nota(s) de dez reais')
                if nota_cinco >0:
                    print(nota_cinco,'nota(s) de cinco reais')

                if nota_dois > 0:
                    print(nota_dois,'nota(s) de dois reais')

                if nota_um > 0:
                    print(nota_um,'nota(s) de um real')

                print('digite "0" para sair')


        while nice ==3:
            from math import radians, sin, cos, tan, hypot
            def xnx():
                print('\nXXXXXXXXX-------XXXXXXXXX')
            def xn():
                print('XXXXXXXXX-------XXXXXXXXX')
            def xnxx():
                print('XXXXXXXXX---EXTRA----XXXXXXXXX')
            fim = 0
            while fim == 0:
                fimm = 0

                while fim == 0:
                    
                    try:
                        co = float(input('\n---------------------------------------\n\nInsira o valor de um dos catetos  do triângulo retângulo.(ele será usado como base): '))
                        
                    except:
                        xnx()
                        print('VALOR DO CATETO INVÁLIDO. Digite um valor apropriado.')
                        xn()
                        continue

                    if co <= 0:
                        xnx()
                        print('VALOR DO CATETO INVÁLIDO. Digite um valor apropriado.')
                        xn()

                    else:
                        break


                while fim == 0:

                    try:
                        an = float(input('\nDigite o ângulo adjacente ao cateto que você escolheu. Nao pode ser o ângulo de 90°: '))

                    except:
                        xnx()
                        print('VALOR INVÁLIDO. Digite um valor apropriado.')
                        xn()
                        continue

                    if an >= 90 or an <= 0:
                        xnx()
                        print('VALOR DE ÂNGULO INVÁLIDO. Digite um valor apropriado.')
                        xn()
                        
                    else:
                        break
                
            
                
                    
                while fim == 0:       
                   
                    a = 90 - an
                    h = co/sin(radians(a))
                    ca = (h**2 - co**2)**(1/2)

                    print('\nCateto adjacente ao ângulo: %.2f'% co)
                    print('Hipotenusa: %.2f'% h)
                    print('Cateto oposto: %.2f'%ca )
                    print('Ângulos:  [90.0°], [{}°], [{}°]'.format('%.2f' %a, '%.2f' %an))

                    peri = ca+co+h
                    area = ((co*ca)/2)
                    incrito = ((ca+co-h)/2)
                    circunscrito = (ca*co*h)/(4*((co*ca)/2))
                    altura = area/(h/2)

                    xnxx()

                    
                    print('perimetro: %.2f' % peri)
                    print('altura: %.2f'% altura)
                    print('area: %.2f'% area)
                    print('raio do circulo  incrito %.2f'% incrito)
                    print('raio do circulo  circunscrito: %.2f'% circunscrito)
                    

                    if input('\nDigite C para efetuar novos valores, ou qualquer outra coisa para parar:  ') in ('c','C'):
                        continue
                    else:
                        print('digite 4 banco')
                        print('digite 3 para triangulo retangulo ')
                        print('digite 2 para jogar rpg')
                        print('digite 5 para jogar o jogo de pedra, papel e tesoura')
                        fim = 1
                        nice = float(input('digite 1 para saber velocida media, 1.1 para distancia,1.2 para tempo'))
                        try:
                            nice = float(input('digite 1 para saber velocida media, 1.1 para distancia,1.2 para tempo'))
                        except:
                            
                            break

                   
                    
                             
        #1-------------------------------------------------------------
        while nice == 1:
            distancia = float(input('distancia: '))
            tempo = float(input('tempo: '))
            velocidade = distancia/tempo
    
            print('')
            print('velocida =',velocidade,)
            print('')
            print('digite 6 para notas de provas')
            print('digite 5 para jogar o jogo de pedra, papel e tesoura')
            print('digite 4 banco')
            print('digite 3 para triangulo retangulo ')
            print('digite 2 para jogar rpg')
            nice = float(input('digite 1 para saber velocida media, 1.1 para distancia,1.2 para tempo'))
        
        while nice == 1.1:
            velocidade = float(input('velocidade: '))
            tempo = float(input('tempo: '))
    
    
            distancia = tempo * velocidade

            print('')
            print('distancia =',distancia)
            print('')
            print('digite 6 para notas de provas')
            print('digite 5 para jogar o jogo de pedra, papel e tesoura')
            print('digite 4 banco')
            print('digite 3 para triangulo retangulo ')
            print('digite 2 para jogar rpg')
            nice = float(input('digite 1 para saber velocida media, 1.1 para distancia,1.2 para tempo'))
   
        while nice == 1.2:
            velocidade = float(input('velocidade: '))
            distancia = float(input('distancia: '))
            tempo = distancia/ velocidade

            print('')
            print('tempo=',tempo)
            print('')
            print('digite 5 para jogar o jogo de pedra, papel e tesoura')
            print('digite 2 para jogar rpg')
            nice = float(input('digite 1 para saber velocida media, 1.1 para distancia,1.2 para tempo'))
            #5----------------------------------------------------------------------------------------
        while nice == 5:
            
            import random
            x = input('digite "p" para pedra, "pa" para papel e "t" para tesoura: ')
            y = random.randrange(1,4)
            print('')
            print('para parar digite zero')
            print('')

            if x == '0':
                break

            if y == 1:   
                y = 'p'
                print('XXXXXXXXXXXXXXXXXXXXX')
                print('maquina escolheu pedra')
                print('XXXXXXXXXXXXXXXXXXXXXX')
            if y == 2:
                y = 'pa'
                print('XXXXXXXXXXXXXXXXXXXXXX')
                print('maquina escolheu papel')
                print('XXXXXXXXXXXXXXXXXXXXXX')
            if y == 3:
                y = 't'
                print('XXXXXXXXXXXXXXXXXXXXXX')
                print('maquina escolheu tesoura')
                print('XXXXXXXXXXXXXXXXXXXXXX')

            if x =='p':
                if y == 'p':
                    print('<<<<<<<<empate>>>>>>>>>>>')
                    print('porque os dois escolheram pedra')
                elif y == 'pa':
                    print('<<<<<<<<<<derrota>>>>>>>>>>>')
                    print('porque papel vence de pedra')
                elif y == 't':
                    print('<<<<<<<<<<<<vitoria>>>>>>>>>')
                    print('porque pedra vence de tesoura')
            elif x == 'pa':
                if y == 'pa':
                    print('<<<<<<<<<<empate>>>>>>>>>')
                    print('porque os dois escolheram papel ')
                if y == 'p':
                    print('<<<<<<<<vitoria>>>>>>>>>')
                    print('porque papel vence de pedra')
                if y == 't':
                    print('<<<<<<<derrota>>>>>>>')
                    print('porque papel perde pra tesoura')

            elif x == 't':
                if y == 't':
                    print('')
                    print('')
                    print('<<<<<<empate>>>>>')
                    print('porque os dois escolheram tesoura')
                    print('')
                    print('')
                if y == 'p':
                    print('')
                    print('')
                    print('<<<<<<<derrota>>>>')
                    print('tesoura perde para pedra ')
                    print('')
                    print('')
                if y == 'pa':
                    print('')
                    print('')
                    print('<<<<<<<<<<vitoria>>>>>')
                    print('porque tesoura vence de papel')
                    print('')
                    print('')
                if x == '0':
                    break

        
            else:
                print('comando invalido')
                print('')
                print('"FIM"')
                print('')


#--------2---------------------------------------------------------                       
        while nice ==2:
            p = 0
            i = 0
            inimigo_vida = 100
            inig_atq = 15
            p1_vida =  80
            habi1 = 10
            habi2 = 15
            habi3 =20
            habi4 = 15
            nivel2_1 = 0
            hb1 = 20
            hb2 = 30
            hb3 = 40
            hb4 = 15
            hb5 = 1
            ingvida = 900
            p2vida = 150
            nivel2_2 = 0
            neemias = 200
            mafia = 200
            print('Neemias estava indo para casa da namorada, quando') 
            print('de repente um cachorro  o atacou ')
            print('')
            print(' hp do inimigo inicial :[',inimigo_vida,'] seu hp inicial :[',p1_vida,']' )
            print('')   
            x = input('digite a, b , c ou d para se defender:')
            print('')
            if x =='a':
                x = habi1
                inig_atq = 8
                inimigo_vida = inimigo_vida - x
                p1_vida = p1_vida - inig_atq
                print('Neemias deu um chute no dog, causou:[',habi1,']de dano')
                print('O Cachorro mordeu a perna dele, Neemias recebeu: [',inig_atq,'] de dano')
                print('')
                print('hp do inimigo:[',inimigo_vida,']   seu hp :[',p1_vida,']' )
                print('')      
                print('')
               

            if x == 'b':
                x = habi2
                inig_atq = 15
                inimigo_vida = inimigo_vida - x
                p1_vida = p1_vida - inig_atq
                print('Neemias dá um soco no dog, causou:[',habi2,']de dano')
                print('Dog morde a mao dele, Neemias recebeu: [',inig_atq,'] de dano')
                print('')
                print('hp do inimigo:[',inimigo_vida,']   seu hp :[',p1_vida,']' )
                print('')
                print('')
                
            if x == 'c':
                x = habi3
                inig_atq = 30
                inimigo_vida = inimigo_vida - x
                p1_vida = p1_vida - inig_atq
                print(' Neemias joga uma pedra no dog, causou[',habi3,']de dano')
                print('dog fica com odio no coraçao e morde o saco do ney, ele recebeu: [',inig_atq,'] de dano')
                print('hp do inimigo:[',inimigo_vida,']   seu hp :[',p1_vida,']' )
                print('')
               
            if x == 'd':
                x = habi4
                inig_atq = 25
                inimigo_vida = inimigo_vida + x
                p1_vida = p1_vida + inig_atq
                print('Neemias corre ,  Neemias curou:[20]')
                print('cachorro corre atras dele , recupera [15] de vida')
                print('')
                print('hp do inimigo:[',inimigo_vida,']   seu hp :[',p1_vida,']' )
                print('')  

            while inimigo_vida > 0:
                if x =='a':
                    x = habi1
                    inig_atq = 8
                    inimigo_vida = inimigo_vida - x
                    p1_vida = p1_vida - inig_atq
                    print('Neemias deu chute no dog, causou:[',habi1,']de dano')
                    print('O Cachorro mordeu a perna dele, Neemias recebeu: [',inig_atq,'] de dano')
                    print('')
                    print('hp do inimigo:[',inimigo_vida,']   seu hp :[',p1_vida,']' )
                    print('')     
                    
               

                if x == 'b':
                    x = habi2
                    inig_atq = 15
                    inimigo_vida = inimigo_vida - x
                    p1_vida = p1_vida - inig_atq
                    print('Neemias da soco no dog, causou:[',habi2,']de dano')
                    print('Dog morde a mao dele, Neemias recebeu: [',inig_atq,'] de dano')
                    print('')
                    print('hp do inimigo:[',inimigo_vida,']   seu hp :[',p1_vida,']' )
                    print('')
                    
                
                if x == 'c':
                    x = habi3
                    inig_atq = 30
                    inimigo_vida = inimigo_vida - x
                    p1_vida = p1_vida - inig_atq
                    print(' Neemias joga uma pedra no dog, causou[',habi3,']de dano')
                    print('dog fica com odio no coraçao e morde o saco do ney, ele recebeu: [',inig_atq,'] de dano')
                    print('hp do inimigo:[',inimigo_vida,']   seu hp :[',p1_vida,']' )
                    print('')
               
                if x == 'd':
                    x = habi4
                    inig_atq = 20
                    inimigo_vida = inimigo_vida + x
                    p1_vida = p1_vida + inig_atq
                    print('Neemias corre ,  Neemias curou:[20]')
                    print('cachorro corre atras dele , recupera [15] de vida')
                    print('')
                    print('hp do inimigo:[',inimigo_vida,']   seu hp :[',p1_vida,']' )
                    print('')
                
                
                if p1_vida  <= 0 >= inimigo_vida:
                    print('xxxxxxxx"Empate"xxxxxxxxxx')
                    nivel2_2 = 1
                elif inimigo_vida <= 0:
                    print('<<<<..<<<<..<<<<Win>>>>..>>>>..>>>>')
                    nivel2_1 = 1
                elif p1_vida <= 0:
                    print('"<<<<..<<<<..<<<<Derrota>>>>..>>>>..>>>>"')
                    inimigo_vida = 0
                    print('feiche o jogo')
                x = input('ataque de novo:')
            z = input('gigite alguma coisa para continuar')#1fase
            while nivel2_1 != 0:
                i = i + 1
                if i == 1:
                    print('quando Neemias da o golpe final no dog um policial passa e vê a situação')
                    print('Ney é preso e levado a jugamendo')
                    print('o dono do dog o processou por matar o cachorro ,agora ele vai lutar pela sua liberdade')
                z = input('digite a, b, c, ou d para dialogar e sair livre da situaçao')
                if z =='a':
                    z = habi1
                    inig_atq = 8
                    ingvida = ingvida - z
                    p2vida = p2vida - inig_atq
                    print('voce usou um bom argumento, causou:[',habi1,']de dano a moral do acusador')
                    print('o acusador usou um mau argumento, deu : [',inig_atq,'] de dano a sua credibilidade')
                    print('')
                    print(' Reputação do Acusador :[',ingvida,']   Reputação do Neemias hp :[',p2vida,']' )
                    print('')      
                    print('')

                elif z == 'b':
                    z = habi2
                    inig_atq = 15
                    ingvida = ingvida - z
                    p2vida = p2vida - inig_atq
                    print('Neemias usaou um argumento eficaz, causou:[',habi2,']de dano a credibilidade')
                    print('acusador, mostra fotos de Ney matando o dog , ele causa: [',inig_atq,'] de dano a imagem de ney')
                    print('')
                    print(' Reputação do Acusador :[',ingvida,']   Reputação do Neemias hp :[',p2vida,']' )
                    print('')
                    print('')
                elif z == 'c':
                    z = habi3
                    inig_atq = 30
                    ingvida = ingvida - z
                    p2vida = p2vida - inig_atq
                    print('Neemias usa um argumento lendario, causa',habi3,']de dano a credibilidade do acusador')
                    print('acusador apela para video do dog brincado com crinças e afirma que o dog era um otimo cachorro,ney perde[',inig_atq,']')
                    print(' Reputação do Acusador :[',ingvida,']   Reputação do Neemias hp :[',p2vida,']' )
                    print('')
                elif z == 'd':
                    z = habi4
                    inig_atq = 25
                    ingvida = ingvida + z
                    p2vida = p2vida + inig_atq
                    print('ney recupera sua credibilidade mostrando as marcas de mordias pelo corpo[25]reputação')
                    print('acusador recupera acredibilade com depoimento do dono do dog chorrando [+15]reputação')
                    print('')
                    print(' Reputação do Acusador :[',ingvida,']   Reputação do Neemias hp :[',p2vida,']' )
                    print('')
                if p2vida  <= 0 >= ingvida:
                    print('xxxxxxxx"Empate"xxxxxxxxxx')
                    nivel2_2 = 1
                elif ingvida <= 0:
                    print('<<<<..<<<<..<<<<Win>>>>..>>>>..>>>>')
                    nivel2_1 = 0
                elif p2vida <= 0:
                    print('"<<<<..<<<<..<<<<Derrota>>>>..>>>>..>>>>"')
                    ingvida = 0
                    print('feiche o jogo')#2fase
                    print('digite 6 para notas de provas')
                    print('digite 5 para jogar o jogo de pedra, papel e tesoura')
                    print('digite 4 banco')
                    print('digite 3 para triangulo retangulo ')
                    print('digite 2 para jogar rpg')
                    nice = float(input('digite 1 para saber velocida media, 1.1 para distancia,1.2 para tempo'))

            while nivel2_2 != 0:
                p = p + 1
                if p == 1:
                    print('no meio da luta epica de ney vs dog')
                    print('um homem chega e pergunta pq Neemias ta batendo no cachorro do maior mafioso do Brasil')
                    print('o homem coloca Neemias dentro de um carro e leva ele para covil')
                    print('o mafioso diz que se ney vencer ele em um luta de boxe ney pode sair livre de la')
                z = input('a,d,c,d use algum deles')
                if z =='a':
                    if mafia%10 == 0:
                        mafia = mafia + 50
                    z = hb1
                    inig_atq = 20
                    mafia = mafia - z
                    neemias = neemias - inig_atq
                    print(' Neemias, causou:[',hb1,']de dano')
                    print('mafioso causa[',inig_atq,'] ')
                    print('')
                    print(' hp mafia :[',mafia,']  Neemias hp :[',neemias,']' )
                    print('')      
                    print('')

                if z == 'b':
                    if mafia%10 == 0:
                        mafia = mafia + 50
                    z = hb2
                    inig_atq = 20
                    mafia = mafia - z
                    neemias = neemias - inig_atq
                    print(' Neemias, causou:[',hb2,']de dano')
                    print('mafioso causa[',inig_atq,'] ')
                    print('')
                    print(' hp mafia :[',mafia,']  Neemias hp :[',neemias,']' )
                    print('')      
                    print('')
                if z == 'c':
                    if mafia%10 == 0:
                        mafia = mafia + 50
                    z = hb3
                    inig_atq = 20
                    mafia = mafia - z
                    neemias = neemias - inig_atq
                    print(' Neemias, causou:[',hb3,']de dano')
                    print('mafioso causa[',inig_atq,'] ')
                    print('')
                    print(' hp mafia :[',mafia,']  Neemias hp :[',neemias,']' )
                    print('')      
                    print('')
                if z == 'd':
                    if mafia%10 == 0:
                        mafia = mafia + 50
                    z = hb4
                    inig_atq = 20
                    mafia = mafia + z
                    neemias = neemias + inig_atq
                    print(' Neemias recupera [20]de vida')
                    print('mafioso recupera [15] de vida ')
                    print('')
                    print(' hp mafia :[',mafia,']  Neemias hp :[',neemias,']' )
                    print('')      
                    print('')
                if z == 'g':
                    if mafia%10 == 0:
                        mafia = mafia + 50
                    z = hb5
                    inig_atq = 20
                    mafia = mafia - z
                    neemias = neemias - inig_atq
                    print(' Neemias, causou:[',hb5,']de dano')
                    print('mafioso causa[',inig_atq,'] ')
                    print('')
                    print(' hp mafia :[',mafia,']  Neemias hp :[',neemias,']' )
                    print('')      
                    print('')
                if neemias  <= 0 >= mafia:
                    print('xxxxxxxx"Empate"xxxxxxxxxx')
                    break
                if mafia <= 0:
                    print('<<<<..<<<<..<<<<Win>>>>..>>>>..>>>>')
                    nivel2_2 = 0
                if neemias <= 0:
                    print('"<<<<..<<<<..<<<<Derrota>>>>..>>>>..>>>>"')
                    nivel2_2 = 0
                    

















           

                    
                    #3fase
            input('fim')
            break
             
                


                    
                
    except:
        print('XXXXXXXXXXXXXXXXXX')
        print('erro')
        print('xxxxxxxxxxxxxxxxxx')
        x = float(input('digite 1 para saber velocida media, 1.1 para distancia,1.2 para tempo'))
print( 'teste')
