n:int =0
n1:int=0
n2:int=0
n3:int=0
mensagem: str = "Mensagem"

def leitura():
    global n,n1,n2,n3
    n = (int(input("Digite a primeiro número:")))
    n1 = (int(input("Digite o segundo número em ordem crescente:")))
    n2 = (int(input("Digite o terceiro número em ordem crescente:")))
    n3 = (int(input("Digite o quarto número:")))


def decisao():
    global n,n1,n2,n3,mensagem
    if(n3<n):
	    mensagem = str(n3) + " " + str(n) + " " +str(n1) + " " + str(n2)
    elif(n3<n1):
	    mensagem = str(n) + " " +str(n3) + " " + str(n1) + " " + str(n2)
    elif(n3<n2):
	    mensagem = str(n) + " " + str(n1) + " " + str(n3) + " " + str(n2)
    else:
	    mensagem = str(n) + " " +str(n1) + " "+  str(n2) + " "  + str(n3)

def exibicao():
    global mensagem
    print (mensagem)

def main():
    leitura()
    decisao()
    exibicao()

if(__name__=="__main__"):
    main()
    
