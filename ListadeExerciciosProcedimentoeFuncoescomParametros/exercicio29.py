
def execucaoeleitura():
    opcao:int = (int(input("Digite 1 para poupança e 2 para renda fixa:")))
    investimento:float = (float(input("Digite o valor do investimento:")))
    decisao(opcao,investimento)
def  decisao(receber_opcao,receber_investimento):
    mensagem:str = "Mensagem"
    opcao:int = receber_opcao
    investimento = receber_investimento
    if(opcao==1):
	    mensagem = "o valor corrigido é " + str(investimento*1.03)
    elif(opcao==2):
	    mensagem = "o valor corrigido é " + str(investimento*1.05)
    else:
        mensagem = "Opção invalida"
    exibicao(mensagem)

def exibicao(receber_mensagem):
    print (receber_mensagem)

def main():
    execucaoeleitura()

if(__name__=="__main__"):
    main()
