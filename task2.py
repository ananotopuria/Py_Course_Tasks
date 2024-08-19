def apply_operation(numbers, operation):

    return [operation(number) for number in numbers]


doubled = apply_operation([1, 2, 3, 4, 5], lambda x: x * 2)
print("Doubled:", doubled)

squared = apply_operation([1, 2, 3, 4, 5], lambda x: x ** 2)
print("Squared:", squared)

filtered = apply_operation([1, 2, 3, 4, 5], lambda x: x if x % 2 != 0 else None)
filtered = [x for x in filtered if x is not None]
print("Filtered (odd numbers):", filtered)
