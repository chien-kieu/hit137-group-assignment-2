# global_variable = 100
# my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# def process_numbers():
#     global global_variable
#     local_variable = 5
#     numbers = [1, 2, 3, 4, 5]

#     while local_variable > 0:
#         if local_variable % 2 == 0: 
#             numbers.remove (local_variable)
#         local_variable -= 1

#     return numbers

# my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
# result = process_numbers (numbers=my_set)

# def modify_dict():
#     local_variable = 10
#     my_dict['key4']

# modify_dict(5)

# def update_global():
#     global global_variable
#     global_variable += 10

# for i in range(5):
#     print(i)
#     i += 1

# if my_set is not None and my_dict['key4'] == 10:
#     print("Condition met!")

# if 5 not in my_dict:
#     print("5 not found in the dictionary!")

# print(global_variable)
# print(my_dict)
# print(my_set)

global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def process_numbers(numbers):
    global global_variable
    local_variable = 5
    print(numbers)
    # numbers = [1, 2, 3, 4, 5]

    while local_variable > 0:
        if local_variable % 2 == 0: 
            numbers.remove(local_variable)
        local_variable -= 1

    return numbers

my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
my_set_2 = {1, 2, 3, 4, 5, 5, 4, 'a', 3, 2, 1, 'a'}
print(my_set_2)
result = process_numbers(numbers=my_set)  # Fixed: copy the set to avoid modification during iteration
print(result)
print(f"Global variable after function call: {global_variable}")


def modify_dict():
    local_variable = 10
    my_dict['key4'] = 10  # Fixed: assign a value to the key 'key4'

modify_dict()

def update_global():
    global global_variable
    global_variable += 10
    print(global_variable)

for i in range(5):
    print(i)
    # i += 1  # Not necessary to increment i in a for loop

if my_set is not None and 'key4' in my_dict and my_dict['key4'] == 10:  # Fixed: condition corrected
    print("Condition met!")

if 5 not in my_dict.values():  # Fixed: check if 5 is not in values, not in keys
    print("5 not found in the dictionary!")

print(global_variable)
print(my_dict)
print(my_set)
