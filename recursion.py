#Part 1
def fibonacci(n):
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example
print(fibonacci(8))

#Part 2
def gcd(a, b):
    # Base case: when remainder becomes 0
    if b == 0:
        return a

    # Recursive case
    return gcd(b, a % b)

# Example
print(gcd(34, 76))

#Part 3
def compareTo(s1, s2):
    # Base cases
    if s1 == "" and s2 == "":
        return 0
    if s1 == "":
        return -1
    if s2 == "":
        return 1

    # Compare first characters
    if s1[0] != s2[0]:
        return ord(s1[0]) - ord(s2[0])

    # Recursive case
    return compareTo(s1[1:], s2[1:])

# Example
print(compareTo("apple", "apricot"))  # Negative number
print(compareTo("hello", "hello"))    # 0
print(compareTo("zoo", "ant"))        # Positive number