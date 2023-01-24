a = 12
b = 13
if a < b:
    print("Yes")

if a == b:
    print("1")
elif a < b:
    print("2")
else:
    print("3")

if a == b and b == a:
    print("Hello!")

if a == b or b > a:
    print("Hello!")

print("Yes") if b > a else print("No")