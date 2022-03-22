def fibo(num):
    fibo_list=[]
    cont = 0
    pri = 0
    sec = 1
    temp = 0

    while cont <= num:
        fibo_list.append(pri)
        temp = pri + sec
        pri = sec
        sec = temp
        cont += 1

    return fibo_list

print(fibo(50))