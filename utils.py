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

result = ncd(num1, num2)
print(result)
