class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for num in nums:
            i=abs(num) -1
            nums[i]= -1*abs(nums[i])
        miss=[]
        for i in range(len(nums)):
	        if nums[i]>0:
		        miss.append(i+1)
        return miss
