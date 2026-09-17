hi:int = (int(input("Digite as horas do horário inicial:")))
mi:int = (int(input("Digite os minutos do horário inicial:")))

hf:int = (int(input("Digite as horas do horário final:")))
mf:int = (int(input("Digite os minutos do horário final:")))
mensagem: str = "Mensagem"


if(hi<hf):
	hi=(hf-hi)

else:
	hi =(24-hi)+hf
	
if(mf<mi):
	mensagem = "O jogo durou " + str(hi-1) + " horas e " + str((60-mi)+mf) + " minutos"
else:
	if(hi==24):
			hi=0
	mensagem = "O jogo durou " + str(hi) + " horas e " + str(mf-mi) + " minutos"

print (mensagem)

