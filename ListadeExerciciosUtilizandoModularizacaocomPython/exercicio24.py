n:int =0
mensagem: str = "Mensagem"

def leitura():
    global n
    n = (int(input("Digite um número:")))



def decisao():
    global mensagem,n
    if(n%6==0):
	    mensagem = "É divisivel por 2 e 3"

    else:
	    mensagem = "Não é divisivel por 2 e 3"

def exibicao():
    global mensagem
    print (mensagem)

def main():
    leitura()
    decisao()
    exibicao()

if(__name__=="__main__"):
    main()

