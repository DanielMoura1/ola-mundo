contas = []
depositos= []
saldo = []

while True:
    def saquei(s):
        
        print('voce recebeu seu dinheiro com nota(s)')
            

        
           
            
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


    
    
    cont = -1
    

    def cria():
        ok = bool(int(input('deseja criar uma conta ?. sim digite"1". nao digite "0" ')))
        if ok == True:
            num = int(input('crie o seu numero da conta: '))
            while num in contas:
                print('numero ja existente:')
                num = int(input(' crie o seu numero da conta: '))
            contas.append(num)
            saldo.append(0)

    def deposito():
        num = int(input('digite o numero da sua conta:'))
        while num in contas:
            global saldo
            dep = input('digite "deposito" para depositar e "saque" para saque ')
            if dep == 'deposito':
            
                deposito = int(input('digite o valor do seu deposito:'))
                depositos.append(deposito)
                cont = -1
                for a in contas:
                    
                    
                    
                    cont = cont +1
                    
                    if a == num:
                        
                        saldo[cont] = saldo[cont] +deposito
            if dep == 'saque':
                saque = int(input('digite o valor do seu saque:'))
                
                cont = -1
                for a in contas:
                    
                    
                    
                    cont = cont +1
                    
                    if a == num:
                        
                        saldo[cont] = saldo[cont] -saque
                saquei(saque)
            
                
                
            
            opp = bool(int(input('deseja ver seu saldo?. sim digite"1". nao digite "0" ')))
            while opp:
                print('saldo',saldo)
                print('contas',contas)
                print('depositos', depositos)
                
                break
            break

                                 

                        
    while True:
            cria()
            deposito()

        
        
