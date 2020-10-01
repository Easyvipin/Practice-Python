import csv
def write_to_file():
    result = []

    while True:
        prod_id = int(input("enter prod id please: "))
        prod_name = input("enter prod name please: ")
        prod_price = int(input("enter price : "))
        prod_qty = int(input("enter quantity "))
        data = [prod_id,prod_name,prod_qty,prod_price]
        result.append(data)
        choice = input("continue? ").upper()
        if "N" in choice:
            break

    with open("product.csv",'w') as f:
        write = csv.writer(f,delimiter =',')
        for each in result:
            write.writerow(each)
        

#to display 
def show_file():
    with open("product.csv",'r') as f:
        read = csv.reader(f)
        for line in read:
            print(line)

write_to_file()
show_file()