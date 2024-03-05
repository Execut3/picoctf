values = [
    112, 105, 99, 111, 67, 84, 70, 123, 103, 48, 48, 100, 95, 107, 49, 
    116, 116, 121, 33, 95, 110, 49, 99, 51, 95, 107, 49, 116, 116, 121, 
    33, 95, 100, 51, 100, 102, 100, 54, 100, 102, 125, 10
]

# Convert decimal values to ASCII characters
ascii_text = ''.join(chr(val) for val in values)

# Print the ASCII text
print(ascii_text)
