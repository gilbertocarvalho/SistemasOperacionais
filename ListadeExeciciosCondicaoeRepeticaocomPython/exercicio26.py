n1:int = (int(input("Digite o primeiro número:")))
n2:int = (int(input("Digite o segundo número:")))

mensagem: str = "Mensagem"
parte1:str = "Mensagem"
parte2:str= "Mensagem"

if(n1>n2):
	parte1 =str(n1)
	parte2 = str(n2)
	n1 = n1%n2
else:
	parte1 = str(n2)
	parte2 = str(n1)
	n1 = n2%n1
	
if(n1==0):
	mensagem = parte1 + " é multiplo de "+parte2
else:
	mensagem = parte1 + " não é multiplo de "+ parte2
print (mensagem)

