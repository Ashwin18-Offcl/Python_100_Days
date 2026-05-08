mystr = "Welcome to day2 Session on Python"
print(mystr)

# Inbuilt method
print("Uppercase", mystr.upper())
print("Lowercase", mystr.lower())
print("Index", mystr.index('day'))

print("count", mystr.count('Python'))
print("find", mystr.find('o'))
print("find", mystr.find('123'))
print("startswith", mystr.startswith('Welcome'))
print("endswith", mystr.endswith('Python'))

# New multiline string
mystr = '''
i am a good boy
i am an coder
'''

print(mystr)

print(type(mystr))

print('capitalizemystr', mystr.capitalize())
print(mystr.count('a'))
print("count", mystr.count('o'))

# Correct find usage
print(mystr.find('good'))

print("length", len(mystr))

print(mystr.isalpha())

# Correct numeric method
print(mystr.isnumeric())

# replace example
print(mystr.replace("coder", "developer"))

# Correct split method
data = mystr.split()

print(data)