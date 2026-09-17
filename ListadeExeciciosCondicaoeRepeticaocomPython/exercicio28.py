preco:float = (float(input("Digite o preço atual:")))
vendamensal:int = (int(input("Digite a venda mensal:")))

if((vendamensal<500)&(preco>30)):
	preco = preco*1.1
elif((vendamensal>=500)&(vendamensal<=1000)&(preco>=30)&(preco<80)):
	preco = preco *1.15
elif((vendamensal>=1000)&(preco>=80)):
	preco = preco * 0.95
print ("o novo preco será: ", preco)

