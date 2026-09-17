n:int = (int(input("Digite a primeiro número:")))
n1:int = (int(input("Digite o segundo número:")))

mensagem: str = "Mensagem"


if(n<n1):
	mensagem = str(n) + " " + str(n1)
else:
	mensagem = str(n1) + " " +str(n)

print (mensagem)

