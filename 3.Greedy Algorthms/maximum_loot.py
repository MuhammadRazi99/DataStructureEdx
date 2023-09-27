from audioop import reverse
import time
def get_third(element):
    return element[2]

def maximum_loot(n,W,qlist):
    for i in range(n):
        qlist[i].append(round(qlist[i][0]/qlist[i][1],4))
    qlist.sort(key=get_third,reverse=True)
    loot=0.0
    while(W!=0):
        for i in range(n):
            if W>qlist[i][1]:
                W -=qlist[i][1]
                loot += qlist[i][0]
            elif W<=qlist[i][1]:
                loot += round(qlist[i][2]*W,4)
                return loot    
    return loot

if __name__ == '__main__':
    n, W=map(int,input().split())
    qlist=[]
    for i  in range(n):
        v,w=map(int,input().split())
        qlist.append([v,w])
    start = time.time()
    print(maximum_loot(n,W,qlist))
    end = time.time()
    print("Time taken=" + str(end - start))
