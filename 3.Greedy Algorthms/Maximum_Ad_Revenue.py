import time

def maximum_Ad_Revenue(n,alist,blist):
    alist.sort()
    blist.sort()
    value=0
    for i in range(n):
        value += alist[i]*blist[i]
    return value

if __name__ == '__main__':
    n=int(input())
    alist=list(map(int,input().split()))
    blist=list(map(int,input().split()))
    start = time.time()
    print(maximum_Ad_Revenue(n,alist,blist))
    end = time.time()
    print("Time taken=" + str(end - start))
