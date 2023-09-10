def tryCatch():

    try:
        k = int(input('Enter a number: '))
        l = int(input('Enter another number: '))
        print(k/l)
    except ZeroDivisionError as e:
        print('Cannot divide a number by zero', e)

    except ValueError as e:
        print('Please enter integer', e)

    except Exception as e:
        print('Something went wrong', e)

tryCatch()