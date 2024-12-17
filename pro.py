from collections import Counter
n = int(input())
l1 = [input().strip() for item in range(n)]
res = Counter(l1)
print(res)
print(len(res))
print(*res.values())


d1 = {'a' : 1,'b' : 2,'c' : 3}
d2 = {'a' : 2,'d' : 3 ,'c' : 4}
counter1 = Counter(d1)
counter2 = Counter(d2)
res = counter1 + counter2
print(res)
