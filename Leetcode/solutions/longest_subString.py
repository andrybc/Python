class Solution(object):
    def lengthOfLongestSubstring(self, s):
        #sliding window problem
        """
        :type s: str
        :rtype: int
        """

        
        # left = 0
        # count = 0
        # seen_chars = set()
        # current_string= ""
        
        # for right, char in enumerate(s):
        
        #     if char in seen_chars:
        #         while s[left] != char:
        #             seen_chars.remove(s[left])
        #             left +=1
        #         left+=1
        #         current_string = s[left:right+1]
        #     else:
        #         seen_chars.add(char)
        #         current_string += char
            
        #     count = len(current_string) if len(current_string)> count else count
        #     #print(count)
        left = 0
        max_length = 0
        seen_chars = set()
        
        for right, char in enumerate(s):
            while char in seen_chars:#while the char is still in set remove every other char until then
                seen_chars.remove(s[left])
                left += 1
            seen_chars.add(char)
            max_length = max(max_length, right - left + 1)#dont need to create another string..can just keep track with left and right variable + 1
                
        return max_length
                    
        return count