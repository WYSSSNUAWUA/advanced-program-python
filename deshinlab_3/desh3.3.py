def even_numbers(limit):
    for i in range(0, limit + 1, 2):
        yield i

def square_numbers(numbers):
    for n in numbers:
        yield n * n

def less_than_200(numbers):
    for n in numbers:
        if n < 200:
            yield n
        else:
            break

pipeline = less_than_200(square_numbers(even_numbers(25)))

print(list(pipeline))
