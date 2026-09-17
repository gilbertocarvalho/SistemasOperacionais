n:int = (int(input("Digite a primeiro número:")))
n1:int = (int(input("Digite o segundo número em ordem crescente:")))
n2:int = (int(input("Digite o terceiro número em ordem crescente:")))
n3:int = (int(input("Digite o quarto número:")))

mensagem: str = "Mensagem"


if(n3<n):
	mensagem = str(n3) + " " + str(n) + " " +str(n1) + " " + str(n2)
elif(n3<n1):
	mensagem = str(n) + " " +str(n3) + " " + str(n1) + " " + str(n2)
elif(n3<n2):
	mensagem = str(n) + " " + str(n1) + " " + str(n3) + " " + str(n2)
else:
	mensagem = str(n) + " " +str(n1) + " "+  str(n2) + " "  + str(n3)
print (mensagem)

