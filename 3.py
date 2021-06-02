#: Write a Python program to convert the Python dictionary object (sort by key) to
#JSON data. Print the object members with indent level 4

import json
str = {'a': 5, 'c': 7, 'b': 3, 'd': 4}
print("Original String:")
print(str)
print("JSON data:")
print(json.dumps(str, sort_keys=True, indent=4))