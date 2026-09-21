
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