# coding: utf-8
def fib():
    s = 0
    a, b = 0, 1
    while b < 4000000:
        
        a, b = b, a + b
        if b%2 == 0:
            s += b
    return s

if __name__ == '__main__':
	print(fib())
        
