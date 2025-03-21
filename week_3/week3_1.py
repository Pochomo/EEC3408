import random

arr = []
for i in range(10):
    arr.append(random.randint(1, 10))
for i in range(10):
    print(arr[i], end = ' ') 
print()

n = int(input())

print("찾는 원소가 몇 번째 인덱스에 있는지: ", (arr.index(n)))
print("찾는 정수의 갯수 : ", arr.count(n))

for _ in range(arr.count(n)):
    arr.remove(n)

for i in range(len(arr)):
    print(arr[i], end = ' ') 