# a = float(input('enter value of a'))
# b = float(input('enter value of b'))

# c_squared = ((a**2)+(b**2))**0.5


# print(c_squared )

value1 = float(input('enter value1'))
value2 = float(input('enter value2'))
power1 =float(input('enter power1'))
power2 =float(input('enter power2'))
initial_result = (value1**power1 + value2**power1)
c_hypo = (initial_result**power2)
display_text = "the hypothenus of "+ str(value1) + " and " + str(value2) + " is " + str(c_hypo)  
print(display_text)
