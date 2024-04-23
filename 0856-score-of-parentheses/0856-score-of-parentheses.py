class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        for i in s:
            if i == "(":
                stack.append(0)  
            else:
                if stack[-1] == 0:  # Check if current ')' corresponds to a '('
                    stack.pop()  
                    stack.append(1)  
                else:
                    # Calculate the score for nested parentheses
                    nested_score = 0
                    while stack[-1] != 0:
                        nested_score += stack.pop()
                    stack.pop()  
                    stack.append(2 * nested_score)  
        return sum(stack)


#(,(,),),(,)