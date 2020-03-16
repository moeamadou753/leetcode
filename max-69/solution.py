class Solution:
    def maximum69Number(self, num: int) -> int:
        """ Naive solution:
            - Find the highest place digit that is non-9 and change it to a 9
            - If all digits are nines, change nothing
        """
        dig_list = list(str(num))
        for i in range(len(dig_list)):
            if (dig_list[i] != str(9)):
                dig_list[i] = str(9)
                new_num = "".join(dig_list)
                return int(new_num)

        return num