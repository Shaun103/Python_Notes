def uni_char(s):
    return len(set(s)) == len(s)

def uni_char2(s):
    chars = set()
    
    for let in s:
        # Check if in set
        if let in chars:
            return False
        else:
            #Add it to the set
            chars.add(let)

    return True




x = uni_char('abcde')
print(x)

x = uni_char2('abcde')
print(x)

x = uni_char2('aaabbbccde')
print(x)
