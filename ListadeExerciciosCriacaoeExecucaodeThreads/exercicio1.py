import multiprocessing
import time

def operacao(valor):
    time.sleep(0.5)
    print("Thread #",valor)

def main():
    cont: int =1
    num_threads=5
    vetor:int = [0]*5
    for cont in range(5):
        vetor[cont] = cont
    with multiprocessing.Pool(processes=num_threads) as conjunto:
        conjunto.map(operacao,vetor)

if(__name__=="__main__"):
    main()





