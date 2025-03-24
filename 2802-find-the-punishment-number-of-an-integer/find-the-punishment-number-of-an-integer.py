class Solution:
    def find_partitions(self, start_index, current_sum, string_num, target):
        # If we've used all digits, check if the sum is valid
        if start_index == len(string_num):
            return current_sum == target

        # If the current sum already exceeds target, stop
        if current_sum > target:
            return False

        # Try all possible splits
        for current_index in range(start_index, len(string_num)):
            current_string = string_num[start_index : current_index + 1]
            addend = int(current_string)

            # Recur with updated sum and index
            if self.find_partitions(current_index + 1, current_sum + addend, string_num, target):
                return True

        return False

    def punishmentNumber(self, n: int) -> int:
        punishment_num = 0

        for current_num in range(1, n + 1):
            square_num = current_num * current_num
            string_num = str(square_num)

            # Check if valid split exists
            if self.find_partitions(0, 0, string_num, current_num):
                punishment_num += square_num

        return punishment_num
