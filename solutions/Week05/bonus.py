def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def prime_list(num):
    primes_list = [i for i in range(2, num + 1) if is_prime(i)]
    print(primes_list)
    return primes_list

num = int(input("Up to which number do you want all prime numbers:"))
prime_list(num)