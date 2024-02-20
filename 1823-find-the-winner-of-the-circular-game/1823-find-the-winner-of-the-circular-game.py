class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        game_list = [i for i in range(1,n+1)]

        current_index = 0

        while len(game_list) > 1:
            remove_index = (current_index + k - 1) % len(game_list)
            game_list.pop(remove_index)
            current_index = remove_index 
        
        return game_list[0]




        