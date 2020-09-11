def bubble_sort(q,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if q[j] > q[j+1]:
                q[j], q[j+1] = q[j+1], q[j]
                # for i in q:
                #     print(i, end=' ')
                # print("\n")
        


n = int(input())
q = list(map(int, input().split()))
bubble_sort(q,n)
for i in q:
    print(i, end=' ')