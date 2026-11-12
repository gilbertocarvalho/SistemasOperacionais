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
    vetor =[0]*4
    i:int =0
    while(i<4):
        vetor[i] = i+1
        i = i +1
    return vetor

def criareexecutarthread():
    vetor = [0]*5
    semaforogerado = None
    vetor = lacoderepeticao()
    with multiprocessing.Manager() as gerenciador:
        semaforogerado  = gerenciador.Semaphore(1)
        with multiprocessing.Pool(processes=4,initializer=init,initargs=(semaforogerado,)) as pool:
            pool.map(pessoa,vetor)

def gerenciarthread():
    with multiprocessing.Manager() as gerenciador:
        semaforogerado  = gerenciador.Semaphore(1)
        return semaforogerado

def porta(recebe_pessoa):
    tempo:int
    tempo = definetempopassagem()
    time.sleep(tempo)
    print(recebe_pessoa ," cruzou  porta em", tempo , "segundos")

def pessoa(recebe_identificador):
    global semaforo

    velocidade: str
    velocidade = definevelocidade()
    time.sleep(0.2)
    pessoaandando(recebe_identificador,velocidade) 
    with semaforo:
        porta("pessoa "+ str( recebe_identificador))

def pessoaandando(recebe_id,recebe_velocidade):
    i : int 
    i =1
    while(i<200):
        time.sleep(0.2)
        print("pessoa" , recebe_id , "esta andando em direção a porta na velocidade de ", recebe_velocidade, "m/s , falta " ,str(200-i) ," metros"  )
        i = i+recebe_velocidade


def definevelocidade():
    velocidade: int
    velocidade = int(random.randint(4000,6999)/1000)
    return velocidade

def definetempopassagem():
    tempopassagem:int
    tempopassagem = int(random.randint(1000,2999)/1000)
    return tempopassagem

if(__name__=="__main__"):
    main()
