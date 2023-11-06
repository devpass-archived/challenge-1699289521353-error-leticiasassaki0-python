def divide(a, b):
    # Add your solution using exception handling here!
    pass

if __name__ == '__main__':
    try:
        result = divide(10, 2)
        print(f'Division result: {result}')
    except ZeroDivisionError:
        print('Error: Division by zero is not allowed!')
    except Exception as e:
        print(f'Error: {e}')
