from math import radians, sin, cos, tan, hypot, acos , degrees


def lt():
    me('TIPO DE TRIÂNGULO EM RELAÇÃO AOS LADOS ')
def at():
    me('TIPO DE TRIÂNGULO EM RELAÇÃO AOS ÂNGULOS ')
    


def main():
    ladoum()
    ladodois()
    angulox()
    contas()
    escrever()
    ifs()
    fim()

def me(tex):
    return print(tex)

def linha1():
    me('-----------------')
def linha2():
    me('-----------------------------------------')
def linha3():
    me('-------------------------------------------------------------')



def erro():
    me('ERRO')
def ladoum():   
    def load():
        global l1
        try:
            l1 = float(input('digite o lado C do triangulo:  ')) 
        except:
            erro()
            return load()
            
        if l1 <= 0:
            erro()
            return load()
        elif l1 > 0:
            linha1()
                
    load()



def ladodois():    
    def load2():
        global l2
        try:
            l2 = float(input('digite o lado lado B do triangulo:  '))
        except:
            erro()
            return load2()
        if l2 <= 0:
            erro()
            return load2()
        elif l2 > 0:
            linha2()
    load2()


def angulox():
    def load3():
        global an
        try:
            an = float(input('digite o valor do ângulo formado pelos dois lados informados '))
        except:
            erro()
            return load3()
        if an >=180 or an <=0:
            erro()
            return load3()
        if 0 < an <180:

            linha3()
    load3()

    
        
   

def te():
    me('triangulo Equilatero',)
def ti():
    me('triangulo isosceles')
def tes():
    me('triangulo escaleno')
def tr():
    me('triangulo retangulo')
def ac():
    me('triangulo acutangulo')
def to():
    me('triangulo obtusangulo')
   



    






def contas():
    global ladox, anga, angb,angc,total,peri,area,altura,altura2,altura3,circunscrito,incrito,lado,ladol1,ladol2,angaa,angbb,angcc
    ladox = (l1**2+l2**2-2*l1*l2*cos(radians(an)))**(1/2)
    anga = degrees(acos((l1**2+l2**2-ladox**2)/(2*l1*l2)))
    angb = degrees(acos((ladox**2+l1**2-l2**2) /(2*ladox*l1)))
    angc = degrees(acos((ladox**2+l2**2-l1**2)/(2*ladox*l2)))
    total = anga + angb + angc
    peri = l1+l2+ladox
    area = 1/2*l1*l2*sin(radians(anga))
    altura = area*2/l1
    altura2 = area*2/l2
    altura3 = area*2/ladox
    circunscrito = (l1*l2*ladox)/(4*area)
    incrito = (2*area)/peri
    lado = '%.2f'% ladox
    ladol1 ='%.2f'% l1
    ladol2 = '%.2f'% l2
    angaa = '%.2f'% anga
    angbb = '%.2f'% angb
    angcc = '%.2f'% angc

def ifs():
        

    if ladol1 == ladol2 == lado:
        lt()
        te()
            
            
    elif ladol1 == ladol2 or ladol2 == lado or ladol1 == lado:
        lt()
        ti()
    else:
        lt()
        tes() 

    if angaa == '90.00' or angbb == '90.00' or angcc == '90.00':
        at()
        tr()
            
    elif anga <90 and angb <90 and angc <90:
        at()
        ac()
    else:
        at()
        to()

        

        
def escrever():
    me('lado C %.2f'%l1)
    me('lado B %.2f'%l2)

    me("lado A %.2f"% ladox)
        
    me('angulo A %.2f'% anga,)
    me('angulo B %.2f'% angb)
    me('angulo C %.2f'%angc)
    
    me('perimetro: %.2f'% peri)
    me('area : %.2f'% area)
    me('altura C: %.2f'% altura)
    me('altura B: %.2f'% altura2)
    me('altura A: %.2f'% altura3)
    me('raio do circulo  circunscrito: %.2f'% circunscrito)
    me('raio do circulo  incrito %.2f'% incrito)
    
    
       
    return
 
    

 
def fim():
    if input('\nDigite s para efetuar novos valores: ') in ('s','S'):
        return main()    
    else:
        return linha1()

    
   

        
main()


    
