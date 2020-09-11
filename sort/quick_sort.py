def quick_sort(q):
    if len(q) <= 1:
        return q
    # 중간값을 pivot으로 선정
    pivot = q[len(q)//2]
    left, mid, right = [], [], []
    for i in q:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            mid.append(i)
    return quick_sort(left) + mid + quick_sort(right)


n = int(input())
q = list(map(int, input().split()))
res = quick_sort(q)
for i in res:
    print(i, end=' ')