my_dict = {"Apple": 2, "Pear": 4, "Cherry": 6}
first_key = list(my_dict.keys())[0]
second_key = list(my_dict.keys())[1]
third_key = list(my_dict.keys())[2]

for value in my_dict.values():
    print(value)
for key in my_dict:
    print(key)
for key in first_key:
    print(key)

sample = 'allinpython'
print(sample.index('i'))  # Answer should be 3

# my_dict = {"Apple": 2, "Pear": 4, "Cherry": 6}: This line creates a dictionary called my_dict with three key-value
# pairs.

# first_key = list(my_dict.keys())[0]: This line gets the first key from the dictionary ("Apple") and stores it in
# the variable first_key.

# second_key = list(my_dict.keys())[1]: This line gets the second key from the dictionary ("Pear") and stores it in
# the variable second_key.

# third_key = list(my_dict.keys())[2]: This line gets the third key from the dictionary ("Cherry") and stores it in
# the variable third_key.

# for value in my_dict.values(): print(value): This loop goes through each value in the dictionary and prints it. So
# it will print 2, 4, and 6.

# for key in my_dict: print(key): This loop goes through each key in the dictionary and prints it. So it will print
# "Apple", "Pear", and "Cherry".

# for key in first_key: print(key): This loop goes through each character in the first_key string ("Apple") and
# prints it. So it will print A, p, p, l, e.

# Remember that strings in Python are iterable, so when you use a for loop on a string, it loops through each
# character. That's why the last loop prints each character of "Apple".
