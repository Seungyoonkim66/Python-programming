def r_findElement(dic, K, l, r):
    if l > r:
        max_index = 0
        for i in range(len(dic)):
            if dic[i] > K:
                max_index = i-1
                return max_index
            elif dic[0] > K:
                return -1
            elif dic[len(dic)-1] < K:
                return len(dic)-1

    mid = (l+r)//2
    if K == dic[mid]:
        return mid
    elif K < dic[mid]:
        return r_findElement(dic,K,l,mid-1)
    elif K > dic[mid]:
        return r_findElement(dic,K,mid+1,r)

N, K = input().split()
N = int(N)
K = int(K)
data = list(input().split())
dic = []
for d in data:
    dic.append(int(d))

res = r_findElement(dic, K, 0, N-1)
print(res)
