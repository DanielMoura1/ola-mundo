def main():
    num1()
    num2()
    qwe()
    mult(x,y)
    div(x,y)
    fim()
def linha():
    print('------------------------------')

def num1():
    global x
    try:
        x = int(input('numero 1'))
    except:
        print('ERRO')
        return num1()
        
    
    if x >10 or x < -10:
        print('ERRO')
        return num1()
       
def num2():
    global y
    try:
        y = int(input('numero 2'))
    except:
        print('ERRO')
        return num2()
    if y >10 or y < -10:
        print('ERRO')
        return num2()
def qwe ():
    global asd
    asd = input('digite "div" para divisão, "resto" para resto e "mult" para multiplicação, digite qualquer coisa para todos.')
    

def mult(x,y):
    if asd != 'div' and  asd != 'resto':
        
        a = 0   
       
        if x == 0 or y == 0:
            print('mult: 0')

        elif x > 0 and y > 0:
            if x >= 10:
                a = a + y
                print(a)
            if x >= 9:
                a = a + y
                print(a)
            if x >= 8:
                a = a + y
                print(a)
            if x >= 7:
                a = a + y
                print(a)
           
           
            if x >= 6:
                a = a + y
                print(a)
            if x >= 5:
                a = a + y
                print(a)
            if x >= 4:
                a = a + y
                print(a)
            if x >= 3:
                a = a + y
                print(a)
            if x >= 2:
                a = a + y
                print(a)
            if x >= 1:
                a = a + y
                print(a)
            
            print('mult',a)
            linha()
        elif x < 0 and y < 0:
            x = x * -1
            y = y * -1
            
            if x >= 10:
                a = a + y
                print(a)
            if x >= 9:
                a = a + y
                print(a)
            if x >= 8:
                a = a + y
                print(a)
            if x >= 7:
                a = a + y
                print(a)
            
            
            if x >= 6:
                a = a + y
                print(a)
            if x >= 5:
                a = a + y
                print(a)
            if x >= 4:
                a = a + y
                print(a)
            if x >= 3:
                a = a + y
                print(a)
            if x >= 2:
                a = a + y
                print(a)
            if x >= 1:
                a = a + y
                print(a)
            
            print('mult',a)
            linha()
        else:
            if x < 0:
                x = x * -1
                print(a)
            if y < 0:
                y = y * -1
                print(a)
            if x >= 10:
                a = a + y
                print(a)
            if x >= 9:
                a = a + y
                print(a)
            if x >= 8:
                a = a + y
                print(a)
            if x >= 7:
                a = a + y
                print(a)
            
            
            if x >= 6:
                a = a + y
                print(a)
            if x >= 5:
                a = a + y
                print(a)
            if x >= 4:
                a = a + y
                print(a)
            if x >= 3:
                a = a + y
                print(a)
            if x >= 2:
                a = a + y
                print(a)
            if x >= 1:
                a = a + y
                print(a)
           
            print('mult',a * -1)
            linha()

