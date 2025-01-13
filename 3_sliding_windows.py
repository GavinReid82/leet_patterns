# --------------------------BRUTE FORCE (ie NOT sliding windows)--------------------------

def max_subarray_sum(arr, k):
    # Initialize max_sum to the smallest possible value
    max_sum = float('-inf')
    show_window = 0
    
    # Loop through valid starting indices for subarrays of size k
    for i in range(len(arr) - k + 1):
        current_sum = 0
        # Calculate the sum of the subarray starting at index i
        for j in range(i, i + k):
            current_sum += arr[j]
        # Update max_sum if a larger sum is found
        if current_sum > max_sum:
            max_sum = current_sum
            show_window = i
            
    return arr[show_window:show_window + k], max_sum

# Test the function
my_array = [3, 1, 7, 4, 2, 1, 5]
print(max_subarray_sum(my_array, 3))  # Output: 13

'''
For my_array = [3, 1, 7, 4, 2, 1, 5] and k = 3:

Subarrays of size 3:
[3, 1, 7] → Sum = 11
[1, 7, 4] → Sum = 12
[7, 4, 2] → Sum = 13
[4, 2, 1] → Sum = 7
[2, 1, 5] → Sum = 8
The function returns 13 as the maximum sum of a subarray of size 3.'''

# The outer loop runs 𝑂(𝑛) times, and for each iteration, the inner loop runs 𝑂(𝑘) times. 
    # Total time complexity: 𝑂(𝑛⋅𝑘)
# Space Complexity: The function uses only a few variables (max_sum, current_sum, i, j), all of which require constant space.
    # No additional data structures (like arrays or lists) are used.
    # Space Complexity: 𝑂(1).


# --------------------------OPTIMISED (ie Sliding windows)--------------------------

def max_subarray_sum(arr, k):
    
    window_sum = sum(arr[:k]) # Computes the sum of the first 𝑘 elements (the first window). This is the initial sum of the first subarray of size 𝑘.

    max_sum = window_sum
    max_start_index = 0 # Keeps track of the starting index of the subarray with the maximum sum.
    
    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        # The sliding window moves one element to the right by subtracting the element going out of the window (arr[i]) 
        # and adding the element coming into the window (arr[i + k]).
        # This avoids recalculating the sum of the entire subarray from scratch, making the algorithm efficient.
        if window_sum > max_sum:
            max_sum = window_sum
            max_start_index = i + 1
            
    return arr[max_start_index:max_start_index + k], max_sum

# Test the function
my_array = [3, 1, 7, 4, 2, 1, 5]
print(max_subarray_sum(my_array, 3))  # Output: 13

# Time Complexity: 𝑂(𝑛)
# Space Complexity: The function uses only constant space for variables (window_sum, max_sum, max_start_index). Space Complexity: 𝑂(1).