

i : int =2

soma:float =1
mensagem:str = "1 "

while(i<51):
	soma = soma + i/(i+(i-1))
	mensagem = mensagem +  " + " +str(i)  + "/" + str(i+i-1)  
	
	i = i + 1
		
mensagem = mensagem + " = " + str(soma)

print(mensagem)



