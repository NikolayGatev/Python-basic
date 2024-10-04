

print("Choose a data type to perform operations on:")
print("1. Strings")
print("2. Numbers")
print("3. Booleans")
print("4. Additional Data Types (List, Tuple, Dictionary)")

# Get the user's choice and store it in a variable
choice = input("Enter the number of your choice (1-4): ")

# If the user chooses Strings (choice == '1'):
if choice == '1':
    string = 'Learning Python is fun!'
    print(f"This is sentence :{string}. We are extracting \"Python\": result: {string[9:15]}")
    print(f'Convert the sentence to uppercase \nresult: {string.upper()}')
    print(f'Replace fun with awesome\nresult: {string.replace('fun', 'awesome')}')


# Extract and print a substring, such as the word "Python" from the sentence.

# Convert the entire sentence to uppercase and print it.

# Replace a word in the sentence (e.g., replace "fun" with "awesome") and print the modified sentence.

# If the user chooses Numbers (choice == '2'):
elif choice == '2':
    print('Entre two numbers')
    print('number 1')
    number_1 = input()
    print('number 2')
    number_2 = input()

    if not float(number_2) and not float(number_1):
        print('Incorrect input')
    else:
        number_1 = float(number_1)
        number_2 = float(number_2)

        print(f'number 1 +  number 2 = {number_1 + number_2}')
        print(f'number 1 -  number 2 = {number_1 - number_2}')
        print(f'number 1 X  number 2 = {number_1 * number_2}')

        if number_2 == 0:
            print('Number 2 is 0 and can not division on 0')
        else:
            print(f'number 1 /  number 2 = {number_1 / number_2}')

        print(f'number 1 ^  number 2 = {number_1 ** number_2}')

# Perform and print the results of addition, subtraction, multiplication, and division.

# Handle division by zero (e.g., print an error message if num2 is zero).

# Perform a power operation, raising num1 to the power of num2, and print the result.

# If the user chooses Booleans (choice == '3'):
elif choice == '3':
    # Declare two boolean variables, e.g., is_python_fun = True, is_sunny = False.
    is_python_fun = True
    s_sunny = False
    print(is_python_fun and s_sunny)
    print(is_python_fun or s_sunny)
    print(not is_python_fun and not s_sunny)
    print(not is_python_fun or not s_sunny)

# Perform and print the results of logical operations: AND, OR, NOT.

# Perform and print the results of comparison operations (e.g., 10 > 5 and 5 == 5).

# If the user chooses Additional Data Types (choice == '4'):
elif choice == '4':
    # ### List Operations ###
    token = [43, 'hello', True]
    print(token)
    token.append(3.45)
    print(token)
    print(token[3])
    print(len(token))

    tuple_ = ('fruits', )
    print(len(tuple_))

    try:
        tuple_[0] = 'apple'
    except:
        print("Error")

    dic = {1:2, 2:'str', 3:True}
    print(dic[2])
    dic[4] = 4.65

# Create a list with mixed data types (e.g., numbers, strings, booleans).

# Append a new element to the list and print the updated list.

# Access and print the 4th element in the list.

# ### Tuple Operations ###
# Create a tuple with some string elements (e.g., fruits).

# Print the length of the tuple.

# Try to modify one element in the tuple and handle the resulting TypeError.

# ### Dictionary Operations ###
# Create a dictionary with some key-value pairs (e.g., name, age, city).

# Access and print the value for one of the keys (e.g., "age").

# Add a new key-value pair to the dictionary and print the updated dictionary.

# If the user enters an invalid choice:
else:
    print('Invalid choose!')
# Print an error message indicating an invalid selection.
