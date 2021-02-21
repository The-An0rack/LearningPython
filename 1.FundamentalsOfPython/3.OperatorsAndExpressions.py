"""
Operator: A special symbol that represents a simple computation like addition, multiplication, or string concatenation.

Following operations are present in python:
I. Arithmetic Operators
    1. Addition(+)
    2. Subtraction(-)
    3. Multiplication(*)
    4. Division(/)
    5. Integer Division(//)
    6. Modular Division(%)
    7. Exponentiation(**)

II. Relational Operator
    (Covered in 5.ConditionalExecution )

III. Logical Operator
    1. and
    2. or
    3. not

Operand: One of the values on which an operator operates.
"""

num1 = 56
num2 = 9
print("Num1: ", num1, ", num2: ", num2)
print("Addition           : " + str(num1 + num2)) #Gives 65
print("Subtraction        : " + str(num1 - num2)) #Gives 47
print("Multiplication     : " + str(num1*num2))   #Gives 504
print("Division           : " + str(num1/num2))   #Gives 6.222222222
print("Integer Division   : " + str(num1//num2))  #Gives 6
print("Modular Division   : " + str(num1%num2))   #Gives 2
print("Exponentiation(2^3): " + str(2**3))        #Gives 8


"""
Expression: a valid combination of operator and operands

Order of precedence of operators:
1. Parentheses have the highest precedence and can be used to force an expression to evaluate
2. Exponentiation has the next highest precedence
3. Next follows multiplication and division (incl. modular division) which have same precedence, followed by addition and subtraction
   which also have same order of precedence
4. Operator with the same precedence are evaluated from left to right
"""


print(7*5%3) #->35%3 ->2
print(3*2**3) #3*8

