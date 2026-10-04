import os

valor:int =0
dir:str=''
arq:str=''
arq:str=''


dir:str  ="/tmp/exercicios"

os.makedirs(dir,exist_ok=True)
os.chmod(dir,0o744)

def main():

    valor:int = int(input("Digite um número entre 1 e 10:"))
    contador : int = 1

    while(contador<=10):
        grava(contador,mult(valor,contador))

        contador = contador+1

def mult(vlr,tab):
    res=vlr*tab
    return res

def grava(c,rslt):
    global dir,arq
    arq='ex34.txt'
    tipo:str=''
    enc:str='utf-8'
    linha:str=''
    linha =str(rslt)+ '\n'
    if(os.path.exists(dir) & os.path.isdir(dir)):
        arq=dir+"/"+arq
        if((os.path.exists(arq)) and  (c>1)):
            tipo='a'
        else:
            tipo='w'
        with open(arq,tipo,encoding=enc) as file:
            file.write(linha)

if(__name__=="__main__"):
    main()

