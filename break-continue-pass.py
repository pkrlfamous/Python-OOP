#break

i = 1
def breaking(i):
    while i < 10:
        if i > 5:
            break
        print(i)
        i += 1

# breaking(i)


#continue

def continue_example():
    for i in range(10):
        if i % 3 == 0:
            continue
        print(i)

continue_example()

#pass

def pass_example():
    for i in range(1, 10):
        if i % 2 != 0:
            pass
        else:
            print(i)

# pass_example()