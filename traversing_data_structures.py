# Example tuple
my_tuple = (1, 2, 3, 4)

# Simple iteration
for item in my_tuple:
    print(item)

# Tuple with multiple elements
my_nested_tuple = [(1, 'a'), (2, 'b'), (3, 'c')]

# Iteration with unpacking
for number, letter in my_nested_tuple:
    print(f"Number: {number}, Letter: {letter}")


# Example of a list of dictionaries
list_of_dicts = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]

for d in list_of_dicts:
    for key, value in d.items():
        print(f"Key: {key}, Value: {value}")

# Example of a dictionary of lists
dict_of_lists = {'fruits': ['apple', 'banana'],
                 'vegetables': ['carrot', 'lettuce']}

for key, value_list in dict_of_lists.items():
    print(f"Category: {key}")
    for item in value_list:
        print(f"Item: {item}")


# Example list
my_list = [1, 2, 3, 4]

# List comprehension to square each number
squared = [x**2 for x in my_list]
print(squared)

# List comprehension to filter even numbers
evens = [x for x in my_list if x % 2 == 0]
print(evens)


# Example list
my_list = [1, 2, 3, 4]

# Generator expression to square each number
squared_gen = (x**2 for x in my_list)
for val in squared_gen:
    print(val)


# Example lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

for num, char in zip(list1, list2):
    print(f"Number: {num}, Character: {char}")
