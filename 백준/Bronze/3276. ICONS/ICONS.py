N = int(input())
lst = [i for i in range(1, N+1)]
arr = []
for i in range(len(lst)):
    for j in range(i+1):
        if lst[i] * lst[j] >= N:
            arr.append([lst[i],lst[j]])
print(* arr[0])