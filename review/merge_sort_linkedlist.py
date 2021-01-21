def merge(q, start, mid, end):
    temp = mid+1

    # left 배열의 마지막 요소가 right 배열의 첫번째 요소보다 작은 경우 
    if q[mid] <= q[temp]:
        return

    while start <= mid and temp <= end:
        if q[start] <= q[temp]:
            temp += 1
        else:
            temp_val = q[temp]
            while temp != start:
                q[temp] = q[temp-1]
                temp -= 1
            
            q[start] = temp_val

            start += 1
            mid += 1
            temp += 1


def mergeSort(q, l, r):
    if l < r:
        mid = l + (r -1) / 2
        mergeSort(q,l,mid)
        mergeSort(q,mid,r)
        merge(q,l,mid,r)

    else: return

def printQ(q):
    for i in q:
        print(i, end=' ')
    print('')




n = int(input())
q = [int(i) for i in input().split()]
q = mergeSort(q, 0, n)
printQ(q)