# create a tuple of names
names_tuple = ("Sheena", "Martin", "Robert", "Natham")
# create a tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')
# for every vowel in the tuple
for vowel in vowels:
    # using list comprehension, generate a list that contain how man vowels is in each name
    count_var = [name.count(vowel) for name in names_tuple]
    # print out the generated lists.
    # First list represents how many "a" in each names,
    # Second list represents how many "e" in each name ...etc.
    print(count_var)
