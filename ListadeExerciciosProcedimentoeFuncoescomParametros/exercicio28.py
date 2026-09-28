def leituraexecucao():
    preco:float = (float(input("Digite o preço atual:")))
    vendamensal:int = (int(input("Digite a venda mensal:")))
    decisao(preco,vendamensal)

def decisao(receber_preco,receber_venda):
    preco:float = receber_preco
    vendamensal:int = receber_venda
    if((vendamensal<500)&(preco<30)):
	    preco = preco*1.1
    elif((vendamensal>=500)&(vendamensal<=1000)&(preco>=30)&(preco<80)):
	    preco = preco *1.15
    elif((vendamensal>=1000)&(preco>=80)):
	    preco = preco * 0.95
    exibicao(preco)

def exibicao(receber_preco):
    print ("o novo preco será: "+ str(receber_preco))

def main():
    leituraexecucao()

if(__name__=="__main__"):
    main()
