import time


def functionNaive(a, b):
        fib = [1, 1]
        for i in range(2, a):
            fib.append(fib[i-1]+fib[i-2])
        return fib[-1] % b


if __name__ == '__main__':
    start = time.time()
    a, b = map(int, input("Enter two number first smaller=").split())
    print(functionNaive(a, b))
    end = time.time()
    print("Time taken=" + str(end - start))
