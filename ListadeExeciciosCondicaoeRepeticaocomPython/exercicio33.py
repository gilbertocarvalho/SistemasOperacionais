n:int = int(input("Digite um número:"))
i : int = 1
soma:int =0
mensagem:str = "1"
while(i<=n):
	soma = soma + 1/i
	if(i!=1):
		mensagem = mensagem + "1/" +str(i)
	if(i!=n):
	    mensagem = mensagem + " + "
	i = i+1
print (mensagem + " = " + str(soma))

