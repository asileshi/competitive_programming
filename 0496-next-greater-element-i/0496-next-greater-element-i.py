class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        stack = []
        for num in nums2:
            if not stack:
                stack.append(num)
            else:
                while stack and stack[-1]<num:
                    hashmap[stack[-1]] = num
                    stack.pop()
                stack.append(num)
        for num in stack:
            hashmap[num] = -1
        return [hashmap[num] for num in nums1]
        