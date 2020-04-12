class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        class FenwickTree():
            def __init__(self,n):
                self.sumarray=[0]*(n+1)
                self.size=n
            
            def lowbit(self,i):
                return (i&-i)
            
            def add(self,i,val):
                while i<=self.size:
                    self.sumarray[i]+=val
                    i+=self.lowbit(i)
            
            def sum(self,i):
                res=0
                while i>0:
                    res+=self.sumarray[i]
                    i-=self.lowbit(i)
                return res
                    
        dict={}
        for i,v in enumerate(sorted(set(nums))):
            dict[v]=i+1
        ans=[0]*len(nums)
        tree=FenwickTree(len(nums))
        for i in range(len(nums)-1,-1,-1):
            ans[i]=tree.sum(dict[nums[i]]-1)
            tree.add(dict[nums[i]],1)
        return ans
