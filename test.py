def area(x,y,unit="meters"):
    print (x*y, "square %s"%unit)
# area(2, "miles", 3)
# area(x=2, unit="feet", y=3)

def foo(bar=[]): # bar defaults to [] 
    bar.append("baz") # this is problematic
    return bar
# print(foo())
# print(foo())
# print(foo([1,2,3,4,5,6,7]))
# print(foo())

def foo(bar=None): 
    if bar is None: # ie, if no bar: ...       
        bar = [] 
    bar.append("baz") 
    return bar 
# print(foo())
# print(foo())
# print(foo([1,2,3,4,5,6,7]))
# print(foo())

# def f(*a, **kw): 
#     print(a, kw, sep="\n")
# f(1, 2, 3, 4, 5, 6, a=2, b=3, c=5)
# f(1, 2, 3, 4, 5, 6)
# f(a=2, b=3, c=5)
# f(a=2, 1, 2, b=3, 3, 4, c=5, 5, 6)

def g(*x): 
    f(x) 
def f(*x):
    print(x)
# f(1, 2, 3)
# g(1, 2, 3)

def printv2(*args,**kwlist):
    print(*args,**kwlist)

def printv3(*args, end="\n", sep=", "):
    for i in args[:-1]:
        print(i,end=sep, sep="")
    print(args[-1],end=end)

# print(1, 2, 3, 4, 5, 6, sep="+")

def f(): pass
f()
print(f())

d=f()
d
print(d)
