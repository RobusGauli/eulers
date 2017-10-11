# coding: utf-8
def multipleof(a, b, limit):
    s = 0
    for i in range(1, limit):
        if i % a == 0 or i % b == 0:
           # print(i)
            s += i
    return s

if __name__ == '__main__':
	import sys
	a, b, limit = sys.argv[1:]
	print(multipleof(int(a), int(b), int(limit)))
# ma
