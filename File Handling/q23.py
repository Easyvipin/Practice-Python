# 23. Write a complete menu driven Python program to implement a Stack of Employees
# containing ENo,Ename n Esalary.(Push ,Pop n Display)

stack_of_employees = []


def add_employee():
    name = input("Enter student's name: ")
    emp_number = int(input(f"Enter {name}'s employee number: "))
    emp_salary = int(input(f"Please enter {name}'s salary: "))
    data = {
        "Employee Name" : name,
        "Emp Number" : emp_number,
        "Emp Salary" : emp_salary 
    }
    stack_of_employees.append(data)


def latest_employee():
    if len(stack_of_employees) != 0 :
        print(stack_of_employees[-1])
    else:
        print("Stack is empty")

def pop_top():
    if len(stack_of_employees) != 0:
        print("Now Popping...")
        stack_of_employees.pop()
    else:
        print("Not possible on Empty Stack")
    
def clear_stack():
    stack_of_employees.clear()

def display_stack():
    for element in range(len(stack_of_employees)-1,-1,-1):
        print(stack_of_employees[element])

def top():
    print(stack_of_employees[-1])

while True:
    print("Press 1 to Add Emp")
    print("Press 2 to Remove Latest Emp")
    print("Press 3 to Show All Emp")
    print("Press 4 to Show Latest Emp")
    print("Press 5 to fire Eveyone")

    first_choice = int(input())
    if first_choice == 1:
        add_employee()
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