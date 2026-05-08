mystr = "Welcome to day2 Session on Python"
print(mystr)

# Inbuilt method
print("Uppercase", mystr.upper())
print("Lowercase", mystr.lower())
print("Index", mystr.index('day'))

# New multiline string
mystr = '''
i am a good boy
i am an coder
'''

print(mystr)

# Do not use in single quotes
print(type(mystr))

# Index always start from zero
print('capitalizemystr', mystr.capitalize())
print(mystr.count('a'))
print("count", mystr.count('o'))