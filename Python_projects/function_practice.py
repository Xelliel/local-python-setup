#1

def greeting():
    print("Hello! Welcome to Python!")

hello()


#2

def lunchbox(arg1, arg2, arg3):
    return [arg1, arg2, arg3]

print(lunchbox(1, 'sandwich', 'apple'))

#3

def eat_lunch(lunch_items):
    if not lunch_items:
        print("My lunchbox is empty!")
    else:
        print(f"First I eat {lunch_items[0]}")
        for item in lunch_items[1:]:
            print(f"Next I eat {item}")



