print('XXXXXXXXXXXXXXXXXXXXXXX[instruções]XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
print('O programa irar pedir para você montar a lista de compras, inserindo o nome do item, quantidade, valor da unidade em centavos, depois vai perguntar se você quer adicionar mais coisas a lista, digite “c” para sim ou digite outra coisa para não. O programa vai dar como saída o valor total das compras ')
print('')
print('Depois disso o programa vai pedir para você cadastrar o seu E-mail. Quando você cadastrar  ele vai perguntar se você quer adicionar mais um e-mail a lista. O valor das compras será  dividido entre os e-mails cadastrados.')
print(' ')
print('E por ultimo o programa vai pedir um dos  e-mails que você cadastrou , ele vai dar como saída o valor que o e-mail vai pagar . Depois disso o programa vai dar a opção de digitar outros dos e-mails para você comparar quanto cada um vai pagar. Depois vai perguntar se você quer fechar o programa ou reiniciar ele.')
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
print('')
while True:
    itens = []
    quantidades = []
    preço = []
    email2 = {} # dicionário
    email = [] # lista
    cont = 0 # quantidade de itens
    total2 = 0 
    conte = 0 # quantidade de e-mails
    Q = 1 # usado para iniciar o "while Q==1:"
    d = 0 # usado para dividir os valores igualmente para cada e-mail

      
    while True:  # Adicionando os itens nas listas 
       
        it = input('Digite o nome do item que voce quer comprar : ')
        itens.append(it)

       
        qu = int(input('Digite a quantidade do item que voce quer comprar : '))
        quantidades.append(qu)

        pre = int(input(' Digite o valor da unidade do item que voce quer comprar em centavos  : '))
        preço.append(pre)
        
       
        cont += 1
        if input('\nDigite C para continuar adicionando coisas nas listas ou digite qualquer outra coisa para avançar : ') in ('c','C'):
            continue
        else:
            break
    while True: #Adicionando os e-mails na lista 
        e= input('Cadastre seu e-mail :')
        while e in email:  # verificando se o e-mail é repetido
            print('E-mail ja cadastrado')
            e= input('Cadastre seu e-mail :')
        email.append(e)
        conte += 1
        
        if input('\nDigite C para inserir mais um e-mail a compra ou digite qualquer outra coisa para continuar : ') in ('c','C'):
            continue
        else:
            break
        
        
    for i in range(cont):
        total =  (quantidades[i]*preço[i])
        total2 += total
        print('item: ',itens[i], '  quantidade: ',quantidades[i] , '  R$: ',total/100)

    x =(total2//conte)
     
    c = total2 - (x*conte) #isso é igual a : c = total2 % conte
   
    print ('Total a pagar :R$', total2/100,)
    

    
    for a in email: # colocando a lista de e-mail e os valores no dicionário
       
        
        if c != 0:
            c = c-1
            d = 1
        else:
            d = 0
             
        email2.setdefault( a, ((x+d)/100))
            
                

   
        
    
    while Q==1:
        senha = input('Digite seu email para saber quanto voce vai pagar: ')
        
        while senha in email2.keys(): 
            print(senha,'vai pagar : R$',email2[senha])
            if input('\nDigite C para  entrar com outro e-mail ou digite outra coisa para continuar : ') in ('c','C'):
                break
            else:
                Q = 0 # usado para parar o "while Q==1:"
                break
        if not senha  in email2.keys():# mensagem de erro
            print('E-mail inválido') 
            
            
        

    if input('\nDigite C para iniciar uma nova execução, digite outra coisa para fechar o programa: ') in ('c','C'):
        continue
    else:
        break
            
        


        


