mensagem: str = "Mensagem"
a: int = 0
b: int =0
c: int =0

def leitura():
    global a,b,c
    a = (int(input("Digite o coeficiente A:")))
    b =  (int(input("Digite o coeficiente B:")))
    c = (int(input("Digite o coeficiente C:")))

def calculo():
    global a,b,c
    c = (b**2) - (4*a*c)

def decisao():
    global a,b,c,mensagem
    if(c<0):
	    mensagem = "Não há raizes"
    else:
	    mensagem = ("primeira raiz é " + str((-b+(c**0.5))/(2*a)) + "  a segunda raiz é " + str((-b-(c**0.5))/(2*a)))
def exibicao():
    global mensagem
    print (mensagem)
def main():
    leitura()
    calculo()
    decisao()
    exibicao()

if(__name__=="__main__"):
    main()
