
# Contents _________________________________________________________________
# Enumerate
# Contents _________________________________________________________________


# Enumerate
lst = ['a', 'b', 'c', 'd']

second = 'abcdefghijklmnopqrstuvwxyz'

third = []

# for number,item in enumerate(second):
#     print(number,":", item)


for letter in second:
    third.append(letter)

print(third)

for number, item in enumerate(third):
    print(number,":", item)
