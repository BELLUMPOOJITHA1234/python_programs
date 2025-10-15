
numbers = [10, 5, 23, 8, 42, 15]

if not numbers:  # Handle the case of an empty list
    print("The list is empty.")
else:
    largest_number = numbers[0]  # Assume the first element is the largest initially
    for num in numbers:
        if num > largest_number:
            largest_number = num
    print(f"The largest number in the list (manual iteration) is: {largest_number}")

