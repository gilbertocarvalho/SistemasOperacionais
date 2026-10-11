
a:int = int(input("Digite a quantidade de horas trabalhadas:"))


b:float = float(input("Digite o  valor por hora:"))

c:float = float(input("Digite o porcentual de desconto:"))

d:int =  int(input("Digite o número de descendentes:"))

salariobruto: float = a*b

salarioliquido:float = salariobruto *(1-(c/100))






print("O salario a receber é  ",salarioliquido+(d*100) )


