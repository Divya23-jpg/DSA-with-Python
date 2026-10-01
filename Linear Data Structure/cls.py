
#  Binary search

# s = [1, 2, 3, 4, 5, 10]
# target = 4
# l = 0
# r = len(s) - 1

# while l <= r:
#     mid = (l + r) // 2
#     if target == s[mid]:
#         print('Target Found at:', mid)
#         break
#     elif target < s[mid]:
#         r = mid - 1
#     else:
#         l = mid + 1




# ! Recursion 

# 
def fun(n):
    if n==0:
        return 
    fun(n-1)
    print(n,end=" ")

# fun(10)


#! find sum 1 to n
def sum_n(n):
    if n==0:
        return 0
    
    return n + sum_n(n-1)



# print(sum_n(10))

# !find multiply 1 to n
def mul_n(n):
    if n==1:
        return 1
    
    return n * mul_n(n-1)



# print(mul_n(3))

# !find fibonacci
def fibo(n):
    if n<=1:
        return n
    
    return fibo(n-1)+fibo(n-2)



# print(fibo(1))

#! Sum of the digits

def sum_digit(n):
    if n==0:
        return 0

    return (n%10) + sum_digit(n//10)

# print(sum_digit(1234))


# ! print array By Recursion

def array_p(i,arr,n):
    if i==n:
        return 
    
    array_p(i+1,arr,n)
    
    print(arr[i],end=" ")

# array_p(0,[1,2,3,4],4)



def array_sort(i,arr,n):
    if i==n-1:
        return True

    if arr[i]>arr[i+1]:
        return False

    return array_sort(i+1,arr,n)

print(array_sort(0,[1,2,3,4],4))

print(array_sort(0,[9,1,3,4],4))



