import multiprocessing
import time
import random

def operacao(valor,distanciamaxima,tamanhomaximodosalto):
    soma: int =0
    i: int =0
    
    while(soma<distanciamaxima):
        time.sleep(0.2)
        salto = random.randint(0,tamanhomaximodosalto)
        soma = soma + salto
        print("O sapo " , valor ," saltou " , salto , " cm distancia percorrida: " ,soma)
        
    print("O sapo  ",valor ," chegou")

def main():
    cont: int =1
    cont0 : int =0
    num_threads=5
    identificador =0
    vetor = [0]*5
    vetor2 = [(0,0,0)]*5
    tamanhosalto = random.randint(1,5)
    for cont0 in range(5):
        vetor2[cont0] = (cont0+1,20,tamanhosalto)
    with multiprocessing.Pool(processes=num_threads) as pool:
        pool.starmap(operacao,vetor2)

if(__name__=="__main__"):
    main()






