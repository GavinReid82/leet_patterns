s = "abcdefghijklmnop"

# Initialize pointers
slow = 0
fast = 1

# Traverse the string
while fast < len(s):
    print(f"Slow pointer at index {slow}: {s[slow]}")
    print(f"Fast pointer at index {fast}: {s[fast]}")
    print("---")
    
    # Move pointers: slow moves by 1 step, fast moves by 2 steps
    slow += 1
    fast += 2

# Since the fast pointer increments by 2 steps for each iteration, the number of iterations is approximately 𝑛/2, where 𝑛=len(s).
    # Each iteration performs constant-time operations (printing the current pointer positions and updating the pointers).
    # Thus, the total time complexity is:𝑂(𝑛)
# The algorithm uses two pointers, slow and fast, which occupy 𝑂(1) space.