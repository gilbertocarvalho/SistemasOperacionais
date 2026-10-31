import multiprocessing
import time
import random

def operacao(valor,recebevetor):
    soma: int =0
    i: int =0
    
    while(i<5):
        time.sleep(0.2)
        soma = soma + recebevetor[i]
        i = i+1
    print("linha:",valor ," soma :",soma)

def main():
    cont: int =1
    cont0 : int =0
    num_threads=5
    identificador =0
    vetor = [0]*5
    vetor2 = [(0,0)]*3
    for cont0 in range(3):
        for cont in range(5):
            vetor = [0]*5
            vetor[cont] = random.randint(1,100)
        vetor2[cont0] = (cont0+1,vetor)
    with multiprocessing.Pool(processes=num_threads) as pool:
        pool.starmap(operacao,vetor2)

if(__name__=="__main__"):
    main()






