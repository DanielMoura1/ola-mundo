from math import radians, sin, cos, tan, hypot
def xnx():
    print('\nXXXXXXXXX-------XXXXXXXXX')
def xn():
    print('XXXXXXXXX-------XXXXXXXXX')
def xnxx():
    print('XXXXXXXXX---EXTRA----XXXXXXXXX')
def pint():
    print('VALOR DO CATETO INVÁLIDO. Digite um valor apropriado.')
    def peri():
        print('perimetro: %.2f' % peri)



    
while True:

    while True:
        
        try:
            co = float(input('\n---------------------------------------\n\nInsira o valor de um dos catetos  do triângulo retângulo.(ele será usado como base): '))
            
        except:
            xnx()
            pint()
            xn()
            continue

        if co <= 0:
            xnx()
            pint()
            xn()

        else:
            break


    while True:

        try:
            an = float(input('\nDigite o ângulo adjacente ao cateto que você escolheu. Nao pode ser o ângulo de 90°: '))

        except:
            xnx()
            pint()
            xn()
            continue

        if an >= 90 or an <= 0:
            xnx()
            pint()
            xn()
            
        else:
            break
        
    while True:        
       
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
        break

    if input('\nDigite C para efetuar novos valores: ') in ('c','C'):
        continue
    else:
        break
          
   
