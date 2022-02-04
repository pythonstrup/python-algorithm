import math

n = 1000
array = [True for i in range(n+1)]

# 시간복잡도 O(N log log N)
# 대신 메모리가 많이 필요함
for i in range(2, int(math.sqrt(n))+1):
    if array[i] == True:
        j = 2
        while i*j <= n:
            array[i*j] = False
            j += 1

for i in range(2, n+1):
    if array[i]:
        print(i, end=" ")