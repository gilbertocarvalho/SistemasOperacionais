
serie :float =1
potencia:int =1
i: int =0
mensagem:str = "1"
for i in range(2,16,1):

	if(i%2==0):
		mensagem = mensagem + " - " 
		serie = serie - (i/i*i)
	 
	else:
		mensagem = mensagem +  " + "
		serie = serie + (i/i*i)
	
	mensagem =  mensagem +  str(i) + "/" + str(i*i) 
mensagem = mensagem + " = " + str(serie)

print(mensagem)



