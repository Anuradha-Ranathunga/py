class Scope:
    def __init__(self):
        pass
        
    def myfunc1(self):
        x = "Jane"
        def myfunc2():
            x = "hello"
            print(x)
        myfunc2()

scope = Scope()
scope.myfunc1()
print(scope.myfunc1())