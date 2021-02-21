"""
Boolean Expressions: An expression that either evaluates to true or false is known as boolean expression.

Boolean expressions uses relational operators(comparision operators) to evaluate to a boolean value.
1. x != y : x is not equal to y
2. x == y : x is equal to y
3. x is y : x is same as y
4. x is not y : x is not the same as y
5. x > y : x is greater than y
6. x >=y : x is greater than equal to y
7. x < y : x is less than y
8. x<= y : x is less than equal to y

Logical operators: Gives combines results for 2 boolean statements.
1. and : results True iff both the operands are true else false.
2. or  : results True if either of operators is True else false.
3. not : (unary operator, i.e. operates on a single operand) results True if operand is false, i.e. converses the
        operator value.

Conditional Statement(s):
1. if
2. if-else
3. if-elif-else

Ternary Operator: It simply allows to test a condition in a single line replacing the multiline if-else making the
code compact.
"""

# Indentation is important
# It defines block

x = 5

if x < 10:
    print("Value of x is less than 10.")

if x < 3:
    print("x is less than 3")

if x <= 10 and x >= 3:
    print("Value of x is greater than equal to 3 and less than equal to 10.")
    print("!!!")

# Above statement can also be written as
if 3 <= x <= 10:
    print("Value of x is greater than equal to 3 and less than equal to 10.")
    print("!!!!")

if x < 5:
    print("x is less than 5")
else:
    print("x is greater than 5")

if x<5:
    print("x is less than 5")
elif x==5:
    print("x is equal to 5")
else:
    print("x is greater than 5")

# Nested Conditionals
if 0 < x:
    if x < 10:
        print("x is a positive single-digit number.")

# Ternary Operator
y = 22 if x > 3 else 5
print(y)            # Gives 22

y = 35 if x > 10 else 7
print(y)            # Gives 7

"""
Difference between == and is
The Equality operator (==) compares the values of both the operands and checks for value equality. 
Whereas the ‘is’ operator checks whether both the operands refer to the same object or not.
"""