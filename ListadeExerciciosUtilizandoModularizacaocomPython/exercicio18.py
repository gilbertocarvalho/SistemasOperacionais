n1:int = 0
n2:int = 0
def leitura():
    global n1,n2
    n1 =(int (input("Digite o primeiro número:")))
    n2 =(int(input("Digite o segundo número:")))

def decisao():
    global n1,n2
    if(n1>n2):
        n1  =( n1 -n2)
    else:
         n1 =( n2 -n1)

def exibicao():
    global n1,n2
    print("a diferenca entre os dois números é: ",n1)

def main():
    leitura()
    decisao()
    exibicao()


if(__name__ =='__main__'):
    main()
