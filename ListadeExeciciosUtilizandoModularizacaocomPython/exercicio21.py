a:float 
mensagem: str = "Mensagem"

def leitura():
    global a
    a = (float(input("Digite a primeira nota:")))
    a = a + (float(input("Digite a segunda nota:")))
    a = a +(float(input("Digite a terceira nota:")))
    a = a +(float(input("Digite a quarta nota:")))
    a = a = a/4

def decisao():
    global mensagem
    if(a<3):
	    mensagem = "RETIDO"
    elif(a<6):
	    mensagem = "EXAME"
    else:
	    mensagem = "APROVADO"
def exibicao():
    global mensagem
    print (mensagem)

def main():
    leitura()
    decisao()
    exibicao()

if(__name__=="__main__"):
    main()
