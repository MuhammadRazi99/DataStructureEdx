import time


def function(a, num):
    fib = [1, 1]
    for i in range(2, num):
        fib.append(int((fib[i - 2] + fib[i - 1]) % 10))
    print(sum(fib[a-1: num])%10)


if __name__ == '__main__':
    a,b = map(int,input("Enter a range=").split())
    start = time.time()
    function(a,b)
    end = time.time()
    print("Time taken=" + str(end - start))
