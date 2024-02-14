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

def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    else:
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                return False
        return True


#for 'pull-request':
def decimal_to_binary_recursive(dec):
    if dec == 0:
        return "0"
    elif dec == 1:
        return "1"
    else:
        chastka = dec // 2
        r = dec % 2
        return decimal_to_binary_recursive(chastka) + str(r)
