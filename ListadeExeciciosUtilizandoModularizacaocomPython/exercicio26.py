n1:int=0
n2:int=0
mensagem: str = "Mensagem"
parte1:str = "Mensagem"
parte2:str= "Mensagem"

def leitura():
    global n1,n2
    n1 =  (int(input("Digite o primeiro número:")))
    n2 = (int(input("Digite o segundo número:")))

def decisao():
    global n1,n2,parte1,parte2,mensagem
    if(n1>n2):
	    parte1 =str(n1)
	    parte2 = str(n2)
	    n1 = n1%n2
    else:
	    parte1 = str(n2)
	    parte2 = str(n1)
	    n1 = n2%n1
	
    if(n1==0):
	    mensagem = parte1 + " é multiplo de "+parte2
    else:
	    mensagem = parte1 + " não é multiplo de "+ parte2
def exibicao():
    global mensagem
    print (mensagem)
def main():
    leitura()
    decisao()
    exibicao()

if(__name__=="__main__"):
    main()
