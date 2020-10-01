import pickle as p


def get_records_to_add():
    data_to_be_added = []
    while True:
        book_title = input("Enter student's name: ")
        book_number = int(input(f"Enter {book_title}'s number: "))
        book_price = int(input(f"Please enter {book_title}'s price: "))
        new_book = {
            "Title":book_title,
            "Number":book_number,
            "Cost":book_price
        }
        data_to_be_added.append(new_book)
        choice = input("Want to add another book?: ").lower()
        if 'n' in choice:
            break
    return data_to_be_added
    
def add_record_to_binaryfile(list_of_data):
    with open("book.dat","wb") as file:
        p.dump(list_of_data,file)
        print("Succesfully added data to file!")

def update_binary_file():
    with open("book.dat","rb+") as file:
        book_info = p.load(file)
        flag = True
        book_title = int(input("Enter roll number for student to update their name: "))
        for book in book_info:
            if book["Title"] == book_title:
                name  = book["Title"]
                print(f"Orignal name is: {name}")
                new_name = input("Enter new name to be updated: ")
                book["Title"] = new_name
                flag = False
                break
        if flag == False:
            file.seek(0)
            p.dump(book_info,file)
            print("Done Bro!")
