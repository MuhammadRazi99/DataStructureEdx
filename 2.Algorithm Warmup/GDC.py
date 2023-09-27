import time


def function(a, b):
        b = b % a
        if b==0:
            return a
        else:
            return function(b, a)



if __name__ == '__main__':
    start = time.time()
    a, b = map(int, input("Enter two number first smaller=").split())
    print(function(a, b))
    end = time.time()
    print("Time taken=" + str(end - start))
