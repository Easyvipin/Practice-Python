# Create a function showEmployee() in such a way that it should accept employee
# name, and it’s salary and display both, and if the salary is missing in function call it
# should show it as 30000

def show_employee(name, salary=30000):
    employee = {
        "Name": name,
        "Salary":salary
    }
    return employee