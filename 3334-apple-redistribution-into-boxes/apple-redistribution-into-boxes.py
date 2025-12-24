class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:

        # Compute the sum of apples
        total_apples = sum(apple)

        # Sort the box array in decreasing order
        capacity.sort(reverse=True)

        # Count the minimum number of boxes that can accommodate this sum
        count = 0
        total = 0
        while count < len(capacity) and total < total_apples:
            total += capacity[count]
            count += 1
        
        return count

        