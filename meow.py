def count_odd_even(lst):
    odd_count = 0
    even_count = 0

    for num in lst:
        if isinstance(num, str):
            print("It's a string!!!")
            odd_count = 0
            even_count = 0
            break
        elif num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return odd_count, even_count


# Example usage:
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_count, even_count = count_odd_even(list1)
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)

list2 = [1, 2, 3, 4, "Oops", 6, 7, 8, 9]
odd_count, even_count = count_odd_even(list2)
