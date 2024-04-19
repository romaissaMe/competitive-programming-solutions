class ListNode:
    def __init__(self,webs,prev=None,next=None):
        self.webs=webs
        self.next=next
        self.prev=prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = ListNode(homepage) 
        

    def visit(self, url: str) -> None:
        self.curr.next = ListNode(url,self.curr)
        self.curr = self.curr.next

        

    def back(self, steps: int) -> str:
        while steps>0 and self.curr.prev:
            self.curr = self.curr.prev
            steps-=1
        return self.curr.webs

    def forward(self, steps: int) -> str:
        while steps>0 and self.curr.next :
            self.curr = self.curr.next
            steps-=1
        return self.curr.webs
        
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)