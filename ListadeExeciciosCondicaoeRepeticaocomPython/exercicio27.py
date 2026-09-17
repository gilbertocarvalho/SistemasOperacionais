n1:int = (int(input("Digite o numero de voltas:")))
n1 = n1 *(int(input("Digite a extensão do circuito em metros:")))
resultado:float = n1 / int(input("Digite o tempo em duração em minutos:"))
resultado = resultado *(6/100)
mensagem: str = "a velocidade média foi de " + str(resultado) + " Km/h"

print (mensagem)

