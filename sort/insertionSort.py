def insertion_sort(q,n):
    for i in range(1,n):
        key = i
        for j in range(0,i):
            if q[key] < q[j]:
                t = q[j]
                q[j] = q[key]
                q[key] = t
        


n = int(input())
q = list(map(int, input().split()))
insertion_sort(q,n)
for i in q:
    print(i, end=' ')