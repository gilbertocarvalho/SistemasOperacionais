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
    vetor =[0]*7
    i:int =0
    while(i<7):
        vetor[i] = i+1
        i = i +1
    return vetor

def criareexecutarthread():
    vetor = [0]*7
    semaforogerado = None
    pos:int
    pos =  multiprocessing.Value('i',0)
    vetor = lacoderepeticao()
    with multiprocessing.Manager() as gerenciador:
        semaforogerado  = gerenciador.Semaphore(5)
        with multiprocessing.Pool(processes=7,initializer=init,initargs=(semaforogerado,)) as pool:
            pool.map(equipe,vetor)
def criarsemaforos():
    i: int
    i = 0
    vetor = [0]*7
    while(i<7):
        vetor[i]= gerenciarthread();
        i = i+1
    return vetor

def gerenciarthread():
    with multiprocessing.Manager() as gerenciador:
        semaforogerado  = gerenciador.Semaphore(1)
        return semaforogerado

def sairdoboxequipe(recebe_identificador,recebe_carro):
    global semafaro
    identificador = recebe_identificador
    carro= recebe_carro
    print("carro " + str(recebe_carro)  + " da equipe " +str(recebe_identificador)+ " saiu do box")
    with semaforo:
        entrarnapista(carro,identificador)
def entrarnapista(recebe_carro,recebe_identificador):
    identificador = recebe_identificador
    carro= recebe_carro
    
    print("carro " + str(recebe_carro)  + " da equipe " +str(recebe_identificador)+ " entrou na pista")
    darumavolta(carro,identificador)
def darumavolta(recebe_carro,recebe_identificador):
    identificador = recebe_identificador
    carro= recebe_carro
    time.sleep(0.4)
    print("carro " + str(recebe_carro)  + " da equipe " +str(recebe_identificador)+ " deu uma volta 1:30:" +str(random.randint(0,999)))
    voltarparaosboxes(carro,identificador)



def voltarparaosboxes(recebe_carro,recebe_identificador):
    print("carro " + str(recebe_carro)  + " da equipe " +str(recebe_identificador)+ " voutou para os boxes")



def equipe(recebe_identificador):
    global semaforo

    time.sleep(0.2)
    carronobox("equipe " + str(recebe_identificador))
    carroescolhido =  definecarro()
    voltacarro1: int
    voltacarro2:int
    voltacarro1 =0
    voltacarro2 =0  
    while((voltacarro1<3) or  (voltacarro2<3)):
        carroescolhido =  definecarro()

        if(voltacarro1<3 and  carroescolhido==1):
            sairdoboxequipe(recebe_identificador,1)
            voltacarro1 = voltacarro1+1
        elif(voltacarro2<3 and  carroescolhido==2):
            sairdoboxequipe(recebe_identificador,2)
            voltacarro2 = voltacarro2+1
    print("equipe " + str(recebe_identificador)+ " finalizou o treino")

def carronobox(recebe_carro):
    print(recebe_carro, " está pronta" )



def definecarro():
    tamanhosalto: int
    tamanhosalto = int(random.randint(1000,2999)/1000)
    return tamanhosalto


if(__name__=="__main__"):
    main()
    