def div(x,y):
    
    if asd != 'mult':
    
   # (+)(+)
   
    
    
        
            
        if y == 0:
            print('nao e possivel dividir por zero')
            return linha()
            
           
       
            
        elif x == 0:
            print('div: 0')
            

               
        
        elif x > 0 and y > 0:
            
            if x < y:
                if asd != 'resto':
                    #aqui
                    print('div :0  ')
                if asd != 'div':
                    print('resto: ',x)
                    return linha()
                else:
                    return linha()
                    
          

            
                
            d = y
            if x == y:
                if asd != 'resto':
                    print('div:',1)
                if asd != 'div':
                    print('resto : 0')
                    return linha()
                else:
                    return
            
                
            y = y + d
            cont = 2
            if y == x:
                if asd != 'resto':
                    print('div:',cont)
                    return linha()
                    
            if y > x:
                a = y -d
                if asd != 'resto':
                    
                    print('div: ',cont -1)
                if asd != 'div': 
                    print('resto:',x - a )
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
            y = y + d
            cont = 3
            if y == x:
                if asd != 'resto':
                    print('div:',cont)
                    return linha()
                    
            if y > x:
                a = y -d
                if asd != 'resto':
                    print('div: ',cont-1 )
                if asd != 'div':
                    print('resto:',x - a )
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

            y = y + d
            cont = 4
            if y == x:
                if asd != 'resto':
                    print('div:',cont)
                    return linha()
                    
            if y > x:
                a = y -d
                if asd != 'resto':
                    print('div: ',cont-1 )
                if asd != 'div':
                    print('resto:',x - a )
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
            y = y + d
            cont = 5
            if y == x:
                if asd != 'resto':
                    print('div:',cont)
                    return linha()
                    
            if y > x:
                a = y -d
                if asd != 'resto':
                    print('div: ',cont-1 )
                if asd != 'div':
                    print('resto:',x - a )
                    return linha()
                else:
                    return linha()
            
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
            y = y + d
            cont = 6
            if y == x:
                if asd != 'resto':
                    print('div:',cont)
                    return linha()
                    
            if y > x:
                a = y -d
                if asd != 'resto':
                    print('div: ',cont-1 )
                if asd != 'div':
                    print('resto:',x - a )
                    return linha()
                else:
                    return linha()           
            
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            y = y + d
            cont = 7
            if y == x:
                if asd != 'resto':
                    print('div:',cont)
                    return linha()
                    
            if y > x:
                a = y -d
                if asd != 'resto':
                    print('div: ',cont-1 )
                if asd != 'div':
                    print('resto:',x - a )
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            y = y + d
            cont = 8
            if y == x:
                if asd != 'resto':
                    print('div:',cont)
                    return linha()
                    
            if y > x:
                a = y -d
                if asd != 'resto':
                    print('div: ',cont-1 )
                if asd != 'div':
                    print('resto:',x - a )
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            y = y + d
            cont = 9
            if y == x:
                if asd != 'resto':
                    print('div:',cont)
                    return linha()
                    
            if y > x:
                a = y -d
                if asd != 'resto':
                    print('div: ',cont-1 )
                if asd != 'div':
                    print('resto:',x - a )
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            y = y + d
            cont = 10
            if y == x:
                if asd != 'resto':
                    print('div:',cont)
                    return linha()
                    
            if y > x:
                a = y -d
                if asd != 'resto':
                    print('div: ',cont-1 )
                if asd != 'div':
                    print('resto:',x - a )
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            y = y + d
            cont = 11
            if y == x:
                if asd != 'resto':
                    print('div:',cont)
                    return linha()
                    
            if y > x:
                a = y -d
                if asd != 'resto':
                    print('div: ',cont-1 )
                if asd != 'div':
                    print('resto:',x - a )
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            y = y + d
            cont = 12
            if y == x:
                if asd != 'resto':
                    print('div:',cont)
                    return linha()
                    
            if y > x:
                a = y -d
                if asd != 'resto':
                    print('div: ',cont-1 )
                if asd != 'div':
                    print('resto:',x - a )
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
       # aquiii (-)(-)
        elif x < 0 and y < 0:
            if x <0:
                y = y *-1
                x = x *-1
                if x < y:
                    if asd != 'resto':
                        print('div : 0 ')
                    if asd != 'div':
                        print(' resto:',-x)
                        return linha()
                    else:
                        return linha()
           
            d = y
            if x == y:
                if asd != 'resto':
                    print('div:',1)
                if asd != 'div':
                    print('resto : 0')
                    return linha()
                else:
                    return linha()
        
            
            y = y + d
            cont = 2
            if y == x:
                if asd != 'resto':
                    print('div:',cont)
                    return linha()
                
            if y > x:
                
                a = y -d
                if asd != 'resto':
                    print('div: ',(cont-1))
                if asd != 'div':
                    print('resto:',-(x - a ))
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
            y = y + d
            cont = 3
            if y == x:
                if asd != 'resto':
                    print('div:',cont)
                    return linha()
                
            if y > x:
                
                a = y -d
                if asd != 'resto':
                    print('div: ',(cont-1))
                if asd != 'div':
                    print('resto:',-(x - a ))
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            y = y + d
            cont = 4
            if y == x:
                if asd != 'resto':
                    print('div:',cont)
                    return linha()
                
            if y > x:
                
                a = y -d
                if asd != 'resto':
                    print('div: ',(cont-1))
                if asd != 'div':
                    print('resto:',-(x - a ))
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            y = y + d
            cont = 5
            if y == x:
                if asd != 'resto':
                    print('div:',cont)
                    return linha()
                
            if y > x:
                
                a = y -d
                if asd != 'resto':
                    print('div: ',(cont-1))
                if asd != 'div':
                    print('resto:',-(x - a ))
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            y = y + d
            cont = 6
            if y == x:
                if asd != 'resto':
                    print('div:',cont)
                    return linha()
                
            if y > x:
                
                a = y -d
                if asd != 'resto':
                    print('div: ',(cont-1))
                if asd != 'div':
                    print('resto:',-(x - a ))
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            y = y + d
            cont = 7
            if y == x:
                if asd != 'resto':
                    print('div:',cont)
                    return linha()
                
            if y > x:
                
                a = y -d
                if asd != 'resto':
                    print('div: ',(cont-1))
                if asd != 'div':
                    print('resto:',-(x - a ))
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            y = y + d
            cont = 8
            if y == x:
                if asd != 'resto':
                    print('div:',cont)
                    return linha()
                
            if y > x:
                
                a = y -d
                if asd != 'resto':
                    print('div: ',(cont-1))
                if asd != 'div':
                    print('resto:',-(x - a ))
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            y = y + d
            cont = 9
            if y == x:
                if asd != 'resto':
                    print('div:',cont)
                    return linha()
                
            if y > x:
                
                a = y -d
                if asd != 'resto':
                    print('div: ',(cont-1))
                if asd != 'div':
                    print('resto:',-(x - a ))
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            y = y + d
            cont = 10
            if y == x:
                if asd != 'resto':
                    print('div:',cont)
                    return linha()
                
            if y > x:
                
                a = y -d
                if asd != 'resto':
                    print('div: ',(cont-1))
                if asd != 'div':
                    print('resto:',-(x - a ))
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            y = y + d
            cont = 11
            if y == x:
                if asd != 'resto':
                    print('div:',cont)
                    return linha()
                
            if y > x:
                
                a = y -d
                if asd != 'resto':
                    print('div: ',(cont-1))
                if asd != 'div':
                    print('resto:',-(x - a ))
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            y = y + d
            cont = 11
            if y == x:
                if asd != 'resto':
                    print('div:',cont)
                    return linha()
                
            if y > x:
                
                a = y -d
                if asd != 'resto':
                    print('div: ',(cont-1))
                if asd != 'div':
                    print('resto:',-(x - a ))
                    return linha()
                else:
                    return linha()
                #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
          # aqui  (+) (-)
          #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        elif y <0:
            
            
            
            if x <0:
                x = x * -1
                
                if x <y:
                    if asd != 'resto':
                        print('div : -1 resto',y-x)
                        
                    if asd !='div':
                        print('resto 0')
                        return linha()
                    else:
                        return linha()
                
            if y <0:
                
                y = y * -1
                
                if y > x:
                    if asd !='resto':
                        print('div : -1 ')
                        
                    if asd != 'div':
                        print('resto:', -(y-x))
                        return linha()
                    else:
                        return linha()
                    
                    
                
            d = y
            if x == y:
                if asd != 'resto':
                    print('div:',-1)
                    
                if asd != 'div':
                    print('resto : 0')
                    return linha()
                else:
                    return linha()
        
            
            y = y + d
            cont = 2
            
            if y == x:
                if asd != 'resto':
                
                    print('div:',-cont)
                    
                if asd !='div':
                    print('resto 0')
                    return linha()
                else:
                    return linha()
                    
                
            
                
                
            if y > x:
                a = y -y
                if asd != 'resto':
                    print('div: ',-(cont ))
                if asd != 'div':
                    print('resto:', -(y-x)  )
                    return linha()
                else:
                    return linha()
                        
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
            y = y + d
            cont = 3
            if y == x:
                if asd != 'resto':
                
                    print('div:',-cont)
                    
                if asd !='div':
                    print('resto 0')
                    return linha()
                else:
                    return linha()
                    
                
            
                
                
            if y > x:
                a = y -y
                if asd != 'resto':
                    print('div: ',-(cont ))
                if asd != 'div':
                    print('resto:', -(y-x)  )
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            y = y + d
            cont = 4
            if y == x:
                if asd != 'resto':
                
                    print('div:',-cont)
                    
                if asd !='div':
                    print('resto 0')
                    return linha()
                else:
                    return linha()
                    
                
            
                
                
            if y > x:
                a = y -y
                if asd != 'resto':
                    print('div: ',-(cont ))
                if asd != 'div':
                    print('resto:', -(y-x)  )
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            y = y + d
            cont = 5
            if y == x:
                if asd != 'resto':
                    
                
                    print('div:',-cont)
                    
                if asd !='div':
                    print('resto 0')
                    return linha()
                else:
                    return linha()
                    
                
            
                
                
            if y > x:
                a = y -y
                if asd != 'resto':
                    print('div: ',-(cont ))
                if asd != 'div':
                    print('resto:', -(y-x)  )
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            y = y + d
            cont = 6
            if y == x:
                if asd != 'resto':
                
                    print('div:',-cont)
                    
                if asd !='div':
                    print('resto 0')
                    return linha()
                else:
                    return linha()
                    
                
            
                
                
            if y > x:
                a = y -y
                if asd != 'resto':
                    print('div: ',-(cont ))
                if asd != 'div':
                    print('resto:', -(y-x)  )
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            y = y + d
            cont = 7
            if y == x:
                if asd != 'resto':
                
                    print('div:',-cont)
                    
                if asd !='div':
                    print('resto 0')
                    return linha()
                else:
                    return linha()
                    
                
            
                
                
            if y > x:
                a = y -y
                if asd != 'resto':
                    print('div: ',-(cont ))
                if asd != 'div':
                    print('resto:', -(y-x)  )
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            y = y + d
            cont = 8
            if y == x:
                if asd != 'resto':
                
                    print('div:',-cont)
                    
                if asd !='div':
                    print('resto 0')
                    return linha()
                else:
                    return linha()
                    
                
            
                
                
            if y > x:
                a = y -y
                if asd != 'resto':
                    print('div: ',-(cont ))
                if asd != 'div':
                    print('resto:', -(y-x)  )
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            y = y + d
            cont = 9
            if y == x:
                if asd != 'resto':
                
                    print('div:',-cont)
                    
                if asd !='div':
                    print('resto 0')
                    return linha()
                else:
                    return linha()
                    
                
            
                
                
            if y > x:
                a = y -y
                if asd != 'resto':
                    print('div: ',-(cont ))
                if asd != 'div':
                    print('resto:', -(y-x)  )
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            y = y + d
            cont = 10
            if y == x:
                if asd != 'resto':
                
                    print('div:',-cont)
                    
                if asd !='div':
                    print('resto 0')
                    return linha()
                else:
                    return linha()
                    
                
            
                
                
            if y > x:
                a = y -y
                if asd != 'resto':
                    print('div: ',-(cont ))
                if asd != 'div':
                    print('resto:', -(y-x)  )
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            y = y + d
            cont = 11
            if y == x:
                if asd != 'resto':
                
                    print('div:',-cont)
                    
                if asd !='div':
                    print('resto 0')
                    return linha()
                else:
                    return linha()
                    
                
            
                
                
            if y > x:
                a = y -y
                if asd != 'resto':
                    print('div: ',-(cont ))
                if asd != 'div':
                    print('resto:', -(y-x)  )
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            y = y + d
            cont = 11
            if y == x:
                if asd != 'resto':
                
                    print('div:',-cont)
                    
                if asd !='div':
                    print('resto 0')
                    return linha()
                else:
                    return linha()
                    
                
            
                
                
            if y > x:
                a = y -y
                if asd != 'resto':
                    print('div: ',-(cont ))
                if asd != 'div':
                    print('resto:', -(y-x)  )
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        #(-)(+)
        elif x<0:
            
            
            
            if x <0:
                x = x * -1
                
                if x <y:
                    if asd != 'resto':
                        print('div : -1 ')
                        
                    if asd != 'div':
                        print('resto',y-x)
                        return linha()
                    else:
                        return linha()
                
            if y <0:
                
                y = y * -1
                if asd !='resto':
                    if y > x:
                        print('div : -1 ')
                    
                if asd != 'div':
                    return linha()
                    print('resto',-(y-x))
                else:
                    return linha()      
                
            d = y
            if x == y:
                if asd != 'resto':
                    print('div:',-1)
                if asd != 'div':
                    print('resto : 0')
                    return linha()
                else:
                    return linha()
                
        
            
            y = y + d
            cont = 2
            if y == x:
                if asd != 'resto':
                    print('div:',-cont)
                    return linha()
                if asd != 'div':
                    print('resto 0')
                    return linha()
                
            if y > x:
                a = y -y
                if asd != 'resto':
                    print('div: ',-(cont ))
                if asd !='div':
                    print('resto:',y-x  )
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
            y = y + d
            cont = 3
            if y == x:
                if asd != 'resto':
                    print('div:',-cont)
                    return linha()
                if asd != 'div':
                    print('resto 0')
                
            if y > x:
                a = y -y
                if asd != 'resto':
                    print('div: ',-(cont ))
                if asd !='div':
                    print('resto:',y-x  )
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            y = y + d
            cont = 4
            if y == x:
                if asd != 'resto':
                    print('div:',-cont)
                    return linha()
                if asd != 'div':
                    print('resto 0')
                    return linha()
                
            if y > x:
                a = y -y
                if asd != 'resto':
                    print('div: ',-(cont ))
                if asd !='div':
                    print('resto:',y-x  )
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            y = y + d
            cont = 5
            if y == x:
                if asd != 'resto':
                    print('div:',-cont)
                    return linha()
                if asd != 'div':
                    print('resto 0')
                    return linha()
                
            if y > x:
                a = y -y
                if asd != 'resto':
                    print('div: ',-(cont ))
                if asd !='div':
                    print('resto:',y-x  )
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            y = y + d
            cont = 6
            if y == x:
                if asd != 'resto':
                    print('div:',-cont)
                    return linha()
                if asd != 'div':
                    print('resto 0')
                    return linha()
                
            if y > x:
                a = y -y
                if asd != 'resto':
                    print('div: ',-(cont ))
                if asd !='div':
                    print('resto:',y-x  )
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            y = y + d
            cont = 7
            if y == x:
                if asd != 'resto':
                    print('div:',-cont)
                    return linha()
                if asd != 'div':
                    print('resto 0')
                    return linha()
                
            if y > x:
                a = y -y
                if asd != 'resto':
                    print('div: ',-(cont ))
                if asd !='div':
                    print('resto:',y-x  )
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            y = y + d
            cont = 8
            if y == x:
                if asd != 'resto':
                    print('div:',-cont)
                    return linha()
                if asd != 'div':
                    print('resto 0')
                    return linha()
                
            if y > x:
                a = y -y
                if asd != 'resto':
                    print('div: ',-(cont ))
                if asd !='div':
                    print('resto:',y-x  )
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            y = y + d
            cont = 9
            if y == x:
                if asd != 'resto':
                    print('div:',-cont)
                    return linha()
                if asd != 'div':
                    print('resto 0')
                    return linha()
                
            if y > x:
                a = y -y
                if asd != 'resto':
                    print('div: ',-(cont ))
                if asd !='div':
                    print('resto:',y-x  )
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            y = y + d
            cont = 10
            if y == x:
                if asd != 'resto':
                    print('div:',-cont)
                    return linha()
                if asd != 'div':
                    print('resto 0')
                    return linha()
                
            if y > x:
                a = y -y
                if asd != 'resto':
                    print('div: ',-(cont ))
                if asd !='div':
                    print('resto:',y-x  )
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            y = y + d
            cont = 11
            if y == x:
                if asd != 'resto':
                    print('div:',-cont)
                    return linha()
                if asd != 'div':
                    print('resto 0')
                    return linha()
                
            if y > x:
                a = y -y
                if asd != 'resto':
                    print('div: ',-(cont ))
                if asd !='div':
                    print('resto:',y-x  )
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
           
            y = y + d
            cont = 12
            if y == x:
                if asd != 'resto':
                    print('div:',-cont)
                    return linha()
                if asd != 'div':
                    print('resto 0')
                    return linha()
                
            if y > x:
                a = y -y
                if asd != 'resto':
                    print('div: ',-(cont ))
                if asd !='div':
                    print('resto:',y-x  )
                    return linha()
                else:
                    return linha()
            #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        
            

     



def fim():
    if input('\nDigite s para efetuar novos valores: ') in ('s','S'):
        return main()    
    else:
        print(' fim')

    
main()


        










   
        

 
    
