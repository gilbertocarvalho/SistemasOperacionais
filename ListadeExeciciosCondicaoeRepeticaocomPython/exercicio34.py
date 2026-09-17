n:int = int(input("Digite um número:"))
i : int = 0

mensagem : str =""
while(i<=10):

	mensagem = mensagem + str(n) + " * " + str(i)+ " = " + str(i*n) + "\n" 
	i = i+1
print (mensagem)

