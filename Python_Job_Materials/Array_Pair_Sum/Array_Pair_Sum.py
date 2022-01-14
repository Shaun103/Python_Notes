

l = [1, 2, 3, 2, -1, 5, 4, 0]
k = 4

def arrayPairSum(k, l):

    target = 0
    output = set()
    seen = set()

    for num in l:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((num, target))
    print(output)


arrayPairSum(k, l)