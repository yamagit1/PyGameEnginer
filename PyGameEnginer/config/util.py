
def test(a, **b):
    print a
    print b

def call(**kargs):
    test(2, **kargs)

x = {1,2}
call(name="test")