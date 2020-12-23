# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
def sortedSquares(nums):
     output=[None]*len(nums)
     left=0
     right=len(nums)-1
     for i in range(len(nums)-1,-1,-1):
         if nums[left]**2 > nums[right]**2:
             output[i]=nums[left]**2
             left+=1
         else:
             output[i]=nums[right]**2
             right-=1
     return output

     # for i in range(len(nums)-1,-1,-1):
     #     if abs(nums[left])>abs(nums[right]):
     #         output[i]=(nums[left])**2
     #         left+=1
     #     else:
     #         output[i]=(nums[right])**2
     #         right-=1
     # return output

print(sortedSquares([-7, -3, 2, 3, 11]))

























     # for i in nums:
     #     output.append(i*i)
     # #[49,9,4,9,121][-7,-3,2,3,11]
     # rightpointer=len(output)-1
     # leftpointer=0
     # while leftpointer<rightpointer:
     #     if output[leftpointer]<output[rightpointer]:
     #         rightpointer-=1
     #     else:
     #         output[leftpointer],output[rightpointer]=output[rightpointer],output[leftpointer]
     #         rightpointer-=1
     #     if leftpointer==rightpointer:
     #         leftpointer+=1
     #         rightpointer=len(output)-1
     # return output
