import time


def function():
    l = list(map(int, input("Enter numbers=").split(" ")))
    return sum(l)


if __name__ == '__main__':
    start = time.time()
    print(function())
    end = time.time()
    print("Time taken=" + str(end - start))
