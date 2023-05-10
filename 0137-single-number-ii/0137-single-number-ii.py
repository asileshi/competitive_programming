class Solution:
    def singleNumber(self, arr: List[int]) -> int:
        bit_counts = [0] * 32  # assume 32-bit integers

        # Count the number of times each bit is set for all numbers in the array
        for num in arr:
            # Handle negative numbers by ignoring the sign bit
            if num < 0:
                num = ((1 << 32) - 1) & num

            for i in range(32):
                bit_counts[i] += (num >> i) & 1

        single_num = 0
        for i in range(32):
            if bit_counts[i] % 3 != 0:
                single_num |= 1 << i

        # Handle negative single number
        if single_num >= (1 << 31):
            single_num -= (1 << 32)

        return single_num
    