import time


def function(l):
    num = max(l)
    l.remove(num)
    num *= max(l)
    return num


if __name__ == '__main__':
    l = list(map(int, input().split()))
    start = time.time()
    print(function(l))
    end = time.time()
    print("Time taken=" + str(end - start))
