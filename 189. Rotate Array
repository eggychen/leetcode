class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        if n==0:return None
        k%=n
        
        def gcd(n1,n2):
            if n2==0:return n1
            return gcd(n2,n1%n2)
        
        times=gcd(n,k)
        for i in range(times):
            dest=(i+k)%n
            tmp=nums[i]
            while dest!=i:
                tmp,nums[dest]=nums[dest],tmp
                dest=(dest+k)%n
            nums[i]=tmp
            
