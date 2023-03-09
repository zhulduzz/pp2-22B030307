#1

mylist = [56,8,90]

def multiply(numbers):
     
    total = 1

    for x in numbers:
        total += x
    return total

print(multiply(mylist))


#2


def count_up_and_lower(string):
    upper_case = 0
    lower_case = 0
    
    for char in string:
        if char.isupper():
            upper_case += 1
        elif char.islower():
            lower_case += 1
        
    print("Upper case count: ", upper_case)
    print("Lower case count: ", lower_case)

Mytext = input()
count_up_and_lower(Mytext)
            


#3

string = input()

reverse = (string[::-1])

if reverse == string:
    print("Pallindrome") 
else:
   print("Not pallindrome")


#5

my_tuple = tuple(input())

def check(my_tuple):

    true_or_false = all(my_tuple)
    
    return true_or_false

print(check(my_tuple))

#example

def all_true(t):
    return all(t)

my_tuple = (True, True, False, True)
result = all_true(my_tuple)
print(result)