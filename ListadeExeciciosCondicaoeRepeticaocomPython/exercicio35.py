n:int = int(input("Digite um número:"))
n2: int = int (input("Digite um segundo número:"))

i : int = n

mensagem : str =""
if(n>n2):
	i=n2
	n2=n
n=0
while(i<=n2):
	if(i%2==1):
		n = n+ i
	i=i+1
print ("A soma dos impares entre os dois valores é:",n)

