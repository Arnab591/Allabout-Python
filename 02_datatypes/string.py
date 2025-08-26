# today we will cover string core , string indexing and string slicing
a = "Arnab"
print(a)
print(id(a))
a = "Srija"
print(a)
print(id(a))
# string is immutable in python
# string is a sequence of character in python
# indexing of string
# 0 1 2 3 4
# A r n a b
print(a[0])

# BASIC OF STRING SLICING
print(a[0:5])
# reverse a string in python
print(a[::-1])
# encoding and decoding
my_text = "Hello Arnab"
print(f"hello my original : {my_text}")
encoded_text = my_text.encode()
print(f"The encoded version is : {encoded_text}")
decoded_text = encoded_text.decode("UTF-8")
print(f"decoded version is : {decoded_text}")
