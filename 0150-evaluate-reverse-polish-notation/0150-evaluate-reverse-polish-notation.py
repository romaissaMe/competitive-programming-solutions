class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops=["+","-","*","/"]
        stack=[]
        for tk in tokens:
            if tk in ops:
                b=stack.pop()
                a=stack.pop()
                stack.append(int(eval(f"{a}{tk}{b}")))
            else:
                stack.append(tk)
        
        return int(stack.pop())