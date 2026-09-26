# !643 Maximum Average Subarray I

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

# ! Optimised
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