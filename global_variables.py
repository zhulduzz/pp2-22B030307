x = "hello"

def func():
    print("Say: " + x)

func()

def myfunc():
    x = "hi"
    print("Say: " + x)

myfunc()

print(x)

def Myfunc():
    global x
    x = "kind"

Myfunc()
print(x)

print(x + " of woman")