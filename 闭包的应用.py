class Foo(object):
    def __init__(self):
        super(Foo, self).__init__()
        self.a = "a"
class Foo1(Foo):
    pass
f = Foo1()
f.a
class Foo(object):
    def __init__(self):
        super(Foo, self).__init__()
        self.a = "a"
    def func(self, a)
class Foo(object):
    def __init__(self):
        super(Foo, self).__init__()
        self.a = "a"
    def func(self, a):
        def func1(self, b)
class Foo(object):
    def __init__(self):
        super(Foo, self).__init__()
        self.a = "a"
    def func(self, a):
        def func1(self, b):
            b += 1
    self.func1(a)
class Foo(object):
    def __init__(self):
        super(Foo, self).__init__()
        self.a = "a"
    def func(self, a):
        def func1(self, b):
            b += 1
        self.func1(a)
self.func(1)
a = Foo()
a.func(3)
lis = []
for i in range(3):
    def foo(x):print x + i
    lis.append(foo)
for f in lis:
    f(2)
for i in range(3):
    def foo(x, y=i):print x + y
    lis.append(foo)
def foo():
    m = 0
    def foo1():
        m = 1
        print m
    print m
foo()
foo1()
print m
def foo():
    m = 0
    def foo1():
        m = 1
        print m
    print m
    foo1()
    print m
foo()
def foo1():
    a = [1]
    def foo2():
        a[0] += 1
        return a[0]
    return foo2
foo1()
print foo1()
def foo1():
    a = [1]
    def foo2():
        a[0] += 1
        return a[0]
    foo2()
    return foo2()
print foo1()
def foo1():
    a = [1]
    def foo2():
        a[0] += 1
        return a[0]
    return foo2()
print foo1()
origin = [0, 0]
x = [0, 50]
y = [0, 50]
def foo(pos=origin):
    def bar(a, b):
        new_x = pos[0] + a[0]*b
        new_y = pos[1] + a[1]*b
        pos[0] = new_x
        pos[1] = new_y
        return pos
    return bar
ba = foo()
print foo([1, 0], 10)
print ba([1, 0], 10)
print foo([0, 1], 20)
print ba([0, 1], 20)
print ba([-1, 0], 10)
def make_filter(keep): 
    def the_filter(file_name): 
        file = open(file_name) 
        lines = file.readlines() 
        file.close() 
        filter_doc = [i for i in lines if keep in i] 
        return filter_doc 
    return the_filter
foo = {'father' : 65, 'mother' : 62, 'sister' : 38, 'brother' : 29, 'me' : 28}
sorted(foo.iteritems(), key=lambda x:x[1])
foo.iteritems()
list(foo.iteritems())
def startAt_v1(x):
    def incrementBy(y):
        return x + y 
    print 'id(incrementBy)=%s' % (id(incrementBy))
    return incrementBy
def startAt_v2(x):
    return lambda y:x+y
if "__main__" == __name__:
    c1 = startAt_v1(2)
    print 'type(c1)=%s, c1(3)=%s' % (type(c1), c1(3))
    print 'id(c1)=%s' % (id(c1))
    c2 = startAt_v2(2)
    print 'type(c2)=%s, c2(3)=%s' % (type(c2), c2(3))
def startAt_v1(x):
    def incrementBy(y):
        return x + y 
    print incrementBy(y)
    print 'id(incrementBy)=%s' % (id(incrementBy))
    return incrementBy
def startAt_v2(x):
    return lambda y:x+y
if "__main__" == __name__:
    c1 = startAt_v1(2)
    print 'type(c1)=%s, c1(3)=%s' % (type(c1), c1(3))
    print 'id(c1)=%s' % (id(c1))
    c2 = startAt_v2(2)
    print 'type(c2)=%s, c2(3)=%s' % (type(c2), c2(3))
def startAt_v1(x):
    def incrementBy(y):
        return x + y 
    print incrementBy
    print 'id(incrementBy)=%s' % (id(incrementBy))
    return incrementBy
def startAt_v2(x):
    return lambda y:x+y
if "__main__" == __name__:
    c1 = startAt_v1(2)
    print 'type(c1)=%s, c1(3)=%s' % (type(c1), c1(3))
    print 'id(c1)=%s' % (id(c1))
    c2 = startAt_v2(2)
    print 'type(c2)=%s, c2(3)=%s' % (type(c2), c2(3))
def foo(func):
    def inner(n, m):
        n += 1
        print 'in inner: fn=%s, n=%s, m=%s' % (fn.__name__, n, m)
        return func(n, m)
    return inner
def foo(func):
    def inner(n, m):
        n += 1
        print 'in inner: fn=%s, n=%s, m=%s' % (fn.__name__, n, m)
        return func(n, m)
    return inner
@foo
def f(n, m):
    print 'in foo: n=%s, m=%s' % (n, m)
    return n * m
print f(2, 3)
def foo(func):
    def inner(n, m):
        n += 1
        print 'in inner: fn=%s, n=%s, m=%s' % (func.__name__, n, m)
        return func(n, m)
    return inner
@foo
def f(n, m):
    print 'in foo: n=%s, m=%s' % (n, m)
    return n * m
print f(2, 3)
def multipliers():
    return [lambda x:i * x for i in range(4)]
print [m(2) for m in multipliers()]
#[6, 6, 6, 6]
def multipliers():
    return [functools].partial(lambda i, x:x * i, i) for i in range(4)]
def multipliers():
    return [functools.partial(lambda i, x: x * i, i) for i in range(4)]
print [m(2) for m in multipliers()]
print [m(2) for m in multipliers()]
import functools
def multipliers():
    return [functools.partial(lambda i, x: x * i, i) for i in range(4)]
print [m(2) for m in multipliers()]
def fun(val):
    print("%x" % id(val))
    def func(passline):
        if val >= passline:
            print "pass"
        else:
            print "failed"
    return func
f = fun(90)
print f.__closure__
f(60)
f(39)
f = fun(59)
f(90)
%hist -f 闭包的应用.py
