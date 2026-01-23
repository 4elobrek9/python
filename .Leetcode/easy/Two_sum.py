class Solution:
    def twoSum(self) -> list[int]:
        nums = list(map(int, input("Введите список чисел, разделенных пробелом: ").split()))
        target = int(input("Введите целевое число: "))
        seen = {}
        
        for i, n in enumerate(nums):
            complement = target - n
            
            if complement in seen:
                return [seen[complement], i]
            
            seen[n] = i
