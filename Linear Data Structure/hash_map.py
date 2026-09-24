
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
# print(Two_sum_transaction(nums,target))



# ! 49. Group Anagrams

def groupAnagrams(strs):
    d = {}
    for word in strs:
        key = ''.join(sorted(word))
        if key in d:
            d[key].append(word)
        else:
            d[key] = [word]
    return list(d.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))


# ! 904. Fruit Into Baskets
def totalFruit(a):
    i = 0
    d = {}
    maxlen = 0
    for j in range(len(a)):
        if a[j] in d:
            d[a[j]] += 1
        else:
            d[a[j]] = 1
        while len(d) > 2:
                d[a[i]] -= 1
                if d[a[i]] == 0:
                    del d[a[i]]
                i += 1
        maxlen = max(maxlen, j - i + 1)
    return maxlen

a = [1,2,1]
print(totalFruit(a))
