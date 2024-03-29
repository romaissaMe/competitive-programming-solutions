class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        X = 0

        for operation in operations:
            if "++" in operation:
                X += 1
            elif "--" in operation:
                X -= 1

        return X