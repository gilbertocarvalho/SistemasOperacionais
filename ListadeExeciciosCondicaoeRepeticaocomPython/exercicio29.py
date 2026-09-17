opcao:int = (int(input("Digite 1 para poupança e 2 para renda fixa:")))
investimento:float = (float(input("Digite o valor do investimento:")))
mensagem:str = "Mensagem"
if(opcao==1):
	mensagem = "o valor corrigido é " + str(investimento*1.03)
elif(opcao==2):
	mensagem = "o valor corrigido é " + str(investimento*1.05)
else:
    mensagem = "Opção invalida"
print (mensagem)

