# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack=[]
        self.current=nestedList  
        self.curidx=0
                  
    def next(self) -> int:
        ret=self.current.getInteger()
        while self.stack:
            self.curidx=self.stack.pop()
            self.current=self.stack.pop()
            self.curidx+=1
            if self.curidx<len(self.current):
                break
        return ret
    
    def hasNext(self) -> bool:
        while type(self.current)==list:
            if self.curidx<len(self.current):
                self.stack.append(self.current)
                self.stack.append(self.curidx)
                self.current=self.current[self.curidx]
                if not self.current.isInteger():
                    self.current=self.current.getList()
                    self.curidx=0
            else:
                if self.stack:
                    self.curidx=self.stack.pop()
                    self.current=self.stack.pop()
                    self.curidx+=1
                else:
                    return False      
        return True
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
