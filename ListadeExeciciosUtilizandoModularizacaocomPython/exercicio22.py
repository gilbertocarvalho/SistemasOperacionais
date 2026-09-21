n:int =0
n:int =0
mensagem: str = "Mensagem"


def leitura():
    global n,n1
    n = (int(input("Digite a primeiro número:")))
    n1 = (int(input("Digite o segundo número:")))


def decisao():
    global n,n1,mensagem
    if(n<n1):
	    mensagem = str(n) + " " + str(n1)
    else:
	    mensagem = str(n1) + " " +str(n)

def exibicao():
    global mensagem
    print (mensagem)

def main():
    leitura()
    decisao()
    exibicao()

if(__name__=="__main__"):
    main()
