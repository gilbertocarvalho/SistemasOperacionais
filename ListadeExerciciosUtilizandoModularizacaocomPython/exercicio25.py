hi:int =0
hf:int =0
mi:int=0
mf:int=0
mensagem: str = "Mensagem"

def leitura():
    global hi,hf,mi,mf
    hi = (int(input("Digite as horas do horário inicial:")))
    mi  = (int(input("Digite os minutos do horário inicial:")))

    hf  = (int(input("Digite as horas do horário final:")))
    mf  = (int(input("Digite os minutos do horário final:")))

def decisao():
    global hi,hf,mi,mf,mensagem
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
def exibicao():
    global mensagem
    print (mensagem)

def main():
    leitura()
    decisao()
    exibicao()

if(__name__=="__main__"):
    main()

