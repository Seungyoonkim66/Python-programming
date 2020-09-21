def insertion_sort(q,n):
    comparison_count = 0
    for i in range(1,n):
        key = i
        for j in range(0,i):
            if q[key] < q[j]:
                t = q[j]
                q[j] = q[key]
                q[key] = t
                comparison_count += 1
        # print(i+1, "번째",q)
    return comparison_count


print("**********Selection Sort**********")

print("\n1. unordered list")
UL = [7,2,3,1,8,4,9,5,6,0]
print(UL)
UL_res = insertion_sort(UL,len(UL))
print(UL)
print("the number of swapping : %d " %(UL_res))
print("")

print("2. ordered list")
OL = [0,1,2,3,4,5,6,7,8,9]
print(OL)
OL_res = insertion_sort(OL,len(OL))
print(OL)
print("the number of swapping : %d " %(OL_res))
print("")

print("3. reversed ordered list")
ROL = [9,8,7,6,5,4,3,2,1,0]
print(ROL)
ROL_res = insertion_sort(ROL,len(ROL))
print(ROL)
print("the number of swapping : %d " %(ROL_res))
print("")
