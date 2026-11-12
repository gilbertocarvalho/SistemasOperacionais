import multiprocessing
import time
import random

semaforo:None

def main():
    criareexecutarthread()

def init(receber_semaforo):
    global semaforo
    semaforo = receber_semaforo


def lacoderepeticao():
    vetor =[0]*5
    i:int =0
    while(i<5):
        vetor[i] = i+1
        i = i +1
    return vetor

def criareexecutarthread():
    vetor = [0]*5
    semaforogerado = None
    vetor = lacoderepeticao()
    with multiprocessing.Manager() as gerenciador:
        semaforogerado  = gerenciador.Semaphore(1)
        with multiprocessing.Pool(processes=5,initializer=init,initargs=(semaforogerado,)) as pool:
            pool.map(carro,vetor)

def gerenciarthread():
    with multiprocessing.Manager() as gerenciador:
        semaforogerado  = gerenciador.Semaphore(1)
        return semaforogerado

def cruzamento(recebe_carro):
    print(recebe_carro ," passou no cruzamento")

def carro(recebe_identificador):
    global semaforo

    sentido: str
    sentido = definesentido()
    time.sleep(0.2)
    carroandando(recebe_identificador,sentido) 
    with semaforo:
        cruzamento("carro "+ str( recebe_identificador) + " no sentido " + str(sentido))

def carroandando(recebe_id,recebe_sentido):
    i : int 
    i =1
    while(i<7):
        time.sleep(0.2)
        print("carro" , recebe_id , "esta andando",recebe_sentido," em direção ao cruzamento")
        i = i+1


def definesentido():
    sentido: int
    sentido = int(random.randint(1000,4999)/1000)
    if(sentido==1):
        return "leste"
    elif(sentido==2):
        return "sul"
    elif(sentido==3):
        return "oeste"
    else:
        return "norte"



if(__name__=="__main__"):
    main()
