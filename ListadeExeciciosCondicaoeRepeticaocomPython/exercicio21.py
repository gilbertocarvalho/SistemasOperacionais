a:float = (float(input("Digite a primeira nota:")))
a = a + (float(input("Digite a segunda nota:")))
a = a +(float(input("Digite a terceira nota:")))
a = a +(float(input("Digite a quarta nota:")))
a = a = a/4
mensagem: str = "Mensagem"


if(a<3):
	mensagem = "RETIDO"
elif(a<6):
	mensagem = "EXAME"
else:
	mensagem = "APROVADO"

print (mensagem)

