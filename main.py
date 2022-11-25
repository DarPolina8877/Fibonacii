def fib(num):
    if 0 <= num <= 1:
        return num
    return fib(num - 2) + fib(num - 1)

def main():
    while (True):
        print('Итог: ' + str(fib(int(input('Введите число: ')))))

if __name__ == '__main__':
    main()