# arr=[2,4,3,1]
# ans=[]
# for i in reversed(arr):
#     ans.append(i)

# print(arr==sorted(ans))


 


def algotutor(n):
    for i in range(n):
        print("Divya")


algotutor(3)




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
                    
        return result