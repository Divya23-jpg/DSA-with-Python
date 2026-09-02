
def shuffle(nums,n):
    x=nums[0:n]
    y=nums[n:2*n]
    ans=[]
    for i in range(0,n):
        ans.append(x[i])
        ans.append(y[i])
    return ans


nums = [2,5,1,3,4,7], n = 3

print(shuffle(nums,n))