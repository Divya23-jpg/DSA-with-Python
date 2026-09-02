arr=[2,4,3,1]
ans=[]
for i in reversed(arr):
    ans.append(i)

# print(arr==sorted(ans))


 


def algotutor(n):
    for i in range(n):
        print("Divya")


# algotutor(3)




class Solution:
    @staticmethod
    def singleNumber(nums: list[int]) -> int:
        result = 0
        
        # Iterate through all 32 possible bit positions
        for i in range(32):
            bit_sum = 0
            bit_mask = 1 << i
            for num in nums:
                if num & bit_mask:
                    bit_sum += 1
            
            if bit_sum % 3 != 0:
                if i == 31: 
                    result -= bit_mask
                else:
                    result |= bit_mask
                    
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
# print(array_concat(nums))



# ! 268 missing number

# ! 1st way
def missing_number(nums):
    n=len(nums)
    for i in range(0,n+1):
        if i not in nums:
            return i
nums=[3,0,1]
# print(missing_number(nums))



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
# print(odd_consecutive(arr))



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

# print(rows_to_col(mat))


# ! leetcode 1089  Duplicates Zero

arr = [1,0,2,3,0,4,5]
n=len(arr)
i=0
while i<n:
    if arr[i]==0:
        arr.pop(n-1)

        arr.insert(i,0)
   
        i+=1

    i+=1

# print("Final arr",arr)


# !Leetcode 912 Sort array [we use insertion sort]

nums=[5,2,3,1]
n=len(nums)
for i in range(n):
    min_index=i

    for j in range(i+1,n):
        if nums[j]<nums[min_index]:
            min_index=j

    nums[i],nums[min_index]=nums[min_index],nums[i]

# print(nums)

#! leetcode 485. Max Consecutive Ones

nums = [1,1,0,1,1,1]
count=0
ans=0
for i in nums:
    if i==1:
        count+=1
        ans=max(count,ans)
    else:
        count=0

# print(ans)


# ! Leetcode 1078. Occurrences After Bigram

text = "alice is a good girl she is a good student"
first = "a"
second = "good"

arr=text.split(" ")
n=len(arr)
ans=[]
for i in range(0,n-2):
    if arr[i]==first and arr[i+1]==second:
        ans.append(arr[i+2])

# print(ans)


# ! Leetcode 1446. Consecutive Characters
s = "abbcccddddeeeeedcba"
count=1
ans=1
n=len(s)
for i in range(n-1):
    if s[i]==s[i+1]:
        count+=1
    else:
        count=1
    ans=max(ans,count)

# print(ans)

#! 2937 Make Three string equal









# !Leetcode 344. Revers the Array Without Built in Function

s=['h','e','l','l','o']
n=len(s)
l=0
r=n-1
while(l<r):
    s[l],s[r]=s[r],s[l]
    l+=1
    r-=1

# print(s)


# ! Leetcode 189 Rotate Array
    # !1st Way
nums=[1,2,3,4,5,6,7]
k=3
# n=len(nums)
# for i in range(k):
#     val=nums.pop(n-1)
#     nums.insert(0,val)

# print(nums)

    # !2nd Way

# def reverse(start,end):
#     while start<end:
#         nums[start],nums[end]=nums[start],nums[end]
#         start+=1
#         end-=1


# N=len(nums)
# k=k%N
# reverse(0,N-1)
# reverse(0,k-1)
# reverse(k,N-1)

# print(nums)

    #! 3rd way

N=len(nums)
k=k%N
arr=nums[N-k:N]+nums[0:N-k]
for i in range(N):
    nums[i]=arr[i]

# print(nums)


# ! Leetcode 852

arr=[0,1,0]
n=len(arr)
for i in range(n-1):
    if arr[i]<arr[i+1]:
        index=i+1
# print(index)


# ! 2nd way

arr=[0,1,0]
n=len(arr)
count=0
for i in range(n-1):
    if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
        count+=1

# print(count)

# ! 2124
s = "aaabbb"
lastA=-1
n=len(s)
for i in range(0,n):
    if s[i]=='a':
        lastA=i
firstB=n
for i in range(0,n):
    if s[i]=='b':
        firstB=i
        break
# print(lastA < firstB)
        
# print(s.rfind("a")<s.find("b") or s.find("b")==-1)



# ! 771
jewels = "aA"
stones = "aAAbbbb"
count=0
for i in stones:
    if i in jewels:
        count+=1
      
# print(count)


# ! 38. Count and Say
n = 4
cur="1"
for i in range(n-1):
    next=""
    count=1
    N=len(cur)
    for i in range(1,N):
        if cur[i]==cur[i-1]:
            count+=1

        else:
            next+=str(count)+str(cur[i-1])
            count=1


    next+=str(count)+str(cur[N-1])
    cur=next

# print(cur)





# ! 169 Majority Element

# ! 1st way bruteforce approach
"""
take a element one by one from the array and count the frequency in the whole array
"""

# ? Brute force 

# ! Complexity will be : O(N*N)
# def majority_bruteForce(nums):
#     n=len(nums)
#     for i in range(n):
#         freq=0
#         for j in range(n):
#             if nums[i]==nums[j]:
#                 freq+=1

