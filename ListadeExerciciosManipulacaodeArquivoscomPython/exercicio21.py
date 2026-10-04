import os


nome:str=''
nota1:float = 0
nota2:float = 0
nota3:float = 0
nota4:float = 0
valor_media:float = 0
dir:str = ''
arq:str=''
  
dir  = "/tmp/exercicios"
os.makedirs(dir,exist_ok=True)
os.chmod(dir,0o744)
  
def entrada():
    global nome,nota1,nota2,nota3,nota4,valor_media
    nome = (input("Digite o nome do aluno:"))
    nota1 = (float(input("Digite a primeira nota:")))
    nota2 = (float(input("Digite a segunda nota:")))
    nota3 = (float(input("Digite a terceira nota:")))
    nota4 = (float(input("Digite a quarta nota:")))
    valor_media = med(nota1,nota2,nota3,nota4)
    cadastro(nome,nota1,nota2,nota3,nota4,valor_media)

def med(n1,n2,n3,n4):
    media:float = (n1+n2+n3+n4)/4
    return media

def cadastro(nm,nt1,nt2,nt3,nt4,vlr_med):
    global dir,arq
    arq='ex21.txt'
    linha: str = nm + ";" + (str(nt1)) + ";" + (str(nt2)) + ";" + (str(nt3)) + ";" + (str(nt4)) + ";" + (str(vlr_med))+ "\n"
    escreveArq(dir,arq,linha)
def escreveArq(caminho,arquivo,linha_arq):
    file:str=''
    tipo:str=''
    enc:str=''
    file = caminho +"/" + arquivo
    enc = 'utf-8'
    linha_cad=linha_arq
    if(os.path.exists(caminho) & os.path.isdir(caminho)):
        if(os.path.exists(file)):
            tipo = 'a'
        else:
            tipo = 'w'
        with open(file,tipo,encoding=enc) as registro:
            registro.write(linha_cad)


def main():
    contador = 1
    while(contador<=5):
        entrada()
        contador = contador + 1
    

if(__name__=="__main__"):
    main()
