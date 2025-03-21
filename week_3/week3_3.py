def cal_fibo(n):
    for i in range(n+1):
        if i == 0 or i == 1:
            arr[i] = 1
        elif i == 2:
            arr[i] = 2
        else:
            arr[i] = arr[i - 1] + arr[i - 2]
    return arr[n]

print('양수 입력(3 이상): ', end = ' ')
n = int(input())
arr = [0] * (n + 1)
cal_fibo(n)
for i in range(n):
    print(arr[i], end = ' ')
