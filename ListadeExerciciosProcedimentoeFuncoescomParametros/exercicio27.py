
def leitura():
    n1:int = (int(input("Digite o numero de voltas:")))
    n1 = n1 *(int(input("Digite a extensão do circuito em metros:")))
    resultado:float = n1 / int(input("Digite o tempo em duração em minutos:"))
    calculo(resultado)

def calculo(receber_resultado):
    resultado:float = receber_resultado
    resultado = resultado *(6/100)
    exibicao(resultado)
def exibicao(resultado):
    mensagem: str = "A velocidade média foi de " + str(resultado) + " Km/h"

    print (mensagem)


def main():
    leitura()

if(__name__=="__main__"):
    main()

