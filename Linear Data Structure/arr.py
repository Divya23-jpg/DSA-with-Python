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
                return sorted([nums[i],nums[j]])

def two_sum_optimized(nums,target):
    seen={}
    for i ,num in enumerate(nums):
        com=target-num
        if com in seen:
            return [seen[com],i]
        seen[num]=i

            



# nums=[2,7,11,15]
nums=[7,-3,2,7,5,-3,10,0,2,8,5,-8,3,12,-3]
target=9

# print(twosum(nums,target))


# ! Twu sum but differenet que


def Two_sum_transaction(nums,target):
    pair=set()
    seen=set()


    for i in nums:
        com=target-i
        if com in seen:
       
            pair.add(tuple(sorted([i, com])))
            

        seen.add(i)


    return [list(p) for p in sorted(pair)]


nums=[7,-3,2,7,5,-3,10,0,2,8,5,-8,3,12,-3]
target=9
print(Two_sum_transaction(nums,target))






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


# ! 2315. Count Asterisks
def countAsterisks(s):
    """
        l|*e*et|c**o|*de|
        l,*e*et,c**o,*de
        *e*et,*de
        l,c**o ---> 2

    """
    def countAstrics(ss):
        return ss.count("*")

    arr=s.split("|")

    n=len(arr)
    count=0
    for i in range(0,n,2):
        count+=countAstrics(arr[i])

    return count


s = "l|*e*et|c**o|*de|"
print(countAsterisks(s))


# ! 1242. Valid Anagram



# ! 1796. Second Largest Digit in a String
def secondHighest(s):
    unique=set()
    for i in s:
        if i.isdigit():
            unique.add(int(i))

    maxV=-1
    secMax=-1
    for i in unique:
        if i>maxV:
            secMax=maxV
            maxV=i

        elif i>secMax:
            secMax=i

                
    return secMax
        
# !2000. Reverse Prefix of Word

# def reversePrefix(word, ch):
#     word=list(word)

#     def reverse(start,end):
#         while start<end:
#         word[start],word[end]=word[end],word[start]
#         start+=1
#         end-=1

#     index=-1
#     n=len(word)
#     for i in range(0,n):
#         if word[i]==ch:
#             index=i
#             break

#     reverse(0,index)
#     return "".join(word)

# ! 6. Zigzag Conversion

def convert(numRows):
    if numRows == 1:
        return s
    arr = []
    for i in range(numRows):
        arr.append([])


    index,dir = 0, 1
    for v in s:
        arr[index].append(v)
        index += dir
        if index == numRows:
            dir = -1
            index = numRows - 2
        elif index == -1:
            dir = 1
            index = 1

    ans = ""
    for v in arr:
        ans += "".join(v)
    return ans

