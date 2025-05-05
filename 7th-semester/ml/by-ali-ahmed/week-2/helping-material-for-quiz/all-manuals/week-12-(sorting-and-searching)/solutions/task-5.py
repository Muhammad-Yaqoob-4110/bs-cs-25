def b_s(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return b_s(arr, target, mid + 1, high)
    else:
        return b_s(arr, target, low, mid - 1)

def sort_list(kl):
    sl = []
    b = 0
    for j in range(len(kl)):
        s = kl[j]
        a = 0
        for i in range(len(sl)):
            if s > sl[i]:
                a += 1
            else:
                break
        b += a
        sl.insert(a, s)
    return sl

lst = eval(input("Enter the list:"))
e = int(input("Entre the number you are searching for:"))
so_ls = sort_list(lst)
print("Sorted List:", so_ls)
index = b_s(so_ls,e, 0, len(so_ls) - 1)
if index != -1:
    print("Element",e, "found at index", index+1)
else:
    print("The required number is not in the list.")
