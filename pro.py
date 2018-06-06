def foo(a):
    if a == 1:
        name = "a"
    elif a == 0:
        name = "b"
foo(a)
foo(1)
a = 2
if a == 2:
    name = "a"
dic["name"] = name
dic = {}
if a == 2:
    name = "a"
dic["name"] = name
dic
class A:
    def foo():
        return "a"
class B(A):
    pass
b = B()
b.foo
b.foo()
b.foo(b)
foo(b)
print foo(b)
class A:
    @poperty
    def foo():
        return "a"
class A:
    def __init__(self):
        self.a = "a"
    def foo():
        return self.a
class B(A):
    pass
b = B()
b.foo
b.foo()
class A:
    def __init__(self):
        self.a = "a"
    def foo(self):
        return self.a
class B(A):
    pass
b = B()
b.foo
print b.foo
print b.foo()
class A:
    def __init__(self):
        self.a = "a"
    @property
    def foo(self):
        return self.a
class B(A):
    pass
b = B()
b.foo
def foo():
    def wrapper(dic):
        dic = {"a":1}
        return func(dic)
    return wrapper
@foo
def f1(dic):
    return f1
def foo(func):
    def wrapper(dic):
        dic = {"a":1}
        return func(dic)
    return wrapper
@foo
def f1(dic):
    return f1
f1(dic)
@foo
def f1(dic):
    return dic
f1(dic)
@foo
def f1():
    return dic
def foo(func):
    def wrapper():
        dic = {"a":1}
        return func(dic)
    return wrapper
@foo
def f1():
    return dic
f1()
f1(dic)
class A:
    def foo(self):
        return self._a
class B(A):
    def foo(self):
        return self._a
b = B()
b.foo()
class C(A):
    pass
c = C()
c.foo()
a = A()
a.foo
a.foo()
%hist -f pro.py
