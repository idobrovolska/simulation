def factorial(n): 
	for i in range(1, n + 1):
		fact *= i


	return fact

def ncd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input())
num2 = int(input())

def power_of_five(n):
    if n == 0:
        return False
    while n % 5 == 0:
        n /= 5
    return n == 1

