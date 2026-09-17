


maior  = 0
menor = 0

mensagem : str =""
i =0
mensagem = "Digite o " +str(i+1) + "º número positivo:"
n:int = int(input(mensagem))

i = i + 1
maior =n 
menor = n
while(i<100):
	mensagem = "Digite o " +str(i+1) + "º número positivo :"
	n= int(input(mensagem))
	if(n<menor):
		menor = n
	elif(n>maior):
		maior = n
	i = i +1
print("O maior número é ", maior)
print("O menor número é ", menor)


