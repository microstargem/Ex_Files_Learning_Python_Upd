# 
# Example file for variables
#

# Declare a variable and initialize it
a = 0
# print(a)


# re-declaring the variable works
# a = "abc"
# print(a)


# ERROR: variables of different types cannot be combined
# print("this is a string" + str(123))


# Global vs. local variables in functions
def aFunction():
    global a
    a = "def"
    print(a)

aFunction()
print(a)

del a
print(a)