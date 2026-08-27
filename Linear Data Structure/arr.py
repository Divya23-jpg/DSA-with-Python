# arr=[2,4,3,1]
# ans=[]
# for i in reversed(arr):
#     ans.append(i)

# print(arr==sorted(ans))


 


# def algotutor(n):
#     for i in range(n):
#         print("Divya")


# algotutor(3)




# class Solution:
#     @staticmethod
#     def singleNumber(nums: list[int]) -> int:
#         result = 0
        
#         # Iterate through all 32 possible bit positions
#         for i in range(32):
#             bit_sum = 0
#             bit_mask = 1 << i
#             for num in nums:
#                 if num & bit_mask:
#                     bit_sum += 1
            
#             if bit_sum % 3 != 0:
#                 if i == 31: 
#                     result -= bit_mask
#                 else:
#                     result |= bit_mask
                    
#         return result


#! 1.Find 2nd and 3rd maximum in array/list without sorting the list?
ans=[3,51,12,7,1]
length=len(ans)
max_1=0
max_2=0

for i in ans:
    if i>max_1:
        max_1=i

    if max_1<max_2:
        max_2=max_1
# print(max_1)
# print(max_2)


#!2.Try to sort the list without using in build function

num=[3,51,12,7,1]
n=len(num)
for i in range(n):
    # For descendingb order we have to n-i-1
    for j in range(0,n-i-1):
        if num[j]>num[j+1]:
            num[j],num[j+1]=num[j+1],num[j]

# print(num)

#! Try to sort in descending order without using in build function
nums=[3,51,12,7,1]
s=len(nums)
for i in range(s):
    # For descendingb order we have to j+i-1
    for j in range(0,j+i-1):
        if nums[j]<nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]

# print(nums)
#!Needs to check all the Characters are in Upper case?lower Case
t="Divya Kumawat"
upper_count=0
lower_count=0
space=0
for i in t:
    if i.isspace():
        continue
    elif i.isupper():
        upper_count+=1
    else:
        lower_count+=1


# print("Number of Upper Count is :",upper_count)
# print("Number of Lower Count is :",lower_count)

# ! Needs to check the string contains all value from 0-9 in any order in the string


# s = "23344556677889900"
# n = []
# flag=0
# # Collect unique characters
# for ch in s:
#     if ch not in n:
#         n.append(ch)

# # Check digits 0–9
# for i in range(0, 10):
#     if str(i) not  in n:   
#         flag=0
#         break

# if flag==1:
#     print(True)
# else:
#     print(False)



# ! Two sum leetcode 

# Brute Force 
def twosum(nums,target):
    n=len(nums)
    for i in range(0,n):
        for  j in range(i+1,n):
            s=nums[i]+nums[j]
            if s==target:
                return [i,j]

# nums=[2,7,11,15]
# target=9

# print(twosum(nums,target))


# ! Single Number

# return single number which is present in array 
# Input arr=[4,1,2,1,2]
# output 4

    # ! 1st way
    # ! usimg in-Built function
def single(arr):
    for i in range(0,len(arr)):
        if arr.count(arr[i]==1):
            return arr[i]

# arr=[4,1,2,1,2]
# print(single(arr))


    # ! usimg two loops
def single(arr):
    count=1
    for i in arr:
        count=0
        for j in arr:
            if i==j:
                count+=1

        if count==1:
            return i

# arr=[4,1,2,1,2]
# print(single(arr))




# ! 1929. Concatenation of an array

def array_concat(num):
    ans=[]
    n=len(nums)
    for i in range(2):
        for i in nums:
            ans.append(i)
    return ans


def array_concat(num):
    return num*2


    
nums=[1,2,3]
print(array_concat(nums))



# ! 268 missing number

# ! 1st way
def missing_number(nums):
    n=len(nums)
    for i in range(0,n+1):
        if i not in nums:
            return i
nums=[3,0,1]
print(missing_number(nums))



# ! 2nd way
def missing_number(nums):
    n=len(nums)
    s=sum(nums)
    total=n*(n+1)//2
    return total-s

# nums=[3,0,1]
# print(missing_number(nums))



#! 1550 Three consicutive Odds

# ! 1st way
def odd_consecutive(arr):
    count=0
    for i in arr:
        if i%2!=0:
            count+=1
            if count==3:
                return True
        else:
            count=0

    return False


# arr=[2,6,4,1]
# print(odd_consecutive(arr))

# ! 2nd way
def odd_consecutive(arr):
    count=0
    n=len(nums)
    for i in range(0,n-2):
        if arr[i]%2 != 0 and arr[i+1]%2 != 0 and arr[i+2]%2 != 0:
            return True
    
    return False


arr=[2,6,4,1]
print(odd_consecutive(arr))



#! Matrix

mat=[
    [1,2,3],
    [3,4,5],
    [7,8,9]
]


# row=len(mat)
# col=len(mat[0])
# for i in range(row):
#     for j in range(col):
#         print(mat[i][j],end=" ")

# print('\n')

# ! Row To Column

def rows_to_col(mat):
    
    row=len(mat)
    col=len(mat[0])
    ans=[]
    for j in range(col):
        cur=[]
        for i in range(row):
            cur.append(mat[i][j])

        ans.append(cur)

    return ans


mat=[
    [1,2,3],
    [3,4,5],
    [7,8,9]
]

print(rows_to_col(mat))


