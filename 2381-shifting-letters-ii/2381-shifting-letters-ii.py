class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        n = len(s)
        pref_shifts= [0]*n
        res=[]
        for start,end,direc in shifts:
            if direc == 0:
                pref_shifts[start] = pref_shifts[start]-1
                if end+1<n:
                    pref_shifts[end+1] = pref_shifts[end+1]+1
            else:
                pref_shifts[start] = pref_shifts[start]+1
                if end+1<n:
                    pref_shifts[end+1] = pref_shifts[end+1]-1
        
        for i in range(1,n):
            pref_shifts[i]+=pref_shifts[i-1]
        
        for i in range(n):
            new_shift = (ord(s[i])-ord('a')+pref_shifts[i])%26
            new_code = ord('a')+new_shift
            res.append(chr(new_code))

        return ''.join(res)


            
            
