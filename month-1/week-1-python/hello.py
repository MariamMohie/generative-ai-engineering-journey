# name = input("What is your name? ").strip().title()
#name = name.strip().title()  # Remove any leading/trailing whitespace and capitalize the first letter of each word in the name
#name = name.capitalize()  # Capitalize the first letter of the name
#name = name.title()  # Capitalize the first letter of each word in the name

# print(f"Hello, {name}!") #?the f-string is used to format the output string, and the variable name 
#? is inserted into the string using curly braces {}. The result is a personalized greeting 
#? that includes the user's name.
#! If U want to write double quotes inside the f-string, U can use single quotes to enclose the string, like this:
#? print(f'Hello, "{name}"!')  #? This will print the name with double quotes around it.
#! OR U can use escape characters to include double quotes inside the f-string, like this:
#? print(f"Hello, \"{name}\"!")  #? This will also print the name with double quotes around it.

 #---------------------------------------------------------------

#? Round function : round(number[, ndigits]) -> number rounded to ndigits precision after the decimal
#? point. If ndigits is omitted or is None, it returns the nearest integer to its input.
#! in the documentation when see squared brackets [] it means that the parameter is optional
# x = float(input("first number: "))
# y = float(input("second number: "))

# z= round(x + y)  # Round the sum of x and y to 2 decimal places

# print(f"{z:,}")  # Print the rounded sum with a comma as the thousands separator

s= "hello , from \nthe other side" #? the \n is an escape character that represents a new line. When the string is printed, the text after \n will appear on a new line.
print(s)

#-----------------------------------------------------

print('c:\this\name') #? the \t is an escape character that represents a tab. When the string is printed, the text after \t will be indented by a tab space.
print(r'c:\this\name') #? the r before the string indicates that it is a raw string, which means that escape characters will not be processed. The string will be printed exactly as it is written, including the backslashes.
#-------------------------------------------
s2 = 3 * 'un'+ 'oui'
print(s2) #? the * operator is used to repeat the string 'un' three times, and then the + operator is used to concatenate the resulting string with 'oui'. The final result is 'unununoui'.
#-------------------------------------------
s3 ='py''thon'
print(s3) #? the two string literals 'py' and 'thon' are concatenated together to form the string 'python'. This is a feature of Python that allows adjacent string literals to be automatically concatenated without the need for an explicit operator.
#-------------------------------------------
prefix = 'Py'
# print(prefix 'thon') #? We cannot concatenate a string literal with a variable  without explicitly using the + operator. The correct way to concatenate the variable prefix with the string literal 'thon' is to use the + operator, like this:
print(prefix + 'thon')#✔️ 

#-------------------------------------------

word = 'Python'
print(word[0])  #? This will print the first character of the string 'Python', which is 'P'.
print(word[-1])  #? This will print the last character of the string 'Python', which is 'n'.
print(word[0:2])  #? This will print the first two characters of the string 'Python', which is 'Py'. 0, 1 indexes are inclusive, while 2 is exclusive.
print(word[2:5])  #? This will print the characters of the string 'Python' starting from index 2 to index 5 (exclusive), which is 'tho'.
print(word[:2])  #? This will print the first two characters of the string 'Python', which is 'Py'. The starting index is omitted, so it defaults to 0.
print(word[-2:])  #? This will print the last two characters of the string 'Python', which is 'on'. The ending index is omitted, so it defaults to the length of the string.
print(word[2:])  #? This will print the characters of the string 'Python' starting from index 2 to the end of the string, which is 'thon'. The ending index is omitted, so it defaults to the length of the string.
#! Note the start is always included, while the end is always excluded. This is a common convention in programming languages and is known as "half-open" or "half-closed" intervals.
"""
+---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
"""

#!----------------------------------Lists-------------------------------------------
rgb = ["Red", "Green", "Blue"]
rgba = rgb
id(rgb) == id(rgba)  # they reference the same object

rgba.append("Alph")
# print(rgb) #? This will print the list ['Red', 'Green', 'Blue', 'Alph']. Since rgba is a reference to the same list object as rgb, appending "Alph" to rgba also modifies the original rgb list.
#! this because in Python, when you assign a list to another variable, you are not creating a new copy of the list. Instead, both variables point to the same list object in memory. Therefore, any changes made to the list through one variable will be reflected in the other variable as well.
 #-------------------------------------------
correct_rgba = rgba[:]
correct_rgba[-1] = "Alpha"
correct_rgba

print(correct_rgba)  #? This will print the list ['Red', 'Green', 'Blue', 'Alpha']. The slice notation [:] creates a new copy of the rgba list, so modifying correct_rgba does not affect the original rgba list.
print(rgba)
#-------------------------------------------
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)

print(x[0])

print(x[0][2])  #? This will print the third element of the first list in x, which is 'c'. The first index [0] selects the first list (a), and the second index [2] selects the third element of that list.
print(x[1][2])  #? This will print the third element of the second list in x, which is 3. The first index [1] selects the second list (n), and the second index [2] selects the third element of that list.

#-------------------------------------------
#? Fabonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. The sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
a,b =0,1
while a<10:
    # print(a)
    a,b =b,a+b  #? This line uses tuple unpacking to simultaneously update the values of a and b. The new value of a is assigned the current value of b, and the new value of b is assigned the sum of the current values of a and b. This effectively generates the next number in the Fibonacci sequence.

#-------------------------------------------
#! Note : the Operator precedence
#? ** has higher precedence than -
-3**2  #? This will print -9. The ** operator has higher precedence than the - operator, so -3**2 is equivalent to -(3**2), which is -9.
(-3)**2  #? This will print 9. The parentheses change the order of operations, so (-3)**2 is equivalent to (-3)*(-3), which is 9.

print(2**3)       # 8
print(-2**3)      # -8
print((-2)**3)    # -8
print((-2)**2)    # 4
print(-2**2)      # -4
"""
When the exponent is even, a negative number raised to that power becomes positive.
When the exponent is odd, it remains negative.
"""

#------------------------------------------- Functions-------------------------------
#? range(start, stop[, step]) -> range object , when U see squared brackets [] it means that the parameter is optional
list(range(5, 10))


list(range(0, 10, 3))


list(range(-10, -100, -30))