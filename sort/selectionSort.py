def selection_sort(q,n):
    for i in range(0, n-1):
        # 리스트의 모든 원소 n-1개에 대해 (마지막 원소 제외)
        min = i
        for j in range(i+1, n):
            # 해당 원소 다음 원소부터 리스트 끝까지 해당 원소와 비교 
            if q[j] < q[min]:
                # min이 해당 원소를 임시로 저장해둔 변수인데 해당 원소가 리스트 순회하면서 자기보다 작은 원소를 찾으면
                min = j
                # 그 원소가 min이 된다. 
        q[i], q[min] = q[min], q[i]
        # 해당 원소와 가장 작았던 원소 min 의 위치를 swap!
        # 이 과정을 n-1번 수행하면 오름차순으로 정렬됨.  

n = int(input())

q = list(map(int, input().split()))

selection_sort(q,n)

for i in q:
    print(i, end=' ')
