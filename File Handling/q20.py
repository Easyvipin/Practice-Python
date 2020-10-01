import csv
#to display comma seperated

def show_file():
    with open("product.csv",'r') as f:
        read = csv.reader(f)
        for line in read:
            print(','.join(line))
