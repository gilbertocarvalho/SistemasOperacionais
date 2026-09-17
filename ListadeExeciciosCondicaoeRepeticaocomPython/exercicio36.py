n:int = int(input("Digite um número:"))


i : int = 1
f :int = 1
j: int =1
soma = 1
mensagem : str ="1 +"
while(i<=n):
	j=i+1
	f=1
	while(j>0):
		f =f *j
		j= j-1
	soma = soma + 1/f
	mensagem = mensagem +"1/" + str(i) + "!"
	if(i<n):
		mensagem = mensagem + " + "
	i = i + 1
	

print (mensagem + " = ",soma+1)

