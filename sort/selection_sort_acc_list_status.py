

def selection_sort(q,n):
    comparison_count = 0
    for i in range(0, n-1):
        # 리스트의 모든 원소 n-1개에 대해 (마지막 원소 제외)
        min = i
        for j in range(i+1, n):
            # 해당 원소 다음 원소부터 리스트 끝까지 해당 원소와 비교 
            if q[j] < q[min]:
                # min이 해당 원소를 임시로 저장해둔 변수인데 해당 원소가 리스트 순회하면서 자기보다 작은 원소를 찾으면
                min = j
                comparison_count += 1
                # 그 원소가 min이 된다. 
        q[i], q[min] = q[min], q[i]
        # print(i+1, "번째",q)
        # 해당 원소와 가장 작았던 원소 min 의 위치를 swap!
        # 이 과정을 n-1번 수행하면 오름차순으로 정렬됨.
    return comparison_count  


print("**********Selection Sort**********")

print("\n1. unordered list")
UL = [7,2,3,1,8,4,9,5,6,0]
print("처음상태",UL)
UL_res = selection_sort(UL,len(UL))
print("정렬상태",UL)
print("the number of comparsions : %d " %(UL_res))
print("")

print("2. ordered list")
OL = [0,1,2,3,4,5,6,7,8,9]
print(OL)
OL_res = selection_sort(OL,len(OL))
print(OL)
print("the number of comparsions : %d " %(OL_res))
print("")

print("3. reversed ordered list")
ROL = [9,8,7,6,5,4,3,2,1,0]
print(ROL)
ROL_res = selection_sort(ROL,len(ROL))
print(ROL)
print("the number of comparsions : %d " %(ROL_res))
print("")


