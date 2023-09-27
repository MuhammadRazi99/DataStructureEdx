import time


def function(num):
    fib = [1, 1]
    for i in range(2, num):
        fib.append(int((fib[i - 2] + fib[i - 1]) % 10))
    print(fib[-1])


if __name__ == '__main__':
    start = time.time()
    num = int(input("Enter a number="))
    function(num)
    end = time.time()
    print("Time taken=" + str(end - start))
