import time
import threading

A = [1, 11, 121, 111, 112]
start = time.time()
summ = 0

def summa(i, A):
    with lock:
        global summ
        summ += sum(A)

def start_threads(N):
    count = min(N, len(A))
    threads = [
        threading.Thread(target = summa, args=(i, A[i*count: (i+1)*count]))
        for i in range(count)
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

lock = threading.Lock()
N = 7
start_threads(N)
print(summ)
print(time.time() - start)