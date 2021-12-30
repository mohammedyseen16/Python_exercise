arr = [1,2,3,44,5,566,566, 566]
arr = list(set(arr))
arr.remove(max(arr))
print(max(arr))
