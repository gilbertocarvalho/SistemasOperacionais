def main():
    n:int = (int(input("Digite um número:")))
    soma:float=1
    mensagem:String = ""
    while(n>=1):
        soma= soma + funcaodivisao(1,funcaofatorial(n))
        n  = n-1
        mensagem =  "+1/" +str(n+1) + "!"+ mensagem
    mensagem = "1"+ mensagem
    print(mensagem+ "=" + str(soma))
def funcaofatorial(receber_n):
    n: int = receber_n
    fatorial:int = 1
    while(n>1):
        fatorial = fatorial*n
        n= n-1
    return fatorial

def funcaodivisao(valor1,valor2):
    return (valor1/valor2)
if(__name__=="__main__"):
    main()
