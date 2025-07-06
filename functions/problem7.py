#variable arguments

def sum_all(*args):
    for i in args:
        print(i)
    return sum(args)

print(sum_all(1,2,3,4))
print(sum_all(1,2,3,4,5))