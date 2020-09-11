
def merge_sort(q):
    if len(q) <= 1:
        return q       
    M = len(q)//2
    A = merge_sort(q[:M])
    B = merge_sort(q[M:])

    return merge(A,B)

def merge(A,B):
    C = []
    i = j = 0

    while len(A) > i and len(B) > j:
        if A[i] > B[j]:
            C.append(B[j])
            j += 1
        else:
            C.append(A[i])
            i += 1
    
    while len(A) > i and len(B) <= j:
        C.append(A[i])
        i += 1
    
    while len(B) > j and len(A) <= i:
        C.append(B[j])
        j += 1
    
    return C  


n = int(input())
q = list(map(int, input().split()))
C = merge_sort(q)
for i in C:
    print(i, end=' ')