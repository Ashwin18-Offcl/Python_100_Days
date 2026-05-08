mystr="Welcome to day2 Session on Python"
print(mystr)
mystr='''
i am a good boy
i am an coder

'''
print(mystr)
# Do not use in single quotes
print(type(mystr))

# Inbuilt method
print("Uppercase",mystr.upper())
print("Lowercase",mystr.lower())
print("Index",mystr.index('day'))

# Index always start from zero not other 
print('capitalizemystr',mystr.capitalize())
print(mystr.count('a'))
print("count",mystr.count('o'))
