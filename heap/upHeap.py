# [ 문제 2 ] 상향식 힙 생성
# 다음 프로그램을 작성해 상향식 힙 생성을 구현하라.
# 입출력 형식:
# 1) main 함수는 아래 형식의 표준입력으로 키들을 한꺼번에 입력받는다.
#     입력 : 첫 번째 라인 : 키 개수
#     두 번째 라인 : 키들

# 2) main 함수는 아래 형식의 표준출력으로 생성된 힙을 인쇄한다.
#     출력 : 첫 번째 라인 : 힙 내용 (레벨 순서)

# 입력 예시 1 
# 3 ↦ 키 개수
# 209 400 77 ↦ 키들

# 출력 예시 1
# □400 209 77 ↦ 힙 인쇄

class Heap2:
    def __init__(self):
        self.list = [0, None]

    def downHeap(self, i, n):
        bigger = i
        left = 2*i
        right = 2*i+1
        #print("bigger = %d left = %d right = %d" %(bigger, left, right))
        if left <= n and self.list[left] > self.list[bigger]:
            bigger = left
        if right <= n and self.list[right] > self.list[bigger]:
            bigger = right
            #print("bogger = %d" %(self.list[bigger]))
        if bigger != i:
            self.list[i], self.list[bigger] = self.list[bigger], self.list[i]
            self.downHeap(bigger, n)

    def insert(self, keys, n):
        for i in keys:
            if self.list[1] == None:
                self.list[1] = int(i)
            else: 
                self.list.append(int(i))
        
        for i in range(n//2, 0, -1):
            self.downHeap(i, n)

    def print(self):
        for i in self.list[1:]:
            print(i, end=" ")
        print()
  

h = Heap2()
n = int(input())
keys = input().split()
h.insert(keys, n)
h.print()