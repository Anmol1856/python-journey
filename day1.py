# Day 1 - Basic python functions
def check_even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def sum_list(numbers):
    return sum(numbers)

def is_prime(n):
    if n <= 1:
        return "Not Prime"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "Not Prime"
    return "Prime"

def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":
    print(check_even_odd(10))
    print(factorial(3))
    print(sum_list([1,2,3,4,5]))
    print(is_prime(9))
    print(reverse_string("Python"))