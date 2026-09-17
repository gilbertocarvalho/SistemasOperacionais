n:int = int(input("Digite um número:"))


ant : int = 1
atual :int = 0
i: int =0

troca:int = 0
mensagem : str =""
while(i<n):
	mensagem = mensagem + str(atual) + " "
	troca = atual
	atual = ant+ atual
	ant = troca
	i = i + 1
	

print (mensagem)

