def is_palindrome(string):
    start = 0
    end = len(string) - 1

    while start < end:
        if string[start] != string[end]:
            return False
        else:
            start += 1
            end -= 1
    return True


print(is_palindrome("racecar"))
print(is_palindrome("gavin"))

# Time Complexity: 𝑂(𝑛)
    # the loop iterates linearly over half the characters of the string. 
    # The total number of iterations is proportional to 𝑛/2, which simplifies to 𝑂(𝑛).
# Space Complexity: 𝑂(1)
        # the function uses a constant amount of additional memory regardless of the size of the input string.
    # 1. Input String:
        # The input string string is passed by reference (not copied).
        # This means the function doesn't create any additional storage for the string itself.
    # 2. The function uses two integer variables:
        # start to track the beginning index and end to track the last index.
        # Both variables occupy a constant amount of space (e.g., 𝑂(1) for two integers).