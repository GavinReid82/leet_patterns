# input:    [1, 2, 3, 4, 5, 6, 7, 8, 9]
# output:   [1, 3, 6, 10, 15, 21, 28, 36, 45]

#For each position i:
    # Add the value of the previous element (arr[i - 1]) to the current element (arr[i]).

# i = 1, output 2 + 1 = 3
# i = 2, output 3 + 3 = 6
# i = 3, output 4 + 6 = 10

def create_prefix_sum(arr):
    for i in range(1, len(arr)):
        arr[i] += arr[i -1]
    return arr

my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(create_prefix_sum(my_array))

# Time Complexity: 𝑂(𝑛) The loop iterates through the array once.
# Space Complexity: 𝑂(1) The calculation is done in place without requiring additional space.




# -----------------------SUM A RANGE (RATHER THAN ENTIRE ARRAY)-----------------------

def preprocess_prefix_sum(nums):
    # Step 1: Preprocess the array to create the prefix sum array
    prefix_sum = [0] * len(nums)
    prefix_sum[0] = nums[0]
    
    for i in range(1, len(nums)):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i]
    
    return prefix_sum

def range_sum_query(prefix_sum, i, j):
    # Step 2: Use the prefix sum array to calculate the range sum
    if i == 0:
        return prefix_sum[j]
    return prefix_sum[j] - prefix_sum[i - 1]

# Example Usage
nums = [1, 2, 3, 4, 5, 6]
prefix_sum = preprocess_prefix_sum(nums)

# Query for range [i, j]
i, j = 1, 3
result = range_sum_query(prefix_sum, i, j)
print("Sum of range [{}:{}]:".format(i, j), result)