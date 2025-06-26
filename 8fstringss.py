letter = "hey my name is {} I'm from {}"
name="Shreya"
country="India"
print(letter.format(name, country))

print(f"hey my name is {name} I'm from {country}")

txt="For only {price:.2f}dollars!"
print(txt.format(price=49.099))

price=49.099
txt = f"For only {price:.2f}dollars!"
print(txt)

print(f"{2*3}")


#docstrings
def add_numbers(a, b):
    """
    This function takes two numbers as input and returns their sum.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of a and b.
    """
    return a + b
print(add_numbers(3, 5))

print(add_numbers.__doc__)
