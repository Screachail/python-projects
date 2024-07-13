# first example - iterator

class Fib:
    def __init__(self, last):
        self.__last = last
        self.__current = 0
        self.__prev_1 = self.__prev_2 = 1


    def __iter__(self):
        return self


    def __next__(self):
        self.__current += 1
        if self.__current > self.__last:
            raise StopIteration
        if self.__current in [1, 2]:
            return 1
        return_value = self.__prev_1 + self.__prev_2
        self.__prev_1, self.__prev_2 = self.__prev_2, return_value
        return return_value


for i in Fib(10):
    print(i, end=" ")


#second example - yield

ddef Fib(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

print(list(Fib(10)))

