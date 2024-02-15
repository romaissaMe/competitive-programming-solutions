class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        left_moves = [0]*len(boxes)
        right_moves= [0]*len(boxes)
        left_balls = [0]*len(boxes)
        right_balls= [0]*len(boxes)
        left_pt=1
        right_pt=len(boxes)-2
        answer= [0]*len(boxes)

        while left_pt<len(boxes)and right_pt>=0:
            left_balls[left_pt]=left_balls[left_pt-1]+int(boxes[left_pt-1])
            right_balls[right_pt]=right_balls[right_pt+1]+int(boxes[right_pt+1])
            left_pt+=1
            right_pt-=1
        
        for i in range(1,len(boxes)):
            left_moves[i] = left_moves[i-1]+left_balls[i]
        
        for i in range(len(boxes)-2,-1,-1):
            right_moves[i] = right_moves[i+1]+right_balls[i]

        
        for i in range(0,len(boxes)):
            answer[i]=left_moves[i]+right_moves[i]
        return answer



        

            
        


        