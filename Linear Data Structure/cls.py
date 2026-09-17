
#  Binary search

s = [1, 2, 3, 4, 5, 10]
target = 4
l = 0
r = len(s) - 1

while l <= r:
    mid = (l + r) // 2
    if target == s[mid]:
        print('Target Found at:', mid)
        break
    elif target < s[mid]:
        r = mid - 1
    else:
        l = mid + 1
