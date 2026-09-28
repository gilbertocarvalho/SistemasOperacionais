def main():
    n:int = (int(input("Digite um número:")))
    n = funcaofatorial(n)
    print ("O fatorial desse numero é ", n)
def funcaofatorial(receber_n):
    n: int = receber_n
    fatorial:int = 1
    while(n>1):
        fatorial = fatorial*n
        n= n-1
    return fatorial

if(__name__=="__main__"):
    main()
