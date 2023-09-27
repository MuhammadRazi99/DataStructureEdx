import time
def maximum_prizes(n):
    sumList=[]
    for i in range(1,n+1):
        if n-i>i:
            sumList.append(i)
            n -= i
        elif n==i:
            sumList.append(i)             
    print(len(sumList))
    print(sumList)

if __name__ == '__main__':
    n=int(input("Enter a number="))
    start = time.time()
    maximum_prizes(n)
    end = time.time()
    print("Time taken=" + str(end - start))
