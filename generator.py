def square_generator(n):
    for i in range(n + 1):
        yield i ** 2

n = int(input("Enter a number: "))
print("Squares of numbers up to", n, ":", list(square_generator(n)))

def even_numbers_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number for even numbers: "))
print("Even numbers between 0 and", n, ":", ", ".join(map(str, even_numbers_generator(n))))

def divisible_by_3_and_4_generator(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter a range limit for numbers divisible by 3 and 4: "))
print("Numbers divisible by 3 and 4 between 0 and", n, ":", list(divisible_by_3_and_4_generator(n)))

def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input("Enter the start of range (a): "))
b = int(input("Enter the end of range (b): "))
print("Squares from", a, "to", b, ":")
for value in squares(a, b):
    print(value)

def countdown_generator(n):
    for i in range(n, -1, -1):
        yield i

n = int(input("Enter a number for countdown: "))
print("Countdown from", n, "to 0:")
for number in countdown_generator(n):
    print(number)
