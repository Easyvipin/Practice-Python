# Write a menu drivenPython program to implement a Stack of integers,floating point
# numbers and strings using a list data-structure.(Push ,Pop n Display)

stack = []
def push(item):
    stack.append(item)


def top():
    if len(stack) != 0 :
        print(stack[-1])
    else:
        print("Stack is empty")

def pop_top():
    if len(stack) != 0:
        print("Now Popping...")
        stack.pop()
    else:
        print("Not possible on Empty Stack")
    
def clear_stack():
    stack.clear()

def display_stack():
    for element in range(len(stack)-1,-1,-1):
        print(stack[element])


while True:
    print("Press 1 to Push to Stack")
    print("Press 2 to Pop from Stack")
    print("Press 3 to show Stack")
    print("Press 4 to get Top of Stack")
    print("Press 5 to clear a Stack")

    first_choice = int(input())
    if first_choice == 1:
        item= input("Enter Item to add: ")
        push(item)
    elif first_choice == 2:
        pop_top()
    elif first_choice == 3:
        display_stack()
    elif first_choice == 4:
        top()
    elif first_choice == 5:
        clear_stack()
    else:
        print("invalid input\n try again?")

    second_choice = input("Another Operation? (y/n)").lower()
    if 'n' in second_choice :
        break