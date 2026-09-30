

double = lambda x: x * 2
print(double(10))

remainder = lambda x, y: x % y
print(remainder(10, 3))

divisible= lambda x: x % 5 == 0
print(divisible(25))

smaller = lambda x, y: x if x < y else y
print(smaller(10, 5))

fahrenheit = lambda c: (c * 9/5) + 32
print(fahrenheit(25))




numbers = [10, 20, 30, 40, 50]
result = map(lambda x: x + 5, numbers)
print(list(result))

names = ["aparna", "ravi", "priya", "kiran"]
result = map(lambda x: x.upper(), names)
print(list(result))




ages = [12, 18, 25, 15, 30, 10, 22]
result = filter(lambda x: x >= 18, ages)
print(list(result))

names = ["Ram", "Aparna", "Ravi", "Priyanka", "Sai"]
result = filter(lambda x: len(x) > 4, names)
print(list(result))



students = [
    ("Aparna", 85),
    ("Ravi", 72),
    ("Priya", 95),
    ("Kiran", 65)
]

result = sorted(students, key=lambda x: x[1], reverse=True)
print(result)