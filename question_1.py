# create a list of number from 1 to 10
one_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# using list comprehension, generate a new list with only even numbers
even_from_one_to_ten = [num for num in one_to_ten if (num % 2 == 0)]
# using list comprehension, generate a new list with only odd numbers
odd_from_one_to_ten = [num for num in one_to_ten if (num % 2 == 1)]
# print out the sum of all even numbers
print(sum(even_from_one_to_ten))
# print out the sum of all odd numbers
print(sum(odd_from_one_to_ten))
