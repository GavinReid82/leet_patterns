# ---------------------------INEFFICIENT O(n2)---------------------------

def next_bigger_element(arr):
    n = len(arr)
    result = [-1] * n

    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                result[i] = arr[j]
                break
    return result

my_arr = [1, 4, 6, 3, 2, 7]
print(next_bigger_element(my_arr))

'''
Iteration Breakdown:
For 1: First number to the right that's larger is 4, so result[0] = 4.
For 4: First number to the right that's larger is 6, so result[1] = 6.
For 6: First number to the right that's larger is 7, so result[2] = 7.
For 3: First number to the right that's larger is 7, so result[3] = 7.
For 2: First number to the right that's larger is 7, so result[4] = 7.
For 7: There's no number to the right that's larger, so result[5] = -1.'''

# ---------------------------STACK OPTIMISED O(n)---------------------------

def next_greater_element(arr):
    n = len(arr)
    stack = []
    result = [-1] * n

    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            result[stack.pop()] = arr[i]
        
        stack.append(i)

    return result

array = [1, 4, 6, 3, 2, 7]
print(next_greater_element(array))

# The for i in range(n) loop runs 𝑂(𝑛) times. 
# Inner while Loop:
    # Each element is pushed onto the stack exactly once and popped from the stack exactly once.
    # The total number of stack operations (push + pop) is 𝑂(𝑛).
# Time complexity is: 𝑂(𝑛)

# The result array requires 𝑂(𝑛) space 