#         if freq>n//2:
#             return nums[i]

# print(majority_bruteForce(nums))

# ? Optimized
# ! Complexity will be : O(nlong)
def majority_optimized(nums):
    nums.sort()
    freq=1
    ans=nums[0]
    n=len(nums)
    for i in range(n):
        if nums[i]==nums[i-1]:
            freq+=1

        else:
            freq=1
            ans=nums[i]

    
        if freq>n//2:
            return ans

# nums=[2,2,1,1,1,2,2]
# print(majority_optimized(nums))

# ! Mrroe's Voting algo
def majority_more_optimized(nums):
    count=0
    ans=0
    n=len(nums)
    for i in range(n):
        if count==0:
            ans=nums[i]
            count=1

        elif ans==nums[i]:
            count+=1

        else:
            count-=1

    return ans

nums=[2,2,1,1,1,2,2]
# print(majority_more_optimized(nums))






# ! 229 Majority Element n//3


nums=[5,0,3,7,1,0,100]
n=len(nums)
res=[]
zeroes=nums.count(0)
for i in range(n):
    if nums[i]!=0:
        res.append(nums[i])



# for _ in range(zeroes):
#     res.append(0)

res.extend([0] * zeroes)
# print(res)




from collections import Counter

def top_k_events(events, k):
    # Count frequency of each event ID
    freq = Counter(events)
    
    # Get k most common event IDs
    result = [event for event, _ in freq.most_common(k)]

    return result

# Example usage
# print(top_k_events([1,1,1,2,2,3], 2)) 



# ! 11.Container with most water

h=[1,8,6,2,5,4,8,3,7]

l=0
r=len(h)-1
max_water=0
while l<r:
    width=r-l
    height=min(h[l],h[r])
    area=width*height

    max_water=max(max_water,area)

    if h[l]<h[r]:
        l+=1

    else:
        r-=1

# print(max_water)





# Leetcode 53.Subarray sum using kadans algorithm
arr=[-2,1,-3,4,-1,2,1,-5,4]

current=0
max_sum=nums[0]
for i in nums:
    current+=i
    max_sum=max(max_sum,current)
    if current<0:
        current=0

# print(max_sum)

# def encoded(arr):
#     l=""
#     n=len(arr)
#     for i in arr:
#         l+=str(len(i))
#         l+="/:"
#         l+=i
#     return l


# arr=["Hello", "World"]
# print(encoded(arr))


def decode(string):
    t=""
    for i in string:
        if i.isalpha():
            t+=i

    return t

            



# string="5/:Hello5/:World"
# print(decode(string))



#! Leetcode 5. Longest Palindromic Substring

"""We know to generate all substring . we just check each substring is plaindrome or not
and return the longest palindrome  substring"""



def longestPalindrome(s): 
    """
        We know how to generate all substring
        We just check each substring is panlindrome or not
        and return longest (panlindrome) substring
        """
    N = len(s)
    def isPanlindrome(start, end):
        flag = True
        while start < end:
            if s[start] != s[end]:
                flag = False
                break
            start += 1
            end -= 1
        return flag

    ans = ""
    for i in range(0, N):
        for j in range(i, N):
            if len(ans) < (j-i+1) and isPanlindrome(i,j):
                ans = s[i:j+1]
    return ans

s = "babad"
# print(longestPalindrome(s))



# ! 413. Arithmetic Slices

"""
Generate sub arrays then check each subarray is valid or not

"""
def numberOfArithmeticSlices(nums):
    N = len(nums)
    """
        We generate all subarrays, and then we will check
        each subarray is valid or not
    """
    count = 0
    def isValid(start, end):
        flag = True
        check = nums[start+1] - nums[start]
        for i in range(start+1, end+1):
            if nums[i] - nums[i-1] != check:
                flag = False
                break
        return flag

    for i in range(0, N):
    #i = 0, j = 2 --> [0,1,2]
        for j in range(i+2,N):
            if isValid(i, j):
                count += 1
    return count


nums=[1,2,3,4]
print(numberOfArithmeticSlices(nums))
# ! 1470. Shuffle the Array


def shuffle(nums,n):
    x=nums[0:n]
    y=nums[n:2*n]
    ans=[]
    for i in range(0,n):
        ans.append(x[i])
        ans.append(y[i])
    return ans


nums = [2,5,1,3,4,7]
n = 3

# print(shuffle(nums,n))


# ! 2022. Convert 1D Array Into 2D Array


def construct2DArray(original,n,m):
    ans = []
    N = len(original)
    if n*m != N:
        return ans
            
    index = 0
    for i in range(0,m):
        cur = []
        for j in range(0, n):
            cur.append(original[index])
            index += 1
        ans.append(cur)
    return ans

original = [1,2,3,4]
m = 2
n = 2

# print(construct2DArray(original,n,m))



# ! 1051. Height Checker
def heightChecker(heights):
    n=len(heights)
    expected=heights[0:n]
    expected.sort()
    count=0
    for i in range(0,n):
        if expected[i]!=heights[i]:
            count+=1

    return count

heights = [1,1,4,2,1,3]
# print(heightChecker(heights))