
n1:int = int(input("Digite o primeiro número:"))
n2:int = int(input("Digite o segundo número:"))
i : int =0
mensagem:str = ""

if(n1>n2):
	i= n2
	n2=n1
	n1=i

while(n1<=n2):
	i = 2
	while(i<n1):
		if(n1%i==0):
			break
		i = i + 1
	if(i==n1):
		mensagem = mensagem + str(n1) + " " 
	
	n1 = n1 +1
print(mensagem)



