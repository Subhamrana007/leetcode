class Solution:
    def asteroidCollision(self, nums: List[int]) -> List[int]:
        stack = []

        for n in nums:
            while stack and n < 0 and stack[-1] > 0 and (abs(n) > abs(stack[-1])):
                stack.pop()

            if stack and stack[-1] < 0 and n > 0:
                stack.append(n)

            elif stack and n < 0 and stack[-1] > 0 and abs(stack[-1]) == abs(n):
                stack.pop()
                continue

            elif stack and n < 0 and stack[-1] > 0:
                continue

            else:
                stack.append(n)

        return stack

            
        