# ! 118. Pascal's Triangle
def generate(numRows):
    arr=[]
    for i in range(0,numRows):
        curr=[]
        for j in range(0,i+1): 
            if j==0 or j==i:
                curr.append(1)
            else:
                curr.append(arr[i-1][j-1] + arr[i-1][j])

        arr.append(curr)

    return arr


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data): # added a new node at the beginning of the list
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def append(self, data): # added a new node at the end of the list
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node



    def delete_value(self, value):
        if not self.head:
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.data == value:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
        print("Value not found in the list.")

    def display(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next
        # print(" -> ".join(map(str, elements)))

# list = LinkedList()
# list.append(1)
# list.append(2)
# list.append(3)
# list.display()  # Output: 1 -> 2 -> 3
# list.prepend(0)
# list.display()  # Output: 0 -> 1 -> 2 -> 3
# list.delete_value(2)
# list.display()  # Output: 0 -> 1 -> 3




# !Maximum find
arr=[3,4,5,6,2]
maxi=arr[0]
for i in range(1,len(arr)):
    if arr[i]>maxi:
        maxi=arr[i]

# print("Maximum :",maxi)

# !Minimum
arr=[3,4,5,6,2]
mini=arr[0]
for i in range(1,len(arr)):
    if mini>arr[i]:
        mini=arr[i]

# print("Minimum :",mini)

# ! Sum of all

arr=[3,4,5,6,2]
sum=0
for i in range(len(arr)):
    sum+=arr[i]

# print("sum of all: ",sum)


# ! Leetcode 344
s = ["h","e","l","l","o"]
# print(s[::-1])

#  Optimal
n=len(s)
l=0
r=n-1
while(l<r):
    s[l],s[r]=s[r],s[l]
    l+=1
    r-=1

# print(s)


# ! 1752 

def check(a):
    count=0
    for i in range(0,len(a)):
        if a[i]>a[(i+1)%len(a)]:
            count+=1
    if(count<=1):
        return True

    return False

# a = [3,4,5,1,2]
# print(check(a))


# ! 26. Remove Duplicates from Sorted Array

def removeduplicates(self,a):
    if len(a)==0:
        return 0

    pos=1
    for i in range(1,len(a)):
        if a[i]!=a[i+1]:
            a[pos]=a[i]
            pos+=1

    return pos
a=[0,0,1,1,1,2,2,3,3,4]
# print(removeduplicates(a))


# ! 186 Roted array

def rotate(nums,k):
    n=len(nums)
    k=k%n
    nums[:] = nums[-k:]+nums[:-k]

nums = [1,2,3,4,5,6,7]
k = 3

# print(rotate(nums,k))



# ! 215. Kth Largest Element in an Array
"""Its easy but cannt do because que says without Sorting"""
        
        
# nums.sort(reverse=True)
# return nums[k-1]

"""
Use Heap becaues it Quikly get the smallest or largest element because it automatically brings maximum or minimum element in the TOP
min heap: Smallest element easily available
max hip: largest element easily available

Heap is also called Priority Que
Default heap is min heap in Python

Use min heap when You acess large element and vice versa
"""

import heapq
# Add Element
# h=[]
# heapq.heappush(h,5)
# heapq.heappop()

def findKthLargest(nums,k):
    min_heap=[]
    for i in nums:
        heapq.heappush(min_heap,i)  #Add element untill the len(min_heap)<k
        if len(min_heap)>k:
            heapq.heappop(min_heap)

    return min_heap[0]


nums = [3,2,1,5,6,4]
k = 2
# print(findKthLargest(nums,k))




def removeElement(nums,val): 
    for i in range(len(nums)):
        if val in nums:
            nums.remove(val)

    return len(nums)

nums = [0,1,2,2,3,0,4,2]
val = 2

# print(removeElement(nums,val))


# ! 1.Two sum
def two_Sum(nums,target):
    seen={}
    for i , num in enumerate(nums):
        c=target-num
        if c in seen:
            return [seen[c],i]
        seen[num]=i

nums = [2,7,11,15]
target = 9
# print(two_Sum(nums,target))


# ! 88.Merge array

def merge(a1,a2,m,n):
    i=m-1
    j=n-1
    k=m+n-1
    while(i>=0 and j>=0):
        if a1[i]>a2[j]:
            a1[k]=a1[i]
            i-=1
        else:
            a1[k]=a2[j]
            j-=1
            
        k-=1

    while j>=0:
        a1[k]=a2[j]
        j-=1
        k-=1

    return a1
a1 = [1,2,3,0,0,0] 
m = 3
a2 = [2,5,6]
n = 3
# print(merge(a1,a2,m,n))



# ! 121. Best Time to Buy and Sell Stock

def maxProfit(a):
    mini=a[0]
    profit=0
    maxP=0
    for i in range(0,len(a)):
        if(a[i]<mini):
            mini=a[i]
        else:
            profit=a[i]-mini
            maxP=max(maxP,profit)

    return maxP

a = [7,1,5,3,6,4]
print(maxProfit(a))


# ! 977 squares of a sorted array
def sortedSquares(self, a):
    n=len(a)
    res=[0]*n
    left=0
    right=n-1
    for i in range(n-1,-1,-1):
        if abs(a[left])> abs(a[right]):
            res[i]=a[left]*a[left]
            left+=1
        else:
            res[i]=a[right]*a[right]
            right-=1
    return res

nums = [-4,-1,0,3,10]
# print(sortedSquares(nums))
# ! 905 sort array by parity
def sortArrayByParity(nums):
    n=len(nums)
    l=0
    r=n-1
    while(l<r):
        while(l<r and nums[l]%2==0):
            l+=1
                
        while(l<r and nums[r]%2==1):
            r-=1

        if l<r:
            nums[l],nums[r]=nums[r],nums[l]
    return nums


nums = [3,1,2,4]
print(sortArrayByParity(nums))
# 643 Maximum Average Subarray I
# Brute force
# def findMaxAverage(nums,k):
#     n=len(nums)
#     maxs=-float('inf')
#     for i in range(0,n-k+1):
#         sum=0
#         for j in range(i,i+k):
#             sum+=nums[j]
#             maxs=max(sum,maxs)

#     return maxs/k


def findMaxAverage_optimised(nums,k):
    n=len(nums)
    wsum=sum(nums[0:k])
    maxS=wsum
    for i in range(k,n):
        wsum=wsum+nums[i]
        wsum=wsum-nums[i-k]
        maxS=max(maxS,wsum)
    
    return maxS/k

nums = [1,12,-5,-6,50,3]
k = 4
# findMaxAverage_optimised(nums,k)



# Template

"""
Fixed size : 
Find the window of size k and perform operation
on that window.

For reamining window just 1 ele




"""


# 1456. Maximum Number of Vowels in a Substring of Given Length

def maxVowels(s,k):
    vowels="aeiou"
    n=len(s)
    v_count=0
    for i in range(0,k):
        if s[i] in vowels:
            v_count+=1

    maxV=v_count

    for i in range(k,n):
        if s[i] in vowels:
            v_count+=1
        if s[i-k] in vowels:
            v_count-=1

        maxV=max(v_count,maxV)

    return maxV

    
s = "abciiidef"
k = 3
print(maxVowels(s,k))