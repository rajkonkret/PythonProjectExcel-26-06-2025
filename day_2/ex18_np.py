import time
import numpy as np

# pip install numpy
lista = list(range(15_000_000))
lista_np = np.arange(15_000_000, dtype=np.int64)


def sum_python():
    total = 0
    for i in lista:
        total += i
    print("Sum is:", total)


def sum_np():
    total = np.sum(lista_np)
    print("Sum is:", total)


start_d = time.time()
sum_python()
end_d = time.time()
print(end_d - start_d)
# Sum is: 112499992500000
# 0.4199714660644531

start_d = time.time()
sum_np()
end_d = time.time()
print(end_d - start_d)
# Sum is: 112499992500000
# 0.009052515029907227
