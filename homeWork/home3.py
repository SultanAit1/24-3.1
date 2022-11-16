class A:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        return self.count + other.count


class S:
    def __init__(self, count):
        self.count = count

    def __sub__(self, other):
        return self.count - other.count


class M:
    def __init__(self, count):
        self.count = count

    def __mul__(self, other):
        return self.count * other.count


class T:
    def __init__(self, count):
        self.count = count

    def __truediv__(self, other):
        return self.count / other.count


class go(A,S,T,M):
    def __init__(self, count):
        A.__init__(self, count)
        S.__init__(self, count)
        M.__init__(self, count)
        T.__init__(self, count)


