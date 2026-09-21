n1:int = 0
n2:int = 0

def leitura():
    global n1,n2
    n1 = (int(input("Digite o primeiro numero:")))
    n2 =  (int(input("Digite o segundo numero:")))

def decisao():
    global n1,n2
    if(n1<n2):
        n1 = n2

def exibicao():
    print ("O maior é : ",n1)

def main():
    leitura()
    decisao()
    exibicao()

if(__name__=='__main__'):
    main()

