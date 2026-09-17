a = (int(input("Digite o coeficiente A:")))
b =  (int(input("Digite o coeficiente B:")))
c = (int(input("Digite o coeficiente C:")))

mensagem: str = "Mensagem"

c = (b**2) - (4*a*c)

if(c<0):
	mensagem = "Não há raizes"
else:
	mensagem = ("primeira raiz é " + str((-b+(c**0.5))/(2*a)) + "  a segunda raiz é " + str((-b-(c**0.5))/(2*a)))

print (mensagem)

