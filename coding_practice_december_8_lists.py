# Coding Practice: December 8 Lists (Option 3: Using Python Exercise Runner)
from typing import List


# Codingbat List-1 Q1 first_last_6
def first_last_6(nums: List[int]) -> bool:
    return nums[0] == 6 or nums [-1] == 6

result = first_last_6([1, 2, 6])
print(result)
print()

# Codingbat List-1 Q2 same_first_last
def same_first_last(nums: List[int]) -> bool:
    return len(nums) > 0 and nums[0] == nums [-1]

result = same_first_last([1, 2, 3])
print(result)
print()

# Codingbat List-1 Q3 make_pi
def make_pi() -> List[int]:
    return [3, 1, 4]

result = make_pi()
print(result)
print()

# Codingbat List-1 Q4 common_end
def common_end(a: List[int], b: List[int]) -> bool:
    return a[0] == b[0] or a[-1] == b[-1]

result = common_end([1, 2, 3], [7, 3])
print(result)
print()

# Codingbat List-1 Q5 sum_3
def sum_3(nums: List[int]) -> int:
    return nums[0] + nums[1] + nums[2]

result = sum_3([1, 2, 3])
print(result)
print()

# Codingbat List-1 Q6 rotate_left_3
def rotate_left_3(nums: List[int]) -> List[int]:
    return [nums[1], nums[2], nums[0]]

result = rotate_left_3([1, 2, 3])
print(result)
print()

# Codingbat List-1 Q7 reverse_3
def reverse_3(nums: List[int]) -> List[int]:
    return [nums[2], nums[1], nums[0]]

result = reverse_3([1, 2, 3])
print(result)
print()

# Codingbat List-1 Q8 max_end_3
def max_end_3(nums: List[int]) -> List[int]:
    if nums[0] > nums[2]:
        return [nums[0], nums[0], nums[0]]
    else:
        return [nums[2], nums[2], nums[2]]

result = max_end_3([1, 2, 3])
print(result)
print()

# Codingbat List-1 Q9 sum_2
def sum_2(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 0:
        return 0
    else:
        return nums[0] + nums[1]

result = sum_2([1, 2, 3])
print(result)
print()

# Codingbat List-1 Q10 middle_way
def middle_way(a: List[int], b: List[int]) -> List[int]:
    return [a[1], b[1]]

result = middle_way([1, 2, 3], [4, 5, 6])
print(result)
print()


# Codingbat List-2 Q1 count_evens
def count_evens(nums: List[int]) -> int:
    i = 0
    number_of_evens = 0
    while i < len(nums):
        if nums[i] % 2 == 0:
            number_of_evens += 1
        i += 1
    return number_of_evens

result = count_evens([2, 1, 2, 3, 4])
print(result)
print()

# Codingbat List-2 Q2 big_diff
def big_diff(nums: List[int]) -> int:
    i = 0
    largest_number = 0
    smallest_number = nums[i]
    while i < len(nums):
        largest_number = max(largest_number, nums[i])
        smallest_number = min(smallest_number, nums[i])
        i += 1
    return largest_number - smallest_number

result = big_diff([10, 3, 5, 6])
print(result)
print()

# Codingbat List-2 Q3 centered_average
def centered_average(nums: List[int]) -> int:
    i = 0
    largest_number = 0
    smallest_number = nums[0]
    sum_of_numbers = 0
    large_number_gone = False
    small_number_gone = False
    while i < len(nums):
        largest_number = max(largest_number, nums[i])
        smallest_number = min(smallest_number, nums[i])
        i += 1
    i = 0
    while i < len(nums):
        if nums[i] == largest_number and large_number_gone == False:
            large_number_gone = True
        elif nums[i] == smallest_number and small_number_gone == False:
            small_number_gone = True
        else:
            sum_of_numbers += nums[i]
        i += 1
    return int(sum_of_numbers / (len(nums) - 2))

result = centered_average([1, 2, 3, 4, 100])
print(result)
print()

# Codingbat List-2 Q4 sum_13
def sum_13(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    else:
        i = 0
        sum_of_numbers = 0
        while i < len(nums):
            if nums[i] == 13:
                i += 1
            else:
                sum_of_numbers += nums[i]
            i += 1
        return sum_of_numbers

result = sum_13([1, 2, 2, 1])
print(result)
print()

# Codingbat List-2 Q5 sum_67
def sum_67(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    else:
        i = 0
        sum_of_numbers = 0
        no_add = False
        while i < len(nums):
            if nums[i] == 6:
                no_add = True
            elif no_add == False:
                sum_of_numbers += nums[i]
            elif nums[i] == 7:
                no_add = False
            i += 1
        return sum_of_numbers

result = sum_67([1, 2, 2])
print(result)
print()

# Codingbat List-2 Q6 has_22
def has_22(nums: List[int]) -> bool:
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1] == 2:
            return True
        i += 1
    return False

result = has_22([1, 2, 2])
print(result)
print()

# Codingbat List-2 Q7 lucky_13
def lucky_13(nums: List[int]) -> bool:
    i = 0
    while i < len(nums):
        if nums[i] == 1 or nums[i] == 3:
            return False
        i += 1
    return True

result = lucky_13([0, 2, 4])
print(result)
print()

# Codingbat List-2 Q8 sum_28
def sum_28(nums: List[int]) -> bool:
    i = 0
    sum_of_twos = 0
    while i < len(nums):
        if nums[i] == 2:
            sum_of_twos += 2
        i += 1
    return sum_of_twos == 8

result = sum_28([2, 3, 2, 2, 4, 2])
print(result)
print()

# Codingbat List-2 Q9 more_14
def more_14(nums: List[int]) -> bool:
    i = 0
    number_of_1 = 0
    number_of_4 = 0
    while i < len(nums):
        if nums[i] == 1:
            number_of_1 += 1
        elif nums[i] == 4:
            number_of_4 += 1
        i += 1
    return number_of_1 > number_of_4

result = more_14([1, 4, 1])
print(result)
print()

# Codingbat List-2 Q10 fizz_array
def fizz_array(n: int) -> List[int]:
    new_list = []
    i = 0
    while i < n:
        new_list.append(i)
        i += 1
    return new_list

result = fizz_array(4)
print(result)
