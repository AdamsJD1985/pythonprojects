"""Celsius to Fahrenheit


You are making a Celsius to Fahrenheit converter.
Write a function to take the Celsius value as an argument and return the
corresponding Fahrenheit value.



Sample Input
36

Sample Output
96.8"""
print(f"input celsius to convert to fahrenheit:")
celsius = int(input())


def convert(c):
    c = 9 / 5 * c + 32
    return (c)


fahrenheit = convert(celsius)
print(fahrenheit)