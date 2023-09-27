import time

def minimum_coins(num):
    coins=[10,5,1]
    output=0
    for i in coins:
        if num >= i:
            output += int(num/i)
            num = num % i
    return output


if __name__ == '__main__':
    num=int(input("Enter a number="))
    start = time.time()
    print(minimum_coins(num))
    end = time.time()
    print("Time taken=" + str(end - start))
