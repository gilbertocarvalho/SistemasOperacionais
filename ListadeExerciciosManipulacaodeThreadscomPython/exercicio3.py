import multiprocessing
import time
import random

semaforo:None

posicao:int
def main():
    criareexecutarthread()

def init(receber_semaforo,receber_posicao):
    global semaforo
    global posicao
    semaforo = receber_semaforo
    posicao = receber_posicao


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
    pos:int
    pos =  multiprocessing.Value('i',0)
    vetor = lacoderepeticao()
    with multiprocessing.Manager() as gerenciador:
        semaforogerado  = gerenciador.Semaphore(1)
        with multiprocessing.Pool(processes=5,initializer=init,initargs=(semaforogerado,pos)) as pool:
            pool.map(sapo,vetor)

def gerenciarthread():
    with multiprocessing.Manager() as gerenciador:
        semaforogerado  = gerenciador.Semaphore(1)
        return semaforogerado

def chegada(recebe_sapo):
    global posicao
    posicao.value = posicao.value + 1
    print(recebe_sapo ," cruzou a linha de chegada em",posicao.value  , "lugar")

def sapo(recebe_identificador):
    global semaforo

    tamanhosaltomaximo: str
    tamanhosaltomaximo = definetamanhosalto()
    time.sleep(0.2)
    sapopulando(recebe_identificador,tamanhosaltomaximo) 
    with semaforo:
        chegada("sapo  "+ str( recebe_identificador))

def sapopulando(recebe_id,recebe_tamanhosalto):
    i : int 
    i =0
    distanciapulada:int
    while(i<20):
        time.sleep(0.2)
        distanciapulada = int((random.randint(0,(((recebe_tamanhosalto+1)*1000)-1))/1000))
        print("o sapo" , recebe_id , "pulou ", distanciapulada, "cm , já percorreu " ,str(i+distanciapulada) ," centimetros"  )
        i = i+distanciapulada


def definetamanhosalto():
    tamanhosalto: int
    tamanhosalto = int(random.randint(1000,5999)/1000)
    return tamanhosalto


if(__name__=="__main__"):
    main()
