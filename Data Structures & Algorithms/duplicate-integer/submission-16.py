class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        Duplicate = False

        for num in nums:
            if num in seen:
                print(f"Duplicate found: {num}")
                Duplicate = True
                return True
            else:
                print("Duplicate not found")
                seen.append(num)
        return Duplicate