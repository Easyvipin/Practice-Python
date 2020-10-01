"""
Create a binary file with name and roll number and marks of students(represented
using a dictionary).Write a complete Menu Driven program to perform following
operations(define a function for each operation):
● Inserting/Appending records to a binary file
● Reading records from a binary file
● Searching a record in a binary file
● Updating a record in a binary file
● Deleting a record from a binary file
"""

import pickle as p

def get_records_to_add():
    data_to_be_added = []
    while True:
        name = input("Enter student's name: ")
        roll_number = int(input(f"Enter {name}'s roll number: "))
        marks = int(input(f"Please enter {name}'s marks: "))
        new_student = {
            "Name":name,
            "Roll Number":roll_number,
            "Marks":marks,
        }
        data_to_be_added.append(new_student)
        choice = input("Want to add another student?: ").lower()
        if 'n' in choice:
            break
    return data_to_be_added
    
def add_record_to_binaryfile(list_of_data):
    with open("student.dat","wb") as file:
        p.dump(list_of_data,file)
        print("Succesfully added data to file!")

def read_binary_file():
    with open("student.dat","rb") as f:
        student_data_to_read = p.load(f)
        for student in student_data_to_read:
            name = student["Name"]
            roll_number = student["Roll Number"]
            marks = student["Marks"]
            print(f"Name of the Student is: {name}.\n {name}'s' roll number is {roll_number} & he scored {marks} marks")
        
def search_binary_file():
    with open("student.dat","rb+") as file:
        data = p.load(file)
        flag = True
        to_search = int(input("Enter Roll Number to Search For: "))
        for info in data:
            if info["Roll Number"] == to_search:
                student_name = info["Name"]
                print(f"Data match found for {student_name}")
                flag = False
                break 
        if flag == True:
            print("Couldnt find that roll number")

def update_binary_file():
    with open("student.dat","rb+") as file:
        students_info = p.load(file)
        flag = True
        roll_number = int(input("Enter roll number for student to update their name: "))
        for student in students_info:
            if student["Roll Number"] == roll_number:
                name  = student["Name"]
                print(f"Orignal name is: {name}")
                new_name = input("Enter new name to be updated: ")
                student["Name"] = new_name
                flag = False
                break
        if flag == False:
            file.seek(0)
            p.dump(students_info,file)
            print("Done Bro!")

def delete_binary_file():
    deleted_name = input("Enter name for which info is to be deleted: ")
    with open("student.dat","rb+") as file:
        entire_file_data = p.load(file)
    with open("student.dat","rb+") as file:
        for student in entire_file_data:
            if student["Name"] == deleted_name:
                continue
            p.dump(student,file)

if __name__ == "__main__":
    while True:
        print("Press 1 for Inserting a Record")
        print("Press 2 for Reading a Record")
        print("Press 3 for Searching a Record")
        print("Press 4 for Updating a Record")
        print("Press 5 for Deleting a Record")
        option = int(input())
        if option == 1:
            list_of_data = get_records_to_add()
            add_record_to_binaryfile(list_of_data)
        elif option == 2:
            read_binary_file()
        elif option == 3:
            search_binary_file()
        elif option == 4:
            update_binary_file()
        else:
            delete_binary_file()
        

        ch = input("Do you want to continue?: ").lower()
        if "n" in ch:
            break