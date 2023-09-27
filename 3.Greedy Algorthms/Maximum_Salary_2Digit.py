import time

def maximum_Salary(n,numberList):
    output=''
    while numberList != []:
        maxDigit='00'
        for num in numberList:
            if int(maxDigit[0])<int(num[0]):
                maxDigit=num
            elif int(maxDigit[0])==int(num[0]):
                if len(maxDigit)<len(num) and num[1]>maxDigit[0]:
                    maxDigit=num
                elif len(maxDigit)>len(num) and num[0]>maxDigit[1]:
                    maxDigit=num
                elif len(maxDigit)==len(num) and len(num)==2 and num[1]>maxDigit[1]:
                    maxDigit=num
        output += str(maxDigit)
        numberList.remove(maxDigit)
    return output

if __name__ == '__main__':
    n=int(input("Enter a number="))
    numberList=list(input().split(" "))
    start = time.time()
    print(maximum_Salary(n,numberList))
    end = time.time()
    print("Time taken=" + str(end - start))
