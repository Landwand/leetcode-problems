class Solution:
    def isPalindrome(self, s: str) -> bool:
        ''' this filter returns an iteratable of containing the Alpha-numeric characters '''
        working_string = ''.join(filter(str.isalnum, s))
        working_string = working_string.lower()

        slength = len(working_string)

        if slength == 1:
            return True

        last_index = slength + 1

        if len(working_string) % 2 == 0: # even
            stop_index = slength/2
        else: # odd
            stop_index = (slength - 1) // 2

        stop_index = int(stop_index)
        
        right_pos = slength - 1
        for left_pos in range(stop_index):
            if working_string[left_pos] == working_string[right_pos]:
                right_pos = right_pos - 1
                continue
            else:
                return False
        return True