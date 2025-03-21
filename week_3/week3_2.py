import random

arr = []

count = 0
while count != 6:
    temp = random.randint(1, 45)
    if temp not in arr:
        arr.append(temp)
        count += 1

arr.sort()

str1 = '당청번호: '
str2 = '보너스 번호: '

arr.insert(0, str1)
arr.insert(7, str2)

while count != 7:
    temp = random.randint(1, 45)
    if temp not in arr:
        arr.append(temp)
        count += 1
        
for i in range(9):
    print(arr[i], end = ' ')