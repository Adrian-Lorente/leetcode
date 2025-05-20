from typing import List, Self


class Entry:
    def __init__(self, value: int, difference: int, indexes: List[int] = []):
        """Defines the difference between a target and a number, and holds the index of said number in an array

        Args:
            value (int): the original value of the entry.
            indexes (List[int]): the position(s) in the array.
            difference (int): holds the value of the operation target - value
        """
        self.value = value
        self.indexes = indexes
        self.difference = difference
        self.appearances = 1

    def merge_entry(self, entry: Self):
        """Merges the entry passed as an argument and the current entry by extending the current indexes list

        Args:
            entry (Self): entry to merge.
        """
        self.indexes = self.indexes + entry.indexes
        self.appearances += 1


class EntryTable(dict):
    """Directly inherits from `dict` built-in class."""

    def __init__(self):
        return super().__init__()

    def set_or_update(self, key, entry: Entry):
        # If key already has a value in the EntryTable, it means the number is duped. Therefore, we only need to add
        if (existing_entry := self.get(key)) is None:
            self[key] = entry
        else:
            existing_entry.merge_entry(entry)
        return


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Define the (hash) table of the entries
        entry_table = EntryTable()

        # Fist loop: calc the differences between target & number for each num in nums, while keeping track of the indexes.
        for index, value in enumerate(nums):
            new_entry = Entry(value=value, difference=target - value, indexes=[index])
            entry_table.set_or_update(key=value, entry=new_entry)

        # Second loop: for each item in the difference_mapper, we try to find the difference
        for _key, entry1 in entry_table.items():
            if (entry2 := entry_table.get(entry1.difference)) is None:
                continue

            # entry2 exists
            if entry1.value + entry2.value != target:
                continue
            # entry1.value + entry2.value == target
            if entry1.value == entry2.value:
                if entry1.appearances == 2:
                    return entry1.indexes
                else:
                    # An number that appears more than twice cannot be a solution
                    continue
            else:
                return [entry1.indexes[0], entry2.indexes[0]]


solution = Solution()

# Case 1:
nums, target = [2, 7, 11, 15], 9
expected_1 = [0, 1]
result_1 = solution.twoSum(nums=nums, target=target)

assert result_1 == expected_1, f"Test 1 failed. Expected {expected_1} but got {result_1}"

# Case 2:
nums, target = [3, 2, 4], 6
expected_2 = [1, 2]
result_2 = solution.twoSum(nums=nums, target=target)

assert result_2 == expected_2, f"Test 2 failed. Expected {expected_2} but got {result_2}"


# Case 3:
nums, target = [3, 3], 6
expected_3 = [0, 1]
result_3 = solution.twoSum(nums=nums, target=target)

assert result_3 == expected_3, f"Test 3 failed. Expected {expected_3} but got {result_3}"